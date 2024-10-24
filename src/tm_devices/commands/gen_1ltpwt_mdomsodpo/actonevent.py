"""The actonevent commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ACTONEVent:ACTION:AUXOUT:STATE <0|1|OFF|ON>
    - ACTONEVent:ACTION:AUXOUT:STATE?
    - ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess <QString>
    - ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess?
    - ACTONEVent:ACTION:EMAIL:STATE <0|1|OFF|ON>
    - ACTONEVent:ACTION:EMAIL:STATE?
    - ACTONEVent:ACTION:PRINT:STATE <0|1|OFF|ON>
    - ACTONEVent:ACTION:PRINT:STATE?
    - ACTONEVent:ACTION:SAVEIMAGE:STATE <0|1|OFF|ON>
    - ACTONEVent:ACTION:SAVEIMAGE:STATE?
    - ACTONEVent:ACTION:SAVEWFM:STATE <0|1|OFF|ON>
    - ACTONEVent:ACTION:SAVEWFM:STATE?
    - ACTONEVent:ACTION:SRQ:STATE <0|1|OFF|ON>
    - ACTONEVent:ACTION:SRQ:STATE?
    - ACTONEVent:ACTION:STOPACQ:STATE <0|1|OFF|ON>
    - ACTONEVent:ACTION:STOPACQ:STATE?
    - ACTONEVent:ACTION:VISUAL:STATE <0|1|OFF|ON>
    - ACTONEVent:ACTION:VISUAL:STATE?
    - ACTONEVent:EVENTTYPe <NONe|TRIGger|ACQCOMPLete>
    - ACTONEVent:EVENTTYPe?
    - ACTONEVent:NUMACQs <NR1>
    - ACTONEVent:NUMACQs?
    - ACTONEVent:REPEATCount <NR1>
    - ACTONEVent:REPEATCount?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ActoneventRepeatcount(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:REPEATCount`` command.

    Description:
        - Sets or returns the number of events to run.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:REPEATCount?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:REPEATCount?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:REPEATCount value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:REPEATCount <NR1>
        - ACTONEVent:REPEATCount?
        ```

    Info:
        - ``NR1`` is an integer that specifies the number of events to run. The default is 1 event
          and the maximum is 1000000 events. A repeat count greater than 1000000 specifies to run
          forever. In this case, the action on event can be terminated by setting the state for all
          actions to OFF. When the repeat count is set to infinite, the query returns 9.9E+37 (IEEE
          positive infinity).
    """


