"""The ref commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - REF:ADDNew <QString>
    - REF:DELete <QString>
    - REF:LIST?
    - REF:REF<x>:DESKew <NR3>
    - REF:REF<x>:LABel:COLor <QString>
    - REF:REF<x>:LABel:COLor?
    - REF:REF<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
    - REF:REF<x>:LABel:FONT:BOLD?
    - REF:REF<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
    - REF:REF<x>:LABel:FONT:ITALic?
    - REF:REF<x>:LABel:FONT:SIZE <NR1>
    - REF:REF<x>:LABel:FONT:SIZE?
    - REF:REF<x>:LABel:FONT:TYPE <QString>
    - REF:REF<x>:LABel:FONT:TYPE?
    - REF:REF<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
    - REF:REF<x>:LABel:FONT:UNDERline?
    - REF:REF<x>:LABel:NAMe <QString>
    - REF:REF<x>:LABel:NAMe?
    - REF:REF<x>:LABel:XPOS <NR1>
    - REF:REF<x>:LABel:XPOS?
    - REF:REF<x>:LABel:YPOS <NR1>
    - REF:REF<x>:LABel:YPOS?
    - REF:REF<x>:SOUrce <QString>
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class RefRefItemSource(SCPICmdWrite):
    """The ``REF:REF<x>:SOUrce`` command.

    Description:
        - This command sets or queries the filename used by the given reference.

    Usage:
        - Using the ``.write(value)`` method will send the ``REF:REF<x>:SOUrce value`` command.

    SCPI Syntax:
        ```
        - REF:REF<x>:SOUrce <QString>
        ```

    Info:
        - ``<QString>`` is the reference file name.
    """

    _WRAP_ARG_WITH_QUOTES = True


class RefRefItemLabelYpos(SCPICmdWrite, SCPICmdRead):
    """The ``REF:REF<x>:LABel:YPOS`` command.

    Description:
        - This command sets or queries the Y-position of the label (attached to the displayed
          waveform of the specified reference), relative to the baseline of the waveform. The
          reference waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:YPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:YPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:YPOS value`` command.

    SCPI Syntax:
        ```
        - REF:REF<x>:LABel:YPOS <NR1>
        - REF:REF<x>:LABel:YPOS?
        ```

    Info:
        - ``<NR1>`` is the location where the waveform label for the selected reference is
          displayed, relative to the baseline of the waveform.
    """


class RefRefItemLabelXpos(SCPICmdWrite, SCPICmdRead):
    """The ``REF:REF<x>:LABel:XPOS`` command.

    Description:
        - This command sets or queries the X-position at which the label (attached to the displayed
          waveform of the specified reference) is displayed, relative to the left edge of the
          waveview. The reference waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:XPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:XPOS value`` command.

    SCPI Syntax:
        ```
        - REF:REF<x>:LABel:XPOS <NR1>
        - REF:REF<x>:LABel:XPOS?
        ```

    Info:
        - ``<NR1>`` is the location (control in divisions) where the waveform label for the selected
          reference is displayed, relative to the left edge of the screen.
    """


class RefRefItemLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``REF:REF<x>:LABel:NAMe`` command.

    Description:
        - This command sets or queries the label of the specified reference. The reference waveform
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:NAMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:NAMe value`` command.

    SCPI Syntax:
        ```
        - REF:REF<x>:LABel:NAMe <QString>
        - REF:REF<x>:LABel:NAMe?
        ```

    Info:
        - ``<QString>`` is the character string that will be used for the reference waveform label
          name.
    """

    _WRAP_ARG_WITH_QUOTES = True


class RefRefItemLabelFontUnderline(SCPICmdWrite, SCPICmdRead):
    """The ``REF:REF<x>:LABel:FONT:UNDERline`` command.

    Description:
        - This command sets or queries the underline state of the specified reference label.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT:UNDERline?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT:UNDERline?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:FONT:UNDERline value``
          command.

    SCPI Syntax:
        ```
        - REF:REF<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
        - REF:REF<x>:LABel:FONT:UNDERline?
        ```

    Info:
        - ``<NR1>`` = 0 disables underline font; any other value turns this feature on.
        - ``OFF`` disables underline font.
        - ``ON`` enables underline font.
    """


