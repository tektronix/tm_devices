"""The ch commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CH<x>:BANdwidth {<NR3>|FULl}
    - CH<x>:BANdwidth:FILTer:OPTIMIZation {STEPRESPONSE|FLATNESS}
    - CH<x>:BANdwidth:FILTer:OPTIMIZation?
    - CH<x>:BANdwidth?
    - CH<x>:DITHERrange <NR3>
    - CH<x>:INVert {ON|OFF|<NR1>}
    - CH<x>:INVert?
    - CH<x>:PROBECOntrol {AUTO|MANual}
    - CH<x>:PROBECOntrol?
    - CH<x>:PROBECal?
    - CH<x>:PROBEFunc:EXTAtten <NR3>
    - CH<x>:PROBEFunc:EXTAtten?
    - CH<x>:PROBEFunc:EXTDBatten <NR3>
    - CH<x>:PROBEFunc:EXTDBatten?
    - CH<x>:PROBEFunc:EXTUnits <QString>
    - CH<x>:PROBEFunc:EXTUnits:STATE {ON|OFF|<NR1>}
    - CH<x>:PROBEFunc:EXTUnits?
    - CH<x>:PRObe:AUTOZero EXECute
    - CH<x>:PRObe:COMPensate
    - CH<x>:PRObe:DEGAUSS EXECute
    - CH<x>:PRObe:DEGAUSS:STATE?
    - CH<x>:PRObe:FORCEDRange <NR3>
    - CH<x>:PRObe:FORCEDRange?
    - CH<x>:PRObe:GAIN?
    - CH<x>:PRObe:ID:SERnumber?
    - CH<x>:PRObe:ID:TYPe?
    - CH<x>:PRObe:ID?
    - CH<x>:PRObe:INPUTMode {A|B|C|D}
    - CH<x>:PRObe:INPUTMode:AOFFSet <NR3>
    - CH<x>:PRObe:INPUTMode:AOFFSet?
    - CH<x>:PRObe:INPUTMode:BOFFSet <NR3>
    - CH<x>:PRObe:INPUTMode:BOFFSet?
    - CH<x>:PRObe:INPUTMode:COFFSet <NR3>
    - CH<x>:PRObe:INPUTMode:COFFSet?
    - CH<x>:PRObe:INPUTMode:DOFFSet <NR3>
    - CH<x>:PRObe:INPUTMode:DOFFSet?
    - CH<x>:PRObe:INPUTMode?
    - CH<x>:PRObe:RESistance?
    - CH<x>:PRObe:SELFCal EXECUTE
    - CH<x>:PRObe:SELFCal:State? EXECUTE
    - CH<x>:PRObe:SET <QString>
    - CH<x>:PRObe:SET?
    - CH<x>:PRObe:STATus?
    - CH<x>:PRObe:UNIts?
    - CH<x>:PRObe?
    - CH<x>:SCALERATio <NR2>
    - CH<x>:SCALERATio?
    - CH<x>:SV:SPANABovebw?
    - CH<x>:SV:SPANBELowdc?
    - CH<x>:TERmination <NR3>
    - CH<x>:TERmination?
    - CH<x>:VTERm:BIAS <NR3>
    - CH<x>:VTERm:BIAS?
    - CH<x>?
    - CH<x>_D<x>:LABel:COLor <QString>
    - CH<x>_D<x>:LABel:COLor?
    - CH<x>_D<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
    - CH<x>_D<x>:LABel:FONT:BOLD?
    - CH<x>_D<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
    - CH<x>_D<x>:LABel:FONT:ITALic?
    - CH<x>_D<x>:LABel:FONT:SIZE <NR1>
    - CH<x>_D<x>:LABel:FONT:SIZE?
    - CH<x>_D<x>:LABel:FONT:TYPE <QString>
    - CH<x>_D<x>:LABel:FONT:TYPE?
    - CH<x>_D<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
    - CH<x>_D<x>:LABel:FONT:UNDERline?
    - CH<x>_D<x>:LABel:NAMe <QString>
    - CH<x>_D<x>:LABel:NAMe?
    - CH<x>_DALL:LABel:COLor <QString>
    - CH<x>_DALL:LABel:COLor?
    - CH<x>_DALL:LABel:FONT:BOLD {ON|OFF|<NR1>}
    - CH<x>_DALL:LABel:FONT:BOLD?
    - CH<x>_DALL:LABel:FONT:ITALic {ON|OFF|<NR1>}
    - CH<x>_DALL:LABel:FONT:ITALic?
    - CH<x>_DALL:LABel:FONT:SIZE <NR1>
    - CH<x>_DALL:LABel:FONT:SIZE?
    - CH<x>_DALL:LABel:FONT:TYPE <QString>
    - CH<x>_DALL:LABel:FONT:TYPE?
    - CH<x>_DALL:LABel:FONT:UNDERline {ON|OFF|<NR1>}
    - CH<x>_DALL:LABel:FONT:UNDERline?
    - CH<x>_DALL:LABel:NAMe <QString>
    - CH<x>_DALL:LABel:NAMe?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdReadWithArguments,
    SCPICmdWrite,
    SCPICmdWriteNoArguments,
    ValidatedChannel,
    ValidatedDigitalBit,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ChannelDallLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_DALL:LABel:NAMe`` command.

    Description:
        - This command sets or queries the label of the specified digital group. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:NAMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:NAMe value`` command.

    SCPI Syntax:
        ```
        - CH<x>_DALL:LABel:NAMe <QString>
        - CH<x>_DALL:LABel:NAMe?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is the name of the group.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelDallLabelFontUnderline(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_DALL:LABel:FONT:UNDERline`` command.

    Description:
        - This command sets or queries the underline state of the specified digital group. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT:UNDERline?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT:UNDERline?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:FONT:UNDERline value``
          command.

    SCPI Syntax:
        ```
        - CH<x>_DALL:LABel:FONT:UNDERline {ON|OFF|<NR1>}
        - CH<x>_DALL:LABel:FONT:UNDERline?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``OFF`` argument turns off underline font.
        - ``ON`` argument turns on underline font.
        - ``<NR1>`` = 0 turns off underline font; any other value turns on underline font.
    """


