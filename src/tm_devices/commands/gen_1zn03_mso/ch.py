"""The ch commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CH<x>:BANdwidth {<NR3>|FULl}
    - CH<x>:BANdwidth?
    - CH<x>:CLIPping?
    - CH<x>:COUPling {AC|DC|DCREJect}
    - CH<x>:COUPling?
    - CH<x>:DESKew <NR3>
    - CH<x>:DESKew?
    - CH<x>:DITHERrange <NR3>
    - CH<x>:DITHERrange?
    - CH<x>:INVert {ON|OFF|<NR1>}
    - CH<x>:INVert?
    - CH<x>:LABel:COLor <QString>
    - CH<x>:LABel:COLor?
    - CH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
    - CH<x>:LABel:FONT:BOLD?
    - CH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
    - CH<x>:LABel:FONT:ITALic?
    - CH<x>:LABel:FONT:SIZE <NR1>
    - CH<x>:LABel:FONT:SIZE?
    - CH<x>:LABel:FONT:TYPE <QString>
    - CH<x>:LABel:FONT:TYPE?
    - CH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
    - CH<x>:LABel:FONT:UNDERline?
    - CH<x>:LABel:NAMe <QString>
    - CH<x>:LABel:NAMe?
    - CH<x>:LABel:XPOS <NR3>
    - CH<x>:LABel:XPOS?
    - CH<x>:LABel:YPOS <NR3>
    - CH<x>:LABel:YPOS?
    - CH<x>:OFFSet <NR3>
    - CH<x>:OFFSet?
    - CH<x>:POSition <NR1>
    - CH<x>:POSition?
    - CH<x>:PROBEFunc:EXTAtten <NR3>
    - CH<x>:PROBEFunc:EXTAtten?
    - CH<x>:PROBEFunc:EXTDBatten <NR3>
    - CH<x>:PROBEFunc:EXTDBatten?
    - CH<x>:PROBEFunc:EXTUnits <QString>
    - CH<x>:PROBEFunc:EXTUnits:STATE {ON|OFF|<NR1>}
    - CH<x>:PROBEFunc:EXTUnits:STATE?
    - CH<x>:PROBEFunc:EXTUnits?
    - CH<x>:SCALERATio <NR2>
    - CH<x>:SCALERATio?
    - CH<x>:SCAle <NR3>
    - CH<x>:SCAle?
    - CH<x>:TERmination <NR3>
    - CH<x>:TERmination?
    - CH<x>:VTERm:BIAS <NR3>
    - CH<x>:VTERm:BIAS?
    - CH<x>?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, ValidatedChannel

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


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


class ChannelScale(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:SCAle`` command.

    Description:
        - This command sets or returns the vertical scale for the specified analog channel. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:SCAle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:SCAle value`` command.

    SCPI Syntax:
        ```
        - CH<x>:SCAle <NR3>
        - CH<x>:SCAle?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the vertical scale for the specified analog channel.
    """


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


