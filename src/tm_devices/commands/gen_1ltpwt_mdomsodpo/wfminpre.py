"""The wfminpre commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - WFMInpre:BIT_Nr <NR1>
    - WFMInpre:BIT_Nr?
    - WFMInpre:BN_Fmt {RI|RP|FP}
    - WFMInpre:BN_Fmt?
    - WFMInpre:BYT_Nr <NR1>
    - WFMInpre:BYT_Nr?
    - WFMInpre:BYT_Or {LSB|MSB}
    - WFMInpre:BYT_Or?
    - WFMInpre:CENTERFREQuency <NR3>
    - WFMInpre:CENTERFREQuency?
    - WFMInpre:DOMain {TIMe|FREQuency}
    - WFMInpre:DOMain?
    - WFMInpre:ENCdg {ASCii|BINary}
    - WFMInpre:ENCdg?
    - WFMInpre:NR_Pt <NR1>
    - WFMInpre:NR_Pt?
    - WFMInpre:PT_Fmt {ENV|Y}
    - WFMInpre:PT_Fmt?
    - WFMInpre:PT_Off <NR1>
    - WFMInpre:PT_Off?
    - WFMInpre:REFLevel <NR3>
    - WFMInpre:REFLevel?
    - WFMInpre:SPAN <NR3>
    - WFMInpre:SPAN?
    - WFMInpre:WFMTYPe {ANALOG|RF_TD|RF_FD}
    - WFMInpre:WFMTYPe?
    - WFMInpre:XINcr <NR3>
    - WFMInpre:XINcr?
    - WFMInpre:XUNit <QString>
    - WFMInpre:XUNit?
    - WFMInpre:XZEro <NR3>
    - WFMInpre:XZEro?
    - WFMInpre:YMUlt <NR3>
    - WFMInpre:YMUlt?
    - WFMInpre:YOFf <NR3>
    - WFMInpre:YOFf?
    - WFMInpre:YUNit <QString>
    - WFMInpre:YUNit?
    - WFMInpre:YZEro <NR3>
    - WFMInpre:YZEro?
    - WFMInpre?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class WfminpreYzero(SCPICmdWrite, SCPICmdRead):
    r"""The ``WFMInpre:YZEro`` command.

    Description:
        - This command specifies the vertical offset of the destination reference waveform in units
          specified by the ``WFMInpre:YUNit`` command. Variations in this number are analogous to
          changing the vertical offset of the waveform. The ``WFMInpre:YMUlt``, ``WFMInpre:YOFf``,
          and ``WFMInpre:YZEro`` commands are used to convert waveform record values to units
          specified using the ``WFMINPRE:YUNIT`` command (YUNit units). It uses the following
          formula (where dl means digitizing levels; ``curve_in_dl`` is a data point value in the
          CURVe data): Value in YUNit units = ((``curve_in_dl`` - YOFf) \* YMUlt) + YZEro

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:YZEro?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:YZEro?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:YZEro value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:YZEro <NR3>
        - WFMInpre:YZEro?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the offset in in units specified by
          the ``WFMInpre:YUNit`` command (YUNits).
    """


class WfminpreYunit(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:YUNit`` command.

    Description:
        - This command specifies the vertical units of data points in the incoming waveform record
          sent to the oscilloscope using the CURVE command. This can be any of several string
          values, depending upon the vertical units of the waveform being sent. Supported units are:
          %, /Hz, A, A/A, A/V, A/W, A/dB, A/s, AA, AW, AdB, As, B, Hz, IRE, S/s, V, V/A, V/V, V/W,
          V/dB, V/s, VV, VW, VdB, volts, Vs, W, W/A, W/V, W/W, W/dB, W/s, WA, WV, WW, WdB, Ws, dB,
          dB/A, dB/V, dB/W, dB/dB, dBA, dBV, dBW, dBdB, day, degrees, div, hr, min, ohms, percent, s

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:YUNit?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:YUNit?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:YUNit value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:YUNit <QString>
        - WFMInpre:YUNit?
        ```

    Info:
        - ``<QString>`` contains the characters that represent the vertical units for the incoming
          waveform.
    """

    _WRAP_ARG_WITH_QUOTES = True


class WfminpreYoff(SCPICmdWrite, SCPICmdRead):
    r"""The ``WFMInpre:YOFf`` command.

    Description:
        - This command specifies the vertical position of the destination reference waveform in
          digitizing levels. There are 25 digitizing levels per vertical division for 1-byte data,
          and 6400 digitizing levels per vertical division for 2-byte data. Variations in this
          number are analogous to changing the vertical position of the waveform. The
          ``WFMInpre:YMUlt``, ``WFMInpre:YOFf``, and ``WFMInpre:YZEro`` commands are used to convert
          waveform record values to units specified using the ``WFMINPRE:YUNIT`` command (YUNit
          units). It uses the following formula (where dl means digitizing levels, and
          ``curve_in_dl`` is a data point value in the CURVe data): Value in YUNit units =
          ((``curve_in_dl`` - YOFf) \* YMUlt) + YZEro

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:YOFf?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:YOFf?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:YOFf value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:YOFf <NR3>
        - WFMInpre:YOFf?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the vertical offset in digitizing
          levels.
    """