class RefRefItemLabelFontType(SCPICmdWrite, SCPICmdRead):
    """The ``REF:REF<x>:LABel:FONT:TYPE`` command.

    Description:
        - This command sets or queries the font type of the specified reference label, such as Arial
          or Times New Roman.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT:TYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:FONT:TYPE value``
          command.

    SCPI Syntax:
        ```
        - REF:REF<x>:LABel:FONT:TYPE <QString>
        - REF:REF<x>:LABel:FONT:TYPE?
        ```

    Info:
        - ``<QString>`` is the font type.
    """

    _WRAP_ARG_WITH_QUOTES = True


class RefRefItemLabelFontSize(SCPICmdWrite, SCPICmdRead):
    """The ``REF:REF<x>:LABel:FONT:SIZE`` command.

    Description:
        - This command sets or queries the font size of the specified reference label.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT:SIZE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:FONT:SIZE value``
          command.

    SCPI Syntax:
        ```
        - REF:REF<x>:LABel:FONT:SIZE <NR1>
        - REF:REF<x>:LABel:FONT:SIZE?
        ```

    Info:
        - ``<NR1>`` is the font size of the label.
    """


class RefRefItemLabelFontItalic(SCPICmdWrite, SCPICmdRead):
    """The ``REF:REF<x>:LABel:FONT:ITALic`` command.

    Description:
        - This command sets or queries the italic state of the specified reference label.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT:ITALic?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT:ITALic?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:FONT:ITALic value``
          command.

    SCPI Syntax:
        ```
        - REF:REF<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
        - REF:REF<x>:LABel:FONT:ITALic?
        ```

    Info:
        - ``<NR1>`` = 0 disables italic font; any other value turns this feature on.
        - ``OFF`` disables italic font.
        - ``ON`` enables italic font.
    """


class RefRefItemLabelFontBold(SCPICmdWrite, SCPICmdRead):
    """The ``REF:REF<x>:LABel:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the specified reference label.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT:BOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT:BOLD?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:FONT:BOLD value``
          command.

    SCPI Syntax:
        ```
        - REF:REF<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
        - REF:REF<x>:LABel:FONT:BOLD?
        ```

    Info:
        - ``<NR1>`` = 0 disables bold font; any other value turns this feature on.
        - ``OFF`` disables bold font.
        - ``ON`` enables bold font.
    """


