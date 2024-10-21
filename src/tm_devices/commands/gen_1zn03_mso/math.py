# pylint: disable=line-too-long
"""The math commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MATH:ADDNew <QString>
    - MATH:DELete <QString>
    - MATH:LIST?
    - MATH:MATH<x>:AVG:MODE {ON|OFF|<NR1>}
    - MATH:MATH<x>:AVG:MODE?
    - MATH:MATH<x>:AVG:WEIGht <NR1>
    - MATH:MATH<x>:AVG:WEIGht?
    - MATH:MATH<x>:CAN:SUPPortedfields {DATa}
    - MATH:MATH<x>:CAN:SUPPortedfields?
    - MATH:MATH<x>:DEFine <QString>
    - MATH:MATH<x>:DEFine?
    - MATH:MATH<x>:FUNCtion {ADD|SUBtract|MULTiply|DIVide}
    - MATH:MATH<x>:FUNCtion?
    - MATH:MATH<x>:GATing {NONE|SCREEN|CURSor}
    - MATH:MATH<x>:GATing?
    - MATH:MATH<x>:I2C:SUPPortedfields {DATa}
    - MATH:MATH<x>:I2C:SUPPortedfields?
    - MATH:MATH<x>:INTERpolation {ON|OFF}
    - MATH:MATH<x>:INTERpolation?
    - MATH:MATH<x>:LABel:COLor <QString>
    - MATH:MATH<x>:LABel:COLor?
    - MATH:MATH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
    - MATH:MATH<x>:LABel:FONT:BOLD?
    - MATH:MATH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
    - MATH:MATH<x>:LABel:FONT:ITALic?
    - MATH:MATH<x>:LABel:FONT:SIZE <NR1>
    - MATH:MATH<x>:LABel:FONT:SIZE?
    - MATH:MATH<x>:LABel:FONT:TYPE <QString>
    - MATH:MATH<x>:LABel:FONT:TYPE?
    - MATH:MATH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
    - MATH:MATH<x>:LABel:FONT:UNDERline?
    - MATH:MATH<x>:LABel:NAMe <QString>
    - MATH:MATH<x>:LABel:NAMe?
    - MATH:MATH<x>:LABel:XPOS <NR1>
    - MATH:MATH<x>:LABel:XPOS?
    - MATH:MATH<x>:LABel:YPOS <NR1>
    - MATH:MATH<x>:LABel:YPOS?
    - MATH:MATH<x>:LIN:SUPPortedfields {DATa}
    - MATH:MATH<x>:LIN:SUPPortedfields?
    - MATH:MATH<x>:PARallel:SUPPortedfields {DATa}
    - MATH:MATH<x>:PARallel:SUPPortedfields?
    - MATH:MATH<x>:RS232C:SUPPortedfields {DATa|TXData|RXData}
    - MATH:MATH<x>:RS232C:SUPPortedfields?
    - MATH:MATH<x>:SENT:SUPPortedfields {FCData|FCDFirst|FCDTwo|SDATa}
    - MATH:MATH<x>:SENT:SUPPortedfields?
    - MATH:MATH<x>:SIGNeddata {ON|OFF}
    - MATH:MATH<x>:SIGNeddata?
    - MATH:MATH<x>:SOUrce1 {CH<x>|MATH<x>|REF<x>}
    - MATH:MATH<x>:SOUrce1?
    - MATH:MATH<x>:SPECTral:WINdow {RECTANGular|HAMMing|HANNing|BLACKMANHarris|KAISERBessel|GAUSSian|FLATTOP2|TEKEXPonential}
    - MATH:MATH<x>:SPECTral:WINdow?
    - MATH:MATH<x>:SPI:SUPPortedfields {DATa|MOSIdata|MISOdata}
    - MATH:MATH<x>:SPI:SUPPortedfields?
    - MATH:MATH<x>:TYPe {BASic|FFT|ADVanced}
    - MATH:MATH<x>:TYPe?
    - MATH:MATH<x>:VUNIT <QString>
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MathMathItemVunit(SCPICmdWrite):
    """The ``MATH:MATH<x>:VUNIT`` command.

    Description:
        - This command specifies or returns the math custom vertical units. The math waveform is
          specified by x.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:VUNIT value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:VUNIT <QString>
        ```

    Info:
        - ``<QString>`` is the custom vertical units.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathMathItemType(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:TYPe`` command.

    Description:
        - This command sets or queries the math type. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:TYPe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:TYPe value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:TYPe {BASic|FFT|ADVanced}
        - MATH:MATH<x>:TYPe?
        ```

    Info:
        - ``BASic`` set the type to basic math.
        - ``FFT`` sets the type to FFT math, which can use any live analog or reference waveform in
          the time domain. NOTE. You can also use FFT as part of a math expression by declaring the
          type.
        - ``ADVanced`` sets the type to advanced math.
    """


class MathMathItemSpiSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPI:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for SPI bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPI:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPI:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:SPI:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPI:SUPPortedfields {DATa|MOSIdata|MISOdata}
        - MATH:MATH<x>:SPI:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
        - ``MOSIdata`` sets the field type to MOSIdata. MOSIdata field is available to select when
          SPI Bus configuration for Data Inputs is set to Two.
        - ``MISOdata`` sets the field type to MISOdata. MISOdata field is available to select when
          SPI Bus configuration for Data Inputs is set to Two.
    """


