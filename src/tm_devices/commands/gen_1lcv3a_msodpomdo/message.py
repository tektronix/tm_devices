"""The message commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MESSage
    - MESSage:BOX <X1>,<Y1>[,<X2>,<Y2>]
    - MESSage:BOX?
    - MESSage:CLEAR
    - MESSage:SHOW <QString>
    - MESSage:SHOW?
    - MESSage:STATE {ON|OFF|<NR1>}
    - MESSage:STATE?
    - MESSage?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MessageState(SCPICmdWrite, SCPICmdRead):
    """The ``MESSage:STATE`` command.

    Description:
        - Controls the display of the message box.

    Usage:
        - Using the ``.query()`` method will send the ``MESSage:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``MESSage:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MESSage:STATE value`` command.

    SCPI Syntax:
        ```
        - MESSage:STATE {ON|OFF|<NR1>}
        - MESSage:STATE?
        ```

    Info:
        - ``OFF or <NR1> = 0`` removes the message window from the screen.
        - ``ON or <NR1> ≠ 0`` displays the message window and its contents on the screen.
    """


class MessageShow(SCPICmdWrite, SCPICmdRead):
    """The ``MESSage:SHOW`` command.

    Description:
        - This command specifies the contents of the message box. ``MESSage:SHOW`` <Qstring> defines
          the content of the message box. Change in string length causes automatic resize of the
          message box to fit the text. The box may be resized using the ``MESSAGE:BOX`` command. The
          ``MESSAGE:STATE`` command is used to turn on and off the message box display.

    Usage:
        - Using the ``.query()`` method will send the ``MESSage:SHOW?`` query.
        - Using the ``.verify(value)`` method will send the ``MESSage:SHOW?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MESSage:SHOW value`` command.

    SCPI Syntax:
        ```
        - MESSage:SHOW <QString>
        - MESSage:SHOW?
        ```

    Info:
        - ``<QString>`` is the message and can include any of the characters shown in the Character
          Set.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MessageClear(SCPICmdWriteNoArguments):
    """The ``MESSage:CLEAR`` command.

    Description:
        - Clears the contents of the message box.

    Usage:
        - Using the ``.write()`` method will send the ``MESSage:CLEAR`` command.

    SCPI Syntax:
        ```
        - MESSage:CLEAR
        ```
    """


class MessageBox(SCPICmdWrite, SCPICmdRead):
    """The ``MESSage:BOX`` command.

    Description:
        - This command specifies the co-ordinates of the message box. This command does not display
          the message unless ``MESSage:STATE`` is on. X1 and Y1 are the screen coordinates of the
          top left corner of the message box. X2 and Y2 are the screen coordinates of the bottom
          right corner of the message box. All four coordinates are returned by the query. Changing
          the text in the message box, using the ``MESSAGE:SHOW`` command, automatically resizes the
          message box. If you want a custom message box size, send the ``MESSAGE:BOX`` command after
          changing the text using the ``MESSAGE:SHOW`` command. Message box settings and data are
          saved and restored in saved setups.

    Usage:
        - Using the ``.query()`` method will send the ``MESSage:BOX?`` query.
        - Using the ``.verify(value)`` method will send the ``MESSage:BOX?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MESSage:BOX value`` command.

    SCPI Syntax:
        ```
        - MESSage:BOX <X1>,<Y1>[,<X2>,<Y2>]
        - MESSage:BOX?
        ```

    Info:
        - ``<X1>`` and <X2> = 0 to 1023, and are pixel positions along the horizontal axis. <X1>
          defines the left and <X2> defines the right side of the window.
        - ``<Y1>`` and <Y2> = 0 to 767, and are pixel positions along the vertical axis. <Y1>
          defines the top and <Y2> defines the bottom of the window. The reserved height of all
          characters is 16 pixels so the window must be at least that high to fully display
          characters. <X2> and <Y2> are optional because the ``MESSAGE:SHOW`` command automatically
          sizes the box to fit the message. All four values are returned in a query.
    """


