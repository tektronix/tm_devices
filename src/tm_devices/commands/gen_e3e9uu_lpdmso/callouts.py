"""The callouts commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CALLOUTS:ADDNew <QString>
    - CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE {CH<x>}
    - CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE?
    - CALLOUTS:CALLOUT<x>:BOOKMark:XPOS <NR1>
    - CALLOUTS:CALLOUT<x>:BOOKMark:XPOS?
    - CALLOUTS:CALLOUT<x>:COLOR <QString>
    - CALLOUTS:CALLOUT<x>:COLOR?
    - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X <NR1>
    - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X?
    - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y <NR1>
    - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y?
    - CALLOUTS:CALLOUT<x>:FONT:BOLD {1|0}
    - CALLOUTS:CALLOUT<x>:FONT:BOLD?
    - CALLOUTS:CALLOUT<x>:FONT:ITALIC {1|0}
    - CALLOUTS:CALLOUT<x>:FONT:ITALIC?
    - CALLOUTS:CALLOUT<x>:FONT:SIZE <NR1>
    - CALLOUTS:CALLOUT<x>:FONT:SIZE?
    - CALLOUTS:CALLOUT<x>:FONT:TYPE <QString>
    - CALLOUTS:CALLOUT<x>:FONT:TYPE?
    - CALLOUTS:CALLOUT<x>:FONT:UNDERLine {1|0}
    - CALLOUTS:CALLOUT<x>:FONT:UNDERLine?
    - CALLOUTS:CALLOUT<x>:TEXT <QString>
    - CALLOUTS:CALLOUT<x>:TEXT?
    - CALLOUTS:CALLOUT<x>:TYPE {NOTE|ARROW|RECTANGLE|BOOKMARK}
    - CALLOUTS:CALLOUT<x>:TYPE?
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


class CalloutsCalloutItemType(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:TYPE`` command.

    Description:
        - This command sets or queries type of the callout.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:TYPE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CALLOUTS:CALLOUT<x>:TYPE value``
          command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:TYPE {NOTE|ARROW|RECTANGLE|BOOKMARK}
        - CALLOUTS:CALLOUT<x>:TYPE?
        ```

    Info:
        - ``NOTE`` specifies callout type as note.
        - ``ARROW`` specifies callout type as arrow.
        - ``RECTANGLE`` specifies callout type as rectangle.
        - ``BOOKMARK`` specifies callout type as bookmark.
    """