class RefRefItemLabelFont(SCPICmdRead):
    """The ``REF:REF<x>:LABel:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bold``: The ``REF:REF<x>:LABel:FONT:BOLD`` command.
        - ``.italic``: The ``REF:REF<x>:LABel:FONT:ITALic`` command.
        - ``.size``: The ``REF:REF<x>:LABel:FONT:SIZE`` command.
        - ``.type``: The ``REF:REF<x>:LABel:FONT:TYPE`` command.
        - ``.underline``: The ``REF:REF<x>:LABel:FONT:UNDERline`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = RefRefItemLabelFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = RefRefItemLabelFontItalic(device, f"{self._cmd_syntax}:ITALic")
        self._size = RefRefItemLabelFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = RefRefItemLabelFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = RefRefItemLabelFontUnderline(device, f"{self._cmd_syntax}:UNDERline")

    @property
    def bold(self) -> RefRefItemLabelFontBold:
        """Return the ``REF:REF<x>:LABel:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the specified reference label.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT:BOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT:BOLD?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:FONT:BOLD value``
              command.

        SCPI Syntax:
            ```
            - REF:REF<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
            - REF:REF<x>:LABel:FONT:BOLD?
            ```

        Info:
            - ``<NR1>`` = 0 disables bold font; any other value turns this feature on.
            - ``OFF`` disables bold font.
            - ``ON`` enables bold font.
        """
        return self._bold

    @property
    def italic(self) -> RefRefItemLabelFontItalic:
        """Return the ``REF:REF<x>:LABel:FONT:ITALic`` command.

        Description:
            - This command sets or queries the italic state of the specified reference label.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT:ITALic?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT:ITALic?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REF:REF<x>:LABel:FONT:ITALic value`` command.

        SCPI Syntax:
            ```
            - REF:REF<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
            - REF:REF<x>:LABel:FONT:ITALic?
            ```

        Info:
            - ``<NR1>`` = 0 disables italic font; any other value turns this feature on.
            - ``OFF`` disables italic font.
            - ``ON`` enables italic font.
        """
        return self._italic

    @property
    def size(self) -> RefRefItemLabelFontSize:
        """Return the ``REF:REF<x>:LABel:FONT:SIZE`` command.

        Description:
            - This command sets or queries the font size of the specified reference label.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT:SIZE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:FONT:SIZE value``
              command.

        SCPI Syntax:
            ```
            - REF:REF<x>:LABel:FONT:SIZE <NR1>
            - REF:REF<x>:LABel:FONT:SIZE?
            ```

        Info:
            - ``<NR1>`` is the font size of the label.
        """
        return self._size

    @property
    def type(self) -> RefRefItemLabelFontType:
        """Return the ``REF:REF<x>:LABel:FONT:TYPE`` command.

        Description:
            - This command sets or queries the font type of the specified reference label, such as
              Arial or Times New Roman.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:FONT:TYPE value``
              command.

        SCPI Syntax:
            ```
            - REF:REF<x>:LABel:FONT:TYPE <QString>
            - REF:REF<x>:LABel:FONT:TYPE?
            ```

        Info:
            - ``<QString>`` is the font type.
        """
        return self._type

    @property
    def underline(self) -> RefRefItemLabelFontUnderline:
        """Return the ``REF:REF<x>:LABel:FONT:UNDERline`` command.

        Description:
            - This command sets or queries the underline state of the specified reference label.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT:UNDERline?``
              query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT:UNDERline?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``REF:REF<x>:LABel:FONT:UNDERline value`` command.

        SCPI Syntax:
            ```
            - REF:REF<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
            - REF:REF<x>:LABel:FONT:UNDERline?
            ```

        Info:
            - ``<NR1>`` = 0 disables underline font; any other value turns this feature on.
            - ``OFF`` disables underline font.
            - ``ON`` enables underline font.
        """
        return self._underline


class RefRefItemLabelColor(SCPICmdWrite, SCPICmdRead):
    """The ``REF:REF<x>:LABel:COLor`` command.

    Description:
        - This command sets or queries the color of the specified ref label.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:COLor?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:COLor?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:COLor value`` command.

    SCPI Syntax:
        ```
        - REF:REF<x>:LABel:COLor <QString>
        - REF:REF<x>:LABel:COLor?
        ```

    Info:
        - ``<QString>`` is the label. To return the color to the default color, send an empty string
          as in this example: ``:REF:REF1:LABEL:COLOR`` ''.
    """

    _WRAP_ARG_WITH_QUOTES = True


class RefRefItemLabel(SCPICmdRead):
    """The ``REF:REF<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.color``: The ``REF:REF<x>:LABel:COLor`` command.
        - ``.font``: The ``REF:REF<x>:LABel:FONT`` command tree.
        - ``.name``: The ``REF:REF<x>:LABel:NAMe`` command.
        - ``.xpos``: The ``REF:REF<x>:LABel:XPOS`` command.
        - ``.ypos``: The ``REF:REF<x>:LABel:YPOS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._color = RefRefItemLabelColor(device, f"{self._cmd_syntax}:COLor")
        self._font = RefRefItemLabelFont(device, f"{self._cmd_syntax}:FONT")
        self._name = RefRefItemLabelName(device, f"{self._cmd_syntax}:NAMe")
        self._xpos = RefRefItemLabelXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = RefRefItemLabelYpos(device, f"{self._cmd_syntax}:YPOS")

    @property
    def color(self) -> RefRefItemLabelColor:
        """Return the ``REF:REF<x>:LABel:COLor`` command.

        Description:
            - This command sets or queries the color of the specified ref label.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:COLor?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:COLor?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:COLor value``
              command.

        SCPI Syntax:
            ```
            - REF:REF<x>:LABel:COLor <QString>
            - REF:REF<x>:LABel:COLor?
            ```

        Info:
            - ``<QString>`` is the label. To return the color to the default color, send an empty
              string as in this example: ``:REF:REF1:LABEL:COLOR`` ''.
        """
        return self._color

    @property
    def font(self) -> RefRefItemLabelFont:
        """Return the ``REF:REF<x>:LABel:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:FONT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bold``: The ``REF:REF<x>:LABel:FONT:BOLD`` command.
            - ``.italic``: The ``REF:REF<x>:LABel:FONT:ITALic`` command.
            - ``.size``: The ``REF:REF<x>:LABel:FONT:SIZE`` command.
            - ``.type``: The ``REF:REF<x>:LABel:FONT:TYPE`` command.
            - ``.underline``: The ``REF:REF<x>:LABel:FONT:UNDERline`` command.
        """
        return self._font

    @property
    def name(self) -> RefRefItemLabelName:
        """Return the ``REF:REF<x>:LABel:NAMe`` command.

        Description:
            - This command sets or queries the label of the specified reference. The reference
              waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:NAMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:NAMe value``
              command.

        SCPI Syntax:
            ```
            - REF:REF<x>:LABel:NAMe <QString>
            - REF:REF<x>:LABel:NAMe?
            ```

        Info:
            - ``<QString>`` is the character string that will be used for the reference waveform
              label name.
        """
        return self._name

    @property
    def xpos(self) -> RefRefItemLabelXpos:
        """Return the ``REF:REF<x>:LABel:XPOS`` command.

        Description:
            - This command sets or queries the X-position at which the label (attached to the
              displayed waveform of the specified reference) is displayed, relative to the left edge
              of the waveview. The reference waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:XPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:XPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:XPOS value``
              command.

        SCPI Syntax:
            ```
            - REF:REF<x>:LABel:XPOS <NR1>
            - REF:REF<x>:LABel:XPOS?
            ```

        Info:
            - ``<NR1>`` is the location (control in divisions) where the waveform label for the
              selected reference is displayed, relative to the left edge of the screen.
        """
        return self._xpos

    @property
    def ypos(self) -> RefRefItemLabelYpos:
        """Return the ``REF:REF<x>:LABel:YPOS`` command.

        Description:
            - This command sets or queries the Y-position of the label (attached to the displayed
              waveform of the specified reference), relative to the baseline of the waveform. The
              reference waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>:LABel:YPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel:YPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``REF:REF<x>:LABel:YPOS value``
              command.

        SCPI Syntax:
            ```
            - REF:REF<x>:LABel:YPOS <NR1>
            - REF:REF<x>:LABel:YPOS?
            ```

        Info:
            - ``<NR1>`` is the location where the waveform label for the selected reference is
              displayed, relative to the baseline of the waveform.
        """
        return self._ypos