class Message(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``MESSage`` command.

    Description:
        - This command sets or queries message box (screen annotation) parameters.

    Usage:
        - Using the ``.query()`` method will send the ``MESSage?`` query.
        - Using the ``.verify(value)`` method will send the ``MESSage?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``MESSage`` command.

    SCPI Syntax:
        ```
        - MESSage
        - MESSage?
        ```

    Properties:
        - ``.box``: The ``MESSage:BOX`` command.
        - ``.clear``: The ``MESSage:CLEAR`` command.
        - ``.show``: The ``MESSage:SHOW`` command.
        - ``.state``: The ``MESSage:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MESSage") -> None:
        super().__init__(device, cmd_syntax)
        self._box = MessageBox(device, f"{self._cmd_syntax}:BOX")
        self._clear = MessageClear(device, f"{self._cmd_syntax}:CLEAR")
        self._show = MessageShow(device, f"{self._cmd_syntax}:SHOW")
        self._state = MessageState(device, f"{self._cmd_syntax}:STATE")

    @property
    def box(self) -> MessageBox:
        """Return the ``MESSage:BOX`` command.

        Description:
            - This command specifies the co-ordinates of the message box. This command does not
              display the message unless ``MESSage:STATE`` is on. X1 and Y1 are the screen
              coordinates of the top left corner of the message box. X2 and Y2 are the screen
              coordinates of the bottom right corner of the message box. All four coordinates are
              returned by the query. Changing the text in the message box, using the
              ``MESSAGE:SHOW`` command, automatically resizes the message box. If you want a custom
              message box size, send the ``MESSAGE:BOX`` command after changing the text using the
              ``MESSAGE:SHOW`` command. Message box settings and data are saved and restored in
              saved setups.

        Usage:
            - Using the ``.query()`` method will send the ``MESSage:BOX?`` query.
            - Using the ``.verify(value)`` method will send the ``MESSage:BOX?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MESSage:BOX value`` command.

        SCPI Syntax:
            ```
            - MESSage:BOX <X1>,<Y1>[,<X2>,<Y2>]
            - MESSage:BOX?
            ```

        Info:
            - ``<X1>`` and <X2> = 0 to 1023, and are pixel positions along the horizontal axis. <X1>
              defines the left and <X2> defines the right side of the window.
            - ``<Y1>`` and <Y2> = 0 to 767, and are pixel positions along the vertical axis. <Y1>
              defines the top and <Y2> defines the bottom of the window. The reserved height of all
              characters is 16 pixels so the window must be at least that high to fully display
              characters. <X2> and <Y2> are optional because the ``MESSAGE:SHOW`` command
              automatically sizes the box to fit the message. All four values are returned in a
              query.
        """
        return self._box

    @property
    def clear(self) -> MessageClear:
        """Return the ``MESSage:CLEAR`` command.

        Description:
            - Clears the contents of the message box.

        Usage:
            - Using the ``.write()`` method will send the ``MESSage:CLEAR`` command.

        SCPI Syntax:
            ```
            - MESSage:CLEAR
            ```
        """
        return self._clear

    @property
    def show(self) -> MessageShow:
        """Return the ``MESSage:SHOW`` command.

        Description:
            - This command specifies the contents of the message box. ``MESSage:SHOW`` <Qstring>
              defines the content of the message box. Change in string length causes automatic
              resize of the message box to fit the text. The box may be resized using the
              ``MESSAGE:BOX`` command. The ``MESSAGE:STATE`` command is used to turn on and off the
              message box display.

        Usage:
            - Using the ``.query()`` method will send the ``MESSage:SHOW?`` query.
            - Using the ``.verify(value)`` method will send the ``MESSage:SHOW?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MESSage:SHOW value`` command.

        SCPI Syntax:
            ```
            - MESSage:SHOW <QString>
            - MESSage:SHOW?
            ```

        Info:
            - ``<QString>`` is the message and can include any of the characters shown in the
              Character Set.
        """
        return self._show

    @property
    def state(self) -> MessageState:
        """Return the ``MESSage:STATE`` command.

        Description:
            - Controls the display of the message box.

        Usage:
            - Using the ``.query()`` method will send the ``MESSage:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``MESSage:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MESSage:STATE value`` command.

        SCPI Syntax:
            ```
            - MESSage:STATE {ON|OFF|<NR1>}
            - MESSage:STATE?
            ```

        Info:
            - ``OFF or <NR1> = 0`` removes the message window from the screen.
            - ``ON or <NR1> ≠ 0`` displays the message window and its contents on the screen.
        """
        return self._state
