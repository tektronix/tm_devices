"""The s commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - S<x>_CH<x>:BANdwidth:ACTUal?
    - S<x>_CH<x>:CLIPping?
    - S<x>_CH<x>:COUPling {AC|DC|DCREJ}
    - S<x>_CH<x>:COUPling?
    - S<x>_CH<x>:DESKew <NR3>
    - S<x>_CH<x>:DESKew?
    - S<x>_CH<x>:LABel:COLor <QString>
    - S<x>_CH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
    - S<x>_CH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
    - S<x>_CH<x>:LABel:FONT:SIZE <NR1>
    - S<x>_CH<x>:LABel:FONT:TYPE <QString>
    - S<x>_CH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
    - S<x>_CH<x>:LABel:NAMe <QString>
    - S<x>_CH<x>:LABel:NAMe?
    - S<x>_CH<x>:LABel:XPOS <NR3>
    - S<x>_CH<x>:LABel:XPOS?
    - S<x>_CH<x>:LABel:YPOS <NR3>
    - S<x>_CH<x>:LABel:YPOS?
    - S<x>_CH<x>:OFFSet <NR3>
    - S<x>_CH<x>:OFFSet?
    - S<x>_CH<x>:POSition <NR1>
    - S<x>_CH<x>:SCAle <NR3>
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedChannel,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SItemChannelScale(SCPICmdWrite):
    """The ``S<x>_CH<x>:SCAle`` command.

    Description:
        - This command sets or returns the vertical scale for the specified remote scope analog
          channel. The remote scope and the channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:SCAle value`` command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:SCAle <NR3>
        ```

    Info:
        - ``<NR3>`` is the vertical scale for the specified analog channel.
    """


class SItemChannelPosition(SCPICmdWrite):
    """The ``S<x>_CH<x>:POSition`` command.

    Description:
        - This command sets or queries the vertical position for the specified analog channel. The
          remote scope and channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:POSition value`` command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:POSition <NR1>
        ```

    Info:
        - ``<NR1>`` is the vertical position for the specified analog channel.
    """


class SItemChannelOffset(SCPICmdWrite, SCPICmdRead):
    """The ``S<x>_CH<x>:OFFSet`` command.

    Description:
        - This command sets or queries the vertical offset for the specified remote scope analog
          channel. The remote scope and channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:OFFSet?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:OFFSet value`` command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:OFFSet <NR3>
        - S<x>_CH<x>:OFFSet?
        ```

    Info:
        - ``<NR3>`` is the offset value for the specified remote scope analog channel.
    """


class SItemChannelLabelYpos(SCPICmdWrite, SCPICmdRead):
    """The ``S<x>_CH<x>:LABel:YPOS`` command.

    Description:
        - This command sets or queries the Y-position of the specified remote scope channel. The
          remote scope and channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>:LABel:YPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:LABel:YPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:YPOS value`` command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:LABel:YPOS <NR3>
        - S<x>_CH<x>:LABel:YPOS?
        ```

    Info:
        - ``<NR3>`` is the location (in pixels) where the waveform label for the selected channel is
          displayed, relative to the baseline of the waveform. Positive values are above the
          baseline and negative values are below.
    """


class SItemChannelLabelXpos(SCPICmdWrite, SCPICmdRead):
    """The ``S<x>_CH<x>:LABel:XPOS`` command.

    Description:
        - This command sets or queries the X-position of the specified remote scope channel. The
          remote scope and channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>:LABel:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:LABel:XPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:XPOS value`` command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:LABel:XPOS <NR3>
        - S<x>_CH<x>:LABel:XPOS?
        ```

    Info:
        - ``<NR3>`` is the location (in pixels) where the waveform label for the selected channel is
          displayed, relative to the left edge of the screen.
    """


class SItemChannelLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``S<x>_CH<x>:LABel:NAMe`` command.

    Description:
        - This command sets or queries the label attached to the displayed waveform for the
          specified remote scope channel. The remote scope and channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:LABel:NAMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:NAMe value`` command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:LABel:NAMe <QString>
        - S<x>_CH<x>:LABel:NAMe?
        ```

    Info:
        - ``<QString>`` is an alphanumeric character string, ranging from 1 through 32 characters in
          length.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SItemChannelLabelFontUnderline(SCPICmdWrite):
    """The ``S<x>_CH<x>:LABel:FONT:UNDERline`` command.

    Description:
        - This command sets or queries the underline state of the specified channel label. The
          channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:FONT:UNDERline value``
          command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
        ```

    Info:
        - ``OFF`` argument turns off underlined font.
        - ``ON`` argument turns on underlined font.
        - ``<NR1>`` = 0 turns off underlined font; any other value turns on underlined font.
    """