class MathMathItemSpi(SCPICmdRead):
    """The ``MATH:MATH<x>:SPI`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPI?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPI?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:SPI:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemSpiSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemSpiSupportedfields:
        """Return the ``MATH:MATH<x>:SPI:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for SPI
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPI:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:SPI:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SPI:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPI:SUPPortedfields {DATa|MOSIdata|MISOdata}
            - MATH:MATH<x>:SPI:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
            - ``MOSIdata`` sets the field type to MOSIdata. MOSIdata field is available to select
              when SPI Bus configuration for Data Inputs is set to Two.
            - ``MISOdata`` sets the field type to MISOdata. MISOdata field is available to select
              when SPI Bus configuration for Data Inputs is set to Two.
        """
        return self._supportedfields


class MathMathItemSpectralWindow(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral:WINdow`` command.

    Description:
        - This command sets or queries the window function used to apply the specified FFT window to
          the input data for the specified math waveform. The Math waveform is specified by x. A
          spectral window determines what the filter shape of the spectral analyzer will be in the
          frequency domain. It can be described by a mathematical function that is multiplied
          point-by-point times the input data to the spectral analyzer. Following is a list of
          arguments that specify the window function used to multiply the input data. The windows
          are listed in the order of their ability to resolve frequencies (resolution bandwidth).

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:WINdow?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:WINdow?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SPECTral:WINdow value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SPECTral:WINdow {RECTANGular|HAMMing|HANNing|BLACKMANHarris|KAISERBessel|GAUSSian|FLATTOP2|TEKEXPonential}
        - MATH:MATH<x>:SPECTral:WINdow?
        ```

    Info:
        - ``RECTANGular`` window function is equivalent to multiplying all gate data by one.
        - ``HAMMing`` window function is based on a cosine series.
        - ``HANNing`` window function is based on a cosine series.
        - ``BLACKMANHarris`` window function is based on a cosine series.
        - ``KAISERBessel`` window function is based on a cosine series.
        - ``GAUSSian`` window function has the best localization characteristics in the joint
          time/frequency plane.
        - ``FLATTOP2`` window function is a cosine series window with a flattened frequency response
          lobe.
        - ``TEKEXPonential`` window has an exponential nonsymmetrical shape in the time domain and a
          triangular shape in the frequency domain.
    """  # noqa: E501


class MathMathItemSpectral(SCPICmdRead):
    """The ``MATH:MATH<x>:SPECTral`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.window``: The ``MATH:MATH<x>:SPECTral:WINdow`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._window = MathMathItemSpectralWindow(device, f"{self._cmd_syntax}:WINdow")

    @property
    def window(self) -> MathMathItemSpectralWindow:
        """Return the ``MATH:MATH<x>:SPECTral:WINdow`` command.

        Description:
            - This command sets or queries the window function used to apply the specified FFT
              window to the input data for the specified math waveform. The Math waveform is
              specified by x. A spectral window determines what the filter shape of the spectral
              analyzer will be in the frequency domain. It can be described by a mathematical
              function that is multiplied point-by-point times the input data to the spectral
              analyzer. Following is a list of arguments that specify the window function used to
              multiply the input data. The windows are listed in the order of their ability to
              resolve frequencies (resolution bandwidth).

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral:WINdow?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral:WINdow?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SPECTral:WINdow value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SPECTral:WINdow {RECTANGular|HAMMing|HANNing|BLACKMANHarris|KAISERBessel|GAUSSian|FLATTOP2|TEKEXPonential}
            - MATH:MATH<x>:SPECTral:WINdow?
            ```

        Info:
            - ``RECTANGular`` window function is equivalent to multiplying all gate data by one.
            - ``HAMMing`` window function is based on a cosine series.
            - ``HANNing`` window function is based on a cosine series.
            - ``BLACKMANHarris`` window function is based on a cosine series.
            - ``KAISERBessel`` window function is based on a cosine series.
            - ``GAUSSian`` window function has the best localization characteristics in the joint
              time/frequency plane.
            - ``FLATTOP2`` window function is a cosine series window with a flattened frequency
              response lobe.
            - ``TEKEXPonential`` window has an exponential nonsymmetrical shape in the time domain
              and a triangular shape in the frequency domain.
        """  # noqa: E501
        return self._window


class MathMathItemSource1(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SOUrce1`` command.

    Description:
        - This command sets or queries the specified math source. This command sets the Basic Math
          components in the user interface, with two sources and a function. You would also need to
          set the math type to Basic to see the change in the user interface, but this will not
          effect the programmable interface. The math waveform and source are specified by x. When
          the ``MATH:MATH<x>:TYPE`` is set to BASIC, SOURCE1 and SOURCE2 can be used.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SOUrce1?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SOUrce1?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SOUrce1 value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SOUrce1 {CH<x>|MATH<x>|REF<x>}
        - MATH:MATH<x>:SOUrce1?
        ```

    Info:
        - ``MATH<x>`` specifies the math number.
        - ``1`` specifies the source number.
        - ``CH<x>`` specifies the source as channel.
        - ``MATH<x>`` specifies the source as math.
        - ``REF<x>`` specifies the source as reference.
    """


class MathMathItemSigneddata(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SIGNeddata`` command.

    Description:
        - This command sets or queries value to denote that bus field is decoded as signed/unsigned
          data for math on bus source. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SIGNeddata?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SIGNeddata?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SIGNeddata value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SIGNeddata {ON|OFF}
        - MATH:MATH<x>:SIGNeddata?
        ```

    Info:
        - ``ON`` indicates that the bus field is decoded as signed data for drawing the math
          waveform.
        - ``OFF`` indicates that the bus field is decoded as unsigned data for drawing the math
          waveform.
    """


class MathMathItemSentSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:SENT:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for SENT bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SENT:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SENT:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:SENT:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:SENT:SUPPortedfields {FCData|FCDFirst|FCDTwo|SDATa}
        - MATH:MATH<x>:SENT:SUPPortedfields?
        ```

    Info:
        - ``FCData`` sets the field type to FCData. FCData field is available to select when SENT
          Bus configuration for Fast Data Channels is set to 2.
        - ``FCDFirst`` sets the field type to FCDFirst.
        - ``FCDTwo`` sets the field type to FCDTwo.
        - ``SDATa`` sets the field type to SDATa. SDATa is available when SENT Bus configuration for
          Slow Channel is not None.
    """


class MathMathItemSent(SCPICmdRead):
    """The ``MATH:MATH<x>:SENT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:SENT?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SENT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:SENT:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemSentSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemSentSupportedfields:
        """Return the ``MATH:MATH<x>:SENT:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for SENT
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SENT:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:SENT:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:SENT:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SENT:SUPPortedfields {FCData|FCDFirst|FCDTwo|SDATa}
            - MATH:MATH<x>:SENT:SUPPortedfields?
            ```

        Info:
            - ``FCData`` sets the field type to FCData. FCData field is available to select when
              SENT Bus configuration for Fast Data Channels is set to 2.
            - ``FCDFirst`` sets the field type to FCDFirst.
            - ``FCDTwo`` sets the field type to FCDTwo.
            - ``SDATa`` sets the field type to SDATa. SDATa is available when SENT Bus configuration
              for Slow Channel is not None.
        """
        return self._supportedfields


class MathMathItemRs232cSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:RS232C:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for RS232C
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:RS232C:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:RS232C:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:RS232C:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:RS232C:SUPPortedfields {DATa|TXData|RXData}
        - MATH:MATH<x>:RS232C:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
        - ``TXData`` sets the field type to TXData. TXData field can be set when RS232 Bus
          configuration for Data Inputs is set to Two.
        - ``RXData`` sets the field type to RXData. RXData field can be set when RS232 Bus
          configuration for Data Inputs is set to Two.
    """


