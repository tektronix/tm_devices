"""The dch commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DCH<x>_D<x>:LABel:COLor <QString>
    - DCH<x>_D<x>:LABel:COLor?
    - DCH<x>_D<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
    - DCH<x>_D<x>:LABel:FONT:BOLD?
    - DCH<x>_D<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
    - DCH<x>_D<x>:LABel:FONT:ITALic?
    - DCH<x>_D<x>:LABel:FONT:SIZE <NR1>
    - DCH<x>_D<x>:LABel:FONT:SIZE?
    - DCH<x>_D<x>:LABel:FONT:TYPE <QString>
    - DCH<x>_D<x>:LABel:FONT:TYPE?
    - DCH<x>_D<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
    - DCH<x>_D<x>:LABel:FONT:UNDERline?
    - DCH<x>_D<x>:LABel:NAMe <QString>
    - DCH<x>_D<x>:LABel:NAMe?
    - DCH<x>_D<x>:THReshold <NR3>
    - DCH<x>_D<x>:THReshold?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDigitalBit,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DchItemDigitalBitThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``DCH<x>_D<x>:THReshold`` command.

    Description:
        - This command sets or queries the threshold level in volts for the specified digital
          channel. If the source channel doesn't exist, a hardware missing error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>_D<x>:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:THReshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:THReshold value`` command.

    SCPI Syntax:
        ```
        - DCH<x>_D<x>:THReshold <NR3>
        - DCH<x>_D<x>:THReshold?
        ```

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``D<x>`` specifies the digital bits. The supported values are 0 to 15. 0 to 7 have common
          a threshold and 8 to 15 have a common threshold.
        - ``<NR3>`` specifies the threshold level in volts for the specified digital channel. The
          minimum value is -20 V and the maximum value is 30.0 V.
    """


class DchItemDigitalBitLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``DCH<x>_D<x>:LABel:NAMe`` command.

    Description:
        - This command sets or queries the label of the specified digital bit.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:NAMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:LABel:NAMe value`` command.

    SCPI Syntax:
        ```
        - DCH<x>_D<x>:LABel:NAMe <QString>
        - DCH<x>_D<x>:LABel:NAMe?
        ```

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``D<x>`` specifies the digital bits. specifies the digital bits. The supported values are
          0 to 15 or DALL (all digital bits).
        - ``<QString>`` is the label name.
    """

    _WRAP_ARG_WITH_QUOTES = True


class DchItemDigitalBitLabelFontUnderline(SCPICmdWrite, SCPICmdRead):
    """The ``DCH<x>_D<x>:LABel:FONT:UNDERline`` command.

    Description:
        - This command sets or queries the underline state of the label of the specified digital
          bit.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT:UNDERline?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:UNDERline?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DCH<x>_D<x>:LABel:FONT:UNDERline value`` command.

    SCPI Syntax:
        ```
        - DCH<x>_D<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
        - DCH<x>_D<x>:LABel:FONT:UNDERline?
        ```

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
        - ``<NR1>`` = 0 turns off underline font; any other value turns on italic font.
        - ``OFF`` turns off underline font.
        - ``ON`` turns on underline font.
    """


class DchItemDigitalBitLabelFontType(SCPICmdWrite, SCPICmdRead):
    """The ``DCH<x>_D<x>:LABel:FONT:TYPE`` command.

    Description:
        - This command sets or queries the font type of the label of the specified digital bit, such
          as Arial or Times New Roman.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:TYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:TYPE value``
          command.

    SCPI Syntax:
        ```
        - DCH<x>_D<x>:LABel:FONT:TYPE <QString>
        - DCH<x>_D<x>:LABel:FONT:TYPE?
        ```

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
        - ``<QString>`` is the font type of the label.
    """

    _WRAP_ARG_WITH_QUOTES = True


class DchItemDigitalBitLabelFontSize(SCPICmdWrite, SCPICmdRead):
    """The ``DCH<x>_D<x>:LABel:FONT:SIZE`` command.

    Description:
        - This command sets or queries the font size of the label of the specified digital bit.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:SIZE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:SIZE value``
          command.

    SCPI Syntax:
        ```
        - DCH<x>_D<x>:LABel:FONT:SIZE <NR1>
        - DCH<x>_D<x>:LABel:FONT:SIZE?
        ```

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
        - ``<NR1>`` specifies the font size in points.
    """


class DchItemDigitalBitLabelFontItalic(SCPICmdWrite, SCPICmdRead):
    """The ``DCH<x>_D<x>:LABel:FONT:ITALic`` command.

    Description:
        - This command sets or queries the italic state of the label of the specified digital bit.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT:ITALic?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:ITALic?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:ITALic value``
          command.

    SCPI Syntax:
        ```
        - DCH<x>_D<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
        - DCH<x>_D<x>:LABel:FONT:ITALic?
        ```

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
        - ``<NR1>`` = 0 turns off italic font; any other value turns on italic font.
        - ``OFF`` turns off italic font.
        - ``ON`` turns on italic font.
    """


class DchItemDigitalBitLabelFontBold(SCPICmdWrite, SCPICmdRead):
    """The ``DCH<x>_D<x>:LABel:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the label of the specified digital bit.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT:BOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:BOLD?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:BOLD value``
          command.

    SCPI Syntax:
        ```
        - DCH<x>_D<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
        - DCH<x>_D<x>:LABel:FONT:BOLD?
        ```

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
        - ``<NR1>`` = 0 turns off bold font; any other value turns on bold font.
        - ``OFF`` turns off bold font.
        - ``ON`` turns on bold font.
    """


class DchItemDigitalBitLabelFont(SCPICmdRead):
    """The ``DCH<x>_D<x>:LABel:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.

    Properties:
        - ``.bold``: The ``DCH<x>_D<x>:LABel:FONT:BOLD`` command.
        - ``.italic``: The ``DCH<x>_D<x>:LABel:FONT:ITALic`` command.
        - ``.size``: The ``DCH<x>_D<x>:LABel:FONT:SIZE`` command.
        - ``.type``: The ``DCH<x>_D<x>:LABel:FONT:TYPE`` command.
        - ``.underline``: The ``DCH<x>_D<x>:LABel:FONT:UNDERline`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = DchItemDigitalBitLabelFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = DchItemDigitalBitLabelFontItalic(device, f"{self._cmd_syntax}:ITALic")
        self._size = DchItemDigitalBitLabelFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = DchItemDigitalBitLabelFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = DchItemDigitalBitLabelFontUnderline(
            device, f"{self._cmd_syntax}:UNDERline"
        )

    @property
    def bold(self) -> DchItemDigitalBitLabelFontBold:
        """Return the ``DCH<x>_D<x>:LABel:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the label of the specified digital bit.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT:BOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:BOLD?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:BOLD value``
              command.

        SCPI Syntax:
            ```
            - DCH<x>_D<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
            - DCH<x>_D<x>:LABel:FONT:BOLD?
            ```

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
            - ``<NR1>`` = 0 turns off bold font; any other value turns on bold font.
            - ``OFF`` turns off bold font.
            - ``ON`` turns on bold font.
        """
        return self._bold

    @property
    def italic(self) -> DchItemDigitalBitLabelFontItalic:
        """Return the ``DCH<x>_D<x>:LABel:FONT:ITALic`` command.

        Description:
            - This command sets or queries the italic state of the label of the specified digital
              bit.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT:ITALic?`` query.
            - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:ITALic?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DCH<x>_D<x>:LABel:FONT:ITALic value`` command.

        SCPI Syntax:
            ```
            - DCH<x>_D<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
            - DCH<x>_D<x>:LABel:FONT:ITALic?
            ```

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
            - ``<NR1>`` = 0 turns off italic font; any other value turns on italic font.
            - ``OFF`` turns off italic font.
            - ``ON`` turns on italic font.
        """
        return self._italic

    @property
    def size(self) -> DchItemDigitalBitLabelFontSize:
        """Return the ``DCH<x>_D<x>:LABel:FONT:SIZE`` command.

        Description:
            - This command sets or queries the font size of the label of the specified digital bit.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:SIZE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:SIZE value``
              command.

        SCPI Syntax:
            ```
            - DCH<x>_D<x>:LABel:FONT:SIZE <NR1>
            - DCH<x>_D<x>:LABel:FONT:SIZE?
            ```

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
            - ``<NR1>`` specifies the font size in points.
        """
        return self._size

    @property
    def type(self) -> DchItemDigitalBitLabelFontType:
        """Return the ``DCH<x>_D<x>:LABel:FONT:TYPE`` command.

        Description:
            - This command sets or queries the font type of the label of the specified digital bit,
              such as Arial or Times New Roman.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT:TYPE value``
              command.

        SCPI Syntax:
            ```
            - DCH<x>_D<x>:LABel:FONT:TYPE <QString>
            - DCH<x>_D<x>:LABel:FONT:TYPE?
            ```

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
            - ``<QString>`` is the font type of the label.
        """
        return self._type

    @property
    def underline(self) -> DchItemDigitalBitLabelFontUnderline:
        """Return the ``DCH<x>_D<x>:LABel:FONT:UNDERline`` command.

        Description:
            - This command sets or queries the underline state of the label of the specified digital
              bit.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT:UNDERline?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DCH<x>_D<x>:LABel:FONT:UNDERline?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DCH<x>_D<x>:LABel:FONT:UNDERline value`` command.

        SCPI Syntax:
            ```
            - DCH<x>_D<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
            - DCH<x>_D<x>:LABel:FONT:UNDERline?
            ```

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
            - ``<NR1>`` = 0 turns off underline font; any other value turns on italic font.
            - ``OFF`` turns off underline font.
            - ``ON`` turns on underline font.
        """
        return self._underline


class DchItemDigitalBitLabelColor(SCPICmdWrite, SCPICmdRead):
    """The ``DCH<x>_D<x>:LABel:COLor`` command.

    Description:
        - This command sets or queries the color of the label of the specified digital bit.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:COLor?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:COLor?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:LABel:COLor value``
          command.

    SCPI Syntax:
        ```
        - DCH<x>_D<x>:LABel:COLor <QString>
        - DCH<x>_D<x>:LABel:COLor?
        ```

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
        - ``<QString>`` is the label color. To return the color to the default color, send an empty
          string as in this example: ``:DCH1_D1:LABEL:COLOR`` ''.
    """

    _WRAP_ARG_WITH_QUOTES = True


class DchItemDigitalBitLabel(SCPICmdRead):
    """The ``DCH<x>_D<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.

    Properties:
        - ``.color``: The ``DCH<x>_D<x>:LABel:COLor`` command.
        - ``.font``: The ``DCH<x>_D<x>:LABel:FONT`` command tree.
        - ``.name``: The ``DCH<x>_D<x>:LABel:NAMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._color = DchItemDigitalBitLabelColor(device, f"{self._cmd_syntax}:COLor")
        self._font = DchItemDigitalBitLabelFont(device, f"{self._cmd_syntax}:FONT")
        self._name = DchItemDigitalBitLabelName(device, f"{self._cmd_syntax}:NAMe")

    @property
    def color(self) -> DchItemDigitalBitLabelColor:
        """Return the ``DCH<x>_D<x>:LABel:COLor`` command.

        Description:
            - This command sets or queries the color of the label of the specified digital bit.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:COLor?`` query.
            - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:COLor?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:LABel:COLor value``
              command.

        SCPI Syntax:
            ```
            - DCH<x>_D<x>:LABel:COLor <QString>
            - DCH<x>_D<x>:LABel:COLor?
            ```

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.
            - ``<QString>`` is the label color. To return the color to the default color, send an
              empty string as in this example: ``:DCH1_D1:LABEL:COLOR`` ''.
        """
        return self._color

    @property
    def font(self) -> DchItemDigitalBitLabelFont:
        """Return the ``DCH<x>_D<x>:LABel:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:FONT?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.

        Sub-properties:
            - ``.bold``: The ``DCH<x>_D<x>:LABel:FONT:BOLD`` command.
            - ``.italic``: The ``DCH<x>_D<x>:LABel:FONT:ITALic`` command.
            - ``.size``: The ``DCH<x>_D<x>:LABel:FONT:SIZE`` command.
            - ``.type``: The ``DCH<x>_D<x>:LABel:FONT:TYPE`` command.
            - ``.underline``: The ``DCH<x>_D<x>:LABel:FONT:UNDERline`` command.
        """
        return self._font

    @property
    def name(self) -> DchItemDigitalBitLabelName:
        """Return the ``DCH<x>_D<x>:LABel:NAMe`` command.

        Description:
            - This command sets or queries the label of the specified digital bit.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel:NAMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:LABel:NAMe value``
              command.

        SCPI Syntax:
            ```
            - DCH<x>_D<x>:LABel:NAMe <QString>
            - DCH<x>_D<x>:LABel:NAMe?
            ```

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``D<x>`` specifies the digital bits. specifies the digital bits. The supported values
              are 0 to 15 or DALL (all digital bits).
            - ``<QString>`` is the label name.
        """
        return self._name


class DchItemDigitalBit(ValidatedDigitalBit, SCPICmdRead):
    """The ``DCH<x>_D<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>_D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.

    Properties:
        - ``.label``: The ``DCH<x>_D<x>:LABel`` command tree.
        - ``.threshold``: The ``DCH<x>_D<x>:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._label = DchItemDigitalBitLabel(device, f"{self._cmd_syntax}:LABel")
        self._threshold = DchItemDigitalBitThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def label(self) -> DchItemDigitalBitLabel:
        """Return the ``DCH<x>_D<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>_D<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.

        Sub-properties:
            - ``.color``: The ``DCH<x>_D<x>:LABel:COLor`` command.
            - ``.font``: The ``DCH<x>_D<x>:LABel:FONT`` command tree.
            - ``.name``: The ``DCH<x>_D<x>:LABel:NAMe`` command.
        """
        return self._label

    @property
    def threshold(self) -> DchItemDigitalBitThreshold:
        """Return the ``DCH<x>_D<x>:THReshold`` command.

        Description:
            - This command sets or queries the threshold level in volts for the specified digital
              channel. If the source channel doesn't exist, a hardware missing error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>_D<x>:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>:THReshold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DCH<x>_D<x>:THReshold value``
              command.

        SCPI Syntax:
            ```
            - DCH<x>_D<x>:THReshold <NR3>
            - DCH<x>_D<x>:THReshold?
            ```

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``D<x>`` specifies the digital bits. The supported values are 0 to 15. 0 to 7 have
              common a threshold and 8 to 15 have a common threshold.
            - ``<NR3>`` specifies the threshold level in volts for the specified digital channel.
              The minimum value is -20 V and the maximum value is 30.0 V.
        """
        return self._threshold


class DchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DCH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DCH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.

    Properties:
        - ``.d``: The ``DCH<x>_D<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DCH<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, DchItemDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: DchItemDigitalBit(device, f"{self._cmd_syntax}_D{x}")
        )

    @property
    def d(self) -> Dict[int, DchItemDigitalBit]:
        """Return the ``DCH<x>_D<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DCH<x>_D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DCH<x>_D<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``D<x>`` specifies the digital bits. The supported values are 0 to 15.

        Sub-properties:
            - ``.label``: The ``DCH<x>_D<x>:LABel`` command tree.
            - ``.threshold``: The ``DCH<x>_D<x>:THReshold`` command.
        """
        return self._d