class WfminpreYmult(SCPICmdWrite, SCPICmdRead):
    r"""The ``WFMInpre:YMUlt`` command.

    Description:
        - This command specifies the vertical scale multiplying factor to be used to convert the
          incoming data point values being sent to the oscilloscope, from digitizing levels into the
          units specified by the ``WFMInpre:YUNit`` command. For one byte waveform data, there are
          256 digitizing levels. For two byte waveform data there are 65,536 digitizing levels. The
          ``WFMInpre:YMUlt``, ``WFMInpre:YOFf``, and ``WFMInpre:YZEro`` values are used to convert
          waveform record values to units specified using the ``WFMINPRE:YUNIT`` command (YUNit
          units). It uses the following formula (where dl means digitizing level; ``curve_in_dl`` is
          a data point value in the CURVe data): Value in YUNit units = ((``curve_in_dl`` - YOFf) \*
          YMUlt) + YZEro

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:YMUlt?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:YMUlt?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:YMUlt value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:YMUlt <NR3>
        - WFMInpre:YMUlt?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the vertical scale factor per
          digitizing level of the incoming waveform points.
    """


class WfminpreXzero(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:XZEro`` command.

    Description:
        - This command specifies the position value of the first data point in the incoming waveform
          record being sent to the oscilloscope using the CURVE command. The units are determined or
          queried using the ``WFMInpre:XUNit`` command and are typically time, in seconds, or
          frequency, in hertz. This time or frequency is relative to the time or frequency of the
          trigger, which is always 0. Thus, the XZEro value can be negative.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:XZEro?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:XZEro?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:XZEro value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:XZEro <NR3>
        - WFMInpre:XZEro?
        ```

    Info:
        - ``<NR3>`` is the floating point value of the position, in XUNits, of the first sample in
          the incoming waveform. If XUNits is 's', <NR3> is the time of the first sample in the
          incoming waveform.
    """


class WfminpreXunit(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:XUNit`` command.

    Description:
        - This command specifies the horizontal units of the x-axis of the data points being sent to
          the oscilloscope using the CURVE command. This value can be in 's' for seconds, or 'Hz'.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:XUNit?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:XUNit?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:XUNit value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:XUNit <QString>
        - WFMInpre:XUNit?
        ```

    Info:
        - ``<QString>`` contains the characters that represent the horizontal units for the incoming
          waveform.
    """

    _WRAP_ARG_WITH_QUOTES = True


class WfminpreXincr(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:XINcr`` command.

    Description:
        - This command specifies the horizontal interval between incoming waveform points sent to
          the oscilloscope using the CURVE command. The units are time, in seconds, or frequency, in
          hertz, and can be specified or queried using the ``WFMInpre:XUNit`` command.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:XINcr?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:XINcr?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:XINcr value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:XINcr <NR3>
        - WFMInpre:XINcr?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the horizontal interval
          representation.
    """


class WfminpreWfmtype(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:WFMTYPe`` command.

    Description:
        - This command specifies the type of waveform that is being transferred to the oscilloscope
          for storage in one of the REF1 - REF4 memory locations. The waveform type possibilities
          are the ANALOG, the RF time domain waveforms (``RF_TD``), or the RF frequency domain
          waveforms (``RF_FD``). The default is ANALOG. This parameter should be set before using
          the CURVe command to transfer a waveform from a PC to an internal reference location. The
          type of waveform that is being transferred in turn determines which window will display it
          on the instrument screen: the time domain window or frequency domain window. Both the
          analog and RF-TD arguments specify the time domain window; the ``RF_FD`` argument
          specifies the frequency domain window.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:WFMTYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:WFMTYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:WFMTYPe value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:WFMTYPe {ANALOG|RF_TD|RF_FD}
        - WFMInpre:WFMTYPe?
        ```

    Info:
        - ``ANALOG`` - this type includes Channels 1-4 and the Math waveform, and specifies to
          display it in the time domain window.
        - ``RF_TD`` - this type includes the three RF time domain traces (RF Amplitude vs. Time, RF
          Frequency vs. Time, and RF Phase vs. Time) and specifies to display it in the time domain
          window.
        - ``RF_FD`` - this type includes the four RF frequency domain traces (RF Normal, RF Average,
          RF Max Hold, and RF Min Hold) and specifies to display it in the frequency domain window.
    """


class WfminpreSpan(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:SPAN`` command.

    Description:
        - This command specifies the frequency span of the incoming RF trace. The span is the range
          of frequencies that can be observed around the center frequency.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:SPAN?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:SPAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:SPAN value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:SPAN <NR3>
        - WFMInpre:SPAN?
        ```

    Info:
        - ``<NR3>`` is a floating point number that can range from 1 kHz to 3 GHz. The maximum span
          is 3 GHz if option 3-SA3 is installed. Without that option, the maximum is identical to
          the analog bandwidth.
    """


class WfminpreReflevel(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:REFLevel`` command.

    Description:
        - This command specifies the Reference Level of the incoming waveform. This command applies
          only to frequency domain waveforms. The Reference Level is adjustable from 10 pico Watts
          (-140dBm) to 1 Watt (+30dBm).

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:REFLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:REFLevel?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:REFLevel value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:REFLevel <NR3>
        - WFMInpre:REFLevel?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the Reference Level of the incoming
          waveform, in watts.
    """


class WfminprePtOff(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:PT_Off`` command.

    Description:
        - The set form of this command is ignored. The query form always returns a 0. (This command
          is listed for compatibility with other Tektronix oscilloscopes.)

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:PT_Off?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:PT_Off?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:PT_Off value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:PT_Off <NR1>
        - WFMInpre:PT_Off?
        ```
    """


class WfminprePtFmt(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:PT_Fmt`` command.

    Description:
        - This command specifies the acquisition format of the data points to be sent to the
          oscilloscope using the CURVE command. This can be Y for YT format, or ENV for envelope
          mode (min/max pairs). For YT format, each data value represents a single waveform data
          point. For envelope format, each data point represents a min/max pair, where the minimum
          value precedes the maximum value.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:PT_Fmt?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:PT_Fmt?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:PT_Fmt value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:PT_Fmt {ENV|Y}
        - WFMInpre:PT_Fmt?
        ```

    Info:
        - ``ENV`` specifies that the waveform is to be transmitted in envelope mode as minimum and
          maximum point pairs. Only Y values are explicitly transmitted. Absolute coordinates are
          given by.
        - ``Xn = XZEro + XINcr (n - PT_Off)``
        - ``Ynmax = YZEro + YMUlt (ynmax - YOFf)``
        - ``Ynmin = YZEro + YMUlt (ynmin - YOFf)``
        - ``Y`` specifies a normal waveform where one ASCII or binary data point is transmitted for
          each point in the waveform record. Only Y values are explicitly transmitted. Absolute
          coordinates are given by.
        - ``Xn = XZEro + XINcr (n - PT_Off)``
        - ``Yn = YZEro + YMUlt (yn - YOFf)``
    """


class WfminpreNrPt(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:NR_Pt`` command.

    Description:
        - This command specifies the number of data points that are in the incoming waveform record
          to be sent to the oscilloscope using the CURVe command.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:NR_Pt?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:NR_Pt?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:NR_Pt value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:NR_Pt <NR1>
        - WFMInpre:NR_Pt?
        ```

    Info:
        - ``<NR1>`` is the number of data points if ``WFMInpre:PT_Fmt`` is set to Y. It is the
          number of min-max pairs if ``WFMInpre:PT_Fmt`` is set to ENV.
    """


class WfminpreEncdg(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:ENCdg`` command.

    Description:
        - This command specifies the type of encoding of the incoming waveform data to be sent to
          the oscilloscope using the CURVe command. Supported types are BINary and ASCii.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:ENCdg?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:ENCdg?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:ENCdg value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:ENCdg {ASCii|BINary}
        - WFMInpre:ENCdg?
        ```

    Info:
        - ``ASCii`` specifies that the incoming data is in ASCII format.
        - ``BINary`` specifies that the incoming data is in a binary format whose further
          interpretation requires knowledge of ``BYT_NR``, ``BIT_NR``, ``BN_FMT``, and ``BYT_OR``.
    """


class WfminpreDomain(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:DOMain`` command.

    Description:
        - This command specifies whether the information being sent to a reference location should
          be treated as integer (time domain) information, or floating point (frequency domain)
          information, for the purposes of storing the data internally. The default is TIMe. This
          parameter should be set before using the CURVe command to transfer a waveform from a PC to
          an internal reference location.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:DOMain?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:DOMain?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:DOMain value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:DOMain {TIMe|FREQuency}
        - WFMInpre:DOMain?
        ```

    Info:
        - ``TIMe`` specifies to treat the information to be transferred as integer values.
        - ``FREQuency`` specifies to treat the information to be transferred as floating point
          values.
    """


class WfminpreCenterfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:CENTERFREQuency`` command.

    Description:
        - This command specifies the center frequency of the incoming RF trace (waveform), in hertz.
          The center frequency is a precise frequency at the center of the frequency domain display.
          In many applications, it is a carrier frequency.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:CENTERFREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:CENTERFREQuency?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:CENTERFREQuency value``
          command.

    SCPI Syntax:
        ```
        - WFMInpre:CENTERFREQuency <NR3>
        - WFMInpre:CENTERFREQuency?
        ```

    Info:
        - ``<NR3>`` is a floating point number.
    """


class WfminpreBytOr(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:BYT_Or`` command.

    Description:
        - This command specifies which byte of incoming binary waveform data is transmitted first
          (the byte order). The byte order can either be MSB (most significant byte first) or LSB
          (least significant byte first, also known as IBM format). This specification only has
          meaning when ``WFMINPRE:ENCDG`` is set to BINary and ``WFMINPRE:BYT_NR`` is 2.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:BYT_Or?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:BYT_Or?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:BYT_Or value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:BYT_Or {LSB|MSB}
        - WFMInpre:BYT_Or?
        ```

    Info:
        - ``LSB`` specifies that the least significant byte will be expected first.
        - ``MSB`` specifies that the most significant byte will be expected first.
    """


class WfminpreBytNr(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:BYT_Nr`` command.

    Description:
        - This command specifies the number of bytes per data point in the waveform data to be sent
          to the oscilloscope using the CURVe command. Changing this value also changes the value of
          ``WFMINPRE:BIT_NR``.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:BYT_Nr?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:BYT_Nr?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:BYT_Nr value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:BYT_Nr <NR1>
        - WFMInpre:BYT_Nr?
        ```

    Info:
        - ``<NR1>`` is the number of bytes per data point. The number of bytes can be 1 or 2 for
          Analog, Math or the digital channels D0 - D15. It can be 4 or 8 for DIGital collection
          data. It must be 4 for frequency domain trace data.
    """


class WfminpreBnFmt(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:BN_Fmt`` command.

    Description:
        - This command specifies the format of the data for outgoing waveforms when
          ``WFMInpre:ENCdg`` is set to BINary. The format can either be RI (signed integer), RP
          (positive integer) or FP (floating point).

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:BN_Fmt?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:BN_Fmt?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:BN_Fmt value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:BN_Fmt {RI|RP|FP}
        - WFMInpre:BN_Fmt?
        ```

    Info:
        - ``RI`` specifies signed integer data point representation.
        - ``RP`` specifies positive integer data point representation.
        - ``FP`` specifies floating point data representation.
    """


class WfminpreBitNr(SCPICmdWrite, SCPICmdRead):
    """The ``WFMInpre:BIT_Nr`` command.

    Description:
        - This command specifies the number of bits per data point in the waveform data to be sent
          to the oscilloscope using the CURVe command. Changing this value also changes the value of
          ``WFMINPRE:BYT_NR``.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre:BIT_Nr?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre:BIT_Nr?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WFMInpre:BIT_Nr value`` command.

    SCPI Syntax:
        ```
        - WFMInpre:BIT_Nr <NR1>
        - WFMInpre:BIT_Nr?
        ```

    Info:
        - ``<NR1>`` number of bits per data point can be 8 , 16, 32 or 64.
    """


#  pylint: disable=too-many-instance-attributes
class Wfminpre(SCPICmdRead):
    """The ``WFMInpre`` command.

    Description:
        - Returns the waveform formatting and scaling specifications to be applied to the next
          incoming CURVe command data.

    Usage:
        - Using the ``.query()`` method will send the ``WFMInpre?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMInpre?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMInpre?
        ```

    Properties:
        - ``.bit_nr``: The ``WFMInpre:BIT_Nr`` command.
        - ``.bn_fmt``: The ``WFMInpre:BN_Fmt`` command.
        - ``.byt_nr``: The ``WFMInpre:BYT_Nr`` command.
        - ``.byt_or``: The ``WFMInpre:BYT_Or`` command.
        - ``.centerfrequency``: The ``WFMInpre:CENTERFREQuency`` command.
        - ``.domain``: The ``WFMInpre:DOMain`` command.
        - ``.encdg``: The ``WFMInpre:ENCdg`` command.
        - ``.nr_pt``: The ``WFMInpre:NR_Pt`` command.
        - ``.pt_fmt``: The ``WFMInpre:PT_Fmt`` command.
        - ``.pt_off``: The ``WFMInpre:PT_Off`` command.
        - ``.reflevel``: The ``WFMInpre:REFLevel`` command.
        - ``.span``: The ``WFMInpre:SPAN`` command.
        - ``.wfmtype``: The ``WFMInpre:WFMTYPe`` command.
        - ``.xincr``: The ``WFMInpre:XINcr`` command.
        - ``.xunit``: The ``WFMInpre:XUNit`` command.
        - ``.xzero``: The ``WFMInpre:XZEro`` command.
        - ``.ymult``: The ``WFMInpre:YMUlt`` command.
        - ``.yoff``: The ``WFMInpre:YOFf`` command.
        - ``.yunit``: The ``WFMInpre:YUNit`` command.
        - ``.yzero``: The ``WFMInpre:YZEro`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "WFMInpre") -> None:
        super().__init__(device, cmd_syntax)
        self._bit_nr = WfminpreBitNr(device, f"{self._cmd_syntax}:BIT_Nr")
        self._bn_fmt = WfminpreBnFmt(device, f"{self._cmd_syntax}:BN_Fmt")
        self._byt_nr = WfminpreBytNr(device, f"{self._cmd_syntax}:BYT_Nr")
        self._byt_or = WfminpreBytOr(device, f"{self._cmd_syntax}:BYT_Or")
        self._centerfrequency = WfminpreCenterfrequency(
            device, f"{self._cmd_syntax}:CENTERFREQuency"
        )
        self._domain = WfminpreDomain(device, f"{self._cmd_syntax}:DOMain")
        self._encdg = WfminpreEncdg(device, f"{self._cmd_syntax}:ENCdg")
        self._nr_pt = WfminpreNrPt(device, f"{self._cmd_syntax}:NR_Pt")
        self._pt_fmt = WfminprePtFmt(device, f"{self._cmd_syntax}:PT_Fmt")
        self._pt_off = WfminprePtOff(device, f"{self._cmd_syntax}:PT_Off")
        self._reflevel = WfminpreReflevel(device, f"{self._cmd_syntax}:REFLevel")
        self._span = WfminpreSpan(device, f"{self._cmd_syntax}:SPAN")
        self._wfmtype = WfminpreWfmtype(device, f"{self._cmd_syntax}:WFMTYPe")
        self._xincr = WfminpreXincr(device, f"{self._cmd_syntax}:XINcr")
        self._xunit = WfminpreXunit(device, f"{self._cmd_syntax}:XUNit")
        self._xzero = WfminpreXzero(device, f"{self._cmd_syntax}:XZEro")
        self._ymult = WfminpreYmult(device, f"{self._cmd_syntax}:YMUlt")
        self._yoff = WfminpreYoff(device, f"{self._cmd_syntax}:YOFf")
        self._yunit = WfminpreYunit(device, f"{self._cmd_syntax}:YUNit")
        self._yzero = WfminpreYzero(device, f"{self._cmd_syntax}:YZEro")

    @property
    def bit_nr(self) -> WfminpreBitNr:
        """Return the ``WFMInpre:BIT_Nr`` command.

        Description:
            - This command specifies the number of bits per data point in the waveform data to be
              sent to the oscilloscope using the CURVe command. Changing this value also changes the
              value of ``WFMINPRE:BYT_NR``.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:BIT_Nr?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:BIT_Nr?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:BIT_Nr value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:BIT_Nr <NR1>
            - WFMInpre:BIT_Nr?
            ```

        Info:
            - ``<NR1>`` number of bits per data point can be 8 , 16, 32 or 64.
        """
        return self._bit_nr

    @property
    def bn_fmt(self) -> WfminpreBnFmt:
        """Return the ``WFMInpre:BN_Fmt`` command.

        Description:
            - This command specifies the format of the data for outgoing waveforms when
              ``WFMInpre:ENCdg`` is set to BINary. The format can either be RI (signed integer), RP
              (positive integer) or FP (floating point).

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:BN_Fmt?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:BN_Fmt?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:BN_Fmt value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:BN_Fmt {RI|RP|FP}
            - WFMInpre:BN_Fmt?
            ```

        Info:
            - ``RI`` specifies signed integer data point representation.
            - ``RP`` specifies positive integer data point representation.
            - ``FP`` specifies floating point data representation.
        """
        return self._bn_fmt

    @property
    def byt_nr(self) -> WfminpreBytNr:
        """Return the ``WFMInpre:BYT_Nr`` command.

        Description:
            - This command specifies the number of bytes per data point in the waveform data to be
              sent to the oscilloscope using the CURVe command. Changing this value also changes the
              value of ``WFMINPRE:BIT_NR``.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:BYT_Nr?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:BYT_Nr?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:BYT_Nr value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:BYT_Nr <NR1>
            - WFMInpre:BYT_Nr?
            ```

        Info:
            - ``<NR1>`` is the number of bytes per data point. The number of bytes can be 1 or 2 for
              Analog, Math or the digital channels D0 - D15. It can be 4 or 8 for DIGital collection
              data. It must be 4 for frequency domain trace data.
        """
        return self._byt_nr

    @property
    def byt_or(self) -> WfminpreBytOr:
        """Return the ``WFMInpre:BYT_Or`` command.

        Description:
            - This command specifies which byte of incoming binary waveform data is transmitted
              first (the byte order). The byte order can either be MSB (most significant byte first)
              or LSB (least significant byte first, also known as IBM format). This specification
              only has meaning when ``WFMINPRE:ENCDG`` is set to BINary and ``WFMINPRE:BYT_NR`` is
              2.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:BYT_Or?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:BYT_Or?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:BYT_Or value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:BYT_Or {LSB|MSB}
            - WFMInpre:BYT_Or?
            ```

        Info:
            - ``LSB`` specifies that the least significant byte will be expected first.
            - ``MSB`` specifies that the most significant byte will be expected first.
        """
        return self._byt_or

    @property
    def centerfrequency(self) -> WfminpreCenterfrequency:
        """Return the ``WFMInpre:CENTERFREQuency`` command.

        Description:
            - This command specifies the center frequency of the incoming RF trace (waveform), in
              hertz. The center frequency is a precise frequency at the center of the frequency
              domain display. In many applications, it is a carrier frequency.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:CENTERFREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:CENTERFREQuency?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:CENTERFREQuency value``
              command.

        SCPI Syntax:
            ```
            - WFMInpre:CENTERFREQuency <NR3>
            - WFMInpre:CENTERFREQuency?
            ```

        Info:
            - ``<NR3>`` is a floating point number.
        """
        return self._centerfrequency

    @property
    def domain(self) -> WfminpreDomain:
        """Return the ``WFMInpre:DOMain`` command.

        Description:
            - This command specifies whether the information being sent to a reference location
              should be treated as integer (time domain) information, or floating point (frequency
              domain) information, for the purposes of storing the data internally. The default is
              TIMe. This parameter should be set before using the CURVe command to transfer a
              waveform from a PC to an internal reference location.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:DOMain?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:DOMain?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:DOMain value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:DOMain {TIMe|FREQuency}
            - WFMInpre:DOMain?
            ```

        Info:
            - ``TIMe`` specifies to treat the information to be transferred as integer values.
            - ``FREQuency`` specifies to treat the information to be transferred as floating point
              values.
        """
        return self._domain

    @property
    def encdg(self) -> WfminpreEncdg:
        """Return the ``WFMInpre:ENCdg`` command.

        Description:
            - This command specifies the type of encoding of the incoming waveform data to be sent
              to the oscilloscope using the CURVe command. Supported types are BINary and ASCii.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:ENCdg?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:ENCdg?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:ENCdg value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:ENCdg {ASCii|BINary}
            - WFMInpre:ENCdg?
            ```

        Info:
            - ``ASCii`` specifies that the incoming data is in ASCII format.
            - ``BINary`` specifies that the incoming data is in a binary format whose further
              interpretation requires knowledge of ``BYT_NR``, ``BIT_NR``, ``BN_FMT``, and
              ``BYT_OR``.
        """
        return self._encdg

    @property
    def nr_pt(self) -> WfminpreNrPt:
        """Return the ``WFMInpre:NR_Pt`` command.

        Description:
            - This command specifies the number of data points that are in the incoming waveform
              record to be sent to the oscilloscope using the CURVe command.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:NR_Pt?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:NR_Pt?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:NR_Pt value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:NR_Pt <NR1>
            - WFMInpre:NR_Pt?
            ```

        Info:
            - ``<NR1>`` is the number of data points if ``WFMInpre:PT_Fmt`` is set to Y. It is the
              number of min-max pairs if ``WFMInpre:PT_Fmt`` is set to ENV.
        """
        return self._nr_pt

    @property
    def pt_fmt(self) -> WfminprePtFmt:
        """Return the ``WFMInpre:PT_Fmt`` command.

        Description:
            - This command specifies the acquisition format of the data points to be sent to the
              oscilloscope using the CURVE command. This can be Y for YT format, or ENV for envelope
              mode (min/max pairs). For YT format, each data value represents a single waveform data
              point. For envelope format, each data point represents a min/max pair, where the
              minimum value precedes the maximum value.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:PT_Fmt?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:PT_Fmt?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:PT_Fmt value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:PT_Fmt {ENV|Y}
            - WFMInpre:PT_Fmt?
            ```

        Info:
            - ``ENV`` specifies that the waveform is to be transmitted in envelope mode as minimum
              and maximum point pairs. Only Y values are explicitly transmitted. Absolute
              coordinates are given by.
            - ``Xn = XZEro + XINcr (n - PT_Off)``
            - ``Ynmax = YZEro + YMUlt (ynmax - YOFf)``
            - ``Ynmin = YZEro + YMUlt (ynmin - YOFf)``
            - ``Y`` specifies a normal waveform where one ASCII or binary data point is transmitted
              for each point in the waveform record. Only Y values are explicitly transmitted.
              Absolute coordinates are given by.
            - ``Xn = XZEro + XINcr (n - PT_Off)``
            - ``Yn = YZEro + YMUlt (yn - YOFf)``
        """
        return self._pt_fmt

    @property
    def pt_off(self) -> WfminprePtOff:
        """Return the ``WFMInpre:PT_Off`` command.

        Description:
            - The set form of this command is ignored. The query form always returns a 0. (This
              command is listed for compatibility with other Tektronix oscilloscopes.)

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:PT_Off?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:PT_Off?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:PT_Off value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:PT_Off <NR1>
            - WFMInpre:PT_Off?
            ```
        """
        return self._pt_off

    @property
    def reflevel(self) -> WfminpreReflevel:
        """Return the ``WFMInpre:REFLevel`` command.

        Description:
            - This command specifies the Reference Level of the incoming waveform. This command
              applies only to frequency domain waveforms. The Reference Level is adjustable from 10
              pico Watts (-140dBm) to 1 Watt (+30dBm).

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:REFLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:REFLevel?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:REFLevel value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:REFLevel <NR3>
            - WFMInpre:REFLevel?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the Reference Level of the
              incoming waveform, in watts.
        """
        return self._reflevel

    @property
    def span(self) -> WfminpreSpan:
        """Return the ``WFMInpre:SPAN`` command.

        Description:
            - This command specifies the frequency span of the incoming RF trace. The span is the
              range of frequencies that can be observed around the center frequency.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:SPAN?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:SPAN?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:SPAN value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:SPAN <NR3>
            - WFMInpre:SPAN?
            ```

        Info:
            - ``<NR3>`` is a floating point number that can range from 1 kHz to 3 GHz. The maximum
              span is 3 GHz if option 3-SA3 is installed. Without that option, the maximum is
              identical to the analog bandwidth.
        """
        return self._span

    @property
    def wfmtype(self) -> WfminpreWfmtype:
        """Return the ``WFMInpre:WFMTYPe`` command.

        Description:
            - This command specifies the type of waveform that is being transferred to the
              oscilloscope for storage in one of the REF1 - REF4 memory locations. The waveform type
              possibilities are the ANALOG, the RF time domain waveforms (``RF_TD``), or the RF
              frequency domain waveforms (``RF_FD``). The default is ANALOG. This parameter should
              be set before using the CURVe command to transfer a waveform from a PC to an internal
              reference location. The type of waveform that is being transferred in turn determines
              which window will display it on the instrument screen: the time domain window or
              frequency domain window. Both the analog and RF-TD arguments specify the time domain
              window; the ``RF_FD`` argument specifies the frequency domain window.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:WFMTYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:WFMTYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:WFMTYPe value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:WFMTYPe {ANALOG|RF_TD|RF_FD}
            - WFMInpre:WFMTYPe?
            ```

        Info:
            - ``ANALOG`` - this type includes Channels 1-4 and the Math waveform, and specifies to
              display it in the time domain window.
            - ``RF_TD`` - this type includes the three RF time domain traces (RF Amplitude vs. Time,
              RF Frequency vs. Time, and RF Phase vs. Time) and specifies to display it in the time
              domain window.
            - ``RF_FD`` - this type includes the four RF frequency domain traces (RF Normal, RF
              Average, RF Max Hold, and RF Min Hold) and specifies to display it in the frequency
              domain window.
        """
        return self._wfmtype

    @property
    def xincr(self) -> WfminpreXincr:
        """Return the ``WFMInpre:XINcr`` command.

        Description:
            - This command specifies the horizontal interval between incoming waveform points sent
              to the oscilloscope using the CURVE command. The units are time, in seconds, or
              frequency, in hertz, and can be specified or queried using the ``WFMInpre:XUNit``
              command.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:XINcr?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:XINcr?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:XINcr value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:XINcr <NR3>
            - WFMInpre:XINcr?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the horizontal interval
              representation.
        """
        return self._xincr

    @property
    def xunit(self) -> WfminpreXunit:
        """Return the ``WFMInpre:XUNit`` command.

        Description:
            - This command specifies the horizontal units of the x-axis of the data points being
              sent to the oscilloscope using the CURVE command. This value can be in 's' for
              seconds, or 'Hz'.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:XUNit?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:XUNit?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:XUNit value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:XUNit <QString>
            - WFMInpre:XUNit?
            ```

        Info:
            - ``<QString>`` contains the characters that represent the horizontal units for the
              incoming waveform.
        """
        return self._xunit

    @property
    def xzero(self) -> WfminpreXzero:
        """Return the ``WFMInpre:XZEro`` command.

        Description:
            - This command specifies the position value of the first data point in the incoming
              waveform record being sent to the oscilloscope using the CURVE command. The units are
              determined or queried using the ``WFMInpre:XUNit`` command and are typically time, in
              seconds, or frequency, in hertz. This time or frequency is relative to the time or
              frequency of the trigger, which is always 0. Thus, the XZEro value can be negative.

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:XZEro?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:XZEro?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:XZEro value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:XZEro <NR3>
            - WFMInpre:XZEro?
            ```

        Info:
            - ``<NR3>`` is the floating point value of the position, in XUNits, of the first sample
              in the incoming waveform. If XUNits is 's', <NR3> is the time of the first sample in
              the incoming waveform.
        """
        return self._xzero

    @property
    def ymult(self) -> WfminpreYmult:
        r"""Return the ``WFMInpre:YMUlt`` command.

        Description:
            - This command specifies the vertical scale multiplying factor to be used to convert the
              incoming data point values being sent to the oscilloscope, from digitizing levels into
              the units specified by the ``WFMInpre:YUNit`` command. For one byte waveform data,
              there are 256 digitizing levels. For two byte waveform data there are 65,536
              digitizing levels. The ``WFMInpre:YMUlt``, ``WFMInpre:YOFf``, and ``WFMInpre:YZEro``
              values are used to convert waveform record values to units specified using the
              ``WFMINPRE:YUNIT`` command (YUNit units). It uses the following formula (where dl
              means digitizing level; ``curve_in_dl`` is a data point value in the CURVe data):
              Value in YUNit units = ((``curve_in_dl`` - YOFf) \* YMUlt) + YZEro

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:YMUlt?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:YMUlt?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:YMUlt value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:YMUlt <NR3>
            - WFMInpre:YMUlt?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the vertical scale factor per
              digitizing level of the incoming waveform points.
        """
        return self._ymult

    @property
    def yoff(self) -> WfminpreYoff:
        r"""Return the ``WFMInpre:YOFf`` command.

        Description:
            - This command specifies the vertical position of the destination reference waveform in
              digitizing levels. There are 25 digitizing levels per vertical division for 1-byte
              data, and 6400 digitizing levels per vertical division for 2-byte data. Variations in
              this number are analogous to changing the vertical position of the waveform. The
              ``WFMInpre:YMUlt``, ``WFMInpre:YOFf``, and ``WFMInpre:YZEro`` commands are used to
              convert waveform record values to units specified using the ``WFMINPRE:YUNIT`` command
              (YUNit units). It uses the following formula (where dl means digitizing levels, and
              ``curve_in_dl`` is a data point value in the CURVe data): Value in YUNit units =
              ((``curve_in_dl`` - YOFf) \* YMUlt) + YZEro

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:YOFf?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:YOFf?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:YOFf value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:YOFf <NR3>
            - WFMInpre:YOFf?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the vertical offset in digitizing
              levels.
        """
        return self._yoff

    @property
    def yunit(self) -> WfminpreYunit:
        """Return the ``WFMInpre:YUNit`` command.

        Description:
            - This command specifies the vertical units of data points in the incoming waveform
              record sent to the oscilloscope using the CURVE command. This can be any of several
              string values, depending upon the vertical units of the waveform being sent. Supported
              units are: %, /Hz, A, A/A, A/V, A/W, A/dB, A/s, AA, AW, AdB, As, B, Hz, IRE, S/s, V,
              V/A, V/V, V/W, V/dB, V/s, VV, VW, VdB, volts, Vs, W, W/A, W/V, W/W, W/dB, W/s, WA, WV,
              WW, WdB, Ws, dB, dB/A, dB/V, dB/W, dB/dB, dBA, dBV, dBW, dBdB, day, degrees, div, hr,
              min, ohms, percent, s

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:YUNit?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:YUNit?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:YUNit value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:YUNit <QString>
            - WFMInpre:YUNit?
            ```

        Info:
            - ``<QString>`` contains the characters that represent the vertical units for the
              incoming waveform.
        """
        return self._yunit

    @property
    def yzero(self) -> WfminpreYzero:
        r"""Return the ``WFMInpre:YZEro`` command.

        Description:
            - This command specifies the vertical offset of the destination reference waveform in
              units specified by the ``WFMInpre:YUNit`` command. Variations in this number are
              analogous to changing the vertical offset of the waveform. The ``WFMInpre:YMUlt``,
              ``WFMInpre:YOFf``, and ``WFMInpre:YZEro`` commands are used to convert waveform record
              values to units specified using the ``WFMINPRE:YUNIT`` command (YUNit units). It uses
              the following formula (where dl means digitizing levels; ``curve_in_dl`` is a data
              point value in the CURVe data): Value in YUNit units = ((``curve_in_dl`` - YOFf) \*
              YMUlt) + YZEro

        Usage:
            - Using the ``.query()`` method will send the ``WFMInpre:YZEro?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMInpre:YZEro?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WFMInpre:YZEro value`` command.

        SCPI Syntax:
            ```
            - WFMInpre:YZEro <NR3>
            - WFMInpre:YZEro?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the offset in in units specified
              by the ``WFMInpre:YUNit`` command (YUNits).
        """
        return self._yzero