class MathMathItemRs232c(SCPICmdRead):
    """The ``MATH:MATH<x>:RS232C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:RS232C?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:RS232C?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:RS232C:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemRs232cSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemRs232cSupportedfields:
        """Return the ``MATH:MATH<x>:RS232C:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for RS232C
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:RS232C:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:RS232C:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:RS232C:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:RS232C:SUPPortedfields {DATa|TXData|RXData}
            - MATH:MATH<x>:RS232C:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
            - ``TXData`` sets the field type to TXData. TXData field can be set when RS232 Bus
              configuration for Data Inputs is set to Two.
            - ``RXData`` sets the field type to RXData. RXData field can be set when RS232 Bus
              configuration for Data Inputs is set to Two.
        """
        return self._supportedfields


class MathMathItemParallelSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:PARallel:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for PARallel
          bus. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:PARallel:SUPPortedfields?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``MATH:MATH<x>:PARallel:SUPPortedfields?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:PARallel:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:PARallel:SUPPortedfields {DATa}
        - MATH:MATH<x>:PARallel:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemParallel(SCPICmdRead):
    """The ``MATH:MATH<x>:PARallel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:PARallel?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:PARallel?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:PARallel:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemParallelSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemParallelSupportedfields:
        """Return the ``MATH:MATH<x>:PARallel:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for
              PARallel bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:PARallel:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:PARallel:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:PARallel:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:PARallel:SUPPortedfields {DATa}
            - MATH:MATH<x>:PARallel:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemLinSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LIN:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for LIN bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LIN:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LIN:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:LIN:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LIN:SUPPortedfields {DATa}
        - MATH:MATH<x>:LIN:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemLin(SCPICmdRead):
    """The ``MATH:MATH<x>:LIN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LIN?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LIN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:LIN:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemLinSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemLinSupportedfields:
        """Return the ``MATH:MATH<x>:LIN:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for LIN
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LIN:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:LIN:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LIN:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LIN:SUPPortedfields {DATa}
            - MATH:MATH<x>:LIN:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemLabelYpos(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:YPOS`` command.

    Description:
        - This command sets or queries the y-position of the specified math label. The Math waveform
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:YPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:YPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:YPOS value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:YPOS <NR1>
        - MATH:MATH<x>:LABel:YPOS?
        ```

    Info:
        - ``<NR1>`` is the location (in pixels) where the label for the selected math waveform is
          displayed, relative to the baseline of the waveform.
    """