class SItemChannelLabelFontType(SCPICmdWrite):
    """The ``S<x>_CH<x>:LABel:FONT:TYPE`` command.

    Description:
        - This command sets or queries the font type of the specified remote scope channel label,
          such as Arial or Times New Roman. The remote scope and channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:FONT:TYPE value``
          command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:LABel:FONT:TYPE <QString>
        ```

    Info:
        - ``<QString>`` is the specified font type.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SItemChannelLabelFontSize(SCPICmdWrite):
    """The ``S<x>_CH<x>:LABel:FONT:SIZE`` command.

    Description:
        - This command sets or queries the font size of the specified channel label. The remote
          scope and channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:FONT:SIZE value``
          command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:LABel:FONT:SIZE <NR1>
        ```

    Info:
        - ``<NR1>`` is the font size.
    """


class SItemChannelLabelFontItalic(SCPICmdWrite):
    """The ``S<x>_CH<x>:LABel:FONT:ITALic`` command.

    Description:
        - This command sets or queries the italic state of the specified remote scope channel label.
          The remote scope and channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:FONT:ITALic value``
          command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
        ```

    Info:
        - ``OFF`` argument turns off italic font.
        - ``ON`` argument turns on italic font.
        - ``<NR1>`` = 0 turns off italic font; any other value turns on italic font.
    """


class SItemChannelLabelFontBold(SCPICmdWrite):
    """The ``S<x>_CH<x>:LABel:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the specified remote scope channel label.
          The remote scope and channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:FONT:BOLD value``
          command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
        ```

    Info:
        - ``OFF`` argument turns off bold font.
        - ``ON`` argument turns on bold font.
        - ``<NR1>`` = 0 turns off bold font; any other value turns on bold font.
    """


class SItemChannelLabelFont(SCPICmdRead):
    """The ``S<x>_CH<x>:LABel:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>:LABel:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:LABel:FONT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bold``: The ``S<x>_CH<x>:LABel:FONT:BOLD`` command.
        - ``.italic``: The ``S<x>_CH<x>:LABel:FONT:ITALic`` command.
        - ``.size``: The ``S<x>_CH<x>:LABel:FONT:SIZE`` command.
        - ``.type``: The ``S<x>_CH<x>:LABel:FONT:TYPE`` command.
        - ``.underline``: The ``S<x>_CH<x>:LABel:FONT:UNDERline`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = SItemChannelLabelFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = SItemChannelLabelFontItalic(device, f"{self._cmd_syntax}:ITALic")
        self._size = SItemChannelLabelFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = SItemChannelLabelFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = SItemChannelLabelFontUnderline(device, f"{self._cmd_syntax}:UNDERline")

    @property
    def bold(self) -> SItemChannelLabelFontBold:
        """Return the ``S<x>_CH<x>:LABel:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the specified remote scope channel
              label. The remote scope and channel is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:FONT:BOLD value``
              command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
            ```

        Info:
            - ``OFF`` argument turns off bold font.
            - ``ON`` argument turns on bold font.
            - ``<NR1>`` = 0 turns off bold font; any other value turns on bold font.
        """
        return self._bold

    @property
    def italic(self) -> SItemChannelLabelFontItalic:
        """Return the ``S<x>_CH<x>:LABel:FONT:ITALic`` command.

        Description:
            - This command sets or queries the italic state of the specified remote scope channel
              label. The remote scope and channel is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``S<x>_CH<x>:LABel:FONT:ITALic value`` command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
            ```

        Info:
            - ``OFF`` argument turns off italic font.
            - ``ON`` argument turns on italic font.
            - ``<NR1>`` = 0 turns off italic font; any other value turns on italic font.
        """
        return self._italic

    @property
    def size(self) -> SItemChannelLabelFontSize:
        """Return the ``S<x>_CH<x>:LABel:FONT:SIZE`` command.

        Description:
            - This command sets or queries the font size of the specified channel label. The remote
              scope and channel is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:FONT:SIZE value``
              command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:LABel:FONT:SIZE <NR1>
            ```

        Info:
            - ``<NR1>`` is the font size.
        """
        return self._size

    @property
    def type(self) -> SItemChannelLabelFontType:
        """Return the ``S<x>_CH<x>:LABel:FONT:TYPE`` command.

        Description:
            - This command sets or queries the font type of the specified remote scope channel
              label, such as Arial or Times New Roman. The remote scope and channel is specified by
              x.

        Usage:
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:FONT:TYPE value``
              command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:LABel:FONT:TYPE <QString>
            ```

        Info:
            - ``<QString>`` is the specified font type.
        """
        return self._type

    @property
    def underline(self) -> SItemChannelLabelFontUnderline:
        """Return the ``S<x>_CH<x>:LABel:FONT:UNDERline`` command.

        Description:
            - This command sets or queries the underline state of the specified channel label. The
              channel is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``S<x>_CH<x>:LABel:FONT:UNDERline value`` command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
            ```

        Info:
            - ``OFF`` argument turns off underlined font.
            - ``ON`` argument turns on underlined font.
            - ``<NR1>`` = 0 turns off underlined font; any other value turns on underlined font.
        """
        return self._underline


