# pylint: disable=too-many-lines
"""The ch commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - CH<x>:AMPSVIAVOLTs:ENAble {<NR1>|OFF|ON}
    - CH<x>:AMPSVIAVOLTs:ENAble?
    - CH<x>:AMPSVIAVOLTs:FACtor <NR3>
    - CH<x>:AMPSVIAVOLTs:FACtor?
    - CH<x>:BANdwidth {FULl|<NR3>}
    - CH<x>:BANdwidth?
    - CH<x>:COUPling {AC|DC|DCREJect}
    - CH<x>:COUPling?
    - CH<x>:DESKew <NR3>
    - CH<x>:DESKew?
    - CH<x>:IMPedance {<NR3>|FIFty|MEG}
    - CH<x>:IMPedance?
    - CH<x>:INVert {ON|OFF}
    - CH<x>:INVert?
    - CH<x>:LABel <Qstring>
    - CH<x>:LABel?
    - CH<x>:OFFSet <NR3>
    - CH<x>:OFFSet?
    - CH<x>:POSition <NR3>
    - CH<x>:POSition?
    - CH<x>:PRObe:AUTOZero EXECute
    - CH<x>:PRObe:CALibrate {EXECute|INITialize}
    - CH<x>:PRObe:CALibrate:CALIBRATABLe?
    - CH<x>:PRObe:CALibrate:STATE?
    - CH<x>:PRObe:COMMAND <QString>, <QString>
    - CH<x>:PRObe:DEGAUss EXECute
    - CH<x>:PRObe:DEGAUss:STATE?
    - CH<x>:PRObe:FORCEDRange <NR3>
    - CH<x>:PRObe:FORCEDRange?
    - CH<x>:PRObe:GAIN <NR3>
    - CH<x>:PRObe:GAIN?
    - CH<x>:PRObe:ID:SERnumber?
    - CH<x>:PRObe:ID:TYPe?
    - CH<x>:PRObe:ID?
    - CH<x>:PRObe:MODel <String>
    - CH<x>:PRObe:MODel?
    - CH<x>:PRObe:PROPDELay <NR3>
    - CH<x>:PRObe:PROPDELay?
    - CH<x>:PRObe:RECDESkew?
    - CH<x>:PRObe:RESistance?
    - CH<x>:PRObe:SIGnal {BYPass|PASS}
    - CH<x>:PRObe:SIGnal?
    - CH<x>:PRObe:UNIts?
    - CH<x>:PRObe?
    - CH<x>:SCAle <NR3>
    - CH<x>:SCAle?
    - CH<x>:TERmination {FIFty|MEG|<NR3>}
    - CH<x>:TERmination?
    - CH<x>:VOLts <NR3>
    - CH<x>:VOLts?
    - CH<x>:YUNits <QString>
    - CH<x>:YUNits?
    - CH<x>?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead, SCPICmdWrite, ValidatedChannel

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class ChannelYunits(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:YUNits`` command.

    **Description:**
        - This command specifies the vertical units for the channel specified by <x>, where x is the
          channel number. String arguments are case insensitive and any unsupported units will
          generate an error. Supported units are: %, /Hz, A, A/A, A/V, A/W, A/dB, A/s, AA, AW, AdB,
          As, B, Hz, IRE, S/s, V, V/A, V/V, V/W, V/dB, V/s, VV, VW, VdB, volts, Vs, W, W/A, W/V,
          W/W, W/dB, W/s, WA, WV, WW, WdB, Ws, dB, dB/A, dB/V, dB/W, dB/dB, dBA, dBV, dBW, dBdB,
          day, degrees, div, hr, min, ohms, percent, s The vertical units affect the 'Probe Type'
          that is shown in the 'Probe Setup' menu: Setting ``CH<x>:YUNits`` to 'V' causes the probe
          type to be displayed as 'Voltage'. When ``CH1:AMSVIAVOLTs:ENAble`` is set to OFF, setting
          ``CH<x>:YUNits`` to 'A' causes the probe type to be displayed as 'Current'. Setting
          ``CH<x>:YUNits`` to anything else causes the probe type not to be displayed (neither
          'Voltage' nor 'Current' are highlighted).

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:YUNits?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:YUNits?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:YUNits value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:YUNits <QString>
        - CH<x>:YUNits?

    **Info:**
        - ``QString`` is a string of text surrounded by quotes, specifying the supported units.
    """

    _WRAP_ARG_WITH_QUOTES = True