class ChannelDallLabelFontType(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_DALL:LABel:FONT:TYPE`` command.

    Description:
        - This command sets or queries the font type of the specified digital group, such as Arial
          or Times New Roman. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT:TYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:FONT:TYPE value``
          command.

    SCPI Syntax:
        ```
        - CH<x>_DALL:LABel:FONT:TYPE <QString>
        - CH<x>_DALL:LABel:FONT:TYPE?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is the font type.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelDallLabelFontSize(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_DALL:LABel:FONT:SIZE`` command.

    Description:
        - This command sets or queries the font size of the specified digital group. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT:SIZE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:FONT:SIZE value``
          command.

    SCPI Syntax:
        ```
        - CH<x>_DALL:LABel:FONT:SIZE <NR1>
        - CH<x>_DALL:LABel:FONT:SIZE?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR1>`` is the font size.
    """


class ChannelDallLabelFontItalic(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_DALL:LABel:FONT:ITALic`` command.

    Description:
        - This command sets or queries the italic state of the specified digital group. The channel
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT:ITALic?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT:ITALic?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:FONT:ITALic value``
          command.

    SCPI Syntax:
        ```
        - CH<x>_DALL:LABel:FONT:ITALic {ON|OFF|<NR1>}
        - CH<x>_DALL:LABel:FONT:ITALic?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``OFF`` argument turns off italic font.
        - ``ON`` argument turns on italic font.
        - ``<NR1>`` = 0 turns off italic font; any other value turns on italic font.
    """


class ChannelDallLabelFontBold(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_DALL:LABel:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the specified digital group. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT:BOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT:BOLD?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:FONT:BOLD value``
          command.

    SCPI Syntax:
        ```
        - CH<x>_DALL:LABel:FONT:BOLD {ON|OFF|<NR1>}
        - CH<x>_DALL:LABel:FONT:BOLD?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``OFF`` argument turns off bold font.
        - ``ON`` argument turns on bold font.
        - ``<NR1>`` = 0 turns off bold font; any other value turns on bold font.
    """


class ChannelDallLabelFont(SCPICmdRead):
    """The ``CH<x>_DALL:LABel:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.bold``: The ``CH<x>_DALL:LABel:FONT:BOLD`` command.
        - ``.italic``: The ``CH<x>_DALL:LABel:FONT:ITALic`` command.
        - ``.size``: The ``CH<x>_DALL:LABel:FONT:SIZE`` command.
        - ``.type``: The ``CH<x>_DALL:LABel:FONT:TYPE`` command.
        - ``.underline``: The ``CH<x>_DALL:LABel:FONT:UNDERline`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = ChannelDallLabelFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = ChannelDallLabelFontItalic(device, f"{self._cmd_syntax}:ITALic")
        self._size = ChannelDallLabelFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = ChannelDallLabelFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = ChannelDallLabelFontUnderline(device, f"{self._cmd_syntax}:UNDERline")

    @property
    def bold(self) -> ChannelDallLabelFontBold:
        """Return the ``CH<x>_DALL:LABel:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the specified digital group. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT:BOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT:BOLD?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:FONT:BOLD value``
              command.

        SCPI Syntax:
            ```
            - CH<x>_DALL:LABel:FONT:BOLD {ON|OFF|<NR1>}
            - CH<x>_DALL:LABel:FONT:BOLD?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``OFF`` argument turns off bold font.
            - ``ON`` argument turns on bold font.
            - ``<NR1>`` = 0 turns off bold font; any other value turns on bold font.
        """
        return self._bold

    @property
    def italic(self) -> ChannelDallLabelFontItalic:
        """Return the ``CH<x>_DALL:LABel:FONT:ITALic`` command.

        Description:
            - This command sets or queries the italic state of the specified digital group. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT:ITALic?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT:ITALic?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>_DALL:LABel:FONT:ITALic value`` command.

        SCPI Syntax:
            ```
            - CH<x>_DALL:LABel:FONT:ITALic {ON|OFF|<NR1>}
            - CH<x>_DALL:LABel:FONT:ITALic?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``OFF`` argument turns off italic font.
            - ``ON`` argument turns on italic font.
            - ``<NR1>`` = 0 turns off italic font; any other value turns on italic font.
        """
        return self._italic

    @property
    def size(self) -> ChannelDallLabelFontSize:
        """Return the ``CH<x>_DALL:LABel:FONT:SIZE`` command.

        Description:
            - This command sets or queries the font size of the specified digital group. The channel
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT:SIZE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:FONT:SIZE value``
              command.

        SCPI Syntax:
            ```
            - CH<x>_DALL:LABel:FONT:SIZE <NR1>
            - CH<x>_DALL:LABel:FONT:SIZE?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR1>`` is the font size.
        """
        return self._size

    @property
    def type(self) -> ChannelDallLabelFontType:
        """Return the ``CH<x>_DALL:LABel:FONT:TYPE`` command.

        Description:
            - This command sets or queries the font type of the specified digital group, such as
              Arial or Times New Roman. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:FONT:TYPE value``
              command.

        SCPI Syntax:
            ```
            - CH<x>_DALL:LABel:FONT:TYPE <QString>
            - CH<x>_DALL:LABel:FONT:TYPE?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is the font type.
        """
        return self._type

    @property
    def underline(self) -> ChannelDallLabelFontUnderline:
        """Return the ``CH<x>_DALL:LABel:FONT:UNDERline`` command.

        Description:
            - This command sets or queries the underline state of the specified digital group. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT:UNDERline?``
              query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT:UNDERline?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>_DALL:LABel:FONT:UNDERline value`` command.

        SCPI Syntax:
            ```
            - CH<x>_DALL:LABel:FONT:UNDERline {ON|OFF|<NR1>}
            - CH<x>_DALL:LABel:FONT:UNDERline?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``OFF`` argument turns off underline font.
            - ``ON`` argument turns on underline font.
            - ``<NR1>`` = 0 turns off underline font; any other value turns on underline font.
        """
        return self._underline


class ChannelDallLabelColor(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_DALL:LABel:COLor`` command.

    Description:
        - This command sets or queries the color of the specified digital group label. The channel
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:COLor?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:COLor?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:COLor value`` command.

    SCPI Syntax:
        ```
        - CH<x>_DALL:LABel:COLor <QString>
        - CH<x>_DALL:LABel:COLor?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is the color of the digital group label. To return the color to the default
          color, send an empty string as in this example: ``:CH5_DALL:LABEL:COLOR`` ''.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelDallLabel(SCPICmdRead):
    """The ``CH<x>_DALL:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.color``: The ``CH<x>_DALL:LABel:COLor`` command.
        - ``.font``: The ``CH<x>_DALL:LABel:FONT`` command tree.
        - ``.name``: The ``CH<x>_DALL:LABel:NAMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._color = ChannelDallLabelColor(device, f"{self._cmd_syntax}:COLor")
        self._font = ChannelDallLabelFont(device, f"{self._cmd_syntax}:FONT")
        self._name = ChannelDallLabelName(device, f"{self._cmd_syntax}:NAMe")

    @property
    def color(self) -> ChannelDallLabelColor:
        """Return the ``CH<x>_DALL:LABel:COLor`` command.

        Description:
            - This command sets or queries the color of the specified digital group label. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:COLor?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:COLor?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:COLor value``
              command.

        SCPI Syntax:
            ```
            - CH<x>_DALL:LABel:COLor <QString>
            - CH<x>_DALL:LABel:COLor?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is the color of the digital group label. To return the color to the
              default color, send an empty string as in this example: ``:CH5_DALL:LABEL:COLOR`` ''.
        """
        return self._color

    @property
    def font(self) -> ChannelDallLabelFont:
        """Return the ``CH<x>_DALL:LABel:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:FONT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.bold``: The ``CH<x>_DALL:LABel:FONT:BOLD`` command.
            - ``.italic``: The ``CH<x>_DALL:LABel:FONT:ITALic`` command.
            - ``.size``: The ``CH<x>_DALL:LABel:FONT:SIZE`` command.
            - ``.type``: The ``CH<x>_DALL:LABel:FONT:TYPE`` command.
            - ``.underline``: The ``CH<x>_DALL:LABel:FONT:UNDERline`` command.
        """
        return self._font

    @property
    def name(self) -> ChannelDallLabelName:
        """Return the ``CH<x>_DALL:LABel:NAMe`` command.

        Description:
            - This command sets or queries the label of the specified digital group. The channel is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel:NAMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>_DALL:LABel:NAMe value``
              command.

        SCPI Syntax:
            ```
            - CH<x>_DALL:LABel:NAMe <QString>
            - CH<x>_DALL:LABel:NAMe?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is the name of the group.
        """
        return self._name


class ChannelDall(SCPICmdRead):
    """The ``CH<x>_DALL`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_DALL?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_DALL?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.label``: The ``CH<x>_DALL:LABel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._label = ChannelDallLabel(device, f"{self._cmd_syntax}:LABel")

    @property
    def label(self) -> ChannelDallLabel:
        """Return the ``CH<x>_DALL:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_DALL:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_DALL:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.color``: The ``CH<x>_DALL:LABel:COLor`` command.
            - ``.font``: The ``CH<x>_DALL:LABel:FONT`` command tree.
            - ``.name``: The ``CH<x>_DALL:LABel:NAMe`` command.
        """
        return self._label


class ChannelDigitalBitLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_D<x>:LABel:NAMe`` command.

    Description:
        - Sets or queries the label of the specified digital bit. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:NAMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:NAMe value`` command.

    SCPI Syntax:
        ```
        - CH<x>_D<x>:LABel:NAMe <QString>
        - CH<x>_D<x>:LABel:NAMe?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is the label.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelDigitalBitLabelFontUnderline(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_D<x>:LABel:FONT:UNDERline`` command.

    Description:
        - This command sets or queries the underline state of the label of the specified digital
          bit. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT:UNDERline?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:UNDERline?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:UNDERline value``
          command.

    SCPI Syntax:
        ```
        - CH<x>_D<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
        - CH<x>_D<x>:LABel:FONT:UNDERline?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``OFF`` argument turns off underline font.
        - ``ON`` argument turns on underline font.
        - ``<NR1>`` = 0 turns off underline font; any other value turns on underline font.
    """


class ChannelDigitalBitLabelFontType(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_D<x>:LABel:FONT:TYPE`` command.

    Description:
        - This command sets or queries the font type of the label of the specified digital bit, such
          as Arial or Times New Roman. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:TYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:TYPE value``
          command.

    SCPI Syntax:
        ```
        - CH<x>_D<x>:LABel:FONT:TYPE <QString>
        - CH<x>_D<x>:LABel:FONT:TYPE?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is the font type of the label.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelDigitalBitLabelFontSize(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_D<x>:LABel:FONT:SIZE`` command.

    Description:
        - This command sets or queries the font size of the label of the specified digital bit. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:SIZE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:SIZE value``
          command.

    SCPI Syntax:
        ```
        - CH<x>_D<x>:LABel:FONT:SIZE <NR1>
        - CH<x>_D<x>:LABel:FONT:SIZE?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR1>`` is the font size.
    """


class ChannelDigitalBitLabelFontItalic(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_D<x>:LABel:FONT:ITALic`` command.

    Description:
        - This command sets or queries the italic state of the label of the specified digital bit.
          The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT:ITALic?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:ITALic?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:ITALic value``
          command.

    SCPI Syntax:
        ```
        - CH<x>_D<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
        - CH<x>_D<x>:LABel:FONT:ITALic?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``OFF`` argument turns off italic font.
        - ``ON`` argument turns on italic font.
        - ``<NR1>`` = 0 turns off italic font; any other value turns on italic font.
    """


class ChannelDigitalBitLabelFontBold(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_D<x>:LABel:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the label of the specified digital bit. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT:BOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:BOLD?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:BOLD value``
          command.

    SCPI Syntax:
        ```
        - CH<x>_D<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
        - CH<x>_D<x>:LABel:FONT:BOLD?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``OFF`` argument turns off bold font.
        - ``ON`` argument turns on bold font.
        - ``<NR1>`` = 0 turns off bold font; any other value turns on bold font.
    """


class ChannelDigitalBitLabelFont(SCPICmdRead):
    """The ``CH<x>_D<x>:LABel:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.bold``: The ``CH<x>_D<x>:LABel:FONT:BOLD`` command.
        - ``.italic``: The ``CH<x>_D<x>:LABel:FONT:ITALic`` command.
        - ``.size``: The ``CH<x>_D<x>:LABel:FONT:SIZE`` command.
        - ``.type``: The ``CH<x>_D<x>:LABel:FONT:TYPE`` command.
        - ``.underline``: The ``CH<x>_D<x>:LABel:FONT:UNDERline`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = ChannelDigitalBitLabelFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = ChannelDigitalBitLabelFontItalic(device, f"{self._cmd_syntax}:ITALic")
        self._size = ChannelDigitalBitLabelFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = ChannelDigitalBitLabelFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = ChannelDigitalBitLabelFontUnderline(
            device, f"{self._cmd_syntax}:UNDERline"
        )

    @property
    def bold(self) -> ChannelDigitalBitLabelFontBold:
        """Return the ``CH<x>_D<x>:LABel:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the label of the specified digital bit.
              The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT:BOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:BOLD?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:BOLD value``
              command.

        SCPI Syntax:
            ```
            - CH<x>_D<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
            - CH<x>_D<x>:LABel:FONT:BOLD?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``OFF`` argument turns off bold font.
            - ``ON`` argument turns on bold font.
            - ``<NR1>`` = 0 turns off bold font; any other value turns on bold font.
        """
        return self._bold

    @property
    def italic(self) -> ChannelDigitalBitLabelFontItalic:
        """Return the ``CH<x>_D<x>:LABel:FONT:ITALic`` command.

        Description:
            - This command sets or queries the italic state of the label of the specified digital
              bit. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT:ITALic?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:ITALic?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>_D<x>:LABel:FONT:ITALic value`` command.

        SCPI Syntax:
            ```
            - CH<x>_D<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
            - CH<x>_D<x>:LABel:FONT:ITALic?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``OFF`` argument turns off italic font.
            - ``ON`` argument turns on italic font.
            - ``<NR1>`` = 0 turns off italic font; any other value turns on italic font.
        """
        return self._italic

    @property
    def size(self) -> ChannelDigitalBitLabelFontSize:
        """Return the ``CH<x>_D<x>:LABel:FONT:SIZE`` command.

        Description:
            - This command sets or queries the font size of the label of the specified digital bit.
              The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:SIZE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:SIZE value``
              command.

        SCPI Syntax:
            ```
            - CH<x>_D<x>:LABel:FONT:SIZE <NR1>
            - CH<x>_D<x>:LABel:FONT:SIZE?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR1>`` is the font size.
        """
        return self._size

    @property
    def type(self) -> ChannelDigitalBitLabelFontType:
        """Return the ``CH<x>_D<x>:LABel:FONT:TYPE`` command.

        Description:
            - This command sets or queries the font type of the label of the specified digital bit,
              such as Arial or Times New Roman. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:TYPE value``
              command.

        SCPI Syntax:
            ```
            - CH<x>_D<x>:LABel:FONT:TYPE <QString>
            - CH<x>_D<x>:LABel:FONT:TYPE?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is the font type of the label.
        """
        return self._type

    @property
    def underline(self) -> ChannelDigitalBitLabelFontUnderline:
        """Return the ``CH<x>_D<x>:LABel:FONT:UNDERline`` command.

        Description:
            - This command sets or queries the underline state of the label of the specified digital
              bit. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT:UNDERline?``
              query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT:UNDERline?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>_D<x>:LABel:FONT:UNDERline value`` command.

        SCPI Syntax:
            ```
            - CH<x>_D<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
            - CH<x>_D<x>:LABel:FONT:UNDERline?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``OFF`` argument turns off underline font.
            - ``ON`` argument turns on underline font.
            - ``<NR1>`` = 0 turns off underline font; any other value turns on underline font.
        """
        return self._underline


class ChannelDigitalBitLabelColor(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>_D<x>:LABel:COLor`` command.

    Description:
        - This command sets or queries the color of the label of the specified digital bit. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:COLor?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:COLor?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:COLor value`` command.

    SCPI Syntax:
        ```
        - CH<x>_D<x>:LABel:COLor <QString>
        - CH<x>_D<x>:LABel:COLor?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is the label color. To return the color to the default color, send an empty
          string as in this example: ``:CH5_D1:LABEL:COLOR`` ''.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelDigitalBitLabel(SCPICmdRead):
    """The ``CH<x>_D<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.color``: The ``CH<x>_D<x>:LABel:COLor`` command.
        - ``.font``: The ``CH<x>_D<x>:LABel:FONT`` command tree.
        - ``.name``: The ``CH<x>_D<x>:LABel:NAMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._color = ChannelDigitalBitLabelColor(device, f"{self._cmd_syntax}:COLor")
        self._font = ChannelDigitalBitLabelFont(device, f"{self._cmd_syntax}:FONT")
        self._name = ChannelDigitalBitLabelName(device, f"{self._cmd_syntax}:NAMe")

    @property
    def color(self) -> ChannelDigitalBitLabelColor:
        """Return the ``CH<x>_D<x>:LABel:COLor`` command.

        Description:
            - This command sets or queries the color of the label of the specified digital bit. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:COLor?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:COLor?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:COLor value``
              command.

        SCPI Syntax:
            ```
            - CH<x>_D<x>:LABel:COLor <QString>
            - CH<x>_D<x>:LABel:COLor?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is the label color. To return the color to the default color, send an
              empty string as in this example: ``:CH5_D1:LABEL:COLOR`` ''.
        """
        return self._color

    @property
    def font(self) -> ChannelDigitalBitLabelFont:
        """Return the ``CH<x>_D<x>:LABel:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:FONT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.bold``: The ``CH<x>_D<x>:LABel:FONT:BOLD`` command.
            - ``.italic``: The ``CH<x>_D<x>:LABel:FONT:ITALic`` command.
            - ``.size``: The ``CH<x>_D<x>:LABel:FONT:SIZE`` command.
            - ``.type``: The ``CH<x>_D<x>:LABel:FONT:TYPE`` command.
            - ``.underline``: The ``CH<x>_D<x>:LABel:FONT:UNDERline`` command.
        """
        return self._font

    @property
    def name(self) -> ChannelDigitalBitLabelName:
        """Return the ``CH<x>_D<x>:LABel:NAMe`` command.

        Description:
            - Sets or queries the label of the specified digital bit. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel:NAMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>_D<x>:LABel:NAMe value``
              command.

        SCPI Syntax:
            ```
            - CH<x>_D<x>:LABel:NAMe <QString>
            - CH<x>_D<x>:LABel:NAMe?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is the label.
        """
        return self._name


class ChannelDigitalBit(ValidatedDigitalBit, SCPICmdRead):
    """The ``CH<x>_D<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>_D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.label``: The ``CH<x>_D<x>:LABel`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._label = ChannelDigitalBitLabel(device, f"{self._cmd_syntax}:LABel")

    @property
    def label(self) -> ChannelDigitalBitLabel:
        """Return the ``CH<x>_D<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_D<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.color``: The ``CH<x>_D<x>:LABel:COLor`` command.
            - ``.font``: The ``CH<x>_D<x>:LABel:FONT`` command tree.
            - ``.name``: The ``CH<x>_D<x>:LABel:NAMe`` command.
        """
        return self._label


class ChannelVtermBias(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:VTERm:BIAS`` command.

    Description:
        - Sets or queries the termination bias voltage for the specified channel (if control is
          available).

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:VTERm:BIAS?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm:BIAS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:VTERm:BIAS value`` command.

    SCPI Syntax:
        ```
        - CH<x>:VTERm:BIAS <NR3>
        - CH<x>:VTERm:BIAS?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the termination voltage.
    """


class ChannelVterm(SCPICmdRead):
    """The ``CH<x>:VTERm`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:VTERm?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.bias``: The ``CH<x>:VTERm:BIAS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bias = ChannelVtermBias(device, f"{self._cmd_syntax}:BIAS")

    @property
    def bias(self) -> ChannelVtermBias:
        """Return the ``CH<x>:VTERm:BIAS`` command.

        Description:
            - Sets or queries the termination bias voltage for the specified channel (if control is
              available).

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:VTERm:BIAS?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm:BIAS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:VTERm:BIAS value`` command.

        SCPI Syntax:
            ```
            - CH<x>:VTERm:BIAS <NR3>
            - CH<x>:VTERm:BIAS?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the termination voltage.
        """
        return self._bias


class ChannelTermination(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:TERmination`` command.

    Description:
        - This command sets or queries the vertical termination for the specified analog channel.
          The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:TERmination?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:TERmination?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:TERmination value`` command.

    SCPI Syntax:
        ```
        - CH<x>:TERmination <NR3>
        - CH<x>:TERmination?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` specifies the channel input resistance, which can be specified as 50 Ω or
          1,000,000 Ω.
    """


class ChannelSvSpanbelowdc(SCPICmdRead):
    """The ``CH<x>:SV:SPANBELowdc`` command.

    Description:
        - This command queries whether the start frequency for the specified spectrum trace channel
          is below 0 Hz.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:SV:SPANBELowdc?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:SV:SPANBELowdc?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:SV:SPANBELowdc?
        ```

    Info:
        - ``CH<x>`` specifies the spectrum trace channel source.
    """


class ChannelSvSpanabovebw(SCPICmdRead):
    """The ``CH<x>:SV:SPANABovebw`` command.

    Description:
        - This command queries whether the stop frequency for the specified spectrum trace channel
          is above the scope input bandwidth.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:SV:SPANABovebw?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:SV:SPANABovebw?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:SV:SPANABovebw?
        ```

    Info:
        - ``CH<x>`` specifies the spectrum trace channel source.
    """


class ChannelSv(SCPICmdRead):
    """The ``CH<x>:SV`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:SV?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:SV?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` specifies the spectrum trace channel source.

    Properties:
        - ``.spanabovebw``: The ``CH<x>:SV:SPANABovebw`` command.
        - ``.spanbelowdc``: The ``CH<x>:SV:SPANBELowdc`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._spanabovebw = ChannelSvSpanabovebw(device, f"{self._cmd_syntax}:SPANABovebw")
        self._spanbelowdc = ChannelSvSpanbelowdc(device, f"{self._cmd_syntax}:SPANBELowdc")

    @property
    def spanabovebw(self) -> ChannelSvSpanabovebw:
        """Return the ``CH<x>:SV:SPANABovebw`` command.

        Description:
            - This command queries whether the stop frequency for the specified spectrum trace
              channel is above the scope input bandwidth.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:SV:SPANABovebw?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:SV:SPANABovebw?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:SV:SPANABovebw?
            ```

        Info:
            - ``CH<x>`` specifies the spectrum trace channel source.
        """
        return self._spanabovebw

    @property
    def spanbelowdc(self) -> ChannelSvSpanbelowdc:
        """Return the ``CH<x>:SV:SPANBELowdc`` command.

        Description:
            - This command queries whether the start frequency for the specified spectrum trace
              channel is below 0 Hz.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:SV:SPANBELowdc?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:SV:SPANBELowdc?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:SV:SPANBELowdc?
            ```

        Info:
            - ``CH<x>`` specifies the spectrum trace channel source.
        """
        return self._spanbelowdc


class ChannelScaleratio(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:SCALERATio`` command.

    Description:
        - This command sets or returns the scale ratio for the specified analog channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:SCALERATio?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:SCALERATio?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:SCALERATio value`` command.

    SCPI Syntax:
        ```
        - CH<x>:SCALERATio <NR2>
        - CH<x>:SCALERATio?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR2>`` is the scale ratio for the specified analog channel.
    """


class ChannelProbeUnits(SCPICmdRead):
    """The ``CH<x>:PRObe:UNIts`` command.

    Description:
        - This query-only command returns a string describing the units of measure for the probe
          attached to the specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:UNIts?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:UNIts?
        ```
    """


class ChannelProbeStatus(SCPICmdRead):
    """The ``CH<x>:PRObe:STATus`` command.

    Description:
        - Queries the probe unsigned integer error value.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:STATus?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:STATus?
        ```
    """


class ChannelProbeSet(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:SET`` command.

    Description:
        - This command sets or queries aspects of probe accessory user interfaces, for example probe
          attenuation factors or probe audible over range. The available arguments for this command
          will vary depending on the accessory you attach to the instrument. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:SET?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:SET?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:SET value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:SET <QString>
        - CH<x>:PRObe:SET?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is a quoted string representing a settable aspect of the attached accessory.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelProbeSelfcalState(SCPICmdReadWithArguments):
    """The ``CH<x>:PRObe:SELFCal:State`` command.

    Description:
        - This query-only command returns the self-calibration state. The channel is specified by x.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``CH<x>:PRObe:SELFCal:State? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``CH<x>:PRObe:SELFCal:State? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:SELFCal:State? EXECUTE
        ```
    """


class ChannelProbeSelfcal(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:SELFCal`` command.

    Description:
        - This command initiates self-calibration on the probe. The channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:SELFCal value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:SELFCal EXECUTE
        ```

    Properties:
        - ``.state``: The ``CH<x>:PRObe:SELFCal:State`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ChannelProbeSelfcalState(device, f"{self._cmd_syntax}:State")

    @property
    def state(self) -> ChannelProbeSelfcalState:
        """Return the ``CH<x>:PRObe:SELFCal:State`` command.

        Description:
            - This query-only command returns the self-calibration state. The channel is specified
              by x.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``CH<x>:PRObe:SELFCal:State? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``CH<x>:PRObe:SELFCal:State? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:SELFCal:State? EXECUTE
            ```
        """
        return self._state


class ChannelProbeResistance(SCPICmdRead):
    """The ``CH<x>:PRObe:RESistance`` command.

    Description:
        - This query-only command returns the resistance of the probe that is attached to the
          specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:RESistance?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:RESistance?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:RESistance?
        ```
    """


class ChannelProbeInputmodeDoffset(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:INPUTMode:DOFFSet`` command.

    Description:
        - Sets or queries the differential offset value of the probe that is attached to the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:DOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:DOFFSet?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode:DOFFSet value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:INPUTMode:DOFFSet <NR3>
        - CH<x>:PRObe:INPUTMode:DOFFSet?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` sets the D (differential) mode offset value, in vertical units (V or A).
    """


class ChannelProbeInputmodeCoffset(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:INPUTMode:COFFSet`` command.

    Description:
        - Sets or queries the common mode offset value of the probe that is attached to the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:COFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:COFFSet?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode:COFFSet value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:INPUTMode:COFFSet <NR3>
        - CH<x>:PRObe:INPUTMode:COFFSet?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` sets the C (common) mode offset value, in vertical units (V or A).
    """


class ChannelProbeInputmodeBoffset(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:INPUTMode:BOFFSet`` command.

    Description:
        - Sets or queries the B mode offset control of the probe that is attached to the specified
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:BOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:BOFFSet?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode:BOFFSet value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:INPUTMode:BOFFSet <NR3>
        - CH<x>:PRObe:INPUTMode:BOFFSet?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` sets the B mode offset value, in vertical units (V or A).
    """


class ChannelProbeInputmodeAoffset(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:INPUTMode:AOFFSet`` command.

    Description:
        - Sets or queries the A mode offset control of the probe that is attached to the specified
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:AOFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:AOFFSet?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode:AOFFSet value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:INPUTMode:AOFFSet <NR3>
        - CH<x>:PRObe:INPUTMode:AOFFSet?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` sets the A mode offset value, in vertical units (V or A).
    """


class ChannelProbeInputmode(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:INPUTMode`` command.

    Description:
        - Sets or queries the input mode of the probe that is attached to the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:INPUTMode {A|B|C|D}
        - CH<x>:PRObe:INPUTMode?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``A`` sets the probe to send single-ended A signals to the instrument.
        - ``B`` sets the probe to send single-ended B signals to the instrument.
        - ``COMMONMODE`` sets the probe to send common-mode signals to the instrument.
        - ``DIFFERENTIAL`` sets the probe to send differential signals to the instrument.

    Properties:
        - ``.aoffset``: The ``CH<x>:PRObe:INPUTMode:AOFFSet`` command.
        - ``.boffset``: The ``CH<x>:PRObe:INPUTMode:BOFFSet`` command.
        - ``.coffset``: The ``CH<x>:PRObe:INPUTMode:COFFSet`` command.
        - ``.doffset``: The ``CH<x>:PRObe:INPUTMode:DOFFSet`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aoffset = ChannelProbeInputmodeAoffset(device, f"{self._cmd_syntax}:AOFFSet")
        self._boffset = ChannelProbeInputmodeBoffset(device, f"{self._cmd_syntax}:BOFFSet")
        self._coffset = ChannelProbeInputmodeCoffset(device, f"{self._cmd_syntax}:COFFSet")
        self._doffset = ChannelProbeInputmodeDoffset(device, f"{self._cmd_syntax}:DOFFSet")

    @property
    def aoffset(self) -> ChannelProbeInputmodeAoffset:
        """Return the ``CH<x>:PRObe:INPUTMode:AOFFSet`` command.

        Description:
            - Sets or queries the A mode offset control of the probe that is attached to the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:AOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:AOFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:PRObe:INPUTMode:AOFFSet value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:INPUTMode:AOFFSet <NR3>
            - CH<x>:PRObe:INPUTMode:AOFFSet?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` sets the A mode offset value, in vertical units (V or A).
        """
        return self._aoffset

    @property
    def boffset(self) -> ChannelProbeInputmodeBoffset:
        """Return the ``CH<x>:PRObe:INPUTMode:BOFFSet`` command.

        Description:
            - Sets or queries the B mode offset control of the probe that is attached to the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:BOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:BOFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:PRObe:INPUTMode:BOFFSet value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:INPUTMode:BOFFSet <NR3>
            - CH<x>:PRObe:INPUTMode:BOFFSet?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` sets the B mode offset value, in vertical units (V or A).
        """
        return self._boffset

    @property
    def coffset(self) -> ChannelProbeInputmodeCoffset:
        """Return the ``CH<x>:PRObe:INPUTMode:COFFSet`` command.

        Description:
            - Sets or queries the common mode offset value of the probe that is attached to the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:COFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:COFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:PRObe:INPUTMode:COFFSet value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:INPUTMode:COFFSet <NR3>
            - CH<x>:PRObe:INPUTMode:COFFSet?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` sets the C (common) mode offset value, in vertical units (V or A).
        """
        return self._coffset

    @property
    def doffset(self) -> ChannelProbeInputmodeDoffset:
        """Return the ``CH<x>:PRObe:INPUTMode:DOFFSet`` command.

        Description:
            - Sets or queries the differential offset value of the probe that is attached to the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode:DOFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode:DOFFSet?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:PRObe:INPUTMode:DOFFSet value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:INPUTMode:DOFFSet <NR3>
            - CH<x>:PRObe:INPUTMode:DOFFSet?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` sets the D (differential) mode offset value, in vertical units (V or A).
        """
        return self._doffset


class ChannelProbeIdType(SCPICmdRead):
    """The ``CH<x>:PRObe:ID:TYPe`` command.

    Description:
        - This query-only command returns the type of probe that is attached to the specified
          channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:ID:TYPe?
        ```
    """


class ChannelProbeIdSernumber(SCPICmdRead):
    """The ``CH<x>:PRObe:ID:SERnumber`` command.

    Description:
        - This query-only command returns the serial number of the probe that is attached to the
          specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:ID:SERnumber?
        ```
    """


class ChannelProbeId(SCPICmdRead):
    """The ``CH<x>:PRObe:ID`` command.

    Description:
        - This query-only command returns the type and serial number of the probe that is attached
          to the specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:ID?
        ```

    Properties:
        - ``.sernumber``: The ``CH<x>:PRObe:ID:SERnumber`` command.
        - ``.type``: The ``CH<x>:PRObe:ID:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sernumber = ChannelProbeIdSernumber(device, f"{self._cmd_syntax}:SERnumber")
        self._type = ChannelProbeIdType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def sernumber(self) -> ChannelProbeIdSernumber:
        """Return the ``CH<x>:PRObe:ID:SERnumber`` command.

        Description:
            - This query-only command returns the serial number of the probe that is attached to the
              specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:ID:SERnumber?
            ```
        """
        return self._sernumber

    @property
    def type(self) -> ChannelProbeIdType:
        """Return the ``CH<x>:PRObe:ID:TYPe`` command.

        Description:
            - This query-only command returns the type of probe that is attached to the specified
              channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:ID:TYPe?
            ```
        """
        return self._type


class ChannelProbeGain(SCPICmdRead):
    """The ``CH<x>:PRObe:GAIN`` command.

    Description:
        - This query-only command returns the gain factor of the probe that is attached to the
          specified channel. The channel is specified by x. The gain of a probe is the output
          divided by the input transfer ratio. For example, a common 10x probe has a gain of 0.1.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:GAIN?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:GAIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:GAIN?
        ```
    """


class ChannelProbeForcedrange(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:FORCEDRange`` command.

    Description:
        - This command sets the attached TekVPI probe to the specified range, or it queries the
          range of the probe attached to the specified channel. If the <NR3> argument does not match
          one of the available ranges, the closest range will be selected. The channel is specified
          by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:FORCEDRange value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:FORCEDRange <NR3>
        - CH<x>:PRObe:FORCEDRange?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` specifies the probe dynamic range.
    """


class ChannelProbeDegaussState(SCPICmdRead):
    """The ``CH<x>:PRObe:DEGAUSS:STATE`` command.

    Description:
        - This command queries whether the probe attached to the specified channel requires a
          degauss operation. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:DEGAUSS:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DEGAUSS:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:DEGAUSS:STATE?
        ```
    """


class ChannelProbeDegauss(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:DEGAUSS`` command.

    Description:
        - This command starts a degauss cycle of the TekVPI probe attached to the specified channel.
          The channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:DEGAUSS value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:DEGAUSS EXECute
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``EXECute`` starts the degauss cycle.

    Properties:
        - ``.state``: The ``CH<x>:PRObe:DEGAUSS:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ChannelProbeDegaussState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ChannelProbeDegaussState:
        """Return the ``CH<x>:PRObe:DEGAUSS:STATE`` command.

        Description:
            - This command queries whether the probe attached to the specified channel requires a
              degauss operation. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:DEGAUSS:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DEGAUSS:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:DEGAUSS:STATE?
            ```
        """
        return self._state


class ChannelProbeCompensate(SCPICmdWriteNoArguments):
    """The ``CH<x>:PRObe:COMPensate`` command.

    Description:
        - This command starts the probe compensation procedure for passive probes. The channel is
          specified by x.

    Usage:
        - Using the ``.write()`` method will send the ``CH<x>:PRObe:COMPensate`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:COMPensate
        ```
    """


class ChannelProbeAutozero(SCPICmdWrite):
    """The ``CH<x>:PRObe:AUTOZero`` command.

    Description:
        - This command executes the attached probe's Auto Zero function, for probes that support
          this feature. See your probe documentation for more details. The channel is specified by
          x.

    Usage:
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:AUTOZero value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PRObe:AUTOZero EXECute
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``EXECute`` sets the probe attached to the specified channel to autozero.
    """


#  pylint: disable=too-many-instance-attributes
class ChannelProbe(SCPICmdRead):
    """The ``CH<x>:PRObe`` command.

    Description:
        - This query-only command returns all information concerning the probe that is attached to
          the specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PRObe?
        ```

    Properties:
        - ``.autozero``: The ``CH<x>:PRObe:AUTOZero`` command.
        - ``.compensate``: The ``CH<x>:PRObe:COMPensate`` command.
        - ``.degauss``: The ``CH<x>:PRObe:DEGAUSS`` command.
        - ``.forcedrange``: The ``CH<x>:PRObe:FORCEDRange`` command.
        - ``.gain``: The ``CH<x>:PRObe:GAIN`` command.
        - ``.id``: The ``CH<x>:PRObe:ID`` command.
        - ``.inputmode``: The ``CH<x>:PRObe:INPUTMode`` command.
        - ``.resistance``: The ``CH<x>:PRObe:RESistance`` command.
        - ``.selfcal``: The ``CH<x>:PRObe:SELFCal`` command.
        - ``.set``: The ``CH<x>:PRObe:SET`` command.
        - ``.status``: The ``CH<x>:PRObe:STATus`` command.
        - ``.units``: The ``CH<x>:PRObe:UNIts`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autozero = ChannelProbeAutozero(device, f"{self._cmd_syntax}:AUTOZero")
        self._compensate = ChannelProbeCompensate(device, f"{self._cmd_syntax}:COMPensate")
        self._degauss = ChannelProbeDegauss(device, f"{self._cmd_syntax}:DEGAUSS")
        self._forcedrange = ChannelProbeForcedrange(device, f"{self._cmd_syntax}:FORCEDRange")
        self._gain = ChannelProbeGain(device, f"{self._cmd_syntax}:GAIN")
        self._id = ChannelProbeId(device, f"{self._cmd_syntax}:ID")
        self._inputmode = ChannelProbeInputmode(device, f"{self._cmd_syntax}:INPUTMode")
        self._resistance = ChannelProbeResistance(device, f"{self._cmd_syntax}:RESistance")
        self._selfcal = ChannelProbeSelfcal(device, f"{self._cmd_syntax}:SELFCal")
        self._set = ChannelProbeSet(device, f"{self._cmd_syntax}:SET")
        self._status = ChannelProbeStatus(device, f"{self._cmd_syntax}:STATus")
        self._units = ChannelProbeUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def autozero(self) -> ChannelProbeAutozero:
        """Return the ``CH<x>:PRObe:AUTOZero`` command.

        Description:
            - This command executes the attached probe's Auto Zero function, for probes that support
              this feature. See your probe documentation for more details. The channel is specified
              by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:AUTOZero value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:AUTOZero EXECute
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``EXECute`` sets the probe attached to the specified channel to autozero.
        """
        return self._autozero

    @property
    def compensate(self) -> ChannelProbeCompensate:
        """Return the ``CH<x>:PRObe:COMPensate`` command.

        Description:
            - This command starts the probe compensation procedure for passive probes. The channel
              is specified by x.

        Usage:
            - Using the ``.write()`` method will send the ``CH<x>:PRObe:COMPensate`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:COMPensate
            ```
        """
        return self._compensate

    @property
    def degauss(self) -> ChannelProbeDegauss:
        """Return the ``CH<x>:PRObe:DEGAUSS`` command.

        Description:
            - This command starts a degauss cycle of the TekVPI probe attached to the specified
              channel. The channel is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:DEGAUSS value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:DEGAUSS EXECute
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``EXECute`` starts the degauss cycle.

        Sub-properties:
            - ``.state``: The ``CH<x>:PRObe:DEGAUSS:STATE`` command.
        """
        return self._degauss

    @property
    def forcedrange(self) -> ChannelProbeForcedrange:
        """Return the ``CH<x>:PRObe:FORCEDRange`` command.

        Description:
            - This command sets the attached TekVPI probe to the specified range, or it queries the
              range of the probe attached to the specified channel. If the <NR3> argument does not
              match one of the available ranges, the closest range will be selected. The channel is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:FORCEDRange value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:FORCEDRange <NR3>
            - CH<x>:PRObe:FORCEDRange?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` specifies the probe dynamic range.
        """
        return self._forcedrange

    @property
    def gain(self) -> ChannelProbeGain:
        """Return the ``CH<x>:PRObe:GAIN`` command.

        Description:
            - This query-only command returns the gain factor of the probe that is attached to the
              specified channel. The channel is specified by x. The gain of a probe is the output
              divided by the input transfer ratio. For example, a common 10x probe has a gain of
              0.1.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:GAIN?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:GAIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:GAIN?
            ```
        """
        return self._gain

    @property
    def id(self) -> ChannelProbeId:
        """Return the ``CH<x>:PRObe:ID`` command.

        Description:
            - This query-only command returns the type and serial number of the probe that is
              attached to the specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:ID?
            ```

        Sub-properties:
            - ``.sernumber``: The ``CH<x>:PRObe:ID:SERnumber`` command.
            - ``.type``: The ``CH<x>:PRObe:ID:TYPe`` command.
        """
        return self._id

    @property
    def inputmode(self) -> ChannelProbeInputmode:
        """Return the ``CH<x>:PRObe:INPUTMode`` command.

        Description:
            - Sets or queries the input mode of the probe that is attached to the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:INPUTMode?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:INPUTMode?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:INPUTMode value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:INPUTMode {A|B|C|D}
            - CH<x>:PRObe:INPUTMode?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``A`` sets the probe to send single-ended A signals to the instrument.
            - ``B`` sets the probe to send single-ended B signals to the instrument.
            - ``COMMONMODE`` sets the probe to send common-mode signals to the instrument.
            - ``DIFFERENTIAL`` sets the probe to send differential signals to the instrument.

        Sub-properties:
            - ``.aoffset``: The ``CH<x>:PRObe:INPUTMode:AOFFSet`` command.
            - ``.boffset``: The ``CH<x>:PRObe:INPUTMode:BOFFSet`` command.
            - ``.coffset``: The ``CH<x>:PRObe:INPUTMode:COFFSet`` command.
            - ``.doffset``: The ``CH<x>:PRObe:INPUTMode:DOFFSet`` command.
        """
        return self._inputmode

    @property
    def resistance(self) -> ChannelProbeResistance:
        """Return the ``CH<x>:PRObe:RESistance`` command.

        Description:
            - This query-only command returns the resistance of the probe that is attached to the
              specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:RESistance?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:RESistance?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:RESistance?
            ```
        """
        return self._resistance

    @property
    def selfcal(self) -> ChannelProbeSelfcal:
        """Return the ``CH<x>:PRObe:SELFCal`` command.

        Description:
            - This command initiates self-calibration on the probe. The channel is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:SELFCal value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:SELFCal EXECUTE
            ```

        Sub-properties:
            - ``.state``: The ``CH<x>:PRObe:SELFCal:State`` command.
        """
        return self._selfcal

    @property
    def set_(self) -> ChannelProbeSet:
        """Return the ``CH<x>:PRObe:SET`` command.

        Description:
            - This command sets or queries aspects of probe accessory user interfaces, for example
              probe attenuation factors or probe audible over range. The available arguments for
              this command will vary depending on the accessory you attach to the instrument. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:SET?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:SET?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:SET value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:SET <QString>
            - CH<x>:PRObe:SET?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is a quoted string representing a settable aspect of the attached
              accessory.
        """
        return self._set

    @property
    def status(self) -> ChannelProbeStatus:
        """Return the ``CH<x>:PRObe:STATus`` command.

        Description:
            - Queries the probe unsigned integer error value.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:STATus?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:STATus?
            ```
        """
        return self._status

    @property
    def units(self) -> ChannelProbeUnits:
        """Return the ``CH<x>:PRObe:UNIts`` command.

        Description:
            - This query-only command returns a string describing the units of measure for the probe
              attached to the specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe:UNIts?
            ```
        """
        return self._units


class ChannelProbefuncExtunitsState(SCPICmdWrite):
    """The ``CH<x>:PROBEFunc:EXTUnits:STATE`` command.

    Description:
        - This command sets or queries the custom units enable state for the specified channel. The
          channel is specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits:STATE value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PROBEFunc:EXTUnits:STATE {ON|OFF|<NR1>}
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``OFF`` argument turns off external units.
        - ``ON`` argument turns on external units.
        - ``<NR1>`` = 0 turns off external units; any other value turns on external units.
    """


class ChannelProbefuncExtunits(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PROBEFunc:EXTUnits`` command.

    Description:
        - This command sets the unit of measurement for the external attenuator of the specified
          channel. The channel is specified by x. The alternate units are used if they are enabled.
          Use the ``CHX:PROBEFUNC:EXTUNITS:STATE`` command to enable or disable the alternate units.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTUnits?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PROBEFunc:EXTUnits <QString>
        - CH<x>:PROBEFunc:EXTUnits?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` indicates the attenuation unit of measurement for the specified channel.

    Properties:
        - ``.state``: The ``CH<x>:PROBEFunc:EXTUnits:STATE`` command.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ChannelProbefuncExtunitsState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ChannelProbefuncExtunitsState:
        """Return the ``CH<x>:PROBEFunc:EXTUnits:STATE`` command.

        Description:
            - This command sets or queries the custom units enable state for the specified channel.
              The channel is specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``CH<x>:PROBEFunc:EXTUnits:STATE value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PROBEFunc:EXTUnits:STATE {ON|OFF|<NR1>}
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``OFF`` argument turns off external units.
            - ``ON`` argument turns on external units.
            - ``<NR1>`` = 0 turns off external units; any other value turns on external units.
        """
        return self._state


class ChannelProbefuncExtdbatten(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PROBEFunc:EXTDBatten`` command.

    Description:
        - This command sets or queries the input-output ratio (expressed in decibel units) of
          external attenuation or gain between the signal and the instrument input channels. The
          channel is specified by x. The query form of this command returns the user-specified
          attenuation in decibels.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTDBatten?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTDBatten?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTDBatten value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PROBEFunc:EXTDBatten <NR3>
        - CH<x>:PROBEFunc:EXTDBatten?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the attenuation value, which is specified in the range from -200.00 dB to
          200.00 dB.
    """


class ChannelProbefuncExtatten(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PROBEFunc:EXTAtten`` command.

    Description:
        - This command is used to specify the attenuation value as a multiplier to the given scale
          factor on the specified channel. The channel is specified by x. The query form of this
          command returns the user-specified attenuation.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTAtten?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTAtten?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTAtten value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PROBEFunc:EXTAtten <NR3>
        - CH<x>:PROBEFunc:EXTAtten?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the attenuation value, which is specified as a multiplier in the range from
          1.00E-10 to 1.00E+10.
    """


class ChannelProbefunc(SCPICmdRead):
    """The ``CH<x>:PROBEFunc`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.extatten``: The ``CH<x>:PROBEFunc:EXTAtten`` command.
        - ``.extdbatten``: The ``CH<x>:PROBEFunc:EXTDBatten`` command.
        - ``.extunits``: The ``CH<x>:PROBEFunc:EXTUnits`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._extatten = ChannelProbefuncExtatten(device, f"{self._cmd_syntax}:EXTAtten")
        self._extdbatten = ChannelProbefuncExtdbatten(device, f"{self._cmd_syntax}:EXTDBatten")
        self._extunits = ChannelProbefuncExtunits(device, f"{self._cmd_syntax}:EXTUnits")

    @property
    def extatten(self) -> ChannelProbefuncExtatten:
        """Return the ``CH<x>:PROBEFunc:EXTAtten`` command.

        Description:
            - This command is used to specify the attenuation value as a multiplier to the given
              scale factor on the specified channel. The channel is specified by x. The query form
              of this command returns the user-specified attenuation.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTAtten?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTAtten?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTAtten value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PROBEFunc:EXTAtten <NR3>
            - CH<x>:PROBEFunc:EXTAtten?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the attenuation value, which is specified as a multiplier in the range
              from 1.00E-10 to 1.00E+10.
        """
        return self._extatten

    @property
    def extdbatten(self) -> ChannelProbefuncExtdbatten:
        """Return the ``CH<x>:PROBEFunc:EXTDBatten`` command.

        Description:
            - This command sets or queries the input-output ratio (expressed in decibel units) of
              external attenuation or gain between the signal and the instrument input channels. The
              channel is specified by x. The query form of this command returns the user-specified
              attenuation in decibels.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTDBatten?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTDBatten?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTDBatten value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PROBEFunc:EXTDBatten <NR3>
            - CH<x>:PROBEFunc:EXTDBatten?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the attenuation value, which is specified in the range from -200.00 dB to
              200.00 dB.
        """
        return self._extdbatten

    @property
    def extunits(self) -> ChannelProbefuncExtunits:
        """Return the ``CH<x>:PROBEFunc:EXTUnits`` command.

        Description:
            - This command sets the unit of measurement for the external attenuator of the specified
              channel. The channel is specified by x. The alternate units are used if they are
              enabled. Use the ``CHX:PROBEFUNC:EXTUNITS:STATE`` command to enable or disable the
              alternate units.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTUnits?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:PROBEFunc:EXTUnits <QString>
            - CH<x>:PROBEFunc:EXTUnits?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` indicates the attenuation unit of measurement for the specified channel.

        Sub-properties:
            - ``.state``: The ``CH<x>:PROBEFunc:EXTUnits:STATE`` command.
        """
        return self._extunits


class ChannelProbecal(SCPICmdRead):
    """The ``CH<x>:PROBECal`` command.

    Description:
        - This query-only command returns the probe calibration state for the specified channel. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBECal?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBECal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:PROBECal?
        ```
    """


class ChannelProbecontrol(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PROBECOntrol`` command.

    Description:
        - This command sets or queries multirange probe range-control policy preference of the probe
          that is attached to CH<x>. The channel number is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBECOntrol?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBECOntrol?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PROBECOntrol value`` command.

    SCPI Syntax:
        ```
        - CH<x>:PROBECOntrol {AUTO|MANual}
        - CH<x>:PROBECOntrol?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``AUTO`` sets the values. The probe range is automatically calculated.
        - ``MANual`` allows you to select various valid values for the probe connected to a
          particular channel.
    """


class ChannelInvert(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:INVert`` command.

    Description:
        - This command sets or queries invert state of the specified channel. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:INVert?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:INVert?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:INVert value`` command.

    SCPI Syntax:
        ```
        - CH<x>:INVert {ON|OFF|<NR1>}
        - CH<x>:INVert?
        ```

    Info:
        - ``OFF`` turns off the channel invert.
        - ``ON`` turns on the channel invert.
        - ``<NR1>`` 0 turns off the channel invert; any other value turns on the channel invert.
    """


class ChannelDitherrange(SCPICmdWrite):
    """The ``CH<x>:DITHERrange`` command.

    Description:
        - This command sets or returns the amount of dithering for the specified analog channel. The
          channel is specified by x. The amount of dithering is a percentage of full scale (10 times
          volts/division). Note: Setting this value to 0.0 for any unused channels may slightly
          improve performance.

    Usage:
        - Using the ``.write(value)`` method will send the ``CH<x>:DITHERrange value`` command.

    SCPI Syntax:
        ```
        - CH<x>:DITHERrange <NR3>
        ```

    Info:
        - ``<NR3>`` is the amount of dithering as a percentage of full scale. Must be between 0.0
          and 100.0 and 0.0 disables dithering.
    """


class ChannelBandwidthFilterOptimization(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:BANdwidth:FILTer:OPTIMIZation`` command.

    Description:
        - This command sets or queries the channel filter shape. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:FILTer:OPTIMIZation?``
          query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth:FILTer:OPTIMIZation?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``CH<x>:BANdwidth:FILTer:OPTIMIZation value`` command.

    SCPI Syntax:
        ```
        - CH<x>:BANdwidth:FILTer:OPTIMIZation {STEPRESPONSE|FLATNESS}
        - CH<x>:BANdwidth:FILTer:OPTIMIZation?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``STEPRESPONSE`` sets a Bessel-Thompson filter that minimizes overshoot with a gradual
          rollof.
        - ``FLATNESS`` sets selects a brick-wall filter optimized for flatness within band with a
          sharp rolloff. Flatness filtering is not compatible with Peak Detect and Envelope
          acquisition modes.
    """


class ChannelBandwidthFilter(SCPICmdRead):
    """The ``CH<x>:BANdwidth:FILTer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:FILTer?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth:FILTer?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.optimization``: The ``CH<x>:BANdwidth:FILTer:OPTIMIZation`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._optimization = ChannelBandwidthFilterOptimization(
            device, f"{self._cmd_syntax}:OPTIMIZation"
        )

    @property
    def optimization(self) -> ChannelBandwidthFilterOptimization:
        """Return the ``CH<x>:BANdwidth:FILTer:OPTIMIZation`` command.

        Description:
            - This command sets or queries the channel filter shape. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:FILTer:OPTIMIZation?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CH<x>:BANdwidth:FILTer:OPTIMIZation?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:BANdwidth:FILTer:OPTIMIZation value`` command.

        SCPI Syntax:
            ```
            - CH<x>:BANdwidth:FILTer:OPTIMIZation {STEPRESPONSE|FLATNESS}
            - CH<x>:BANdwidth:FILTer:OPTIMIZation?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``STEPRESPONSE`` sets a Bessel-Thompson filter that minimizes overshoot with a gradual
              rollof.
            - ``FLATNESS`` sets selects a brick-wall filter optimized for flatness within band with
              a sharp rolloff. Flatness filtering is not compatible with Peak Detect and Envelope
              acquisition modes.
        """
        return self._optimization


class ChannelBandwidth(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:BANdwidth`` command.

    Description:
        - This command sets or queries the selectable low-pass bandwidth limit filter of the
          specified channel. The channel is specified by x. The query form of this command always
          returns the approximate realized bandwidth of the channel. Available arguments depend upon
          the instrument and the attached accessories.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:BANdwidth?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:BANdwidth value`` command.

    SCPI Syntax:
        ```
        - CH<x>:BANdwidth {<NR3>|FULl}
        - CH<x>:BANdwidth?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the desired bandwidth. The instrument rounds this value to an available
          bandwidth using geometric rounding and then uses this value to set the upper bandwidth.
        - ``FULl`` disables any optional bandwidth limiting. The specified channel operates at its
          maximum bandwidth.

    Properties:
        - ``.filter``: The ``CH<x>:BANdwidth:FILTer`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._filter = ChannelBandwidthFilter(device, f"{self._cmd_syntax}:FILTer")

    @property
    def filter(self) -> ChannelBandwidthFilter:
        """Return the ``CH<x>:BANdwidth:FILTer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:BANdwidth:FILTer?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth:FILTer?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.optimization``: The ``CH<x>:BANdwidth:FILTer:OPTIMIZation`` command.
        """
        return self._filter


#  pylint: disable=too-many-instance-attributes
class Channel(ValidatedChannel, SCPICmdRead):
    """The ``CH<x>`` command.

    Description:
        - This query-only command returns the vertical parameters for the specified channel. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>?
        ```

    Properties:
        - ``.bandwidth``: The ``CH<x>:BANdwidth`` command.
        - ``.ditherrange``: The ``CH<x>:DITHERrange`` command.
        - ``.invert``: The ``CH<x>:INVert`` command.
        - ``.probecontrol``: The ``CH<x>:PROBECOntrol`` command.
        - ``.probecal``: The ``CH<x>:PROBECal`` command.
        - ``.probefunc``: The ``CH<x>:PROBEFunc`` command tree.
        - ``.probe``: The ``CH<x>:PRObe`` command.
        - ``.scaleratio``: The ``CH<x>:SCALERATio`` command.
        - ``.sv``: The ``CH<x>:SV`` command tree.
        - ``.termination``: The ``CH<x>:TERmination`` command.
        - ``.vterm``: The ``CH<x>:VTERm`` command tree.
        - ``.d``: The ``CH<x>_D<x>`` command tree.
        - ``.dall``: The ``CH<x>_DALL`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CH<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._bandwidth = ChannelBandwidth(device, f"{self._cmd_syntax}:BANdwidth")
        self._ditherrange = ChannelDitherrange(device, f"{self._cmd_syntax}:DITHERrange")
        self._invert = ChannelInvert(device, f"{self._cmd_syntax}:INVert")
        self._probecontrol = ChannelProbecontrol(device, f"{self._cmd_syntax}:PROBECOntrol")
        self._probecal = ChannelProbecal(device, f"{self._cmd_syntax}:PROBECal")
        self._probefunc = ChannelProbefunc(device, f"{self._cmd_syntax}:PROBEFunc")
        self._probe = ChannelProbe(device, f"{self._cmd_syntax}:PRObe")
        self._scaleratio = ChannelScaleratio(device, f"{self._cmd_syntax}:SCALERATio")
        self._sv = ChannelSv(device, f"{self._cmd_syntax}:SV")
        self._termination = ChannelTermination(device, f"{self._cmd_syntax}:TERmination")
        self._vterm = ChannelVterm(device, f"{self._cmd_syntax}:VTERm")
        self._d: Dict[int, ChannelDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: ChannelDigitalBit(device, f"{self._cmd_syntax}_D{x}")
        )
        self._dall = ChannelDall(device, f"{self._cmd_syntax}_DALL")

    @property
    def bandwidth(self) -> ChannelBandwidth:
        """Return the ``CH<x>:BANdwidth`` command.

        Description:
            - This command sets or queries the selectable low-pass bandwidth limit filter of the
              specified channel. The channel is specified by x. The query form of this command
              always returns the approximate realized bandwidth of the channel. Available arguments
              depend upon the instrument and the attached accessories.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:BANdwidth?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:BANdwidth value`` command.

        SCPI Syntax:
            ```
            - CH<x>:BANdwidth {<NR3>|FULl}
            - CH<x>:BANdwidth?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the desired bandwidth. The instrument rounds this value to an available
              bandwidth using geometric rounding and then uses this value to set the upper
              bandwidth.
            - ``FULl`` disables any optional bandwidth limiting. The specified channel operates at
              its maximum bandwidth.

        Sub-properties:
            - ``.filter``: The ``CH<x>:BANdwidth:FILTer`` command tree.
        """
        return self._bandwidth

    @property
    def ditherrange(self) -> ChannelDitherrange:
        """Return the ``CH<x>:DITHERrange`` command.

        Description:
            - This command sets or returns the amount of dithering for the specified analog channel.
              The channel is specified by x. The amount of dithering is a percentage of full scale
              (10 times volts/division). Note: Setting this value to 0.0 for any unused channels may
              slightly improve performance.

        Usage:
            - Using the ``.write(value)`` method will send the ``CH<x>:DITHERrange value`` command.

        SCPI Syntax:
            ```
            - CH<x>:DITHERrange <NR3>
            ```

        Info:
            - ``<NR3>`` is the amount of dithering as a percentage of full scale. Must be between
              0.0 and 100.0 and 0.0 disables dithering.
        """
        return self._ditherrange

    @property
    def invert(self) -> ChannelInvert:
        """Return the ``CH<x>:INVert`` command.

        Description:
            - This command sets or queries invert state of the specified channel. The channel is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:INVert?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:INVert?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:INVert value`` command.

        SCPI Syntax:
            ```
            - CH<x>:INVert {ON|OFF|<NR1>}
            - CH<x>:INVert?
            ```

        Info:
            - ``OFF`` turns off the channel invert.
            - ``ON`` turns on the channel invert.
            - ``<NR1>`` 0 turns off the channel invert; any other value turns on the channel invert.
        """
        return self._invert

    @property
    def probecontrol(self) -> ChannelProbecontrol:
        """Return the ``CH<x>:PROBECOntrol`` command.

        Description:
            - This command sets or queries multirange probe range-control policy preference of the
              probe that is attached to CH<x>. The channel number is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBECOntrol?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBECOntrol?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PROBECOntrol value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PROBECOntrol {AUTO|MANual}
            - CH<x>:PROBECOntrol?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``AUTO`` sets the values. The probe range is automatically calculated.
            - ``MANual`` allows you to select various valid values for the probe connected to a
              particular channel.
        """
        return self._probecontrol

    @property
    def probecal(self) -> ChannelProbecal:
        """Return the ``CH<x>:PROBECal`` command.

        Description:
            - This query-only command returns the probe calibration state for the specified channel.
              The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBECal?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBECal?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PROBECal?
            ```
        """
        return self._probecal

    @property
    def probefunc(self) -> ChannelProbefunc:
        """Return the ``CH<x>:PROBEFunc`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.extatten``: The ``CH<x>:PROBEFunc:EXTAtten`` command.
            - ``.extdbatten``: The ``CH<x>:PROBEFunc:EXTDBatten`` command.
            - ``.extunits``: The ``CH<x>:PROBEFunc:EXTUnits`` command.
        """
        return self._probefunc

    @property
    def probe(self) -> ChannelProbe:
        """Return the ``CH<x>:PRObe`` command.

        Description:
            - This query-only command returns all information concerning the probe that is attached
              to the specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:PRObe?
            ```

        Sub-properties:
            - ``.autozero``: The ``CH<x>:PRObe:AUTOZero`` command.
            - ``.compensate``: The ``CH<x>:PRObe:COMPensate`` command.
            - ``.degauss``: The ``CH<x>:PRObe:DEGAUSS`` command.
            - ``.forcedrange``: The ``CH<x>:PRObe:FORCEDRange`` command.
            - ``.gain``: The ``CH<x>:PRObe:GAIN`` command.
            - ``.id``: The ``CH<x>:PRObe:ID`` command.
            - ``.inputmode``: The ``CH<x>:PRObe:INPUTMode`` command.
            - ``.resistance``: The ``CH<x>:PRObe:RESistance`` command.
            - ``.selfcal``: The ``CH<x>:PRObe:SELFCal`` command.
            - ``.set``: The ``CH<x>:PRObe:SET`` command.
            - ``.status``: The ``CH<x>:PRObe:STATus`` command.
            - ``.units``: The ``CH<x>:PRObe:UNIts`` command.
        """
        return self._probe

    @property
    def scaleratio(self) -> ChannelScaleratio:
        """Return the ``CH<x>:SCALERATio`` command.

        Description:
            - This command sets or returns the scale ratio for the specified analog channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:SCALERATio?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:SCALERATio?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:SCALERATio value`` command.

        SCPI Syntax:
            ```
            - CH<x>:SCALERATio <NR2>
            - CH<x>:SCALERATio?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR2>`` is the scale ratio for the specified analog channel.
        """
        return self._scaleratio

    @property
    def sv(self) -> ChannelSv:
        """Return the ``CH<x>:SV`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:SV?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:SV?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` specifies the spectrum trace channel source.

        Sub-properties:
            - ``.spanabovebw``: The ``CH<x>:SV:SPANABovebw`` command.
            - ``.spanbelowdc``: The ``CH<x>:SV:SPANBELowdc`` command.
        """
        return self._sv

    @property
    def termination(self) -> ChannelTermination:
        """Return the ``CH<x>:TERmination`` command.

        Description:
            - This command sets or queries the vertical termination for the specified analog
              channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:TERmination?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:TERmination?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:TERmination value`` command.

        SCPI Syntax:
            ```
            - CH<x>:TERmination <NR3>
            - CH<x>:TERmination?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` specifies the channel input resistance, which can be specified as 50 Ω or
              1,000,000 Ω.
        """
        return self._termination

    @property
    def vterm(self) -> ChannelVterm:
        """Return the ``CH<x>:VTERm`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:VTERm?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:VTERm?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.bias``: The ``CH<x>:VTERm:BIAS`` command.
        """
        return self._vterm

    @property
    def d(self) -> Dict[int, ChannelDigitalBit]:
        """Return the ``CH<x>_D<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_D<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.label``: The ``CH<x>_D<x>:LABel`` command tree.
        """
        return self._d

    @property
    def dall(self) -> ChannelDall:
        """Return the ``CH<x>_DALL`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>_DALL?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>_DALL?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.label``: The ``CH<x>_DALL:LABel`` command tree.
        """
        return self._dall