class RefRefItemDeskew(SCPICmdWrite):
    """The ``REF:REF<x>:DESKew`` command.

    Description:
        - This command sets or queries the deskew value used for the specified reference.

    Usage:
        - Using the ``.write(value)`` method will send the ``REF:REF<x>:DESKew value`` command.

    SCPI Syntax:
        ```
        - REF:REF<x>:DESKew <NR3>
        ```

    Info:
        - ``<NR3>`` is the deskew value used for the specified reference.
    """


class RefRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``REF:REF<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REF:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:REF<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.deskew``: The ``REF:REF<x>:DESKew`` command.
        - ``.label``: The ``REF:REF<x>:LABel`` command tree.
        - ``.source``: The ``REF:REF<x>:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._deskew = RefRefItemDeskew(device, f"{self._cmd_syntax}:DESKew")
        self._label = RefRefItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._source = RefRefItemSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def deskew(self) -> RefRefItemDeskew:
        """Return the ``REF:REF<x>:DESKew`` command.

        Description:
            - This command sets or queries the deskew value used for the specified reference.

        Usage:
            - Using the ``.write(value)`` method will send the ``REF:REF<x>:DESKew value`` command.

        SCPI Syntax:
            ```
            - REF:REF<x>:DESKew <NR3>
            ```

        Info:
            - ``<NR3>`` is the deskew value used for the specified reference.
        """
        return self._deskew

    @property
    def label(self) -> RefRefItemLabel:
        """Return the ``REF:REF<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.color``: The ``REF:REF<x>:LABel:COLor`` command.
            - ``.font``: The ``REF:REF<x>:LABel:FONT`` command tree.
            - ``.name``: The ``REF:REF<x>:LABel:NAMe`` command.
            - ``.xpos``: The ``REF:REF<x>:LABel:XPOS`` command.
            - ``.ypos``: The ``REF:REF<x>:LABel:YPOS`` command.
        """
        return self._label

    @property
    def source(self) -> RefRefItemSource:
        """Return the ``REF:REF<x>:SOUrce`` command.

        Description:
            - This command sets or queries the filename used by the given reference.

        Usage:
            - Using the ``.write(value)`` method will send the ``REF:REF<x>:SOUrce value`` command.

        SCPI Syntax:
            ```
            - REF:REF<x>:SOUrce <QString>
            ```

        Info:
            - ``<QString>`` is the reference file name.
        """
        return self._source