class ChannelVolts(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:VOLts`` command.

    **Description:**
        - This command specifies the vertical sensitivity for channel <x>, where x is the channel
          number.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:VOLts?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:VOLts?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:VOLts value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:VOLts <NR3>
        - CH<x>:VOLts?

    **Info:**
        - ``<NR3>`` is the vertical sensitivity, in volts.
    """


class ChannelTermination(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:TERmination`` command.

    **Description:**
        - Sets the connected-disconnected status of a 50 Ω resistor which may be connected between
          the specified channel's coupled input and oscilloscope ground. The channel is specified by
          <x>. There is also a corresponding query that requests the termination parameter and
          translates this enumeration into one of the two float values.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:TERmination?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:TERmination?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:TERmination value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:TERmination {FIFty|MEG|<NR3>}
        - CH<x>:TERmination?

    **Info:**
        - ``FIFty`` sets the channel <x> input resistance to 50 Ω.
        - ``MEG`` sets the channel <x> input resistance to 1 MΩ.
        - ``<NR3>`` is a floating point number that specifies the channel <x> input resistance
          numerically.
    """


class ChannelScale(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:SCAle`` command.

    **Description:**
        - This command specifies the vertical scale for the channel specified by <x>, where x is the
          channel number. This setting controls the vertical size of the acquisition window as well
          as the display scale. The range and resolution of scale values depends on the probe
          attached and any other external factors you have specified. For a signal with constant
          amplitude, increasing the scale causes the waveform to be displayed smaller. Decreasing
          the scale causes the waveform to be displayed larger.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:SCAle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:SCAle value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:SCAle <NR3>
        - CH<x>:SCAle?

    **Info:**
        - ``<NR3>`` is a floating point number that specifies the vertical channel scale in
          units-per-division. The value entered here is truncated to three significant digits.
    """


class ChannelProbeUnits(SCPICmdRead):
    """The ``CH<x>:PRObe:UNIts`` command.

    **Description:**
        - This query-only command returns a string describing the units of measure for the probe
          attached to the specified channel. The channel is specified by x.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:UNIts?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:UNIts?
    """


class ChannelProbeSignal(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:SIGnal`` command.

    **Description:**
        - This command specifies the input bypass setting of a TekVPI probe attached to channel <x>,
          where x is the channel number. The probe must support input bypass, for example TCP0001.
          This command is ignored if sent to an unsupported probe.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:SIGnal?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:SIGnal?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:SIGnal value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:SIGnal {BYPass|PASS}
        - CH<x>:PRObe:SIGnal?

    **Info:**
        - ``BYPass`` sets the probe to Bypass mode.
        - ``PASS`` sets the probe to Pass mode.
    """


class ChannelProbeResistance(SCPICmdRead):
    """The ``CH<x>:PRObe:RESistance`` command.

    **Description:**
        - This query-only command returns the resistance of the probe that is attached to the
          specified channel. The channel is specified by x.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:RESistance?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:RESistance?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:RESistance?
    """


class ChannelProbeRecdeskew(SCPICmdRead):
    """The ``CH<x>:PRObe:RECDESkew`` command.

    **Description:**
        - Returns the recommended deskew for the probe connected to the specified channel.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:RECDESkew?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:RECDESkew?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:RECDESkew?
    """


class ChannelProbePropdelay(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:PROPDELay`` command.

    **Description:**
        - This command specifies the propagation delay for the probe connected to the specified
          channel.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:PROPDELay?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:PROPDELay?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:PROPDELay value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:PROPDELay <NR3>
        - CH<x>:PRObe:PROPDELay?

    **Info:**
        - ``<NR3>`` is a floating point number that specifies the propagation time delay for the
          connected probe.
    """


class ChannelProbeModel(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:MODel`` command.

    **Description:**
        - This command specifies the probe model for the specified channel. If a coded probe is
          attached or the specified model is not recognized, an error event is set. The argument
          must be a supported probe. To find the list of supported probes, push the front-panel
          channel 1, 2, 3, or 4 button, then push the lower-menu More item as many times as needed
          to select Deskew. Push Probe Model on the side menu and turn knob a to help you read from
          the resulting list. Alternatively, you can push Test > Analysis > Deskew > Configure >
          Probe Model and read from the resulting list.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:MODel?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:MODel?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:MODel value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:MODel <String>
        - CH<x>:PRObe:MODel?
    """


class ChannelProbeIdType(SCPICmdRead):
    """The ``CH<x>:PRObe:ID:TYPe`` command.

    **Description:**
        - This query-only command returns the type of probe that is attached to the specified
          channel. The channel is specified by x.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:ID:TYPe?
    """


class ChannelProbeIdSernumber(SCPICmdRead):
    """The ``CH<x>:PRObe:ID:SERnumber`` command.

    **Description:**
        - This query-only command returns the serial number of the probe that is attached to the
          specified channel. The channel is specified by x.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:ID:SERnumber?
    """


class ChannelProbeId(SCPICmdRead):
    """The ``CH<x>:PRObe:ID`` command.

    **Description:**
        - This query-only command returns the type and serial number of the probe that is attached
          to the specified channel. The channel is specified by x.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:ID?

    Properties:
        - ``.sernumber``: The ``CH<x>:PRObe:ID:SERnumber`` command.
        - ``.type``: The ``CH<x>:PRObe:ID:TYPe`` command.
    """

    def __init__(self, device: Optional["PIDevice"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._sernumber = ChannelProbeIdSernumber(device, f"{self._cmd_syntax}:SERnumber")
        self._type = ChannelProbeIdType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def sernumber(self) -> ChannelProbeIdSernumber:
        """Return the ``CH<x>:PRObe:ID:SERnumber`` command.

        **Description:**
            - This query-only command returns the serial number of the probe that is attached to the
              specified channel. The channel is specified by x.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:SERnumber?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:ID:SERnumber?
        """
        return self._sernumber

    @property
    def type(self) -> ChannelProbeIdType:
        """Return the ``CH<x>:PRObe:ID:TYPe`` command.

        **Description:**
            - This query-only command returns the type of probe that is attached to the specified
              channel. The channel is specified by x.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:ID:TYPe?
        """
        return self._type


class ChannelProbeGain(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:GAIN`` command.

    **Description:**
        - This command specifies the gain factor for the probe attached to the channel specified by
          <x>, where x is the channel number. The 'gain' of a probe is the output divided by the
          input transfer ratio. For example, a common 10x probe has a gain of 0.1 V.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:GAIN?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:GAIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:GAIN value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:GAIN <NR3>
        - CH<x>:PRObe:GAIN?

    **Info:**
        - ``<NR3>`` is a floating point number that specifies the probe gain. Allowed values depend
          on the specific probe.
    """


class ChannelProbeForcedrange(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:FORCEDRange`` command.

    **Description:**
        - This command sets the attached TekVPI probe to the specified range, or it queries the
          range of the probe attached to the specified channel. If the <NR3> argument does not match
          one of the available ranges, the closest range will be selected. The channel is specified
          by x.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:FORCEDRange value``
          command.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:FORCEDRange <NR3>
        - CH<x>:PRObe:FORCEDRange?

    **Info:**
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` specifies the probe dynamic range.
    """


class ChannelProbeDegaussState(SCPICmdRead):
    """The ``CH<x>:PRObe:DEGAUss:STATE`` command.

    **Description:**
        - This command returns the state of the probe degauss for the channel specified by <x>,
          where is x is the channel number.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:DEGAUss:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DEGAUss:STATE?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:DEGAUss:STATE?
    """


class ChannelProbeDegauss(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:DEGAUss`` command.

    **Description:**
        - This command starts a degauss auto-zero cycle on a TekVPI current probe attached to the
          input channel specified by <x>, where x is the channel number.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:DEGAUss value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:DEGAUss EXECute

    **Info:**
        - ``EXECute`` initiates the degauss operation.

    Properties:
        - ``.state``: The ``CH<x>:PRObe:DEGAUss:STATE`` command.
    """

    def __init__(self, device: Optional["PIDevice"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = ChannelProbeDegaussState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> ChannelProbeDegaussState:
        """Return the ``CH<x>:PRObe:DEGAUss:STATE`` command.

        **Description:**
            - This command returns the state of the probe degauss for the channel specified by <x>,
              where is x is the channel number.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:DEGAUss:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:DEGAUss:STATE?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:DEGAUss:STATE?
        """
        return self._state


class ChannelProbeCommand(SCPICmdWrite):
    """The ``CH<x>:PRObe:COMMAND`` command.

    **Description:**
        - Sets the state of the probe control specified with the first argument to the state
          specified with the second argument. The commands and states are unique to the attached
          probe. Only certain VPI probes support this command. See the specific probe documentation
          for how to set these string arguments. The command form takes 2 string arguments: the
          first is the probe command enumeration and the second is the data value. The query form
          requires a single quoted string argument to specify the probe command enumeration for
          which the response data is requested.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:COMMAND value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:COMMAND <QString>, <QString>

    **Info:**
        - ``<QString>`` are quoted strings specifying the probe command and value to set in the
          probe attached to the specified channel.
    """


class ChannelProbeCalibrateState(SCPICmdRead):
    """The ``CH<x>:PRObe:CALibrate:STATE`` command.

    **Description:**
        - This query returns the calibration state of the probe connected to the specified channel.
          If the probe is calibratable, the state could be either DEFAULT (not calibrated),
          COMPensated, or RUNNING (calibration is proceeding). If the probe is not calibratable,
          DEFAULT will be returned. The channel is specified by x, which can range from 1 through 4.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:CALibrate:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:CALibrate:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:CALibrate:STATE?
    """


class ChannelProbeCalibrateCalibratable(SCPICmdRead):
    """The ``CH<x>:PRObe:CALibrate:CALIBRATABLe`` command.

    **Description:**
        - This query returns the state of the probe attached to channel 1-4, either 0 if the probe
          is not calibratable, or 1 if the probe is calibratable. The channel is specified by x,
          which can range from 1 through 4.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe:CALibrate:CALIBRATABLe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:CALibrate:CALIBRATABLe?``
          query and raise an AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:CALibrate:CALIBRATABLe?
    """


class ChannelProbeCalibrate(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:PRObe:CALibrate`` command.

    **Description:**
        - This command executes a calibration or initialization for the probe attached to channel
          1-4, if the probe is calibratable. To determine whether the probe is calibratable, use
          ``CHX:PROBE:CALIBRATE:CALIBRATABLE``. The channel is specified by x, which can range from
          1 through 4.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:CALibrate value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:CALibrate {EXECute|INITialize}

    **Info:**
        - ``EXECute`` - executes a calibration for the attached probe.
        - ``INITialize`` - initializes the attached probe.

    Properties:
        - ``.calibratable``: The ``CH<x>:PRObe:CALibrate:CALIBRATABLe`` command.
        - ``.state``: The ``CH<x>:PRObe:CALibrate:STATE`` command.
    """

    def __init__(self, device: Optional["PIDevice"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._calibratable = ChannelProbeCalibrateCalibratable(
            device, f"{self._cmd_syntax}:CALIBRATABLe"
        )
        self._state = ChannelProbeCalibrateState(device, f"{self._cmd_syntax}:STATE")

    @property
    def calibratable(self) -> ChannelProbeCalibrateCalibratable:
        """Return the ``CH<x>:PRObe:CALibrate:CALIBRATABLe`` command.

        **Description:**
            - This query returns the state of the probe attached to channel 1-4, either 0 if the
              probe is not calibratable, or 1 if the probe is calibratable. The channel is specified
              by x, which can range from 1 through 4.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:CALibrate:CALIBRATABLe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CH<x>:PRObe:CALibrate:CALIBRATABLe?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:CALibrate:CALIBRATABLe?
        """
        return self._calibratable

    @property
    def state(self) -> ChannelProbeCalibrateState:
        """Return the ``CH<x>:PRObe:CALibrate:STATE`` command.

        **Description:**
            - This query returns the calibration state of the probe connected to the specified
              channel. If the probe is calibratable, the state could be either DEFAULT (not
              calibrated), COMPensated, or RUNNING (calibration is proceeding). If the probe is not
              calibratable, DEFAULT will be returned. The channel is specified by x, which can range
              from 1 through 4.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:CALibrate:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:CALibrate:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:CALibrate:STATE?
        """
        return self._state


class ChannelProbeAutozero(SCPICmdWrite):
    """The ``CH<x>:PRObe:AUTOZero`` command.

    **Description:**
        - This command executes the attached probe's Auto Zero function, for probes that support
          this feature. See your probe documentation for more details. The channel is specified by
          x.

    **Usage:**
        - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:AUTOZero value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe:AUTOZero EXECute

    **Info:**
        - ``CH<x>`` is the channel number.
        - ``EXECute`` sets the probe attached to the specified channel to autozero.
    """


#  pylint: disable=too-many-instance-attributes
class ChannelProbe(SCPICmdRead):
    """The ``CH<x>:PRObe`` command.

    **Description:**
        - This query-only command returns all information concerning the probe that is attached to
          the specified channel. The channel is specified by x.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:PRObe?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - CH<x>:PRObe?

    Properties:
        - ``.autozero``: The ``CH<x>:PRObe:AUTOZero`` command.
        - ``.calibrate``: The ``CH<x>:PRObe:CALibrate`` command.
        - ``.command``: The ``CH<x>:PRObe:COMMAND`` command.
        - ``.degauss``: The ``CH<x>:PRObe:DEGAUss`` command.
        - ``.forcedrange``: The ``CH<x>:PRObe:FORCEDRange`` command.
        - ``.gain``: The ``CH<x>:PRObe:GAIN`` command.
        - ``.id``: The ``CH<x>:PRObe:ID`` command.
        - ``.model``: The ``CH<x>:PRObe:MODel`` command.
        - ``.propdelay``: The ``CH<x>:PRObe:PROPDELay`` command.
        - ``.recdeskew``: The ``CH<x>:PRObe:RECDESkew`` command.
        - ``.resistance``: The ``CH<x>:PRObe:RESistance`` command.
        - ``.signal``: The ``CH<x>:PRObe:SIGnal`` command.
        - ``.units``: The ``CH<x>:PRObe:UNIts`` command.
    """

    def __init__(self, device: Optional["PIDevice"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autozero = ChannelProbeAutozero(device, f"{self._cmd_syntax}:AUTOZero")
        self._calibrate = ChannelProbeCalibrate(device, f"{self._cmd_syntax}:CALibrate")
        self._command = ChannelProbeCommand(device, f"{self._cmd_syntax}:COMMAND")
        self._degauss = ChannelProbeDegauss(device, f"{self._cmd_syntax}:DEGAUss")
        self._forcedrange = ChannelProbeForcedrange(device, f"{self._cmd_syntax}:FORCEDRange")
        self._gain = ChannelProbeGain(device, f"{self._cmd_syntax}:GAIN")
        self._id = ChannelProbeId(device, f"{self._cmd_syntax}:ID")
        self._model = ChannelProbeModel(device, f"{self._cmd_syntax}:MODel")
        self._propdelay = ChannelProbePropdelay(device, f"{self._cmd_syntax}:PROPDELay")
        self._recdeskew = ChannelProbeRecdeskew(device, f"{self._cmd_syntax}:RECDESkew")
        self._resistance = ChannelProbeResistance(device, f"{self._cmd_syntax}:RESistance")
        self._signal = ChannelProbeSignal(device, f"{self._cmd_syntax}:SIGnal")
        self._units = ChannelProbeUnits(device, f"{self._cmd_syntax}:UNIts")

    @property
    def autozero(self) -> ChannelProbeAutozero:
        """Return the ``CH<x>:PRObe:AUTOZero`` command.

        **Description:**
            - This command executes the attached probe's Auto Zero function, for probes that support
              this feature. See your probe documentation for more details. The channel is specified
              by x.

        **Usage:**
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:AUTOZero value``
              command.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:AUTOZero EXECute

        **Info:**
            - ``CH<x>`` is the channel number.
            - ``EXECute`` sets the probe attached to the specified channel to autozero.
        """
        return self._autozero

    @property
    def calibrate(self) -> ChannelProbeCalibrate:
        """Return the ``CH<x>:PRObe:CALibrate`` command.

        **Description:**
            - This command executes a calibration or initialization for the probe attached to
              channel 1-4, if the probe is calibratable. To determine whether the probe is
              calibratable, use ``CHX:PROBE:CALIBRATE:CALIBRATABLE``. The channel is specified by x,
              which can range from 1 through 4.

        **Usage:**
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:CALibrate value``
              command.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:CALibrate {EXECute|INITialize}

        **Info:**
            - ``EXECute`` - executes a calibration for the attached probe.
            - ``INITialize`` - initializes the attached probe.

        Sub-properties:
            - ``.calibratable``: The ``CH<x>:PRObe:CALibrate:CALIBRATABLe`` command.
            - ``.state``: The ``CH<x>:PRObe:CALibrate:STATE`` command.
        """
        return self._calibrate

    @property
    def command(self) -> ChannelProbeCommand:
        """Return the ``CH<x>:PRObe:COMMAND`` command.

        **Description:**
            - Sets the state of the probe control specified with the first argument to the state
              specified with the second argument. The commands and states are unique to the attached
              probe. Only certain VPI probes support this command. See the specific probe
              documentation for how to set these string arguments. The command form takes 2 string
              arguments: the first is the probe command enumeration and the second is the data
              value. The query form requires a single quoted string argument to specify the probe
              command enumeration for which the response data is requested.

        **Usage:**
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:COMMAND value``
              command.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:COMMAND <QString>, <QString>

        **Info:**
            - ``<QString>`` are quoted strings specifying the probe command and value to set in the
              probe attached to the specified channel.
        """
        return self._command

    @property
    def degauss(self) -> ChannelProbeDegauss:
        """Return the ``CH<x>:PRObe:DEGAUss`` command.

        **Description:**
            - This command starts a degauss auto-zero cycle on a TekVPI current probe attached to
              the input channel specified by <x>, where x is the channel number.

        **Usage:**
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:DEGAUss value``
              command.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:DEGAUss EXECute

        **Info:**
            - ``EXECute`` initiates the degauss operation.

        Sub-properties:
            - ``.state``: The ``CH<x>:PRObe:DEGAUss:STATE`` command.
        """
        return self._degauss

    @property
    def forcedrange(self) -> ChannelProbeForcedrange:
        """Return the ``CH<x>:PRObe:FORCEDRange`` command.

        **Description:**
            - This command sets the attached TekVPI probe to the specified range, or it queries the
              range of the probe attached to the specified channel. If the <NR3> argument does not
              match one of the available ranges, the closest range will be selected. The channel is
              specified by x.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:FORCEDRange?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:FORCEDRange value``
              command.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:FORCEDRange <NR3>
            - CH<x>:PRObe:FORCEDRange?

        **Info:**
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` specifies the probe dynamic range.
        """
        return self._forcedrange

    @property
    def gain(self) -> ChannelProbeGain:
        """Return the ``CH<x>:PRObe:GAIN`` command.

        **Description:**
            - This command specifies the gain factor for the probe attached to the channel specified
              by <x>, where x is the channel number. The 'gain' of a probe is the output divided by
              the input transfer ratio. For example, a common 10x probe has a gain of 0.1 V.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:GAIN?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:GAIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:GAIN value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:GAIN <NR3>
            - CH<x>:PRObe:GAIN?

        **Info:**
            - ``<NR3>`` is a floating point number that specifies the probe gain. Allowed values
              depend on the specific probe.
        """
        return self._gain

    @property
    def id(self) -> ChannelProbeId:
        """Return the ``CH<x>:PRObe:ID`` command.

        **Description:**
            - This query-only command returns the type and serial number of the probe that is
              attached to the specified channel. The channel is specified by x.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:ID?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:ID?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:ID?

        Sub-properties:
            - ``.sernumber``: The ``CH<x>:PRObe:ID:SERnumber`` command.
            - ``.type``: The ``CH<x>:PRObe:ID:TYPe`` command.
        """
        return self._id

    @property
    def model(self) -> ChannelProbeModel:
        """Return the ``CH<x>:PRObe:MODel`` command.

        **Description:**
            - This command specifies the probe model for the specified channel. If a coded probe is
              attached or the specified model is not recognized, an error event is set. The argument
              must be a supported probe. To find the list of supported probes, push the front-panel
              channel 1, 2, 3, or 4 button, then push the lower-menu More item as many times as
              needed to select Deskew. Push Probe Model on the side menu and turn knob a to help you
              read from the resulting list. Alternatively, you can push Test > Analysis > Deskew >
              Configure > Probe Model and read from the resulting list.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:MODel?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:MODel?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:MODel value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:MODel <String>
            - CH<x>:PRObe:MODel?
        """
        return self._model

    @property
    def propdelay(self) -> ChannelProbePropdelay:
        """Return the ``CH<x>:PRObe:PROPDELay`` command.

        **Description:**
            - This command specifies the propagation delay for the probe connected to the specified
              channel.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:PROPDELay?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:PROPDELay?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:PROPDELay value``
              command.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:PROPDELay <NR3>
            - CH<x>:PRObe:PROPDELay?

        **Info:**
            - ``<NR3>`` is a floating point number that specifies the propagation time delay for the
              connected probe.
        """
        return self._propdelay

    @property
    def recdeskew(self) -> ChannelProbeRecdeskew:
        """Return the ``CH<x>:PRObe:RECDESkew`` command.

        **Description:**
            - Returns the recommended deskew for the probe connected to the specified channel.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:RECDESkew?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:RECDESkew?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:RECDESkew?
        """
        return self._recdeskew

    @property
    def resistance(self) -> ChannelProbeResistance:
        """Return the ``CH<x>:PRObe:RESistance`` command.

        **Description:**
            - This query-only command returns the resistance of the probe that is attached to the
              specified channel. The channel is specified by x.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:RESistance?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:RESistance?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:RESistance?
        """
        return self._resistance

    @property
    def signal(self) -> ChannelProbeSignal:
        """Return the ``CH<x>:PRObe:SIGnal`` command.

        **Description:**
            - This command specifies the input bypass setting of a TekVPI probe attached to channel
              <x>, where x is the channel number. The probe must support input bypass, for example
              TCP0001. This command is ignored if sent to an unsupported probe.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:SIGnal?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:SIGnal?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:PRObe:SIGnal value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:SIGnal {BYPass|PASS}
            - CH<x>:PRObe:SIGnal?

        **Info:**
            - ``BYPass`` sets the probe to Bypass mode.
            - ``PASS`` sets the probe to Pass mode.
        """
        return self._signal

    @property
    def units(self) -> ChannelProbeUnits:
        """Return the ``CH<x>:PRObe:UNIts`` command.

        **Description:**
            - This query-only command returns a string describing the units of measure for the probe
              attached to the specified channel. The channel is specified by x.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe:UNIts?
        """
        return self._units


class ChannelPosition(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:POSition`` command.

    **Description:**
        - This command specifies the vertical position of channel <x>, where x is the channel number
          (1-4). The position value is applied to the signal before it is digitized. Increasing the
          position value of a waveform causes the waveform to move up. Decreasing the position value
          causes the waveform to move down. The position value determines the vertical graticule
          coordinate at which input signal values, minus the present offset setting for that
          channel, are displayed. For example, if the position for Channel 3 is set to 2.0 and the
          offset is set to 3.0, then input signals equal to 3.0 units are displayed 2.0 divisions
          above the center of the screen (at 1 V/div).

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:POSition?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:POSition value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:POSition <NR3>
        - CH<x>:POSition?

    **Info:**
        - ``<NR3>`` is a floating point number that specifies the position value for channel <x>, in
          divisions, from the center graticule. The range is 8 to -8 divisions.
    """


class ChannelOffset(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:OFFSet`` command.

    **Description:**
        - This command sets or queries the vertical offset for the specified analog channel.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:OFFSet?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:OFFSet value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:OFFSet <NR3>
        - CH<x>:OFFSet?

    **Info:**
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the offset value for the specified channel.
    """


class ChannelLabel(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:LABel`` command.

    **Description:**
        - This command specifies the waveform label for channel <x>, where x is the channel number
          (1-4).

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:LABel?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:LABel value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:LABel <Qstring>
        - CH<x>:LABel?

    **Info:**
        - ``<Qstring>`` is an alphanumeric string of text, enclosed in quotes, that contains the
          text label information for the channel <x> waveform. The text string is limited to 30
          characters.
    """


class ChannelInvert(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:INVert`` command.

    **Description:**
        - This command specifies the invert function for channel <x>, where is the channel number
          (1-4) . When on, the invert function inverts the waveform for the specified channel.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:INVert?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:INVert?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:INVert value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:INVert {ON|OFF}
        - CH<x>:INVert?

    **Info:**
        - ``OFF`` sets the invert function for channel <x> to off.
        - ``ON`` sets the invert function for channel <x> to on.
    """


class ChannelImpedance(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:IMPedance`` command.

    **Description:**
        - This command specifies the input impedance of channel <x>, where x is the channel number.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:IMPedance?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:IMPedance?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:IMPedance value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:IMPedance {<NR3>|FIFty|MEG}
        - CH<x>:IMPedance?

    **Info:**
        - ``FIFty`` sets the input impedance of channel <x> to 50Ω.
        - ``MEG`` sets the input impedance of channel <x> to 1 MΩ.
        - ``<NR3>`` specifies the input impedance for channel <x>. Valid values are 50 or 1.00E+06.
    """


class ChannelDeskew(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:DESKew`` command.

    **Description:**
        - This command sets or queries the horizontal deskew time for the specified channel. The
          channel is specified by x.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:DESKew?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:DESKew?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:DESKew value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:DESKew <NR3>
        - CH<x>:DESKew?

    **Info:**
        - ``CH<x>`` is the channel number.
        - ``<NR3>`` is the deskew time for this channel, ranging from -125 ns to +125 ns with a
          resolution of 40 ps. Out-of-range values are clipped.
    """


class ChannelCoupling(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:COUPling`` command.

    **Description:**
        - This command sets or queries the input coupling setting for the specified analog channel.
          The channel is specified by x. The available arguments depend on the attached accessories.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:COUPling?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:COUPling?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:COUPling value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:COUPling {AC|DC|DCREJect}
        - CH<x>:COUPling?

    **Info:**
        - ``CH<x>`` is the channel number.
        - ``AC`` sets the specified channel to AC coupling.
        - ``DC`` sets the specified channel to DC coupling.
        - ``DCREJect`` sets DC Reject coupling when probes are attached that support that feature.
    """


class ChannelBandwidth(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:BANdwidth`` command.

    **Description:**
        - This command specifies the selectable low-pass bandwidth limit filter for channel <x>,
          where x is the channel number (1-4). Available bandwidth limits vary by model, and are
          also influenced by attached probes. Furthermore, some oscilloscope models support options
          to increase the analog bandwidth. The presence of those options also affects the available
          bandwidth limits. To see what the available bandwidth limits are, on the UI, push the
          relevant channel's front panel button and the push the Bandwidth lower menu button, and
          see what bandwidths are listed in the side menu.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:BANdwidth?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:BANdwidth value`` command.

    **SCPI Syntax:**

    ::

        - CH<x>:BANdwidth {FULl|<NR3>}
        - CH<x>:BANdwidth?

    **Info:**
        - ``FULl`` disables any optional bandwidth limiting. The specified channel operates at its
          maximum attainable bandwidth.
        - ``<NR3>`` is a double-precision ASCII string. The oscilloscope rounds this value to an
          available bandwidth using geometric rounding, and then uses this value to set the upper
          bandwidth limit.
    """


class ChannelAmpsviavoltsFactor(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:AMPSVIAVOLTs:FACtor`` command.

    **Description:**
        - This command specifies the amps via volts factor for the specified channel (1-4).

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:AMPSVIAVOLTs:FACtor?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:AMPSVIAVOLTs:FACtor?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:AMPSVIAVOLTs:FACtor value``
          command.

    **SCPI Syntax:**

    ::

        - CH<x>:AMPSVIAVOLTs:FACtor <NR3>
        - CH<x>:AMPSVIAVOLTs:FACtor?

    **Info:**
        - ``<NR3>`` is a double-precision ASCII string that represents the amps via volts factor.
    """


class ChannelAmpsviavoltsEnable(SCPICmdWrite, SCPICmdRead):
    """The ``CH<x>:AMPSVIAVOLTs:ENAble`` command.

    **Description:**
        - This command specifies the state of the amps via volts feature for the specified channel.
          This feature supports measuring current via the voltage drop across a resistor (1-4).

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:AMPSVIAVOLTs:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:AMPSVIAVOLTs:ENAble?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``CH<x>:AMPSVIAVOLTs:ENAble value``
          command.

    **SCPI Syntax:**

    ::

        - CH<x>:AMPSVIAVOLTs:ENAble {<NR1>|OFF|ON}
        - CH<x>:AMPSVIAVOLTs:ENAble?

    **Info:**
        - ``OFF`` sets the amps via volts function for channel <x> to off.
        - ``ON`` sets the amps via volts function for channel <x> to on.
        - ``<NR1>`` = 0 sets the amps via volts function to off. Any other value sets the function
          to on.
    """


class ChannelAmpsviavolts(SCPICmdRead):
    """The ``CH<x>:AMPSVIAVOLTs`` command tree.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>:AMPSVIAVOLTs?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>:AMPSVIAVOLTs?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``CH<x>:AMPSVIAVOLTs:ENAble`` command.
        - ``.factor``: The ``CH<x>:AMPSVIAVOLTs:FACtor`` command.
    """

    def __init__(self, device: Optional["PIDevice"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = ChannelAmpsviavoltsEnable(device, f"{self._cmd_syntax}:ENAble")
        self._factor = ChannelAmpsviavoltsFactor(device, f"{self._cmd_syntax}:FACtor")

    @property
    def enable(self) -> ChannelAmpsviavoltsEnable:
        """Return the ``CH<x>:AMPSVIAVOLTs:ENAble`` command.

        **Description:**
            - This command specifies the state of the amps via volts feature for the specified
              channel. This feature supports measuring current via the voltage drop across a
              resistor (1-4).

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:AMPSVIAVOLTs:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:AMPSVIAVOLTs:ENAble?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:AMPSVIAVOLTs:ENAble value``
              command.

        **SCPI Syntax:**

        ::

            - CH<x>:AMPSVIAVOLTs:ENAble {<NR1>|OFF|ON}
            - CH<x>:AMPSVIAVOLTs:ENAble?

        **Info:**
            - ``OFF`` sets the amps via volts function for channel <x> to off.
            - ``ON`` sets the amps via volts function for channel <x> to on.
            - ``<NR1>`` = 0 sets the amps via volts function to off. Any other value sets the
              function to on.
        """
        return self._enable

    @property
    def factor(self) -> ChannelAmpsviavoltsFactor:
        """Return the ``CH<x>:AMPSVIAVOLTs:FACtor`` command.

        **Description:**
            - This command specifies the amps via volts factor for the specified channel (1-4).

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:AMPSVIAVOLTs:FACtor?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:AMPSVIAVOLTs:FACtor?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:AMPSVIAVOLTs:FACtor value``
              command.

        **SCPI Syntax:**

        ::

            - CH<x>:AMPSVIAVOLTs:FACtor <NR3>
            - CH<x>:AMPSVIAVOLTs:FACtor?

        **Info:**
            - ``<NR3>`` is a double-precision ASCII string that represents the amps via volts
              factor.
        """
        return self._factor


#  pylint: disable=too-many-instance-attributes
class Channel(ValidatedChannel, SCPICmdRead):
    """The ``CH<x>`` command.

    **Description:**
        - This query-only command returns the vertical parameters for the specified channel. The
          channel is specified by x.

    **Usage:**
        - Using the ``.query()`` method will send the ``CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - CH<x>?

    Properties:
        - ``.ampsviavolts``: The ``CH<x>:AMPSVIAVOLTs`` command tree.
        - ``.bandwidth``: The ``CH<x>:BANdwidth`` command.
        - ``.coupling``: The ``CH<x>:COUPling`` command.
        - ``.deskew``: The ``CH<x>:DESKew`` command.
        - ``.impedance``: The ``CH<x>:IMPedance`` command.
        - ``.invert``: The ``CH<x>:INVert`` command.
        - ``.label``: The ``CH<x>:LABel`` command.
        - ``.offset``: The ``CH<x>:OFFSet`` command.
        - ``.position``: The ``CH<x>:POSition`` command.
        - ``.probe``: The ``CH<x>:PRObe`` command.
        - ``.scale``: The ``CH<x>:SCAle`` command.
        - ``.termination``: The ``CH<x>:TERmination`` command.
        - ``.volts``: The ``CH<x>:VOLts`` command.
        - ``.yunits``: The ``CH<x>:YUNits`` command.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "CH<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._ampsviavolts = ChannelAmpsviavolts(device, f"{self._cmd_syntax}:AMPSVIAVOLTs")
        self._bandwidth = ChannelBandwidth(device, f"{self._cmd_syntax}:BANdwidth")
        self._coupling = ChannelCoupling(device, f"{self._cmd_syntax}:COUPling")
        self._deskew = ChannelDeskew(device, f"{self._cmd_syntax}:DESKew")
        self._impedance = ChannelImpedance(device, f"{self._cmd_syntax}:IMPedance")
        self._invert = ChannelInvert(device, f"{self._cmd_syntax}:INVert")
        self._label = ChannelLabel(device, f"{self._cmd_syntax}:LABel")
        self._offset = ChannelOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._position = ChannelPosition(device, f"{self._cmd_syntax}:POSition")
        self._probe = ChannelProbe(device, f"{self._cmd_syntax}:PRObe")
        self._scale = ChannelScale(device, f"{self._cmd_syntax}:SCAle")
        self._termination = ChannelTermination(device, f"{self._cmd_syntax}:TERmination")
        self._volts = ChannelVolts(device, f"{self._cmd_syntax}:VOLts")
        self._yunits = ChannelYunits(device, f"{self._cmd_syntax}:YUNits")

    @property
    def ampsviavolts(self) -> ChannelAmpsviavolts:
        """Return the ``CH<x>:AMPSVIAVOLTs`` command tree.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:AMPSVIAVOLTs?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:AMPSVIAVOLTs?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``CH<x>:AMPSVIAVOLTs:ENAble`` command.
            - ``.factor``: The ``CH<x>:AMPSVIAVOLTs:FACtor`` command.
        """
        return self._ampsviavolts

    @property
    def bandwidth(self) -> ChannelBandwidth:
        """Return the ``CH<x>:BANdwidth`` command.

        **Description:**
            - This command specifies the selectable low-pass bandwidth limit filter for channel <x>,
              where x is the channel number (1-4). Available bandwidth limits vary by model, and are
              also influenced by attached probes. Furthermore, some oscilloscope models support
              options to increase the analog bandwidth. The presence of those options also affects
              the available bandwidth limits. To see what the available bandwidth limits are, on the
              UI, push the relevant channel's front panel button and the push the Bandwidth lower
              menu button, and see what bandwidths are listed in the side menu.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:BANdwidth?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:BANdwidth?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:BANdwidth value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:BANdwidth {FULl|<NR3>}
            - CH<x>:BANdwidth?

        **Info:**
            - ``FULl`` disables any optional bandwidth limiting. The specified channel operates at
              its maximum attainable bandwidth.
            - ``<NR3>`` is a double-precision ASCII string. The oscilloscope rounds this value to an
              available bandwidth using geometric rounding, and then uses this value to set the
              upper bandwidth limit.
        """
        return self._bandwidth

    @property
    def coupling(self) -> ChannelCoupling:
        """Return the ``CH<x>:COUPling`` command.

        **Description:**
            - This command sets or queries the input coupling setting for the specified analog
              channel. The channel is specified by x. The available arguments depend on the attached
              accessories.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:COUPling?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:COUPling?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:COUPling value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:COUPling {AC|DC|DCREJect}
            - CH<x>:COUPling?

        **Info:**
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

        **Description:**
            - This command sets or queries the horizontal deskew time for the specified channel. The
              channel is specified by x.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:DESKew?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:DESKew?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:DESKew value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:DESKew <NR3>
            - CH<x>:DESKew?

        **Info:**
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the deskew time for this channel, ranging from -125 ns to +125 ns with a
              resolution of 40 ps. Out-of-range values are clipped.
        """
        return self._deskew

    @property
    def impedance(self) -> ChannelImpedance:
        """Return the ``CH<x>:IMPedance`` command.

        **Description:**
            - This command specifies the input impedance of channel <x>, where x is the channel
              number.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:IMPedance?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:IMPedance?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:IMPedance value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:IMPedance {<NR3>|FIFty|MEG}
            - CH<x>:IMPedance?

        **Info:**
            - ``FIFty`` sets the input impedance of channel <x> to 50Ω.
            - ``MEG`` sets the input impedance of channel <x> to 1 MΩ.
            - ``<NR3>`` specifies the input impedance for channel <x>. Valid values are 50 or
              1.00E+06.
        """
        return self._impedance

    @property
    def invert(self) -> ChannelInvert:
        """Return the ``CH<x>:INVert`` command.

        **Description:**
            - This command specifies the invert function for channel <x>, where is the channel
              number (1-4) . When on, the invert function inverts the waveform for the specified
              channel.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:INVert?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:INVert?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:INVert value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:INVert {ON|OFF}
            - CH<x>:INVert?

        **Info:**
            - ``OFF`` sets the invert function for channel <x> to off.
            - ``ON`` sets the invert function for channel <x> to on.
        """
        return self._invert

    @property
    def label(self) -> ChannelLabel:
        """Return the ``CH<x>:LABel`` command.

        **Description:**
            - This command specifies the waveform label for channel <x>, where x is the channel
              number (1-4).

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:LABel?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:LABel value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:LABel <Qstring>
            - CH<x>:LABel?

        **Info:**
            - ``<Qstring>`` is an alphanumeric string of text, enclosed in quotes, that contains the
              text label information for the channel <x> waveform. The text string is limited to 30
              characters.
        """
        return self._label

    @property
    def offset(self) -> ChannelOffset:
        """Return the ``CH<x>:OFFSet`` command.

        **Description:**
            - This command sets or queries the vertical offset for the specified analog channel.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:OFFSet?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:OFFSet value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:OFFSet <NR3>
            - CH<x>:OFFSet?

        **Info:**
            - ``CH<x>`` is the channel number.
            - ``<NR3>`` is the offset value for the specified channel.
        """
        return self._offset

    @property
    def position(self) -> ChannelPosition:
        """Return the ``CH<x>:POSition`` command.

        **Description:**
            - This command specifies the vertical position of channel <x>, where x is the channel
              number (1-4). The position value is applied to the signal before it is digitized.
              Increasing the position value of a waveform causes the waveform to move up. Decreasing
              the position value causes the waveform to move down. The position value determines the
              vertical graticule coordinate at which input signal values, minus the present offset
              setting for that channel, are displayed. For example, if the position for Channel 3 is
              set to 2.0 and the offset is set to 3.0, then input signals equal to 3.0 units are
              displayed 2.0 divisions above the center of the screen (at 1 V/div).

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:POSition?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:POSition value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:POSition <NR3>
            - CH<x>:POSition?

        **Info:**
            - ``<NR3>`` is a floating point number that specifies the position value for channel
              <x>, in divisions, from the center graticule. The range is 8 to -8 divisions.
        """
        return self._position

    @property
    def probe(self) -> ChannelProbe:
        """Return the ``CH<x>:PRObe`` command.

        **Description:**
            - This query-only command returns all information concerning the probe that is attached
              to the specified channel. The channel is specified by x.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:PRObe?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:PRObe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - CH<x>:PRObe?

        Sub-properties:
            - ``.autozero``: The ``CH<x>:PRObe:AUTOZero`` command.
            - ``.calibrate``: The ``CH<x>:PRObe:CALibrate`` command.
            - ``.command``: The ``CH<x>:PRObe:COMMAND`` command.
            - ``.degauss``: The ``CH<x>:PRObe:DEGAUss`` command.
            - ``.forcedrange``: The ``CH<x>:PRObe:FORCEDRange`` command.
            - ``.gain``: The ``CH<x>:PRObe:GAIN`` command.
            - ``.id``: The ``CH<x>:PRObe:ID`` command.
            - ``.model``: The ``CH<x>:PRObe:MODel`` command.
            - ``.propdelay``: The ``CH<x>:PRObe:PROPDELay`` command.
            - ``.recdeskew``: The ``CH<x>:PRObe:RECDESkew`` command.
            - ``.resistance``: The ``CH<x>:PRObe:RESistance`` command.
            - ``.signal``: The ``CH<x>:PRObe:SIGnal`` command.
            - ``.units``: The ``CH<x>:PRObe:UNIts`` command.
        """
        return self._probe

    @property
    def scale(self) -> ChannelScale:
        """Return the ``CH<x>:SCAle`` command.

        **Description:**
            - This command specifies the vertical scale for the channel specified by <x>, where x is
              the channel number. This setting controls the vertical size of the acquisition window
              as well as the display scale. The range and resolution of scale values depends on the
              probe attached and any other external factors you have specified. For a signal with
              constant amplitude, increasing the scale causes the waveform to be displayed smaller.
              Decreasing the scale causes the waveform to be displayed larger.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:SCAle?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:SCAle value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:SCAle <NR3>
            - CH<x>:SCAle?

        **Info:**
            - ``<NR3>`` is a floating point number that specifies the vertical channel scale in
              units-per-division. The value entered here is truncated to three significant digits.
        """
        return self._scale

    @property
    def termination(self) -> ChannelTermination:
        """Return the ``CH<x>:TERmination`` command.

        **Description:**
            - Sets the connected-disconnected status of a 50 Ω resistor which may be connected
              between the specified channel's coupled input and oscilloscope ground. The channel is
              specified by <x>. There is also a corresponding query that requests the termination
              parameter and translates this enumeration into one of the two float values.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:TERmination?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:TERmination?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:TERmination value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:TERmination {FIFty|MEG|<NR3>}
            - CH<x>:TERmination?

        **Info:**
            - ``FIFty`` sets the channel <x> input resistance to 50 Ω.
            - ``MEG`` sets the channel <x> input resistance to 1 MΩ.
            - ``<NR3>`` is a floating point number that specifies the channel <x> input resistance
              numerically.
        """
        return self._termination

    @property
    def volts(self) -> ChannelVolts:
        """Return the ``CH<x>:VOLts`` command.

        **Description:**
            - This command specifies the vertical sensitivity for channel <x>, where x is the
              channel number.

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:VOLts?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:VOLts?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:VOLts value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:VOLts <NR3>
            - CH<x>:VOLts?

        **Info:**
            - ``<NR3>`` is the vertical sensitivity, in volts.
        """
        return self._volts

    @property
    def yunits(self) -> ChannelYunits:
        """Return the ``CH<x>:YUNits`` command.

        **Description:**
            - This command specifies the vertical units for the channel specified by <x>, where x is
              the channel number. String arguments are case insensitive and any unsupported units
              will generate an error. Supported units are: %, /Hz, A, A/A, A/V, A/W, A/dB, A/s, AA,
              AW, AdB, As, B, Hz, IRE, S/s, V, V/A, V/V, V/W, V/dB, V/s, VV, VW, VdB, volts, Vs, W,
              W/A, W/V, W/W, W/dB, W/s, WA, WV, WW, WdB, Ws, dB, dB/A, dB/V, dB/W, dB/dB, dBA, dBV,
              dBW, dBdB, day, degrees, div, hr, min, ohms, percent, s The vertical units affect the
              'Probe Type' that is shown in the 'Probe Setup' menu: Setting ``CH<x>:YUNits`` to 'V'
              causes the probe type to be displayed as 'Voltage'. When ``CH1:AMSVIAVOLTs:ENAble`` is
              set to OFF, setting ``CH<x>:YUNits`` to 'A' causes the probe type to be displayed as
              'Current'. Setting ``CH<x>:YUNits`` to anything else causes the probe type not to be
              displayed (neither 'Voltage' nor 'Current' are highlighted).

        **Usage:**
            - Using the ``.query()`` method will send the ``CH<x>:YUNits?`` query.
            - Using the ``.verify(value)`` method will send the ``CH<x>:YUNits?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``CH<x>:YUNits value`` command.

        **SCPI Syntax:**

        ::

            - CH<x>:YUNits <QString>
            - CH<x>:YUNits?

        **Info:**
            - ``QString`` is a string of text surrounded by quotes, specifying the supported units.
        """
        return self._yunits