class MathMathItemLabelXpos(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:XPOS`` command.

    Description:
        - This command sets or queries the X position of the specified math label. Maths are
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:XPOS?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:XPOS?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:XPOS value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:XPOS <NR1>
        - MATH:MATH<x>:LABel:XPOS?
        ```

    Info:
        - ``<NR1>`` is the location (in pixels) where the label for the selected math waveform is
          displayed, relative to the left edge of the display.
    """


class MathMathItemLabelName(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:NAMe`` command.

    Description:
        - This command sets or queries the label string, which is used for annotating the math
          waveform on the screen. The math waveform to which the label is attached is specified by
          x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:NAMe?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:NAMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:NAMe value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:NAMe <QString>
        - MATH:MATH<x>:LABel:NAMe?
        ```

    Info:
        - ``<QString>`` specifies the label to annotate the math waveform.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathMathItemLabelFontUnderline(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:FONT:UNDERline`` command.

    Description:
        - This command sets or queries the underline state of the specified math label. The math
          waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT:UNDERline?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:UNDERline?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:LABel:FONT:UNDERline value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
        - MATH:MATH<x>:LABel:FONT:UNDERline?
        ```

    Info:
        - ``<NR1>`` = 0 turns off underline, and any other integer turns on underline.
        - ``OFF`` turns off underline.
        - ``ON`` turns on underline.
    """


class MathMathItemLabelFontType(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:FONT:TYPE`` command.

    Description:
        - This command sets or queries font type of the specified math label, such as Arial or Times
          New Roman. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:TYPE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:TYPE value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:FONT:TYPE <QString>
        - MATH:MATH<x>:LABel:FONT:TYPE?
        ```

    Info:
        - ``<QString>`` is the name of the font type.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathMathItemLabelFontSize(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:FONT:SIZE`` command.

    Description:
        - This command sets or queries font size of the specified math label. The math waveform is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:SIZE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:SIZE value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:FONT:SIZE <NR1>
        - MATH:MATH<x>:LABel:FONT:SIZE?
        ```

    Info:
        - ``<NR1>`` is the font size of the specified math label.
    """


class MathMathItemLabelFontItalic(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:FONT:ITALic`` command.

    Description:
        - This command sets or queries italic state of the specified math label. The math waveform
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT:ITALic?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:ITALic?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:ITALic value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
        - MATH:MATH<x>:LABel:FONT:ITALic?
        ```

    Info:
        - ``<NR1>`` = 0 turns off italic, and any other integer turns on italic.
        - ``OFF`` turns off italic.
        - ``ON`` turns on italic.
    """


class MathMathItemLabelFontBold(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:FONT:BOLD`` command.

    Description:
        - This command sets or queries the bold state of the specified math label. The math waveform
          is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT:BOLD?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:BOLD?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:BOLD value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
        - MATH:MATH<x>:LABel:FONT:BOLD?
        ```

    Info:
        - ``<NR1>`` = 0 turns off bold, and any other integer turns on bold.
        - ``OFF`` turns off bold.
        - ``ON`` turns on bold.
    """


class MathMathItemLabelFont(SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:FONT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bold``: The ``MATH:MATH<x>:LABel:FONT:BOLD`` command.
        - ``.italic``: The ``MATH:MATH<x>:LABel:FONT:ITALic`` command.
        - ``.size``: The ``MATH:MATH<x>:LABel:FONT:SIZE`` command.
        - ``.type``: The ``MATH:MATH<x>:LABel:FONT:TYPE`` command.
        - ``.underline``: The ``MATH:MATH<x>:LABel:FONT:UNDERline`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bold = MathMathItemLabelFontBold(device, f"{self._cmd_syntax}:BOLD")
        self._italic = MathMathItemLabelFontItalic(device, f"{self._cmd_syntax}:ITALic")
        self._size = MathMathItemLabelFontSize(device, f"{self._cmd_syntax}:SIZE")
        self._type = MathMathItemLabelFontType(device, f"{self._cmd_syntax}:TYPE")
        self._underline = MathMathItemLabelFontUnderline(device, f"{self._cmd_syntax}:UNDERline")

    @property
    def bold(self) -> MathMathItemLabelFontBold:
        """Return the ``MATH:MATH<x>:LABel:FONT:BOLD`` command.

        Description:
            - This command sets or queries the bold state of the specified math label. The math
              waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT:BOLD?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:BOLD?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LABel:FONT:BOLD value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:FONT:BOLD {ON|OFF|<NR1>}
            - MATH:MATH<x>:LABel:FONT:BOLD?
            ```

        Info:
            - ``<NR1>`` = 0 turns off bold, and any other integer turns on bold.
            - ``OFF`` turns off bold.
            - ``ON`` turns on bold.
        """
        return self._bold

    @property
    def italic(self) -> MathMathItemLabelFontItalic:
        """Return the ``MATH:MATH<x>:LABel:FONT:ITALic`` command.

        Description:
            - This command sets or queries italic state of the specified math label. The math
              waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT:ITALic?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:ITALic?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LABel:FONT:ITALic value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:FONT:ITALic {ON|OFF|<NR1>}
            - MATH:MATH<x>:LABel:FONT:ITALic?
            ```

        Info:
            - ``<NR1>`` = 0 turns off italic, and any other integer turns on italic.
            - ``OFF`` turns off italic.
            - ``ON`` turns on italic.
        """
        return self._italic

    @property
    def size(self) -> MathMathItemLabelFontSize:
        """Return the ``MATH:MATH<x>:LABel:FONT:SIZE`` command.

        Description:
            - This command sets or queries font size of the specified math label. The math waveform
              is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:SIZE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LABel:FONT:SIZE value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:FONT:SIZE <NR1>
            - MATH:MATH<x>:LABel:FONT:SIZE?
            ```

        Info:
            - ``<NR1>`` is the font size of the specified math label.
        """
        return self._size

    @property
    def type(self) -> MathMathItemLabelFontType:
        """Return the ``MATH:MATH<x>:LABel:FONT:TYPE`` command.

        Description:
            - This command sets or queries font type of the specified math label, such as Arial or
              Times New Roman. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LABel:FONT:TYPE value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:FONT:TYPE <QString>
            - MATH:MATH<x>:LABel:FONT:TYPE?
            ```

        Info:
            - ``<QString>`` is the name of the font type.
        """
        return self._type

    @property
    def underline(self) -> MathMathItemLabelFontUnderline:
        """Return the ``MATH:MATH<x>:LABel:FONT:UNDERline`` command.

        Description:
            - This command sets or queries the underline state of the specified math label. The math
              waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT:UNDERline?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:LABel:FONT:UNDERline?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:LABel:FONT:UNDERline value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:FONT:UNDERline {ON|OFF|<NR1>}
            - MATH:MATH<x>:LABel:FONT:UNDERline?
            ```

        Info:
            - ``<NR1>`` = 0 turns off underline, and any other integer turns on underline.
            - ``OFF`` turns off underline.
            - ``ON`` turns on underline.
        """
        return self._underline


class MathMathItemLabelColor(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:LABel:COLor`` command.

    Description:
        - This command sets or queries color of the specified math's label. The math waveform is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:COLor?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:COLor?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:COLor value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:LABel:COLor <QString>
        - MATH:MATH<x>:LABel:COLor?
        ```

    Info:
        - ``<QString`` > is the color of the label. To return the color to the default color, send
          an empty string as in this example: ``:MATH:MATH1:LABEL:COLOR`` ''.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathMathItemLabel(SCPICmdRead):
    """The ``MATH:MATH<x>:LABel`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.color``: The ``MATH:MATH<x>:LABel:COLor`` command.
        - ``.font``: The ``MATH:MATH<x>:LABel:FONT`` command tree.
        - ``.name``: The ``MATH:MATH<x>:LABel:NAMe`` command.
        - ``.xpos``: The ``MATH:MATH<x>:LABel:XPOS`` command.
        - ``.ypos``: The ``MATH:MATH<x>:LABel:YPOS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._color = MathMathItemLabelColor(device, f"{self._cmd_syntax}:COLor")
        self._font = MathMathItemLabelFont(device, f"{self._cmd_syntax}:FONT")
        self._name = MathMathItemLabelName(device, f"{self._cmd_syntax}:NAMe")
        self._xpos = MathMathItemLabelXpos(device, f"{self._cmd_syntax}:XPOS")
        self._ypos = MathMathItemLabelYpos(device, f"{self._cmd_syntax}:YPOS")

    @property
    def color(self) -> MathMathItemLabelColor:
        """Return the ``MATH:MATH<x>:LABel:COLor`` command.

        Description:
            - This command sets or queries color of the specified math's label. The math waveform is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:COLor?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:COLor?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:COLor value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:COLor <QString>
            - MATH:MATH<x>:LABel:COLor?
            ```

        Info:
            - ``<QString`` > is the color of the label. To return the color to the default color,
              send an empty string as in this example: ``:MATH:MATH1:LABEL:COLOR`` ''.
        """
        return self._color

    @property
    def font(self) -> MathMathItemLabelFont:
        """Return the ``MATH:MATH<x>:LABel:FONT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:FONT?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:FONT?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bold``: The ``MATH:MATH<x>:LABel:FONT:BOLD`` command.
            - ``.italic``: The ``MATH:MATH<x>:LABel:FONT:ITALic`` command.
            - ``.size``: The ``MATH:MATH<x>:LABel:FONT:SIZE`` command.
            - ``.type``: The ``MATH:MATH<x>:LABel:FONT:TYPE`` command.
            - ``.underline``: The ``MATH:MATH<x>:LABel:FONT:UNDERline`` command.
        """
        return self._font

    @property
    def name(self) -> MathMathItemLabelName:
        """Return the ``MATH:MATH<x>:LABel:NAMe`` command.

        Description:
            - This command sets or queries the label string, which is used for annotating the math
              waveform on the screen. The math waveform to which the label is attached is specified
              by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:NAMe?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:NAMe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:NAMe value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:NAMe <QString>
            - MATH:MATH<x>:LABel:NAMe?
            ```

        Info:
            - ``<QString>`` specifies the label to annotate the math waveform.
        """
        return self._name

    @property
    def xpos(self) -> MathMathItemLabelXpos:
        """Return the ``MATH:MATH<x>:LABel:XPOS`` command.

        Description:
            - This command sets or queries the X position of the specified math label. Maths are
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:XPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:XPOS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:XPOS value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:XPOS <NR1>
            - MATH:MATH<x>:LABel:XPOS?
            ```

        Info:
            - ``<NR1>`` is the location (in pixels) where the label for the selected math waveform
              is displayed, relative to the left edge of the display.
        """
        return self._xpos

    @property
    def ypos(self) -> MathMathItemLabelYpos:
        """Return the ``MATH:MATH<x>:LABel:YPOS`` command.

        Description:
            - This command sets or queries the y-position of the specified math label. The Math
              waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel:YPOS?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel:YPOS?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:LABel:YPOS value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:LABel:YPOS <NR1>
            - MATH:MATH<x>:LABel:YPOS?
            ```

        Info:
            - ``<NR1>`` is the location (in pixels) where the label for the selected math waveform
              is displayed, relative to the baseline of the waveform.
        """
        return self._ypos


class MathMathItemInterpolation(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:INTERpolation`` command.

    Description:
        - This command sets or queries whether sinc interpolation is enabled for math on bus source.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:INTERpolation?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:INTERpolation?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:INTERpolation value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:INTERpolation {ON|OFF}
        - MATH:MATH<x>:INTERpolation?
        ```

    Info:
        - ``ON`` indicates that the sinc interpolation is used for math waveform.
        - ``OFF`` indicates no interpolation is used for math waveform. Waveform will appear
          'stair-steppy' in this case.
    """


class MathMathItemI2cSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:I2C:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for I2C bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:I2C:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:I2C:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:I2C:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:I2C:SUPPortedfields {DATa}
        - MATH:MATH<x>:I2C:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemI2c(SCPICmdRead):
    """The ``MATH:MATH<x>:I2C`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:I2C?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:I2C?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:I2C:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemI2cSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemI2cSupportedfields:
        """Return the ``MATH:MATH<x>:I2C:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for I2C
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:I2C:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:I2C:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:I2C:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:I2C:SUPPortedfields {DATa}
            - MATH:MATH<x>:I2C:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemGating(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:GATing`` command.

    Description:
        - This command specifies or returns the gating setting. It only applies to Math FFT plots.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:GATing?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:GATing?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:GATing value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:GATing {NONE|SCREEN|CURSor}
        - MATH:MATH<x>:GATing?
        ```

    Info:
        - ``NONE`` turns off math gating.
        - ``SCREEN`` turns on gating, using the left and right edges of the screen.
        - ``CURSor`` limits math to the portion of the waveform between the vertical bar cursors,
          even if they are off screen.
    """


class MathMathItemFunction(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:FUNCtion`` command.

    Description:
        - This command sets or queries the basic math arithmetic function. The math waveform is
          specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:FUNCtion?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FUNCtion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FUNCtion value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:FUNCtion {ADD|SUBtract|MULTiply|DIVide}
        - MATH:MATH<x>:FUNCtion?
        ```

    Info:
        - ``ADD`` sets the basic math function to add.
        - ``SUBtract`` sets the basic math function to subtract.
        - ``MULTiply`` sets the basic math function to multiply.
        - ``DIVide`` sets the basic math function to divide.
    """


class MathMathItemDefine(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:DEFine`` command.

    Description:
        - This command allows you to define new waveforms using mathematical expressions. The query
          form of this command returns the math definition for the specified math waveform. The math
          waveform is specified by x. You can specify a math expression from waveforms, measurements
          and scalar sources, functions, operands, and numerical constants. Math expressions can be
          simple, such as Ch1, which specifies that a waveform should show the signal source of
          Channel 1 with no mathematical computation. Math expressions can also be complex,
          consisting of 100 plus characters and comprising many sources (including other math
          waveforms), functions, and operands. As an example, you can enter the expression
          Log(Ch1+Ch2), which specifies that the signals from channels 1 and 2 are to be
          algebraically added, and the base 10 log of the sum is to be shown as the final math
          waveform.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:DEFine?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:DEFine?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:DEFine value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:DEFine <QString>
        - MATH:MATH<x>:DEFine?
        ```

    Info:
        - ``<QString>`` quoted string argument is the mathematical expression that defines the
          waveform. ``MATH:MATH<x>:DEFINE?`` is for use when the ``MATH:MATH<x>:TYPE`` is ADVANCED.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathMathItemCanSupportedfields(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:CAN:SUPPortedfields`` command.

    Description:
        - This command sets or queries the field type for the math for the bus source for CAN bus.
          The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:CAN:SUPPortedfields?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:CAN:SUPPortedfields?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``MATH:MATH<x>:CAN:SUPPortedfields value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:CAN:SUPPortedfields {DATa}
        - MATH:MATH<x>:CAN:SUPPortedfields?
        ```

    Info:
        - ``DATa`` sets the field type to DATa.
    """


class MathMathItemCan(SCPICmdRead):
    """The ``MATH:MATH<x>:CAN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:CAN?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:CAN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.supportedfields``: The ``MATH:MATH<x>:CAN:SUPPortedfields`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._supportedfields = MathMathItemCanSupportedfields(
            device, f"{self._cmd_syntax}:SUPPortedfields"
        )

    @property
    def supportedfields(self) -> MathMathItemCanSupportedfields:
        """Return the ``MATH:MATH<x>:CAN:SUPPortedfields`` command.

        Description:
            - This command sets or queries the field type for the math for the bus source for CAN
              bus. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:CAN:SUPPortedfields?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``MATH:MATH<x>:CAN:SUPPortedfields?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MATH:MATH<x>:CAN:SUPPortedfields value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:CAN:SUPPortedfields {DATa}
            - MATH:MATH<x>:CAN:SUPPortedfields?
            ```

        Info:
            - ``DATa`` sets the field type to DATa.
        """
        return self._supportedfields


class MathMathItemAvgWeight(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:AVG:WEIGht`` command.

    Description:
        - This command sets or queries the number of acquisitions at which the averaging algorithm
          will begin exponential averaging. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:AVG:WEIGht?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AVG:WEIGht?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:AVG:WEIGht value``
          command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:AVG:WEIGht <NR1>
        - MATH:MATH<x>:AVG:WEIGht?
        ```

    Info:
        - ``<NR1>`` is the number of acquisitions at which the averaging algorithm will begin
          exponential averaging.
    """


class MathMathItemAvgMode(SCPICmdWrite, SCPICmdRead):
    """The ``MATH:MATH<x>:AVG:MODE`` command.

    Description:
        - This command sets or queries the math average mode flag. If the flag is set to 1, math
          averaging is turned on. The math waveform is specified by x.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:AVG:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AVG:MODE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:AVG:MODE value`` command.

    SCPI Syntax:
        ```
        - MATH:MATH<x>:AVG:MODE {ON|OFF|<NR1>}
        - MATH:MATH<x>:AVG:MODE?
        ```

    Info:
        - ``<NR1>`` = 0 turns off average mode, and any other integer turns on average mode.
        - ``OFF`` turns off average mode.
        - ``ON`` turns on average mode.
    """


class MathMathItemAvg(SCPICmdRead):
    """The ``MATH:MATH<x>:AVG`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>:AVG?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AVG?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``MATH:MATH<x>:AVG:MODE`` command.
        - ``.weight``: The ``MATH:MATH<x>:AVG:WEIGht`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = MathMathItemAvgMode(device, f"{self._cmd_syntax}:MODE")
        self._weight = MathMathItemAvgWeight(device, f"{self._cmd_syntax}:WEIGht")

    @property
    def mode(self) -> MathMathItemAvgMode:
        """Return the ``MATH:MATH<x>:AVG:MODE`` command.

        Description:
            - This command sets or queries the math average mode flag. If the flag is set to 1, math
              averaging is turned on. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:AVG:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AVG:MODE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:AVG:MODE value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:AVG:MODE {ON|OFF|<NR1>}
            - MATH:MATH<x>:AVG:MODE?
            ```

        Info:
            - ``<NR1>`` = 0 turns off average mode, and any other integer turns on average mode.
            - ``OFF`` turns off average mode.
            - ``ON`` turns on average mode.
        """
        return self._mode

    @property
    def weight(self) -> MathMathItemAvgWeight:
        """Return the ``MATH:MATH<x>:AVG:WEIGht`` command.

        Description:
            - This command sets or queries the number of acquisitions at which the averaging
              algorithm will begin exponential averaging. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:AVG:WEIGht?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AVG:WEIGht?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:AVG:WEIGht value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:AVG:WEIGht <NR1>
            - MATH:MATH<x>:AVG:WEIGht?
            ```

        Info:
            - ``<NR1>`` is the number of acquisitions at which the averaging algorithm will begin
              exponential averaging.
        """
        return self._weight


#  pylint: disable=too-many-instance-attributes
class MathMathItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MATH:MATH<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:MATH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.avg``: The ``MATH:MATH<x>:AVG`` command tree.
        - ``.can``: The ``MATH:MATH<x>:CAN`` command tree.
        - ``.define``: The ``MATH:MATH<x>:DEFine`` command.
        - ``.function``: The ``MATH:MATH<x>:FUNCtion`` command.
        - ``.gating``: The ``MATH:MATH<x>:GATing`` command.
        - ``.i2c``: The ``MATH:MATH<x>:I2C`` command tree.
        - ``.interpolation``: The ``MATH:MATH<x>:INTERpolation`` command.
        - ``.label``: The ``MATH:MATH<x>:LABel`` command tree.
        - ``.lin``: The ``MATH:MATH<x>:LIN`` command tree.
        - ``.parallel``: The ``MATH:MATH<x>:PARallel`` command tree.
        - ``.rs232c``: The ``MATH:MATH<x>:RS232C`` command tree.
        - ``.sent``: The ``MATH:MATH<x>:SENT`` command tree.
        - ``.signeddata``: The ``MATH:MATH<x>:SIGNeddata`` command.
        - ``.source1``: The ``MATH:MATH<x>:SOUrce1`` command.
        - ``.spectral``: The ``MATH:MATH<x>:SPECTral`` command tree.
        - ``.spi``: The ``MATH:MATH<x>:SPI`` command tree.
        - ``.type``: The ``MATH:MATH<x>:TYPe`` command.
        - ``.vunit``: The ``MATH:MATH<x>:VUNIT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._avg = MathMathItemAvg(device, f"{self._cmd_syntax}:AVG")
        self._can = MathMathItemCan(device, f"{self._cmd_syntax}:CAN")
        self._define = MathMathItemDefine(device, f"{self._cmd_syntax}:DEFine")
        self._function = MathMathItemFunction(device, f"{self._cmd_syntax}:FUNCtion")
        self._gating = MathMathItemGating(device, f"{self._cmd_syntax}:GATing")
        self._i2c = MathMathItemI2c(device, f"{self._cmd_syntax}:I2C")
        self._interpolation = MathMathItemInterpolation(device, f"{self._cmd_syntax}:INTERpolation")
        self._label = MathMathItemLabel(device, f"{self._cmd_syntax}:LABel")
        self._lin = MathMathItemLin(device, f"{self._cmd_syntax}:LIN")
        self._parallel = MathMathItemParallel(device, f"{self._cmd_syntax}:PARallel")
        self._rs232c = MathMathItemRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._sent = MathMathItemSent(device, f"{self._cmd_syntax}:SENT")
        self._signeddata = MathMathItemSigneddata(device, f"{self._cmd_syntax}:SIGNeddata")
        self._source1 = MathMathItemSource1(device, f"{self._cmd_syntax}:SOUrce1")
        self._spectral = MathMathItemSpectral(device, f"{self._cmd_syntax}:SPECTral")
        self._spi = MathMathItemSpi(device, f"{self._cmd_syntax}:SPI")
        self._type = MathMathItemType(device, f"{self._cmd_syntax}:TYPe")
        self._vunit = MathMathItemVunit(device, f"{self._cmd_syntax}:VUNIT")

    @property
    def avg(self) -> MathMathItemAvg:
        """Return the ``MATH:MATH<x>:AVG`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:AVG?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:AVG?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``MATH:MATH<x>:AVG:MODE`` command.
            - ``.weight``: The ``MATH:MATH<x>:AVG:WEIGht`` command.
        """
        return self._avg

    @property
    def can(self) -> MathMathItemCan:
        """Return the ``MATH:MATH<x>:CAN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:CAN?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:CAN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:CAN:SUPPortedfields`` command.
        """
        return self._can

    @property
    def define(self) -> MathMathItemDefine:
        """Return the ``MATH:MATH<x>:DEFine`` command.

        Description:
            - This command allows you to define new waveforms using mathematical expressions. The
              query form of this command returns the math definition for the specified math
              waveform. The math waveform is specified by x. You can specify a math expression from
              waveforms, measurements and scalar sources, functions, operands, and numerical
              constants. Math expressions can be simple, such as Ch1, which specifies that a
              waveform should show the signal source of Channel 1 with no mathematical computation.
              Math expressions can also be complex, consisting of 100 plus characters and comprising
              many sources (including other math waveforms), functions, and operands. As an example,
              you can enter the expression Log(Ch1+Ch2), which specifies that the signals from
              channels 1 and 2 are to be algebraically added, and the base 10 log of the sum is to
              be shown as the final math waveform.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:DEFine?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:DEFine?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:DEFine value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:DEFine <QString>
            - MATH:MATH<x>:DEFine?
            ```

        Info:
            - ``<QString>`` quoted string argument is the mathematical expression that defines the
              waveform. ``MATH:MATH<x>:DEFINE?`` is for use when the ``MATH:MATH<x>:TYPE`` is
              ADVANCED.
        """
        return self._define

    @property
    def function(self) -> MathMathItemFunction:
        """Return the ``MATH:MATH<x>:FUNCtion`` command.

        Description:
            - This command sets or queries the basic math arithmetic function. The math waveform is
              specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:FUNCtion?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:FUNCtion?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:FUNCtion value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:FUNCtion {ADD|SUBtract|MULTiply|DIVide}
            - MATH:MATH<x>:FUNCtion?
            ```

        Info:
            - ``ADD`` sets the basic math function to add.
            - ``SUBtract`` sets the basic math function to subtract.
            - ``MULTiply`` sets the basic math function to multiply.
            - ``DIVide`` sets the basic math function to divide.
        """
        return self._function

    @property
    def gating(self) -> MathMathItemGating:
        """Return the ``MATH:MATH<x>:GATing`` command.

        Description:
            - This command specifies or returns the gating setting. It only applies to Math FFT
              plots. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:GATing?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:GATing?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:GATing value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:GATing {NONE|SCREEN|CURSor}
            - MATH:MATH<x>:GATing?
            ```

        Info:
            - ``NONE`` turns off math gating.
            - ``SCREEN`` turns on gating, using the left and right edges of the screen.
            - ``CURSor`` limits math to the portion of the waveform between the vertical bar
              cursors, even if they are off screen.
        """
        return self._gating

    @property
    def i2c(self) -> MathMathItemI2c:
        """Return the ``MATH:MATH<x>:I2C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:I2C?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:I2C?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:I2C:SUPPortedfields`` command.
        """
        return self._i2c

    @property
    def interpolation(self) -> MathMathItemInterpolation:
        """Return the ``MATH:MATH<x>:INTERpolation`` command.

        Description:
            - This command sets or queries whether sinc interpolation is enabled for math on bus
              source. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:INTERpolation?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:INTERpolation?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:INTERpolation value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:INTERpolation {ON|OFF}
            - MATH:MATH<x>:INTERpolation?
            ```

        Info:
            - ``ON`` indicates that the sinc interpolation is used for math waveform.
            - ``OFF`` indicates no interpolation is used for math waveform. Waveform will appear
              'stair-steppy' in this case.
        """
        return self._interpolation

    @property
    def label(self) -> MathMathItemLabel:
        """Return the ``MATH:MATH<x>:LABel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LABel?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LABel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.color``: The ``MATH:MATH<x>:LABel:COLor`` command.
            - ``.font``: The ``MATH:MATH<x>:LABel:FONT`` command tree.
            - ``.name``: The ``MATH:MATH<x>:LABel:NAMe`` command.
            - ``.xpos``: The ``MATH:MATH<x>:LABel:XPOS`` command.
            - ``.ypos``: The ``MATH:MATH<x>:LABel:YPOS`` command.
        """
        return self._label

    @property
    def lin(self) -> MathMathItemLin:
        """Return the ``MATH:MATH<x>:LIN`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:LIN?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:LIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:LIN:SUPPortedfields`` command.
        """
        return self._lin

    @property
    def parallel(self) -> MathMathItemParallel:
        """Return the ``MATH:MATH<x>:PARallel`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:PARallel?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:PARallel?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:PARallel:SUPPortedfields`` command.
        """
        return self._parallel

    @property
    def rs232c(self) -> MathMathItemRs232c:
        """Return the ``MATH:MATH<x>:RS232C`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:RS232C?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:RS232C?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:RS232C:SUPPortedfields`` command.
        """
        return self._rs232c

    @property
    def sent(self) -> MathMathItemSent:
        """Return the ``MATH:MATH<x>:SENT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SENT?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SENT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:SENT:SUPPortedfields`` command.
        """
        return self._sent

    @property
    def signeddata(self) -> MathMathItemSigneddata:
        """Return the ``MATH:MATH<x>:SIGNeddata`` command.

        Description:
            - This command sets or queries value to denote that bus field is decoded as
              signed/unsigned data for math on bus source. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SIGNeddata?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SIGNeddata?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SIGNeddata value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SIGNeddata {ON|OFF}
            - MATH:MATH<x>:SIGNeddata?
            ```

        Info:
            - ``ON`` indicates that the bus field is decoded as signed data for drawing the math
              waveform.
            - ``OFF`` indicates that the bus field is decoded as unsigned data for drawing the math
              waveform.
        """
        return self._signeddata

    @property
    def source1(self) -> MathMathItemSource1:
        """Return the ``MATH:MATH<x>:SOUrce1`` command.

        Description:
            - This command sets or queries the specified math source. This command sets the Basic
              Math components in the user interface, with two sources and a function. You would also
              need to set the math type to Basic to see the change in the user interface, but this
              will not effect the programmable interface. The math waveform and source are specified
              by x. When the ``MATH:MATH<x>:TYPE`` is set to BASIC, SOURCE1 and SOURCE2 can be used.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SOUrce1?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SOUrce1?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:SOUrce1 value``
              command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:SOUrce1 {CH<x>|MATH<x>|REF<x>}
            - MATH:MATH<x>:SOUrce1?
            ```

        Info:
            - ``MATH<x>`` specifies the math number.
            - ``1`` specifies the source number.
            - ``CH<x>`` specifies the source as channel.
            - ``MATH<x>`` specifies the source as math.
            - ``REF<x>`` specifies the source as reference.
        """
        return self._source1

    @property
    def spectral(self) -> MathMathItemSpectral:
        """Return the ``MATH:MATH<x>:SPECTral`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPECTral?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPECTral?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.window``: The ``MATH:MATH<x>:SPECTral:WINdow`` command.
        """
        return self._spectral

    @property
    def spi(self) -> MathMathItemSpi:
        """Return the ``MATH:MATH<x>:SPI`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:SPI?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:SPI?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.supportedfields``: The ``MATH:MATH<x>:SPI:SUPPortedfields`` command.
        """
        return self._spi

    @property
    def type(self) -> MathMathItemType:
        """Return the ``MATH:MATH<x>:TYPe`` command.

        Description:
            - This command sets or queries the math type. The math waveform is specified by x.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>:TYPe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:TYPe value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:TYPe {BASic|FFT|ADVanced}
            - MATH:MATH<x>:TYPe?
            ```

        Info:
            - ``BASic`` set the type to basic math.
            - ``FFT`` sets the type to FFT math, which can use any live analog or reference waveform
              in the time domain. NOTE. You can also use FFT as part of a math expression by
              declaring the type.
            - ``ADVanced`` sets the type to advanced math.
        """
        return self._type

    @property
    def vunit(self) -> MathMathItemVunit:
        """Return the ``MATH:MATH<x>:VUNIT`` command.

        Description:
            - This command specifies or returns the math custom vertical units. The math waveform is
              specified by x.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:MATH<x>:VUNIT value`` command.

        SCPI Syntax:
            ```
            - MATH:MATH<x>:VUNIT <QString>
            ```

        Info:
            - ``<QString>`` is the custom vertical units.
        """
        return self._vunit


class MathList(SCPICmdRead):
    """The ``MATH:LIST`` command.

    Description:
        - This query returns a comma separated list of all currently defined math waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``MATH:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MATH:LIST?
        ```
    """


class MathDelete(SCPICmdWrite):
    """The ``MATH:DELete`` command.

    Description:
        - This command deletes the specified math.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:DELete value`` command.

    SCPI Syntax:
        ```
        - MATH:DELete <QString>
        ```

    Info:
        - ``<QString>`` is a quoted string specifying the math waveform to delete. The quoted string
          is of the form 'MATH<NR1>', where <NR1> is ≥1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class MathAddnew(SCPICmdWrite):
    """The ``MATH:ADDNew`` command.

    Description:
        - This command adds the specified math.

    Usage:
        - Using the ``.write(value)`` method will send the ``MATH:ADDNew value`` command.

    SCPI Syntax:
        ```
        - MATH:ADDNew <QString>
        ```

    Info:
        - ``<QString>`` is the quoted string specifying the math waveform to add. The argument is of
          the form 'MATH<NR1>', where <NR1> is ≥1.
    """

    _WRAP_ARG_WITH_QUOTES = True


class Math(SCPICmdRead):
    """The ``MATH`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MATH?`` query.
        - Using the ``.verify(value)`` method will send the ``MATH?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.addnew``: The ``MATH:ADDNew`` command.
        - ``.delete``: The ``MATH:DELete`` command.
        - ``.list``: The ``MATH:LIST`` command.
        - ``.math``: The ``MATH:MATH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MATH") -> None:
        super().__init__(device, cmd_syntax)
        self._addnew = MathAddnew(device, f"{self._cmd_syntax}:ADDNew")
        self._delete = MathDelete(device, f"{self._cmd_syntax}:DELete")
        self._list = MathList(device, f"{self._cmd_syntax}:LIST")
        self._math: Dict[int, MathMathItem] = DefaultDictPassKeyToFactory(
            lambda x: MathMathItem(device, f"{self._cmd_syntax}:MATH{x}")
        )

    @property
    def addnew(self) -> MathAddnew:
        """Return the ``MATH:ADDNew`` command.

        Description:
            - This command adds the specified math.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:ADDNew value`` command.

        SCPI Syntax:
            ```
            - MATH:ADDNew <QString>
            ```

        Info:
            - ``<QString>`` is the quoted string specifying the math waveform to add. The argument
              is of the form 'MATH<NR1>', where <NR1> is ≥1.
        """
        return self._addnew

    @property
    def delete(self) -> MathDelete:
        """Return the ``MATH:DELete`` command.

        Description:
            - This command deletes the specified math.

        Usage:
            - Using the ``.write(value)`` method will send the ``MATH:DELete value`` command.

        SCPI Syntax:
            ```
            - MATH:DELete <QString>
            ```

        Info:
            - ``<QString>`` is a quoted string specifying the math waveform to delete. The quoted
              string is of the form 'MATH<NR1>', where <NR1> is ≥1.
        """
        return self._delete

    @property
    def list(self) -> MathList:
        """Return the ``MATH:LIST`` command.

        Description:
            - This query returns a comma separated list of all currently defined math waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:LIST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MATH:LIST?
            ```
        """
        return self._list

    @property
    def math(self) -> Dict[int, MathMathItem]:
        """Return the ``MATH:MATH<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MATH:MATH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MATH:MATH<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.avg``: The ``MATH:MATH<x>:AVG`` command tree.
            - ``.can``: The ``MATH:MATH<x>:CAN`` command tree.
            - ``.define``: The ``MATH:MATH<x>:DEFine`` command.
            - ``.function``: The ``MATH:MATH<x>:FUNCtion`` command.
            - ``.gating``: The ``MATH:MATH<x>:GATing`` command.
            - ``.i2c``: The ``MATH:MATH<x>:I2C`` command tree.
            - ``.interpolation``: The ``MATH:MATH<x>:INTERpolation`` command.
            - ``.label``: The ``MATH:MATH<x>:LABel`` command tree.
            - ``.lin``: The ``MATH:MATH<x>:LIN`` command tree.
            - ``.parallel``: The ``MATH:MATH<x>:PARallel`` command tree.
            - ``.rs232c``: The ``MATH:MATH<x>:RS232C`` command tree.
            - ``.sent``: The ``MATH:MATH<x>:SENT`` command tree.
            - ``.signeddata``: The ``MATH:MATH<x>:SIGNeddata`` command.
            - ``.source1``: The ``MATH:MATH<x>:SOUrce1`` command.
            - ``.spectral``: The ``MATH:MATH<x>:SPECTral`` command tree.
            - ``.spi``: The ``MATH:MATH<x>:SPI`` command tree.
            - ``.type``: The ``MATH:MATH<x>:TYPe`` command.
            - ``.vunit``: The ``MATH:MATH<x>:VUNIT`` command.
        """
        return self._math