class RefList(SCPICmdRead):
    """The ``REF:LIST`` command.

    Description:
        - This command returns a comma separated list of all currently defined references.

    Usage:
        - Using the ``.query()`` method will send the ``REF:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``REF:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - REF:LIST?
        ```
    """


class RefDelete(SCPICmdWrite):
    """The ``REF:DELete`` command.

    Description:
        - Deletes the specified reference. Argument is of the form 'REF<NR1>', where NR1 ≥ 1.

    Usage:
        - Using the ``.write(value)`` method will send the ``REF:DELete value`` command.

    SCPI Syntax:
        ```
        - REF:DELete <QString>
        ```

    Info:
        - ``<QString>`` is the specified reference. Argument is of the form 'REF<NR1>', where NR1 ≥
          1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class RefAddnew(SCPICmdWrite):
    """The ``REF:ADDNew`` command.

    Description:
        - This command adds the specified reference. Argument is of the form 'REF<NR1> ', where NR1
          ≥ 1.

    Usage:
        - Using the ``.write(value)`` method will send the ``REF:ADDNew value`` command.

    SCPI Syntax:
        ```
        - REF:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` is the specified reference. Argument is of the form 'REF<NR1> ', where NR1 ≥
          1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Ref(SCPICmdRead):
    """The ``REF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``REF?`` query.
        - Using the ``.verify(value)`` method will send the ``REF?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``REF:ADDNew`` command.
        - ``.delete``: The ``REF:DELete`` command.
        - ``.list``: The ``REF:LIST`` command.
        - ``.ref``: The ``REF:REF<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "REF") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = RefAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = RefDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = RefList(device, f"{self._cmd_syntax}:LIST")
        self._ref: Dict[int, RefRefItem] = DefaultDictPassKeyToFactory(
            lambda x: RefRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def addnew(self) -> RefAddnew:
        """Return the ``REF:ADDNew`` command.

        Description:
            - This command adds the specified reference. Argument is of the form 'REF<NR1> ', where
              NR1 ≥ 1.

        Usage:
            - Using the ``.write(value)`` method will send the ``REF:ADDNew value`` command.

        SCPI Syntax:
            ```
            - REF:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` is the specified reference. Argument is of the form 'REF<NR1> ', where
              NR1 ≥ 1.
        """
        return self._addnew

    @property
    def delete(self) -> RefDelete:
        """Return the ``REF:DELete`` command.

        Description:
            - Deletes the specified reference. Argument is of the form 'REF<NR1>', where NR1 ≥ 1.

        Usage:
            - Using the ``.write(value)`` method will send the ``REF:DELete value`` command.

        SCPI Syntax:
            ```
            - REF:DELete <QString>
            ```

        Info:
            - ``<QString>`` is the specified reference. Argument is of the form 'REF<NR1>', where
              NR1 ≥ 1.
        """
        return self._delete

    @property
    def list(self) -> RefList:
        """Return the ``REF:LIST`` command.

        Description:
            - This command returns a comma separated list of all currently defined references.

        Usage:
            - Using the ``.query()`` method will send the ``REF:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:LIST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - REF:LIST?
            ```
        """
        return self._list

    @property
    def ref(self) -> Dict[int, RefRefItem]:
        """Return the ``REF:REF<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``REF:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``REF:REF<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.deskew``: The ``REF:REF<x>:DESKew`` command.
            - ``.label``: The ``REF:REF<x>:LABel`` command tree.
            - ``.source``: The ``REF:REF<x>:SOUrce`` command.
        """
        return self._ref