class CalloutsCalloutItemText(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:TEXT`` command.

    Description:
        - This command sets or queries the callout text.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:TEXT?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:TEXT?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CALLOUTS:CALLOUT<x>:TEXT value``
          command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:TEXT <QString>
        - CALLOUTS:CALLOUT<x>:TEXT?
        ```

    Info:
        - ``<QString>`` specifies the callout text.
    """

    _WRAP_ARG_WITH_QUOTES = True


class CalloutsCalloutItemFontUnderline(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:FONT:UNDERLine`` command.

    Description:
        - This command sets or queries the underline state of the callout text.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:UNDERLine?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:UNDERLine?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CALLOUTS:CALLOUT<x>:FONT:UNDERLine value`` command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:FONT:UNDERLine {1|0}
        - CALLOUTS:CALLOUT<x>:FONT:UNDERLine?
        ```

    Info:
        - ``1`` underlines the callout text.
        - ``0`` does not underline the callout text.
    """


class CalloutsCalloutItemFontType(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:FONT:TYPE`` command.

    Description:
        - This command sets or queries type of the callout.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:TYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:TYPE value``
          command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:FONT:TYPE <QString>
        - CALLOUTS:CALLOUT<x>:FONT:TYPE?
        ```

    Info:
        - ``<QString>`` specifies the type of font for the callout text. The available font types
          include: DejaVu Sans, DejaVu Sans Mono, DejaVu Serif, Frutiger LT Std, Monospace, Sans
          Serif, Serif, Ubuntu, Ubuntu Condensed, and Ubuntu Mono.
    """

    _WRAP_ARG_WITH_QUOTES = True


class CalloutsCalloutItemFontSize(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:FONT:SIZE`` command.

    Description:
        - This command sets or queries the font size of the callout text.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:SIZE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:SIZE value``
          command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:FONT:SIZE <NR1>
        - CALLOUTS:CALLOUT<x>:FONT:SIZE?
        ```

    Info:
        - ``<NR1>`` specifies the font size in points.
    """


class CalloutsCalloutItemFontItalic(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:FONT:ITALIC`` command.

    Description:
        - This command sets or queries the italic state of the callout text.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:ITALIC?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:ITALIC?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:ITALIC value``
          command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:FONT:ITALIC {1|0}
        - CALLOUTS:CALLOUT<x>:FONT:ITALIC?
        ```

    Info:
        - ``1`` specifies the callout font style as italic.
        - ``0`` does not specify the font style as italic.
    """


class CalloutsCalloutItemFontBold(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the callout text.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:BOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:BOLD?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:BOLD value``
          command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:FONT:BOLD {1|0}
        - CALLOUTS:CALLOUT<x>:FONT:BOLD?
        ```

    Info:
        - ``1`` specifies the callout font weight as bold.
        - ``0`` specifies the callout font weight as normal.
    """


class CalloutsCalloutItemFont(SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bold``: The ``CALLOUTS:CALLOUT<x>:FONT:BOLD`` command.
        - ``.italic``: The ``CALLOUTS:CALLOUT<x>:FONT:ITALIC`` command.
        - ``.size``: The ``CALLOUTS:CALLOUT<x>:FONT:SIZE`` command.
        - ``.type``: The ``CALLOUTS:CALLOUT<x>:FONT:TYPE`` command.
        - ``.underline``: The ``CALLOUTS:CALLOUT<x>:FONT:UNDERLine`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = CalloutsCalloutItemFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = CalloutsCalloutItemFontItalic(device, f"{self._cmd_syntax}:ITALIC")
        self._size = CalloutsCalloutItemFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = CalloutsCalloutItemFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = CalloutsCalloutItemFontUnderline(device, f"{self._cmd_syntax}:UNDERLine")

    @property
    def bold(self) -> CalloutsCalloutItemFontBold:
        """Return the ``CALLOUTS:CALLOUT<x>:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the callout text.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:BOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:BOLD?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:FONT:BOLD value`` command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:FONT:BOLD {1|0}
            - CALLOUTS:CALLOUT<x>:FONT:BOLD?
            ```

        Info:
            - ``1`` specifies the callout font weight as bold.
            - ``0`` specifies the callout font weight as normal.
        """
        return self._bold

    @property
    def italic(self) -> CalloutsCalloutItemFontItalic:
        """Return the ``CALLOUTS:CALLOUT<x>:FONT:ITALIC`` command.

        Description:
            - This command sets or queries the italic state of the callout text.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:ITALIC?``
              query.
            - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:ITALIC?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:FONT:ITALIC value`` command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:FONT:ITALIC {1|0}
            - CALLOUTS:CALLOUT<x>:FONT:ITALIC?
            ```

        Info:
            - ``1`` specifies the callout font style as italic.
            - ``0`` does not specify the font style as italic.
        """
        return self._italic

    @property
    def size(self) -> CalloutsCalloutItemFontSize:
        """Return the ``CALLOUTS:CALLOUT<x>:FONT:SIZE`` command.

        Description:
            - This command sets or queries the font size of the callout text.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:SIZE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:FONT:SIZE value`` command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:FONT:SIZE <NR1>
            - CALLOUTS:CALLOUT<x>:FONT:SIZE?
            ```

        Info:
            - ``<NR1>`` specifies the font size in points.
        """
        return self._size

    @property
    def type(self) -> CalloutsCalloutItemFontType:
        """Return the ``CALLOUTS:CALLOUT<x>:FONT:TYPE`` command.

        Description:
            - This command sets or queries type of the callout.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:FONT:TYPE value`` command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:FONT:TYPE <QString>
            - CALLOUTS:CALLOUT<x>:FONT:TYPE?
            ```

        Info:
            - ``<QString>`` specifies the type of font for the callout text. The available font
              types include: DejaVu Sans, DejaVu Sans Mono, DejaVu Serif, Frutiger LT Std,
              Monospace, Sans Serif, Serif, Ubuntu, Ubuntu Condensed, and Ubuntu Mono.
        """
        return self._type

    @property
    def underline(self) -> CalloutsCalloutItemFontUnderline:
        """Return the ``CALLOUTS:CALLOUT<x>:FONT:UNDERLine`` command.

        Description:
            - This command sets or queries the underline state of the callout text.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT:UNDERLine?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:FONT:UNDERLine?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:FONT:UNDERLine value`` command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:FONT:UNDERLine {1|0}
            - CALLOUTS:CALLOUT<x>:FONT:UNDERLine?
            ```

        Info:
            - ``1`` underlines the callout text.
            - ``0`` does not underline the callout text.
        """
        return self._underline


class CalloutsCalloutItemDisplaypositionY(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y`` command.

    Description:
        - This command sets or queries vertical display position of the callout text.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y value`` command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y <NR1>
        - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y?
        ```

    Info:
        - ``<NR1>`` specifies the callout vertical display position.
    """


class CalloutsCalloutItemDisplaypositionX(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X`` command.

    Description:
        - This command sets or queries horizontal display position of the callout text.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X value`` command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X <NR1>
        - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X?
        ```

    Info:
        - ``<NR1>`` specifies the callout horizontal display position.
    """


class CalloutsCalloutItemDisplayposition(SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition?``
          query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.x``: The ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X`` command.
        - ``.y``: The ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._x = CalloutsCalloutItemDisplaypositionX(device, f"{self._cmd_syntax}:X")
        self._y = CalloutsCalloutItemDisplaypositionY(device, f"{self._cmd_syntax}:Y")

    @property
    def x(self) -> CalloutsCalloutItemDisplaypositionX:
        """Return the ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X`` command.

        Description:
            - This command sets or queries horizontal display position of the callout text.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X value`` command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X <NR1>
            - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X?
            ```

        Info:
            - ``<NR1>`` specifies the callout horizontal display position.
        """
        return self._x

    @property
    def y(self) -> CalloutsCalloutItemDisplaypositionY:
        """Return the ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y`` command.

        Description:
            - This command sets or queries vertical display position of the callout text.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y value`` command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y <NR1>
            - CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y?
            ```

        Info:
            - ``<NR1>`` specifies the callout vertical display position.
        """
        return self._y


class CalloutsCalloutItemColor(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:COLOR`` command.

    Description:
        - This command sets or queries the text color of the callout.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:COLOR?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:COLOR?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CALLOUTS:CALLOUT<x>:COLOR value``
          command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:COLOR <QString>
        - CALLOUTS:CALLOUT<x>:COLOR?
        ```

    Info:
        - ``<QString>`` specifies the callout text color using hexadecimal color values.
    """

    _WRAP_ARG_WITH_QUOTES = True


class CalloutsCalloutItemBookmarkXpos(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:BOOKMark:XPOS`` command.

    Description:
        - This command sets or queries the X-Position of the Bookmark callout type.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:BOOKMark:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:BOOKMark:XPOS?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CALLOUTS:CALLOUT<x>:BOOKMark:XPOS value`` command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:BOOKMark:XPOS <NR1>
        - CALLOUTS:CALLOUT<x>:BOOKMark:XPOS?
        ```

    Info:
        - ``<NR1>`` specifies the location of the bookmark linked to the source waveform in X-axis.
    """


class CalloutsCalloutItemBookmarkSource(SCPICmdWrite, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE`` command.

    Description:
        - This command sets or queries the source of the Bookmark callout type.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE?``
          query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE value`` command.

    SCPI Syntax:
        ```
        - CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE {CH<x>}
        - CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE?
        ```

    Info:
        - ``CH1`` specifies the bookmark callout source as Ch1.
        - ``CH2`` specifies the bookmark callout source as Ch2.
        - ``CH3`` specifies the bookmark callout source as Ch3.
        - ``CH4`` specifies the bookmark callout source as Ch4.
    """


class CalloutsCalloutItemBookmark(SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>:BOOKMark`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:BOOKMark?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:BOOKMark?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE`` command.
        - ``.xpos``: The ``CALLOUTS:CALLOUT<x>:BOOKMark:XPOS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = CalloutsCalloutItemBookmarkSource(device, f"{self._cmd_syntax}:SOURCE")
        self._xpos = CalloutsCalloutItemBookmarkXpos(device, f"{self._cmd_syntax}:XPOS")

    @property
    def source(self) -> CalloutsCalloutItemBookmarkSource:
        """Return the ``CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE`` command.

        Description:
            - This command sets or queries the source of the Bookmark callout type.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE value`` command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE {CH<x>}
            - CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE?
            ```

        Info:
            - ``CH1`` specifies the bookmark callout source as Ch1.
            - ``CH2`` specifies the bookmark callout source as Ch2.
            - ``CH3`` specifies the bookmark callout source as Ch3.
            - ``CH4`` specifies the bookmark callout source as Ch4.
        """
        return self._source

    @property
    def xpos(self) -> CalloutsCalloutItemBookmarkXpos:
        """Return the ``CALLOUTS:CALLOUT<x>:BOOKMark:XPOS`` command.

        Description:
            - This command sets or queries the X-Position of the Bookmark callout type.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:BOOKMark:XPOS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:BOOKMark:XPOS?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:BOOKMark:XPOS value`` command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:BOOKMark:XPOS <NR1>
            - CALLOUTS:CALLOUT<x>:BOOKMark:XPOS?
            ```

        Info:
            - ``<NR1>`` specifies the location of the bookmark linked to the source waveform in
              X-axis.
        """
        return self._xpos


class CalloutsCalloutItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CALLOUTS:CALLOUT<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bookmark``: The ``CALLOUTS:CALLOUT<x>:BOOKMark`` command tree.
        - ``.color``: The ``CALLOUTS:CALLOUT<x>:COLOR`` command.
        - ``.displayposition``: The ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition`` command tree.
        - ``.font``: The ``CALLOUTS:CALLOUT<x>:FONT`` command tree.
        - ``.text``: The ``CALLOUTS:CALLOUT<x>:TEXT`` command.
        - ``.type``: The ``CALLOUTS:CALLOUT<x>:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bookmark = CalloutsCalloutItemBookmark(device, f"{self._cmd_syntax}:BOOKMark")
        self._color = CalloutsCalloutItemColor(device, f"{self._cmd_syntax}:COLOR")
        self._displayposition = CalloutsCalloutItemDisplayposition(
            device, f"{self._cmd_syntax}:DISPLAYPOSition"
        )
        self._font = CalloutsCalloutItemFont(device, f"{self._cmd_syntax}:FONT")
        self._text = CalloutsCalloutItemText(device, f"{self._cmd_syntax}:TEXT")
        self._type = CalloutsCalloutItemType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def bookmark(self) -> CalloutsCalloutItemBookmark:
        """Return the ``CALLOUTS:CALLOUT<x>:BOOKMark`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:BOOKMark?`` query.
            - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:BOOKMark?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``CALLOUTS:CALLOUT<x>:BOOKMark:SOURCE`` command.
            - ``.xpos``: The ``CALLOUTS:CALLOUT<x>:BOOKMark:XPOS`` command.
        """
        return self._bookmark

    @property
    def color(self) -> CalloutsCalloutItemColor:
        """Return the ``CALLOUTS:CALLOUT<x>:COLOR`` command.

        Description:
            - This command sets or queries the text color of the callout.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:COLOR?`` query.
            - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:COLOR?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CALLOUTS:CALLOUT<x>:COLOR value``
              command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:COLOR <QString>
            - CALLOUTS:CALLOUT<x>:COLOR?
            ```

        Info:
            - ``<QString>`` specifies the callout text color using hexadecimal color values.
        """
        return self._color

    @property
    def displayposition(self) -> CalloutsCalloutItemDisplayposition:
        """Return the ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.x``: The ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:X`` command.
            - ``.y``: The ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition:Y`` command.
        """
        return self._displayposition

    @property
    def font(self) -> CalloutsCalloutItemFont:
        """Return the ``CALLOUTS:CALLOUT<x>:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:FONT?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bold``: The ``CALLOUTS:CALLOUT<x>:FONT:BOLD`` command.
            - ``.italic``: The ``CALLOUTS:CALLOUT<x>:FONT:ITALIC`` command.
            - ``.size``: The ``CALLOUTS:CALLOUT<x>:FONT:SIZE`` command.
            - ``.type``: The ``CALLOUTS:CALLOUT<x>:FONT:TYPE`` command.
            - ``.underline``: The ``CALLOUTS:CALLOUT<x>:FONT:UNDERLine`` command.
        """
        return self._font

    @property
    def text(self) -> CalloutsCalloutItemText:
        """Return the ``CALLOUTS:CALLOUT<x>:TEXT`` command.

        Description:
            - This command sets or queries the callout text.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:TEXT?`` query.
            - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:TEXT?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CALLOUTS:CALLOUT<x>:TEXT value``
              command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:TEXT <QString>
            - CALLOUTS:CALLOUT<x>:TEXT?
            ```

        Info:
            - ``<QString>`` specifies the callout text.
        """
        return self._text

    @property
    def type(self) -> CalloutsCalloutItemType:
        """Return the ``CALLOUTS:CALLOUT<x>:TYPE`` command.

        Description:
            - This command sets or queries type of the callout.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>:TYPE?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CALLOUTS:CALLOUT<x>:TYPE value``
              command.

        SCPI Syntax:
            ```
            - CALLOUTS:CALLOUT<x>:TYPE {NOTE|ARROW|RECTANGLE|BOOKMARK}
            - CALLOUTS:CALLOUT<x>:TYPE?
            ```

        Info:
            - ``NOTE`` specifies callout type as note.
            - ``ARROW`` specifies callout type as arrow.
            - ``RECTANGLE`` specifies callout type as rectangle.
            - ``BOOKMARK`` specifies callout type as bookmark.
        """
        return self._type


class CalloutsAddnew(SCPICmdWrite):
    """The ``CALLOUTS:ADDNew`` command.

    Description:
        - This command adds the specified callout. A Note is the default callout type.

    Usage:
        - Using the ``.write(value)`` method will send the ``CALLOUTS:ADDNew value`` command.

    SCPI Syntax:
        ```
        - CALLOUTS:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` specifies the callout. The argument is of the form 'CALLOUT<NR1>', where
          <NR1> is a number value ≥ 1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Callouts(SCPICmdRead):
    """The ``CALLOUTS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALLOUTS?`` query.
        - Using the ``.verify(value)`` method will send the ``CALLOUTS?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``CALLOUTS:ADDNew`` command.
        - ``.callout``: The ``CALLOUTS:CALLOUT<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CALLOUTS") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = CalloutsAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._callout: Dict[int, CalloutsCalloutItem] = DefaultDictPassKeyToFactory(
            lambda x: CalloutsCalloutItem(device, f"{self._cmd_syntax}:CALLOUT{x}")
        )

    @property
    def addnew(self) -> CalloutsAddnew:
        """Return the ``CALLOUTS:ADDNew`` command.

        Description:
            - This command adds the specified callout. A Note is the default callout type.

        Usage:
            - Using the ``.write(value)`` method will send the ``CALLOUTS:ADDNew value`` command.

        SCPI Syntax:
            ```
            - CALLOUTS:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` specifies the callout. The argument is of the form 'CALLOUT<NR1>', where
              <NR1> is a number value ≥ 1.
        """
        return self._addnew

    @property
    def callout(self) -> Dict[int, CalloutsCalloutItem]:
        """Return the ``CALLOUTS:CALLOUT<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALLOUTS:CALLOUT<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CALLOUTS:CALLOUT<x>?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bookmark``: The ``CALLOUTS:CALLOUT<x>:BOOKMark`` command tree.
            - ``.color``: The ``CALLOUTS:CALLOUT<x>:COLOR`` command.
            - ``.displayposition``: The ``CALLOUTS:CALLOUT<x>:DISPLAYPOSition`` command tree.
            - ``.font``: The ``CALLOUTS:CALLOUT<x>:FONT`` command tree.
            - ``.text``: The ``CALLOUTS:CALLOUT<x>:TEXT`` command.
            - ``.type``: The ``CALLOUTS:CALLOUT<x>:TYPE`` command.
        """
        return self._callout