class SItemChannelLabelColor(SCPICmdWrite):
    """The ``S<x>_CH<x>:LABel:COLor`` command.

    Description:
        - This command sets or queries the color of the specified remote scope channel label. The
          remote scope and channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:COLor value`` command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:LABel:COLor <QString>
        ```

    Info:
        - ``<QString>`` is the label color. To return the color to the default color, send an empty
          string as in this example: ``S1_CH5:LABEL:COLOR`` ''.
    """

    _WRAP_ARG_WITH_QUOTES = True


class SItemChannelLabel(SCPICmdRead):
    """The ``S<x>_CH<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.color``: The ``S<x>_CH<x>:LABel:COLor`` command.
        - ``.font``: The ``S<x>_CH<x>:LABel:FONT`` command tree.
        - ``.name``: The ``S<x>_CH<x>:LABel:NAMe`` command.
        - ``.xpos``: The ``S<x>_CH<x>:LABel:XPOS`` command.
        - ``.ypos``: The ``S<x>_CH<x>:LABel:YPOS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._color = SItemChannelLabelColor(device, f"{self._cmd_syntax}:COLor")
        self._font = SItemChannelLabelFont(device, f"{self._cmd_syntax}:FONT")
        self._name = SItemChannelLabelName(device, f"{self._cmd_syntax}:NAMe")
        self._xpos = SItemChannelLabelXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = SItemChannelLabelYpos(device, f"{self._cmd_syntax}:YPOS")

    @property
    def color(self) -> SItemChannelLabelColor:
        """Return the ``S<x>_CH<x>:LABel:COLor`` command.

        Description:
            - This command sets or queries the color of the specified remote scope channel label.
              The remote scope and channel is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:COLor value``
              command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:LABel:COLor <QString>
            ```

        Info:
            - ``<QString>`` is the label color. To return the color to the default color, send an
              empty string as in this example: ``S1_CH5:LABEL:COLOR`` ''.
        """
        return self._color

    @property
    def font(self) -> SItemChannelLabelFont:
        """Return the ``S<x>_CH<x>:LABel:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>:LABel:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:LABel:FONT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bold``: The ``S<x>_CH<x>:LABel:FONT:BOLD`` command.
            - ``.italic``: The ``S<x>_CH<x>:LABel:FONT:ITALic`` command.
            - ``.size``: The ``S<x>_CH<x>:LABel:FONT:SIZE`` command.
            - ``.type``: The ``S<x>_CH<x>:LABel:FONT:TYPE`` command.
            - ``.underline``: The ``S<x>_CH<x>:LABel:FONT:UNDERline`` command.
        """
        return self._font

    @property
    def name(self) -> SItemChannelLabelName:
        """Return the ``S<x>_CH<x>:LABel:NAMe`` command.

        Description:
            - This command sets or queries the label attached to the displayed waveform for the
              specified remote scope channel. The remote scope and channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:LABel:NAMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:NAMe value``
              command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:LABel:NAMe <QString>
            - S<x>_CH<x>:LABel:NAMe?
            ```

        Info:
            - ``<QString>`` is an alphanumeric character string, ranging from 1 through 32
              characters in length.
        """
        return self._name

    @property
    def xpos(self) -> SItemChannelLabelXpos:
        """Return the ``S<x>_CH<x>:LABel:XPOS`` command.

        Description:
            - This command sets or queries the X-position of the specified remote scope channel. The
              remote scope and channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>:LABel:XPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:LABel:XPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:XPOS value``
              command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:LABel:XPOS <NR3>
            - S<x>_CH<x>:LABel:XPOS?
            ```

        Info:
            - ``<NR3>`` is the location (in pixels) where the waveform label for the selected
              channel is displayed, relative to the left edge of the screen.
        """
        return self._xpos

    @property
    def ypos(self) -> SItemChannelLabelYpos:
        """Return the ``S<x>_CH<x>:LABel:YPOS`` command.

        Description:
            - This command sets or queries the Y-position of the specified remote scope channel. The
              remote scope and channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>:LABel:YPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:LABel:YPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:LABel:YPOS value``
              command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:LABel:YPOS <NR3>
            - S<x>_CH<x>:LABel:YPOS?
            ```

        Info:
            - ``<NR3>`` is the location (in pixels) where the waveform label for the selected
              channel is displayed, relative to the baseline of the waveform. Positive values are
              above the baseline and negative values are below.
        """
        return self._ypos


class SItemChannelDeskew(SCPICmdWrite, SCPICmdRead):
    """The ``S<x>_CH<x>:DESKew`` command.

    Description:
        - This command sets or queries the horizontal deskew time for the specified channel. The
          remote scope and channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>:DESKew?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:DESKew?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:DESKew value`` command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:DESKew <NR3>
        - S<x>_CH<x>:DESKew?
        ```

    Info:
        - ``<NR3>`` is the deskew time for this channel, ranging from -125 ns to +125 ns with a
          resolution of 40 ps. Out-of-range values are clipped.
    """


class SItemChannelCoupling(SCPICmdWrite, SCPICmdRead):
    """The ``S<x>_CH<x>:COUPling`` command.

    Description:
        - This command sets or queries the input coupling setting for the specified remote scope
          analog channel. The remote scope and the channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>:COUPling?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:COUPling?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:COUPling value`` command.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:COUPling {AC|DC|DCREJ}
        - S<x>_CH<x>:COUPling?
        ```

    Info:
        - ``AC`` sets the specified channel to AC coupling.
        - ``DC`` sets the specified channel to DC coupling.
        - ``DCREJect`` sets DC Reject coupling when probes are attached that support that feature.
    """


class SItemChannelClipping(SCPICmdRead):
    """The ``S<x>_CH<x>:CLIPping`` command.

    Description:
        - Queries whether the specified remote scope channel's input signal is clipping (exceeding)
          the channel A/D converter range. The remote scope and channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>:CLIPping?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:CLIPping?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:CLIPping?
        ```
    """


class SItemChannelBandwidthActual(SCPICmdRead):
    """The ``S<x>_CH<x>:BANdwidth:ACTUal`` command.

    Description:
        - Queries whether the actual bandwidth of the specified remote scope channel. The remote
          scope and channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>:BANdwidth:ACTUal?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:BANdwidth:ACTUal?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - S<x>_CH<x>:BANdwidth:ACTUal?
        ```
    """


class SItemChannelBandwidth(SCPICmdRead):
    """The ``S<x>_CH<x>:BANdwidth`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>:BANdwidth?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:BANdwidth?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.actual``: The ``S<x>_CH<x>:BANdwidth:ACTUal`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._actual = SItemChannelBandwidthActual(device, f"{self._cmd_syntax}:ACTUal")

    @property
    def actual(self) -> SItemChannelBandwidthActual:
        """Return the ``S<x>_CH<x>:BANdwidth:ACTUal`` command.

        Description:
            - Queries whether the actual bandwidth of the specified remote scope channel. The remote
              scope and channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>:BANdwidth:ACTUal?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:BANdwidth:ACTUal?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:BANdwidth:ACTUal?
            ```
        """
        return self._actual