class ChannelProbefuncExtunitsState(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PROBEFunc:EXTUnits:STATE`` command.

    Description:
        - This command sets or queries measure current status as ON or OFF. The channel is specified
          by x. If this command is set, the vertical scale is set to 'A', as it implies that the
          unit is measuring current from a voltage probe. When it is unset, the vertical scale is
          set to the value of ``CHX:PROBEFUNC:EXTUNITS`` ('V' or 'A').

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTUnits:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits:STATE value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:PROBEFunc:EXTUnits:STATE {ON|OFF|<NR1>}
        - CH<x>:PROBEFunc:EXTUnits:STATE?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``OFF`` argument turns current status off.
        - ``ON`` argument turns current status on.
        - ``<NR1>`` = 0 turns current status off; any other value turns current status on.
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
            - This command sets or queries measure current status as ON or OFF. The channel is
              specified by x. If this command is set, the vertical scale is set to 'A', as it
              implies that the unit is measuring current from a voltage probe. When it is unset, the
              vertical scale is set to the value of ``CHX:PROBEFUNC:EXTUNITS`` ('V' or 'A').

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:PROBEFunc:EXTUnits:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PROBEFunc:EXTUnits:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``CH<x>:PROBEFunc:EXTUnits:STATE value`` command.

        SCPI Syntax:
            ```
            - CH<x>:PROBEFunc:EXTUnits:STATE {ON|OFF|<NR1>}
            - CH<x>:PROBEFunc:EXTUnits:STATE?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``OFF`` argument turns current status off.
            - ``ON`` argument turns current status on.
            - ``<NR1>`` = 0 turns current status off; any other value turns current status on.
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


class ChannelPosition(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:POSition`` command.

    Description:
        - This command sets or queries the vertical position for the specified analog channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:POSition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:POSition value`` command.

    SCPI Syntax:
        ```
        - CH<x>:POSition <NR1>
        - CH<x>:POSition?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR1>`` is the vertical position for the specified analog channel.
    """


class ChannelOffset(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:OFFSet`` command.

    Description:
        - This command sets or queries the vertical offset for the specified analog channel.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:OFFSet?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:OFFSet value`` command.

    SCPI Syntax:
        ```
        - CH<x>:OFFSet <NR3>
        - CH<x>:OFFSet?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the offset value for the specified channel.
    """


class ChannelLabelYpos(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:YPOS`` command.

    Description:
        - This command sets or queries the Y-position of the specified channel label. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:YPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:YPOS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:YPOS value`` command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:YPOS <NR3>
        - CH<x>:LABel:YPOS?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the location (in pixels) where the waveform label for the selected channel is
          displayed, relative to the baseline of the waveform. Positive values are above the
          baseline and negative values are below.
    """


class ChannelLabelXpos(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:XPOS`` command.

    Description:
        - This command sets or queries the X-position of the specified channel label. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:XPOS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:XPOS value`` command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:XPOS <NR3>
        - CH<x>:LABel:XPOS?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the location (in pixels) where the waveform label for the selected channel is
          displayed, relative to the left edge of the screen.
    """


class ChannelLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:NAMe`` command.

    Description:
        - This command sets or queries the label attached to the displayed waveform for the
          specified channel. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:NAMe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:NAMe value`` command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:NAMe <QString>
        - CH<x>:LABel:NAMe?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is an alphanumeric character string, ranging from 1 through 32 characters in
          length.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelLabelFontUnderline(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:FONT:UNDERline`` command.

    Description:
        - This command sets or queries the underline state of the specified channel label. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT:UNDERline?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT:UNDERline?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:FONT:UNDERline value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
        - CH<x>:LABel:FONT:UNDERline?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``OFF`` argument turns off underlined font.
        - ``ON`` argument turns on underlined font.
        - ``<NR1>`` = 0 turns off underlined font; any other value turns on underlined font.
    """


class ChannelLabelFontType(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:FONT:TYPE`` command.

    Description:
        - This command sets or queries the font type of the specified channel label, such as Arial
          or Times New Roman. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT:TYPE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:FONT:TYPE value`` command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:FONT:TYPE <QString>
        - CH<x>:LABel:FONT:TYPE?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is the specified font type.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelLabelFontSize(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:FONT:SIZE`` command.

    Description:
        - This command sets or queries the font size of the specified channel label. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT:SIZE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:FONT:SIZE value`` command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:FONT:SIZE <NR1>
        - CH<x>:LABel:FONT:SIZE?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR1>`` is the font size.
    """


class ChannelLabelFontItalic(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:FONT:ITALic`` command.

    Description:
        - This command sets or queries the italic state of the specified channel label. The channel
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT:ITALic?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT:ITALic?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:FONT:ITALic value``
          command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
        - CH<x>:LABel:FONT:ITALic?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``OFF`` argument turns off italic font.
        - ``ON`` argument turns on italic font.
        - ``<NR1>`` = 0 turns off italic font; any other value turns on italic font.
    """


class ChannelLabelFontBold(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the specified channel label. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT:BOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT:BOLD?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:FONT:BOLD value`` command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
        - CH<x>:LABel:FONT:BOLD?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``OFF`` argument turns off bold font.
        - ``ON`` argument turns on bold font.
        - ``<NR1>`` = 0 turns off bold font; any other value turns on bold font.
    """


class ChannelLabelFont(SCPICmdRead):
    """The ``CH<x>:LABel:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.bold``: The ``CH<x>:LABel:FONT:BOLD`` command.
        - ``.italic``: The ``CH<x>:LABel:FONT:ITALic`` command.
        - ``.size``: The ``CH<x>:LABel:FONT:SIZE`` command.
        - ``.type``: The ``CH<x>:LABel:FONT:TYPE`` command.
        - ``.underline``: The ``CH<x>:LABel:FONT:UNDERline`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = ChannelLabelFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = ChannelLabelFontItalic(device, f"{self._cmd_syntax}:ITALic")
        self._size = ChannelLabelFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = ChannelLabelFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = ChannelLabelFontUnderline(device, f"{self._cmd_syntax}:UNDERline")

    @property
    def bold(self) -> ChannelLabelFontBold:
        """Return the ``CH<x>:LABel:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the specified channel label. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT:BOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT:BOLD?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:FONT:BOLD value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
            - CH<x>:LABel:FONT:BOLD?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``OFF`` argument turns off bold font.
            - ``ON`` argument turns on bold font.
            - ``<NR1>`` = 0 turns off bold font; any other value turns on bold font.
        """
        return self._bold

    @property
    def italic(self) -> ChannelLabelFontItalic:
        """Return the ``CH<x>:LABel:FONT:ITALic`` command.

        Description:
            - This command sets or queries the italic state of the specified channel label. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT:ITALic?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT:ITALic?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:FONT:ITALic value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
            - CH<x>:LABel:FONT:ITALic?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``OFF`` argument turns off italic font.
            - ``ON`` argument turns on italic font.
            - ``<NR1>`` = 0 turns off italic font; any other value turns on italic font.
        """
        return self._italic

    @property
    def size(self) -> ChannelLabelFontSize:
        """Return the ``CH<x>:LABel:FONT:SIZE`` command.

        Description:
            - This command sets or queries the font size of the specified channel label. The channel
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT:SIZE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:FONT:SIZE value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:FONT:SIZE <NR1>
            - CH<x>:LABel:FONT:SIZE?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR1>`` is the font size.
        """
        return self._size

    @property
    def type(self) -> ChannelLabelFontType:
        """Return the ``CH<x>:LABel:FONT:TYPE`` command.

        Description:
            - This command sets or queries the font type of the specified channel label, such as
              Arial or Times New Roman. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT:TYPE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:FONT:TYPE value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:FONT:TYPE <QString>
            - CH<x>:LABel:FONT:TYPE?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is the specified font type.
        """
        return self._type

    @property
    def underline(self) -> ChannelLabelFontUnderline:
        """Return the ``CH<x>:LABel:FONT:UNDERline`` command.

        Description:
            - This command sets or queries the underline state of the specified channel label. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT:UNDERline?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT:UNDERline?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:FONT:UNDERline value``
              command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
            - CH<x>:LABel:FONT:UNDERline?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``OFF`` argument turns off underlined font.
            - ``ON`` argument turns on underlined font.
            - ``<NR1>`` = 0 turns off underlined font; any other value turns on underlined font.
        """
        return self._underline


class ChannelLabelColor(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel:COLor`` command.

    Description:
        - This command sets or queries the color of the specified channel label. The channel is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel:COLor?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:COLor?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel:COLor value`` command.

    SCPI Syntax:
        ```
        - CH<x>:LABel:COLor <QString>
        - CH<x>:LABel:COLor?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<QString>`` is the label color. To return the color to the default color, send an empty
          string as in this example: ``CH5:LABEL:COLOR`` ''.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelLabel(SCPICmdRead):
    """The ``CH<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``CH<x>`` is the channel number.

    Properties:
        - ``.color``: The ``CH<x>:LABel:COLor`` command.
        - ``.font``: The ``CH<x>:LABel:FONT`` command tree.
        - ``.name``: The ``CH<x>:LABel:NAMe`` command.
        - ``.xpos``: The ``CH<x>:LABel:XPOS`` command.
        - ``.ypos``: The ``CH<x>:LABel:YPOS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._color = ChannelLabelColor(device, f"{self._cmd_syntax}:COLor")
        self._font = ChannelLabelFont(device, f"{self._cmd_syntax}:FONT")
        self._name = ChannelLabelName(device, f"{self._cmd_syntax}:NAMe")
        self._xpos = ChannelLabelXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = ChannelLabelYpos(device, f"{self._cmd_syntax}:YPOS")

    @property
    def color(self) -> ChannelLabelColor:
        """Return the ``CH<x>:LABel:COLor`` command.

        Description:
            - This command sets or queries the color of the specified channel label. The channel is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:COLor?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:COLor?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:COLor value`` command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:COLor <QString>
            - CH<x>:LABel:COLor?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is the label color. To return the color to the default color, send an
              empty string as in this example: ``CH5:LABEL:COLOR`` ''.
        """
        return self._color

    @property
    def font(self) -> ChannelLabelFont:
        """Return the ``CH<x>:LABel:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:FONT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.bold``: The ``CH<x>:LABel:FONT:BOLD`` command.
            - ``.italic``: The ``CH<x>:LABel:FONT:ITALic`` command.
            - ``.size``: The ``CH<x>:LABel:FONT:SIZE`` command.
            - ``.type``: The ``CH<x>:LABel:FONT:TYPE`` command.
            - ``.underline``: The ``CH<x>:LABel:FONT:UNDERline`` command.
        """
        return self._font

    @property
    def name(self) -> ChannelLabelName:
        """Return the ``CH<x>:LABel:NAMe`` command.

        Description:
            - This command sets or queries the label attached to the displayed waveform for the
              specified channel. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:NAMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:NAMe value`` command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:NAMe <QString>
            - CH<x>:LABel:NAMe?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<QString>`` is an alphanumeric character string, ranging from 1 through 32
              characters in length.
        """
        return self._name

    @property
    def xpos(self) -> ChannelLabelXpos:
        """Return the ``CH<x>:LABel:XPOS`` command.

        Description:
            - This command sets or queries the X-position of the specified channel label. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:XPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:XPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:XPOS value`` command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:XPOS <NR3>
            - CH<x>:LABel:XPOS?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the location (in pixels) where the waveform label for the selected
              channel is displayed, relative to the left edge of the screen.
        """
        return self._xpos

    @property
    def ypos(self) -> ChannelLabelYpos:
        """Return the ``CH<x>:LABel:YPOS`` command.

        Description:
            - This command sets or queries the Y-position of the specified channel label. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel:YPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel:YPOS?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel:YPOS value`` command.

        SCPI Syntax:
            ```
            - CH<x>:LABel:YPOS <NR3>
            - CH<x>:LABel:YPOS?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the location (in pixels) where the waveform label for the selected
              channel is displayed, relative to the baseline of the waveform. Positive values are
              above the baseline and negative values are below.
        """
        return self._ypos


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


class ChannelDitherrange(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:DITHERrange`` command.

    Description:
        - This command sets or returns the amount of dithering for the specified analog channel. The
          channel is specified by x. The amount of dithering is a percentage of full scale (10 times
          volts/division). Note: Setting this value to 0.0 for any unused channels may slightly
          improve performance.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:DITHERrange?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:DITHERrange?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:DITHERrange value`` command.

    SCPI Syntax:
        ```
        - CH<x>:DITHERrange <NR3>
        - CH<x>:DITHERrange?
        ```

    Info:
        - ``<NR3>`` is the amount of dithering as a percentage of full scale. Must be between 0.0
          and 100.0 and 0.0 disables dithering.
    """


class ChannelDeskew(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:DESKew`` command.

    Description:
        - This command sets or queries the horizontal deskew time for the specified channel. The
          channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:DESKew?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:DESKew?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:DESKew value`` command.

    SCPI Syntax:
        ```
        - CH<x>:DESKew <NR3>
        - CH<x>:DESKew?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the deskew time for this channel, ranging from -125 ns to +125 ns with a
          resolution of 40 ps. Out-of-range values are clipped.
    """


class ChannelCoupling(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:COUPling`` command.

    Description:
        - This command sets or queries the input coupling setting for the specified analog channel.
          The channel is specified by x. The available arguments depend on the attached accessories.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:COUPling?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:COUPling?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:COUPling value`` command.

    SCPI Syntax:
        ```
        - CH<x>:COUPling {AC|DC|DCREJect}
        - CH<x>:COUPling?
        ```

    Info:
        - ``CH<x>`` is the channel number.
        - ``AC`` sets the specified channel to AC coupling.
        - ``DC`` sets the specified channel to DC coupling.
        - ``DCREJect`` sets DC Reject coupling when probes are attached that support that feature.
    """


class ChannelClipping(SCPICmdRead):
    """The ``CH<x>:CLIPping`` command.

    Description:
        - Queries whether the specified channel's input signal is clipping (exceeding) the channel
          A/D converter range. The channel is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``CH<x>:CLIPping?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:CLIPping?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CH<x>:CLIPping?
        ```
    """


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
    """


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
        - ``.clipping``: The ``CH<x>:CLIPping`` command.
        - ``.coupling``: The ``CH<x>:COUPling`` command.
        - ``.deskew``: The ``CH<x>:DESKew`` command.
        - ``.ditherrange``: The ``CH<x>:DITHERrange`` command.
        - ``.invert``: The ``CH<x>:INVert`` command.
        - ``.label``: The ``CH<x>:LABel`` command tree.
        - ``.offset``: The ``CH<x>:OFFSet`` command.
        - ``.position``: The ``CH<x>:POSition`` command.
        - ``.probefunc``: The ``CH<x>:PROBEFunc`` command tree.
        - ``.scaleratio``: The ``CH<x>:SCALERATio`` command.
        - ``.scale``: The ``CH<x>:SCAle`` command.
        - ``.termination``: The ``CH<x>:TERmination`` command.
        - ``.vterm``: The ``CH<x>:VTERm`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CH<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._bandwidth = ChannelBandwidth(device, f"{self._cmd_syntax}:BANdwidth")
        self._clipping = ChannelClipping(device, f"{self._cmd_syntax}:CLIPping")
        self._coupling = ChannelCoupling(device, f"{self._cmd_syntax}:COUPling")
        self._deskew = ChannelDeskew(device, f"{self._cmd_syntax}:DESKew")
        self._ditherrange = ChannelDitherrange(device, f"{self._cmd_syntax}:DITHERrange")
        self._invert = ChannelInvert(device, f"{self._cmd_syntax}:INVert")
        self._label = ChannelLabel(device, f"{self._cmd_syntax}:LABel")
        self._offset = ChannelOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._position = ChannelPosition(device, f"{self._cmd_syntax}:POSition")
        self._probefunc = ChannelProbefunc(device, f"{self._cmd_syntax}:PROBEFunc")
        self._scaleratio = ChannelScaleratio(device, f"{self._cmd_syntax}:SCALERATio")
        self._scale = ChannelScale(device, f"{self._cmd_syntax}:SCAle")
        self._termination = ChannelTermination(device, f"{self._cmd_syntax}:TERmination")
        self._vterm = ChannelVterm(device, f"{self._cmd_syntax}:VTERm")

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
        """
        return self._bandwidth

    @property
    def clipping(self) -> ChannelClipping:
        """Return the ``CH<x>:CLIPping`` command.

        Description:
            - Queries whether the specified channel's input signal is clipping (exceeding) the
              channel A/D converter range. The channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:CLIPping?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:CLIPping?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CH<x>:CLIPping?
            ```
        """
        return self._clipping

    @property
    def coupling(self) -> ChannelCoupling:
        """Return the ``CH<x>:COUPling`` command.

        Description:
            - This command sets or queries the input coupling setting for the specified analog
              channel. The channel is specified by x. The available arguments depend on the attached
              accessories.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:COUPling?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:COUPling?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:COUPling value`` command.

        SCPI Syntax:
            ```
            - CH<x>:COUPling {AC|DC|DCREJect}
            - CH<x>:COUPling?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``AC`` sets the specified channel to AC coupling.
            - ``DC`` sets the specified channel to DC coupling.
            - ``DCREJect`` sets DC Reject coupling when probes are attached that support that
              feature.
        """
        return self._coupling

    @property
    def deskew(self) -> ChannelDeskew:
        """Return the ``CH<x>:DESKew`` command.

        Description:
            - This command sets or queries the horizontal deskew time for the specified channel. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:DESKew?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:DESKew?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:DESKew value`` command.

        SCPI Syntax:
            ```
            - CH<x>:DESKew <NR3>
            - CH<x>:DESKew?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the deskew time for this channel, ranging from -125 ns to +125 ns with a
              resolution of 40 ps. Out-of-range values are clipped.
        """
        return self._deskew

    @property
    def ditherrange(self) -> ChannelDitherrange:
        """Return the ``CH<x>:DITHERrange`` command.

        Description:
            - This command sets or returns the amount of dithering for the specified analog channel.
              The channel is specified by x. The amount of dithering is a percentage of full scale
              (10 times volts/division). Note: Setting this value to 0.0 for any unused channels may
              slightly improve performance.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:DITHERrange?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:DITHERrange?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:DITHERrange value`` command.

        SCPI Syntax:
            ```
            - CH<x>:DITHERrange <NR3>
            - CH<x>:DITHERrange?
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
    def label(self) -> ChannelLabel:
        """Return the ``CH<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Info:
            - ``CH<x>`` is the channel number.

        Sub-properties:
            - ``.color``: The ``CH<x>:LABel:COLor`` command.
            - ``.font``: The ``CH<x>:LABel:FONT`` command tree.
            - ``.name``: The ``CH<x>:LABel:NAMe`` command.
            - ``.xpos``: The ``CH<x>:LABel:XPOS`` command.
            - ``.ypos``: The ``CH<x>:LABel:YPOS`` command.
        """
        return self._label

    @property
    def offset(self) -> ChannelOffset:
        """Return the ``CH<x>:OFFSet`` command.

        Description:
            - This command sets or queries the vertical offset for the specified analog channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:OFFSet value`` command.

        SCPI Syntax:
            ```
            - CH<x>:OFFSet <NR3>
            - CH<x>:OFFSet?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the offset value for the specified channel.
        """
        return self._offset

    @property
    def position(self) -> ChannelPosition:
        """Return the ``CH<x>:POSition`` command.

        Description:
            - This command sets or queries the vertical position for the specified analog channel.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:POSition?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:POSition value`` command.

        SCPI Syntax:
            ```
            - CH<x>:POSition <NR1>
            - CH<x>:POSition?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR1>`` is the vertical position for the specified analog channel.
        """
        return self._position

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
    def scale(self) -> ChannelScale:
        """Return the ``CH<x>:SCAle`` command.

        Description:
            - This command sets or returns the vertical scale for the specified analog channel. The
              channel is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``CH<x>:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:SCAle?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:SCAle value`` command.

        SCPI Syntax:
            ```
            - CH<x>:SCAle <NR3>
            - CH<x>:SCAle?
            ```

        Info:
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the vertical scale for the specified analog channel.
        """
        return self._scale

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