class ActoneventNumacqs(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:NUMACQs`` command.

    Description:
        - Sets (or queries) the number of acquisitions to complete for the event type ACQCOMPLete.
          The default is 1 acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:NUMACQs?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:NUMACQs?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:NUMACQs value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:NUMACQs <NR1>
        - ACTONEVent:NUMACQs?
        ```
    """


class ActoneventEventtype(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:EVENTTYPe`` command.

    Description:
        - Specifies (or queries) which event to act on (TRIGger, ACQCOMPLete, or NONe) when using an
          Act on Event command. The default is NONe. To specify the action to take, use the
          ``ACTONEVent:ACTION`` commands.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:EVENTTYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:EVENTTYPe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:EVENTTYPe value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:EVENTTYPe <NONe|TRIGger|ACQCOMPLete>
        - ACTONEVent:EVENTTYPe?
        ```

    Info:
        - ``NONe`` no event (this is the default).
        - ``TRIGger`` specifies to act when a trigger occurs.
        - ``ACQCOMPLete`` specifies to act when acquisition completes.
    """


class ActoneventActionVisualState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:ACTION:VISUAL:STATE`` command.

    Description:
        - Displays a visual notification when a specified event occurs, or queries the state of the
          'display a visual notification' action. The default state is 0 (off). To specify an event,
          use the command ``ACTONEVENT:EVENTTYPE``.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:VISUAL:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:VISUAL:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:ACTION:VISUAL:STATE value``
          command.

    SCPI Syntax:
        ```
        - ACTONEVent:ACTION:VISUAL:STATE <0|1|OFF|ON>
        - ACTONEVent:ACTION:VISUAL:STATE?
        ```

    Info:
        - ``1, ON`` displays a visual notification when the specified event occurs.
        - ``0, OFF`` turns off this action.
    """


class ActoneventActionVisual(SCPICmdRead):
    """The ``ACTONEVent:ACTION:VISUAL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:VISUAL?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:VISUAL?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:ACTION:VISUAL:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventActionVisualState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventActionVisualState:
        """Return the ``ACTONEVent:ACTION:VISUAL:STATE`` command.

        Description:
            - Displays a visual notification when a specified event occurs, or queries the state of
              the 'display a visual notification' action. The default state is 0 (off). To specify
              an event, use the command ``ACTONEVENT:EVENTTYPE``.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:VISUAL:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:VISUAL:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:ACTION:VISUAL:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:ACTION:VISUAL:STATE <0|1|OFF|ON>
            - ACTONEVent:ACTION:VISUAL:STATE?
            ```

        Info:
            - ``1, ON`` displays a visual notification when the specified event occurs.
            - ``0, OFF`` turns off this action.
        """
        return self._state


class ActoneventActionStopacqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:ACTION:STOPACQ:STATE`` command.

    Description:
        - Stops acquisitions when a specified event occurs, or queries the state of the 'stop
          acquisition' action. The default state is 0 (off). To specify an event, use the command
          ``ACTONEVENT:EVENTTYPE``.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:STOPACQ:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:STOPACQ:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:ACTION:STOPACQ:STATE value``
          command.

    SCPI Syntax:
        ```
        - ACTONEVent:ACTION:STOPACQ:STATE <0|1|OFF|ON>
        - ACTONEVent:ACTION:STOPACQ:STATE?
        ```

    Info:
        - ``1, ON`` stops acquisitions when the specified event occurs.
        - ``0, OFF`` turns off this action.
    """


class ActoneventActionStopacq(SCPICmdRead):
    """The ``ACTONEVent:ACTION:STOPACQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:STOPACQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:STOPACQ?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:ACTION:STOPACQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventActionStopacqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventActionStopacqState:
        """Return the ``ACTONEVent:ACTION:STOPACQ:STATE`` command.

        Description:
            - Stops acquisitions when a specified event occurs, or queries the state of the 'stop
              acquisition' action. The default state is 0 (off). To specify an event, use the
              command ``ACTONEVENT:EVENTTYPE``.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:STOPACQ:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:STOPACQ:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:ACTION:STOPACQ:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:ACTION:STOPACQ:STATE <0|1|OFF|ON>
            - ACTONEVent:ACTION:STOPACQ:STATE?
            ```

        Info:
            - ``1, ON`` stops acquisitions when the specified event occurs.
            - ``0, OFF`` turns off this action.
        """
        return self._state


class ActoneventActionSrqState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:ACTION:SRQ:STATE`` command.

    Description:
        - Sets or returns the enabled state of the generate service request (SRQ) action when a
          specified event occurs. The default state is 0. When this control is set, the instrument
          will set the OPC bit (bit 0) in the SESR (Standard Events Status Register) when the
          specified event occurs. In order to generate a service request interrupt (SRQ), the SRER
          (Service Request Enable Register), DESER (Device Event Status Enable Register), and the
          ESER (Event Status Enable Register) must be set appropriately as described in the
          programmer manual Synchronization Methods section. Upon completion of the mask test, event
          code 2600 ('Mask testing complete') is queued to the event queue. To specify an event, use
          the command ``ACTONEVENT:EVENTTYPE``.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SRQ:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:SRQ:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:ACTION:SRQ:STATE value``
          command.

    SCPI Syntax:
        ```
        - ACTONEVent:ACTION:SRQ:STATE <0|1|OFF|ON>
        - ACTONEVent:ACTION:SRQ:STATE?
        ```

    Info:
        - ``1, ON`` generates an SRQ when the specified event occurs.
        - ``0, OFF`` turns off this action.
    """


class ActoneventActionSrq(SCPICmdRead):
    """The ``ACTONEVent:ACTION:SRQ`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SRQ?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:SRQ?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:ACTION:SRQ:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventActionSrqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventActionSrqState:
        """Return the ``ACTONEVent:ACTION:SRQ:STATE`` command.

        Description:
            - Sets or returns the enabled state of the generate service request (SRQ) action when a
              specified event occurs. The default state is 0. When this control is set, the
              instrument will set the OPC bit (bit 0) in the SESR (Standard Events Status Register)
              when the specified event occurs. In order to generate a service request interrupt
              (SRQ), the SRER (Service Request Enable Register), DESER (Device Event Status Enable
              Register), and the ESER (Event Status Enable Register) must be set appropriately as
              described in the programmer manual Synchronization Methods section. Upon completion of
              the mask test, event code 2600 ('Mask testing complete') is queued to the event queue.
              To specify an event, use the command ``ACTONEVENT:EVENTTYPE``.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SRQ:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:SRQ:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACTONEVent:ACTION:SRQ:STATE value``
              command.

        SCPI Syntax:
            ```
            - ACTONEVent:ACTION:SRQ:STATE <0|1|OFF|ON>
            - ACTONEVent:ACTION:SRQ:STATE?
            ```

        Info:
            - ``1, ON`` generates an SRQ when the specified event occurs.
            - ``0, OFF`` turns off this action.
        """
        return self._state


class ActoneventActionSavewfmState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:ACTION:SAVEWFM:STATE`` command.

    Description:
        - Saves the currently selected waveform data to a file when a specified event occurs, or
          queries the state of the 'save waveform to file' action. The default state is 0 (off). To
          specify an event, use the command ``ACTONEVENT:EVENTTYPE``.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SAVEWFM:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:SAVEWFM:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:ACTION:SAVEWFM:STATE value``
          command.

    SCPI Syntax:
        ```
        - ACTONEVent:ACTION:SAVEWFM:STATE <0|1|OFF|ON>
        - ACTONEVent:ACTION:SAVEWFM:STATE?
        ```

    Info:
        - ``1, ON`` saves the waveform to a file when the specified event occurs.
        - ``0, OFF`` turns off this action.
    """


class ActoneventActionSavewfm(SCPICmdRead):
    """The ``ACTONEVent:ACTION:SAVEWFM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SAVEWFM?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:SAVEWFM?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:ACTION:SAVEWFM:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventActionSavewfmState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventActionSavewfmState:
        """Return the ``ACTONEVent:ACTION:SAVEWFM:STATE`` command.

        Description:
            - Saves the currently selected waveform data to a file when a specified event occurs, or
              queries the state of the 'save waveform to file' action. The default state is 0 (off).
              To specify an event, use the command ``ACTONEVENT:EVENTTYPE``.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SAVEWFM:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:SAVEWFM:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:ACTION:SAVEWFM:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:ACTION:SAVEWFM:STATE <0|1|OFF|ON>
            - ACTONEVent:ACTION:SAVEWFM:STATE?
            ```

        Info:
            - ``1, ON`` saves the waveform to a file when the specified event occurs.
            - ``0, OFF`` turns off this action.
        """
        return self._state


class ActoneventActionSaveimageState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:ACTION:SAVEIMAGE:STATE`` command.

    Description:
        - Saves a screen image to file when a specified event occurs, or queries the state of the
          'save screen image to a file' action. The default state is 0 (off). To specify an event,
          use the command ``ACTONEVENT:EVENTTYPE``.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SAVEIMAGE:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:SAVEIMAGE:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:ACTION:SAVEIMAGE:STATE value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:ACTION:SAVEIMAGE:STATE <0|1|OFF|ON>
        - ACTONEVent:ACTION:SAVEIMAGE:STATE?
        ```

    Info:
        - ``1, ON`` saves a screen image to a file when the specified event occurs.
        - ``0, OFF`` turns off this action.
    """


class ActoneventActionSaveimage(SCPICmdRead):
    """The ``ACTONEVent:ACTION:SAVEIMAGE`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SAVEIMAGE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:SAVEIMAGE?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:ACTION:SAVEIMAGE:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventActionSaveimageState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventActionSaveimageState:
        """Return the ``ACTONEVent:ACTION:SAVEIMAGE:STATE`` command.

        Description:
            - Saves a screen image to file when a specified event occurs, or queries the state of
              the 'save screen image to a file' action. The default state is 0 (off). To specify an
              event, use the command ``ACTONEVENT:EVENTTYPE``.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SAVEIMAGE:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:ACTION:SAVEIMAGE:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:ACTION:SAVEIMAGE:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:ACTION:SAVEIMAGE:STATE <0|1|OFF|ON>
            - ACTONEVent:ACTION:SAVEIMAGE:STATE?
            ```

        Info:
            - ``1, ON`` saves a screen image to a file when the specified event occurs.
            - ``0, OFF`` turns off this action.
        """
        return self._state


class ActoneventActionPrintState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:ACTION:PRINT:STATE`` command.

    Description:
        - Sends a screen image to a printer when a specified event occurs, or queries the state of
          the 'send screen image' action. The default state is 0 (off). To specify an event, use the
          command ``ACTONEVENT:EVENTTYPE``.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:PRINT:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:PRINT:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:ACTION:PRINT:STATE value``
          command.

    SCPI Syntax:
        ```
        - ACTONEVent:ACTION:PRINT:STATE <0|1|OFF|ON>
        - ACTONEVent:ACTION:PRINT:STATE?
        ```

    Info:
        - ``1, ON`` sends a screen image to the printer when the specified event occurs.
        - ``0, OFF`` turns off this action.
    """


class ActoneventActionPrint(SCPICmdRead):
    """The ``ACTONEVent:ACTION:PRINT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:PRINT?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:PRINT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:ACTION:PRINT:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventActionPrintState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventActionPrintState:
        """Return the ``ACTONEVent:ACTION:PRINT:STATE`` command.

        Description:
            - Sends a screen image to a printer when a specified event occurs, or queries the state
              of the 'send screen image' action. The default state is 0 (off). To specify an event,
              use the command ``ACTONEVENT:EVENTTYPE``.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:PRINT:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:PRINT:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:ACTION:PRINT:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:ACTION:PRINT:STATE <0|1|OFF|ON>
            - ACTONEVent:ACTION:PRINT:STATE?
            ```

        Info:
            - ``1, ON`` sends a screen image to the printer when the specified event occurs.
            - ``0, OFF`` turns off this action.
        """
        return self._state


class ActoneventActionEmailState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:ACTION:EMAIL:STATE`` command.

    Description:
        - Sends an email when a specified event occurs, or queries the state of the 'send email'
          action. The default state is 0 (off). To specify an email address for the recipient, use
          the command ``ACTONEVENT:ACTION:EMAIL:SETUP:TOADDRESS To`` specify an event, use the
          command ``ACTONEVENT:EVENTTYPE``.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:EMAIL:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:EMAIL:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:ACTION:EMAIL:STATE value``
          command.

    SCPI Syntax:
        ```
        - ACTONEVent:ACTION:EMAIL:STATE <0|1|OFF|ON>
        - ACTONEVent:ACTION:EMAIL:STATE?
        ```

    Info:
        - ``1, ON`` sends an email when the specified event occurs.
        - ``0, OFF`` turns off this action.
    """


class ActoneventActionEmailSetupToaddress(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess`` command.

    Description:
        - Sets (or queries) the email address for the recipient when the
          ``ACTONEVENT:ACTION:EMAIL:STATE`` command is used. To set up the email address for the
          sender, use ``EMAIL:SETUP:FROMADDRESS``.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess value`` command.

    SCPI Syntax:
        ```
        - ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess <QString>
        - ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess?
        ```
    """

    _WRAP_ARG_WITH_QUOTES = True


class ActoneventActionEmailSetup(SCPICmdRead):
    """The ``ACTONEVent:ACTION:EMAIL:SETUp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:EMAIL:SETUp?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:EMAIL:SETUp?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.toaddress``: The ``ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._toaddress = ActoneventActionEmailSetupToaddress(
            device, f"{self._cmd_syntax}:TOADDRess"
        )

    @property
    def toaddress(self) -> ActoneventActionEmailSetupToaddress:
        """Return the ``ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess`` command.

        Description:
            - Sets (or queries) the email address for the recipient when the
              ``ACTONEVENT:ACTION:EMAIL:STATE`` command is used. To set up the email address for the
              sender, use ``EMAIL:SETUP:FROMADDRESS``.

        Usage:
            - Using the ``.query()`` method will send the
              ``ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess?`` query.
            - Using the ``.verify(value)`` method will send the
              ``ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess <QString>
            - ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess?
            ```
        """
        return self._toaddress


class ActoneventActionEmail(SCPICmdRead):
    """The ``ACTONEVent:ACTION:EMAIL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:EMAIL?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:EMAIL?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.setup``: The ``ACTONEVent:ACTION:EMAIL:SETUp`` command tree.
        - ``.state``: The ``ACTONEVent:ACTION:EMAIL:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._setup = ActoneventActionEmailSetup(device, f"{self._cmd_syntax}:SETUp")
        self._state = ActoneventActionEmailState(device, f"{self._cmd_syntax}:STATE")

    @property
    def setup(self) -> ActoneventActionEmailSetup:
        """Return the ``ACTONEVent:ACTION:EMAIL:SETUp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:EMAIL:SETUp?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:EMAIL:SETUp?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.toaddress``: The ``ACTONEVent:ACTION:EMAIL:SETUp:TOADDRess`` command.
        """
        return self._setup

    @property
    def state(self) -> ActoneventActionEmailState:
        """Return the ``ACTONEVent:ACTION:EMAIL:STATE`` command.

        Description:
            - Sends an email when a specified event occurs, or queries the state of the 'send email'
              action. The default state is 0 (off). To specify an email address for the recipient,
              use the command ``ACTONEVENT:ACTION:EMAIL:SETUP:TOADDRESS To`` specify an event, use
              the command ``ACTONEVENT:EVENTTYPE``.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:EMAIL:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:EMAIL:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:ACTION:EMAIL:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:ACTION:EMAIL:STATE <0|1|OFF|ON>
            - ACTONEVent:ACTION:EMAIL:STATE?
            ```

        Info:
            - ``1, ON`` sends an email when the specified event occurs.
            - ``0, OFF`` turns off this action.
        """
        return self._state


class ActoneventActionAuxoutState(SCPICmdWrite, SCPICmdRead):
    """The ``ACTONEVent:ACTION:AUXOUT:STATE`` command.

    Description:
        - Sends a pulse to the Auxiliary Out port when a specified event occurs, or queries the
          state of the 'pulse to aux out' action. The default state is 0 (off). To specify an event,
          use the command ``ACTONEVENT:EVENTTYPE``.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:AUXOUT:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:AUXOUT:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ACTONEVent:ACTION:AUXOUT:STATE value``
          command.

    SCPI Syntax:
        ```
        - ACTONEVent:ACTION:AUXOUT:STATE <0|1|OFF|ON>
        - ACTONEVent:ACTION:AUXOUT:STATE?
        ```

    Info:
        - ``1, ON`` sends a pulse to the Auxiliary Out port when the specified event occurs.
        - ``0, OFF`` turns off this action.
    """


class ActoneventActionAuxout(SCPICmdRead):
    """The ``ACTONEVent:ACTION:AUXOUT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:AUXOUT?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:AUXOUT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``ACTONEVent:ACTION:AUXOUT:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ActoneventActionAuxoutState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ActoneventActionAuxoutState:
        """Return the ``ACTONEVent:ACTION:AUXOUT:STATE`` command.

        Description:
            - Sends a pulse to the Auxiliary Out port when a specified event occurs, or queries the
              state of the 'pulse to aux out' action. The default state is 0 (off). To specify an
              event, use the command ``ACTONEVENT:EVENTTYPE``.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:AUXOUT:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:AUXOUT:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``ACTONEVent:ACTION:AUXOUT:STATE value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:ACTION:AUXOUT:STATE <0|1|OFF|ON>
            - ACTONEVent:ACTION:AUXOUT:STATE?
            ```

        Info:
            - ``1, ON`` sends a pulse to the Auxiliary Out port when the specified event occurs.
            - ``0, OFF`` turns off this action.
        """
        return self._state


#  pylint: disable=too-many-instance-attributes
class ActoneventAction(SCPICmdRead):
    """The ``ACTONEVent:ACTION`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent:ACTION?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.auxout``: The ``ACTONEVent:ACTION:AUXOUT`` command tree.
        - ``.email``: The ``ACTONEVent:ACTION:EMAIL`` command tree.
        - ``.print``: The ``ACTONEVent:ACTION:PRINT`` command tree.
        - ``.saveimage``: The ``ACTONEVent:ACTION:SAVEIMAGE`` command tree.
        - ``.savewfm``: The ``ACTONEVent:ACTION:SAVEWFM`` command tree.
        - ``.srq``: The ``ACTONEVent:ACTION:SRQ`` command tree.
        - ``.stopacq``: The ``ACTONEVent:ACTION:STOPACQ`` command tree.
        - ``.visual``: The ``ACTONEVent:ACTION:VISUAL`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._auxout = ActoneventActionAuxout(device, f"{self._cmd_syntax}:AUXOUT")
        self._email = ActoneventActionEmail(device, f"{self._cmd_syntax}:EMAIL")
        self._print = ActoneventActionPrint(device, f"{self._cmd_syntax}:PRINT")
        self._saveimage = ActoneventActionSaveimage(device, f"{self._cmd_syntax}:SAVEIMAGE")
        self._savewfm = ActoneventActionSavewfm(device, f"{self._cmd_syntax}:SAVEWFM")
        self._srq = ActoneventActionSrq(device, f"{self._cmd_syntax}:SRQ")
        self._stopacq = ActoneventActionStopacq(device, f"{self._cmd_syntax}:STOPACQ")
        self._visual = ActoneventActionVisual(device, f"{self._cmd_syntax}:VISUAL")

    @property
    def auxout(self) -> ActoneventActionAuxout:
        """Return the ``ACTONEVent:ACTION:AUXOUT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:AUXOUT?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:AUXOUT?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:ACTION:AUXOUT:STATE`` command.
        """
        return self._auxout

    @property
    def email(self) -> ActoneventActionEmail:
        """Return the ``ACTONEVent:ACTION:EMAIL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:EMAIL?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:EMAIL?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.setup``: The ``ACTONEVent:ACTION:EMAIL:SETUp`` command tree.
            - ``.state``: The ``ACTONEVent:ACTION:EMAIL:STATE`` command.
        """
        return self._email

    @property
    def print(self) -> ActoneventActionPrint:
        """Return the ``ACTONEVent:ACTION:PRINT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:PRINT?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:PRINT?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:ACTION:PRINT:STATE`` command.
        """
        return self._print

    @property
    def saveimage(self) -> ActoneventActionSaveimage:
        """Return the ``ACTONEVent:ACTION:SAVEIMAGE`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SAVEIMAGE?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:SAVEIMAGE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:ACTION:SAVEIMAGE:STATE`` command.
        """
        return self._saveimage

    @property
    def savewfm(self) -> ActoneventActionSavewfm:
        """Return the ``ACTONEVent:ACTION:SAVEWFM`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SAVEWFM?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:SAVEWFM?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:ACTION:SAVEWFM:STATE`` command.
        """
        return self._savewfm

    @property
    def srq(self) -> ActoneventActionSrq:
        """Return the ``ACTONEVent:ACTION:SRQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:SRQ?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:SRQ?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:ACTION:SRQ:STATE`` command.
        """
        return self._srq

    @property
    def stopacq(self) -> ActoneventActionStopacq:
        """Return the ``ACTONEVent:ACTION:STOPACQ`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:STOPACQ?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:STOPACQ?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:ACTION:STOPACQ:STATE`` command.
        """
        return self._stopacq

    @property
    def visual(self) -> ActoneventActionVisual:
        """Return the ``ACTONEVent:ACTION:VISUAL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION:VISUAL?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION:VISUAL?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``ACTONEVent:ACTION:VISUAL:STATE`` command.
        """
        return self._visual


class Actonevent(SCPICmdRead):
    """The ``ACTONEVent`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ACTONEVent?`` query.
        - Using the ``.verify(value)`` method will send the ``ACTONEVent?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.action``: The ``ACTONEVent:ACTION`` command tree.
        - ``.eventtype``: The ``ACTONEVent:EVENTTYPe`` command.
        - ``.numacqs``: The ``ACTONEVent:NUMACQs`` command.
        - ``.repeatcount``: The ``ACTONEVent:REPEATCount`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "ACTONEVent"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._action = ActoneventAction(device, f"{self._cmd_syntax}:ACTION")
        self._eventtype = ActoneventEventtype(device, f"{self._cmd_syntax}:EVENTTYPe")
        self._numacqs = ActoneventNumacqs(device, f"{self._cmd_syntax}:NUMACQs")
        self._repeatcount = ActoneventRepeatcount(device, f"{self._cmd_syntax}:REPEATCount")

    @property
    def action(self) -> ActoneventAction:
        """Return the ``ACTONEVent:ACTION`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:ACTION?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:ACTION?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.auxout``: The ``ACTONEVent:ACTION:AUXOUT`` command tree.
            - ``.email``: The ``ACTONEVent:ACTION:EMAIL`` command tree.
            - ``.print``: The ``ACTONEVent:ACTION:PRINT`` command tree.
            - ``.saveimage``: The ``ACTONEVent:ACTION:SAVEIMAGE`` command tree.
            - ``.savewfm``: The ``ACTONEVent:ACTION:SAVEWFM`` command tree.
            - ``.srq``: The ``ACTONEVent:ACTION:SRQ`` command tree.
            - ``.stopacq``: The ``ACTONEVent:ACTION:STOPACQ`` command tree.
            - ``.visual``: The ``ACTONEVent:ACTION:VISUAL`` command tree.
        """
        return self._action

    @property
    def eventtype(self) -> ActoneventEventtype:
        """Return the ``ACTONEVent:EVENTTYPe`` command.

        Description:
            - Specifies (or queries) which event to act on (TRIGger, ACQCOMPLete, or NONe) when
              using an Act on Event command. The default is NONe. To specify the action to take, use
              the ``ACTONEVent:ACTION`` commands.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:EVENTTYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:EVENTTYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACTONEVent:EVENTTYPe value``
              command.

        SCPI Syntax:
            ```
            - ACTONEVent:EVENTTYPe <NONe|TRIGger|ACQCOMPLete>
            - ACTONEVent:EVENTTYPe?
            ```

        Info:
            - ``NONe`` no event (this is the default).
            - ``TRIGger`` specifies to act when a trigger occurs.
            - ``ACQCOMPLete`` specifies to act when acquisition completes.
        """
        return self._eventtype

    @property
    def numacqs(self) -> ActoneventNumacqs:
        """Return the ``ACTONEVent:NUMACQs`` command.

        Description:
            - Sets (or queries) the number of acquisitions to complete for the event type
              ACQCOMPLete. The default is 1 acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:NUMACQs?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:NUMACQs?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACTONEVent:NUMACQs value`` command.

        SCPI Syntax:
            ```
            - ACTONEVent:NUMACQs <NR1>
            - ACTONEVent:NUMACQs?
            ```
        """
        return self._numacqs

    @property
    def repeatcount(self) -> ActoneventRepeatcount:
        """Return the ``ACTONEVent:REPEATCount`` command.

        Description:
            - Sets or returns the number of events to run.

        Usage:
            - Using the ``.query()`` method will send the ``ACTONEVent:REPEATCount?`` query.
            - Using the ``.verify(value)`` method will send the ``ACTONEVent:REPEATCount?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ACTONEVent:REPEATCount value``
              command.

        SCPI Syntax:
            ```
            - ACTONEVent:REPEATCount <NR1>
            - ACTONEVent:REPEATCount?
            ```

        Info:
            - ``NR1`` is an integer that specifies the number of events to run. The default is 1
              event and the maximum is 1000000 events. A repeat count greater than 1000000 specifies
              to run forever. In this case, the action on event can be terminated by setting the
              state for all actions to OFF. When the repeat count is set to infinite, the query
              returns 9.9E+37 (IEEE positive infinity).
        """
        return self._repeatcount