#  pylint: disable=too-many-instance-attributes
class SItemChannel(ValidatedChannel, SCPICmdRead):
    """The ``S<x>_CH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>_CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bandwidth``: The ``S<x>_CH<x>:BANdwidth`` command tree.
        - ``.clipping``: The ``S<x>_CH<x>:CLIPping`` command.
        - ``.coupling``: The ``S<x>_CH<x>:COUPling`` command.
        - ``.deskew``: The ``S<x>_CH<x>:DESKew`` command.
        - ``.label``: The ``S<x>_CH<x>:LABel`` command tree.
        - ``.offset``: The ``S<x>_CH<x>:OFFSet`` command.
        - ``.position``: The ``S<x>_CH<x>:POSition`` command.
        - ``.scale``: The ``S<x>_CH<x>:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bandwidth = SItemChannelBandwidth(device, f"{self._cmd_syntax}:BANdwidth")
        self._clipping = SItemChannelClipping(device, f"{self._cmd_syntax}:CLIPping")
        self._coupling = SItemChannelCoupling(device, f"{self._cmd_syntax}:COUPling")
        self._deskew = SItemChannelDeskew(device, f"{self._cmd_syntax}:DESKew")
        self._label = SItemChannelLabel(device, f"{self._cmd_syntax}:LABel")
        self._offset = SItemChannelOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._position = SItemChannelPosition(device, f"{self._cmd_syntax}:POSition")
        self._scale = SItemChannelScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def bandwidth(self) -> SItemChannelBandwidth:
        """Return the ``S<x>_CH<x>:BANdwidth`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>:BANdwidth?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:BANdwidth?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.actual``: The ``S<x>_CH<x>:BANdwidth:ACTUal`` command.
        """
        return self._bandwidth

    @property
    def clipping(self) -> SItemChannelClipping:
        """Return the ``S<x>_CH<x>:CLIPping`` command.

        Description:
            - Queries whether the specified remote scope channel's input signal is clipping
              (exceeding) the channel A/D converter range. The remote scope and channel is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>:CLIPping?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:CLIPping?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:CLIPping?
            ```
        """
        return self._clipping

    @property
    def coupling(self) -> SItemChannelCoupling:
        """Return the ``S<x>_CH<x>:COUPling`` command.

        Description:
            - This command sets or queries the input coupling setting for the specified remote scope
              analog channel. The remote scope and the channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>:COUPling?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:COUPling?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:COUPling value``
              command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:COUPling {AC|DC|DCREJ}
            - S<x>_CH<x>:COUPling?
            ```

        Info:
            - ``AC`` sets the specified channel to AC coupling.
            - ``DC`` sets the specified channel to DC coupling.
            - ``DCREJect`` sets DC Reject coupling when probes are attached that support that
              feature.
        """
        return self._coupling

    @property
    def deskew(self) -> SItemChannelDeskew:
        """Return the ``S<x>_CH<x>:DESKew`` command.

        Description:
            - This command sets or queries the horizontal deskew time for the specified channel. The
              remote scope and channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>:DESKew?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:DESKew?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:DESKew value`` command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:DESKew <NR3>
            - S<x>_CH<x>:DESKew?
            ```

        Info:
            - ``<NR3>`` is the deskew time for this channel, ranging from -125 ns to +125 ns with a
              resolution of 40 ps. Out-of-range values are clipped.
        """
        return self._deskew

    @property
    def label(self) -> SItemChannelLabel:
        """Return the ``S<x>_CH<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.color``: The ``S<x>_CH<x>:LABel:COLor`` command.
            - ``.font``: The ``S<x>_CH<x>:LABel:FONT`` command tree.
            - ``.name``: The ``S<x>_CH<x>:LABel:NAMe`` command.
            - ``.xpos``: The ``S<x>_CH<x>:LABel:XPOS`` command.
            - ``.ypos``: The ``S<x>_CH<x>:LABel:YPOS`` command.
        """
        return self._label

    @property
    def offset(self) -> SItemChannelOffset:
        """Return the ``S<x>_CH<x>:OFFSet`` command.

        Description:
            - This command sets or queries the vertical offset for the specified remote scope analog
              channel. The remote scope and channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>:OFFSet?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:OFFSet value`` command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:OFFSet <NR3>
            - S<x>_CH<x>:OFFSet?
            ```

        Info:
            - ``<NR3>`` is the offset value for the specified remote scope analog channel.
        """
        return self._offset

    @property
    def position(self) -> SItemChannelPosition:
        """Return the ``S<x>_CH<x>:POSition`` command.

        Description:
            - This command sets or queries the vertical position for the specified analog channel.
              The remote scope and channel is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:POSition value``
              command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:POSition <NR1>
            ```

        Info:
            - ``<NR1>`` is the vertical position for the specified analog channel.
        """
        return self._position

    @property
    def scale(self) -> SItemChannelScale:
        """Return the ``S<x>_CH<x>:SCAle`` command.

        Description:
            - This command sets or returns the vertical scale for the specified remote scope analog
              channel. The remote scope and the channel is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``S<x>_CH<x>:SCAle value`` command.

        SCPI Syntax:
            ```
            - S<x>_CH<x>:SCAle <NR3>
            ```

        Info:
            - ``<NR3>`` is the vertical scale for the specified analog channel.
        """
        return self._scale


class SItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``S<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``S<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``S<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``S<x>_CH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "S<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, SItemChannel] = DefaultDictPassKeyToFactory(
            lambda x: SItemChannel(device, f"{self._cmd_syntax}_CH{x}")
        )

    @property
    def ch(self) -> Dict[int, SItemChannel]:
        """Return the ``S<x>_CH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``S<x>_CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``S<x>_CH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bandwidth``: The ``S<x>_CH<x>:BANdwidth`` command tree.
            - ``.clipping``: The ``S<x>_CH<x>:CLIPping`` command.
            - ``.coupling``: The ``S<x>_CH<x>:COUPling`` command.
            - ``.deskew``: The ``S<x>_CH<x>:DESKew`` command.
            - ``.label``: The ``S<x>_CH<x>:LABel`` command tree.
            - ``.offset``: The ``S<x>_CH<x>:OFFSet`` command.
            - ``.position``: The ``S<x>_CH<x>:POSition`` command.
            - ``.scale``: The ``S<x>_CH<x>:SCAle`` command.
        """
        return self._ch
