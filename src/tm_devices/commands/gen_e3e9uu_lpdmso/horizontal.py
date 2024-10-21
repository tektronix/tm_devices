"""The horizontal commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HORizontal:ACQDURATION?
    - HORizontal:DELay:MODe {ON|OFF|<NR1>}
    - HORizontal:DELay:MODe?
    - HORizontal:DELay:TIMe <NR3>
    - HORizontal:DELay:TIMe?
    - HORizontal:DIVisions?
    - HORizontal:FASTframe:COUNt <NR1>
    - HORizontal:FASTframe:COUNt?
    - HORizontal:FASTframe:MAXFRames?
    - HORizontal:FASTframe:MULtipleframes:MODe {OFF|OVERlay}
    - HORizontal:FASTframe:MULtipleframes:MODe?
    - HORizontal:FASTframe:REF:FRAme <NR1>
    - HORizontal:FASTframe:REF:FRAme?
    - HORizontal:FASTframe:REF:INCLUde {ON|OFF|<NR1>}
    - HORizontal:FASTframe:REF:INCLUde?
    - HORizontal:FASTframe:SELECTED <NR1>
    - HORizontal:FASTframe:SELECTED?
    - HORizontal:FASTframe:STATE {ON|OFF|<NR1>}
    - HORizontal:FASTframe:STATE?
    - HORizontal:FASTframe:SUMFrame {NONe|AVErage|ENVelope}
    - HORizontal:FASTframe:SUMFrame:STATE {ON|OFF|<NR1>}
    - HORizontal:FASTframe:SUMFrame:STATE?
    - HORizontal:FASTframe:TIMEStamp:ALL?
    - HORizontal:FASTframe:TIMEStamp:DELTa?
    - HORizontal:FASTframe:TIMEStamp:REFerence?
    - HORizontal:FASTframe:TIMEStamp:SELECTED?
    - HORizontal:FASTframe:XZEro:ALL?
    - HORizontal:FASTframe:XZEro:REF?
    - HORizontal:FASTframe:XZEro:SELECTED?
    - HORizontal:FASTframe?
    - HORizontal:HISTory:CSTAts {AACQs|HONLy}
    - HORizontal:HISTory:CSTAts?
    - HORizontal:HISTory:OVERlay {ON|OFF}
    - HORizontal:HISTory:OVERlay?
    - HORizontal:HISTory:REF:ACQ <NR1>
    - HORizontal:HISTory:REF:ACQ?
    - HORizontal:HISTory:REF:INClude {ON|OFF}
    - HORizontal:HISTory:REF:INClude?
    - HORizontal:HISTory:SELected <NR1>
    - HORizontal:HISTory:SELected?
    - HORizontal:HISTory:STATe {OFF|ON|1|0}
    - HORizontal:HISTory:STATe?
    - HORizontal:HISTory:TIMEStamp:DELTa?
    - HORizontal:HISTory:TIMEStamp:REFerence?
    - HORizontal:HISTory:TIMEStamp:SELECTED?
    - HORizontal:MAIn:INTERPRatio?
    - HORizontal:MODe {AUTO|MANual}
    - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue <NR1>
    - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue?
    - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride {OFF|ON|0|1}
    - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride?
    - HORizontal:MODe:MANual:CONFIGure {HORIZontalscale|RECORDLength}
    - HORizontal:MODe:MANual:CONFIGure?
    - HORizontal:MODe:RECOrdlength <NR1>
    - HORizontal:MODe:RECOrdlength?
    - HORizontal:MODe:SAMPLERate <NR1>
    - HORizontal:MODe:SAMPLERate?
    - HORizontal:MODe:SCAle <NR1>
    - HORizontal:MODe:SCAle?
    - HORizontal:MODe?
    - HORizontal:POSition <NR3>
    - HORizontal:POSition?
    - HORizontal:PREViewstate?
    - HORizontal:RECOrdlength <NR1>
    - HORizontal:RECOrdlength?
    - HORizontal:ROLL?
    - HORizontal:SAMPLERate <NR3>
    - HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide {OFF|ON|0|1}
    - HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide?
    - HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue {AUTOmatic|<NR3>}
    - HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue?
    - HORizontal:SAMPLERate?
    - HORizontal:SCAle <NR3>
    - HORizontal:SCAle?
    - HORizontal?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class HorizontalScale(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:SCAle`` command.

    Description:
        - This command sets or queries the horizontal scale.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:SCAle?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:SCAle value`` command.

    SCPI Syntax:
        ```
        - HORizontal:SCAle <NR3>
        - HORizontal:SCAle?
        ```

    Info:
        - ``<NR3>`` is the horizontal scale in time per division.
    """


class HorizontalSamplerateAnalyzemodeMinimumValue(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue`` command.

    Description:
        - Sets or queries the minimum sample rate used by Analysis Automatic horizontal mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue value`` command.

    SCPI Syntax:
        ```
        - HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue {AUTOmatic|<NR3>}
        - HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue?
        ```

    Info:
        - ``AUTOmatic`` allows the instrument to set the minimum value.
        - ``<NR3>`` is the minimum sample rate.
    """


class HorizontalSamplerateAnalyzemodeMinimumOverride(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide`` command.

    Description:
        - Sets or queries the flag which allows override of the horizontal analyze minimum sample
          rate.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide value`` command.

    SCPI Syntax:
        ```
        - HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide {OFF|ON|0|1}
        - HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide?
        ```

    Info:
        - ``0`` does not allow override of the horizontal analyze minimum sample rate.
        - ``1`` allows override of the horizontal analyze minimum sample rate.
        - ``OFF`` does not allow override of the horizontal analyze minimum sample rate.
        - ``ON`` allows override of the horizontal analyze minimum sample rate.
    """


class HorizontalSamplerateAnalyzemodeMinimum(SCPICmdRead):
    """The ``HORizontal:SAMPLERate:ANALYZemode:MINimum`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:SAMPLERate:ANALYZemode:MINimum?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:SAMPLERate:ANALYZemode:MINimum?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.override``: The ``HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide`` command.
        - ``.value``: The ``HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._override = HorizontalSamplerateAnalyzemodeMinimumOverride(
            device, f"{self._cmd_syntax}:OVERRide"
        )
        self._value = HorizontalSamplerateAnalyzemodeMinimumValue(
            device, f"{self._cmd_syntax}:VALue"
        )

    @property
    def override(self) -> HorizontalSamplerateAnalyzemodeMinimumOverride:
        """Return the ``HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide`` command.

        Description:
            - Sets or queries the flag which allows override of the horizontal analyze minimum
              sample rate.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide value`` command.

        SCPI Syntax:
            ```
            - HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide {OFF|ON|0|1}
            - HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide?
            ```

        Info:
            - ``0`` does not allow override of the horizontal analyze minimum sample rate.
            - ``1`` allows override of the horizontal analyze minimum sample rate.
            - ``OFF`` does not allow override of the horizontal analyze minimum sample rate.
            - ``ON`` allows override of the horizontal analyze minimum sample rate.
        """
        return self._override

    @property
    def value(self) -> HorizontalSamplerateAnalyzemodeMinimumValue:
        """Return the ``HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue`` command.

        Description:
            - Sets or queries the minimum sample rate used by Analysis Automatic horizontal mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue value`` command.

        SCPI Syntax:
            ```
            - HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue {AUTOmatic|<NR3>}
            - HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue?
            ```

        Info:
            - ``AUTOmatic`` allows the instrument to set the minimum value.
            - ``<NR3>`` is the minimum sample rate.
        """
        return self._value


class HorizontalSamplerateAnalyzemode(SCPICmdRead):
    """The ``HORizontal:SAMPLERate:ANALYZemode`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:SAMPLERate:ANALYZemode?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:SAMPLERate:ANALYZemode?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.minimum``: The ``HORizontal:SAMPLERate:ANALYZemode:MINimum`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._minimum = HorizontalSamplerateAnalyzemodeMinimum(
            device, f"{self._cmd_syntax}:MINimum"
        )

    @property
    def minimum(self) -> HorizontalSamplerateAnalyzemodeMinimum:
        """Return the ``HORizontal:SAMPLERate:ANALYZemode:MINimum`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:SAMPLERate:ANALYZemode:MINimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:SAMPLERate:ANALYZemode:MINimum?`` query and raise an AssertionError if
              the returned value does not match ``value``.

        Sub-properties:
            - ``.override``: The ``HORizontal:SAMPLERate:ANALYZemode:MINimum:OVERRide`` command.
            - ``.value``: The ``HORizontal:SAMPLERate:ANALYZemode:MINimum:VALue`` command.
        """
        return self._minimum


class HorizontalSamplerate(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:SAMPLERate`` command.

    Description:
        - This command sets or queries the horizontal sample rate.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:SAMPLERate?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:SAMPLERate?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:SAMPLERate value`` command.

    SCPI Syntax:
        ```
        - HORizontal:SAMPLERate <NR3>
        - HORizontal:SAMPLERate?
        ```

    Info:
        - ``<NR3>`` is the horizontal sample rate in samples per second.

    Properties:
        - ``.analyzemode``: The ``HORizontal:SAMPLERate:ANALYZemode`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._analyzemode = HorizontalSamplerateAnalyzemode(
            device, f"{self._cmd_syntax}:ANALYZemode"
        )

    @property
    def analyzemode(self) -> HorizontalSamplerateAnalyzemode:
        """Return the ``HORizontal:SAMPLERate:ANALYZemode`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:SAMPLERate:ANALYZemode?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:SAMPLERate:ANALYZemode?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.minimum``: The ``HORizontal:SAMPLERate:ANALYZemode:MINimum`` command tree.
        """
        return self._analyzemode


class HorizontalRoll(SCPICmdRead):
    """The ``HORizontal:ROLL`` command.

    Description:
        - Queries the horizontal roll mode status.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:ROLL?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:ROLL?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:ROLL?
        ```
    """


class HorizontalRecordlength(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:RECOrdlength`` command.

    Description:
        - This command sets or queries the horizontal record length. To change the record length the
          Horizontal Mode must be set to Manual.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:RECOrdlength?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:RECOrdlength?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:RECOrdlength value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:RECOrdlength <NR1>
        - HORizontal:RECOrdlength?
        ```

    Info:
        - ``<NR1>`` is the horizontal record length.
    """


class HorizontalPreviewstate(SCPICmdRead):
    """The ``HORizontal:PREViewstate`` command.

    Description:
        - This query returns the display system preview state.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:PREViewstate?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:PREViewstate?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:PREViewstate?
        ```
    """


class HorizontalPosition(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:POSition`` command.

    Description:
        - This command sets or queries the horizontal position as a percent of screen width. When
          Horizontal Delay Mode is turned off, this command is equivalent to adjusting the
          HORIZONTAL POSITION knob on the front panel. When Horizontal Delay Mode is turned on, the
          horizontal position is forced to 50%.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:POSition?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:POSition value`` command.

    SCPI Syntax:
        ```
        - HORizontal:POSition <NR3>
        - HORizontal:POSition?
        ```

    Info:
        - ``<NR3>`` is from 0 to ≈100 and is the position of the trigger point on the screen (0 =
          left edge, 100 = right edge).
    """


class HorizontalModeScale(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODe:SCAle`` command.

    Description:
        - This command sets or queries the horizontal scale.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODe:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODe:SCAle value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MODe:SCAle <NR1>
        - HORizontal:MODe:SCAle?
        ```

    Info:
        - ``<NR1>`` is the horizontal scale in seconds per division.
    """


class HorizontalModeSamplerate(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODe:SAMPLERate`` command.

    Description:
        - This command sets or queries the sample rate.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODe:SAMPLERate?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:SAMPLERate?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODe:SAMPLERate value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:MODe:SAMPLERate <NR1>
        - HORizontal:MODe:SAMPLERate?
        ```

    Info:
        - ``<NR1>`` is the sample rate in samples per second.
    """


class HorizontalModeRecordlength(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODe:RECOrdlength`` command.

    Description:
        - This command sets or queries the record length.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODe:RECOrdlength?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:RECOrdlength?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODe:RECOrdlength value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:MODe:RECOrdlength <NR1>
        - HORizontal:MODe:RECOrdlength?
        ```

    Info:
        - ``<NR1>`` is the record length in samples. Manual mode lets you change the record length,
          while the record length is read only for Automatic mode.
    """


class HorizontalModeManualConfigure(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODe:MANual:CONFIGure`` command.

    Description:
        - Sets or queries which horizontal control (scale or record length) will primarily change
          when the sample rate is changed in Manual mode. If the selected control (scale or record
          length) reaches a limit then the unselected control (record length or scale) may also
          change.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODe:MANual:CONFIGure?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:MANual:CONFIGure?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:MODe:MANual:CONFIGure value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MODe:MANual:CONFIGure {HORIZontalscale|RECORDLength}
        - HORizontal:MODe:MANual:CONFIGure?
        ```

    Info:
        - ``HORIZontalscale`` will change when sample rate is adjusted.
        - ``RECORDLength`` will change when sample rate is adjusted.
    """


class HorizontalModeManual(SCPICmdRead):
    """The ``HORizontal:MODe:MANual`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODe:MANual?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:MANual?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.configure``: The ``HORizontal:MODe:MANual:CONFIGure`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._configure = HorizontalModeManualConfigure(device, f"{self._cmd_syntax}:CONFIGure")

    @property
    def configure(self) -> HorizontalModeManualConfigure:
        """Return the ``HORizontal:MODe:MANual:CONFIGure`` command.

        Description:
            - Sets or queries which horizontal control (scale or record length) will primarily
              change when the sample rate is changed in Manual mode. If the selected control (scale
              or record length) reaches a limit then the unselected control (record length or scale)
              may also change.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODe:MANual:CONFIGure?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:MODe:MANual:CONFIGure?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:MODe:MANual:CONFIGure value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MODe:MANual:CONFIGure {HORIZontalscale|RECORDLength}
            - HORizontal:MODe:MANual:CONFIGure?
            ```

        Info:
            - ``HORIZontalscale`` will change when sample rate is adjusted.
            - ``RECORDLength`` will change when sample rate is adjusted.
        """
        return self._configure


class HorizontalModeAutomaticFastacqRecordlengthMaximumZoomoverride(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride`` command.

    Description:
        - Sets or queries the flag which allows override of the horizontal FastAcq maximum record
          length.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride {OFF|ON|0|1}
        - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride?
        ```

    Info:
        - ``OFF`` does not allow override of the horizontal FastAcq maximum record length.
        - ``ON`` allows override of the horizontal FastAcq maximum record length.
        - ``0`` does not allow override of the horizontal FastAcq maximum record length.
        - ``1`` allows override of the horizontal FastAcq maximum record length.
    """


class HorizontalModeAutomaticFastacqRecordlengthMaximumValue(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue`` command.

    Description:
        - Sets or queries the horizontal FastAcq maximum record length.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue <NR1>
        - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue?
        ```

    Info:
        - ``<NR1>`` is the horizontal FastAcq maximum record length.
    """


class HorizontalModeAutomaticFastacqRecordlengthMaximum(SCPICmdRead):
    """The ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.value``: The ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue`` command.
        - ``.zoomoverride``: The
          ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._value = HorizontalModeAutomaticFastacqRecordlengthMaximumValue(
            device, f"{self._cmd_syntax}:VALue"
        )
        self._zoomoverride = HorizontalModeAutomaticFastacqRecordlengthMaximumZoomoverride(
            device, f"{self._cmd_syntax}:ZOOMOVERride"
        )

    @property
    def value(self) -> HorizontalModeAutomaticFastacqRecordlengthMaximumValue:
        """Return the ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue`` command.

        Description:
            - Sets or queries the horizontal FastAcq maximum record length.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue <NR1>
            - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue?
            ```

        Info:
            - ``<NR1>`` is the horizontal FastAcq maximum record length.
        """
        return self._value

    @property
    def zoomoverride(self) -> HorizontalModeAutomaticFastacqRecordlengthMaximumZoomoverride:
        """``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride`` command.

        Description:
            - Sets or queries the flag which allows override of the horizontal FastAcq maximum
              record length.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride {OFF|ON|0|1}
            - HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride?
            ```

        Info:
            - ``OFF`` does not allow override of the horizontal FastAcq maximum record length.
            - ``ON`` allows override of the horizontal FastAcq maximum record length.
            - ``0`` does not allow override of the horizontal FastAcq maximum record length.
            - ``1`` allows override of the horizontal FastAcq maximum record length.
        """
        return self._zoomoverride


class HorizontalModeAutomaticFastacqRecordlength(SCPICmdRead):
    """The ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength`` command tree.

    Usage:
        - Using the ``.query()`` method will send the
          ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength?`` query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength?`` query and raise an AssertionError if
          the returned value does not match ``value``.

    Properties:
        - ``.maximum``: The ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._maximum = HorizontalModeAutomaticFastacqRecordlengthMaximum(
            device, f"{self._cmd_syntax}:MAXimum"
        )

    @property
    def maximum(self) -> HorizontalModeAutomaticFastacqRecordlengthMaximum:
        """Return the ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.value``: The ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:VALue``
              command.
            - ``.zoomoverride``: The
              ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum:ZOOMOVERride`` command.
        """
        return self._maximum


class HorizontalModeAutomaticFastacq(SCPICmdRead):
    """The ``HORizontal:MODe:AUTOmatic:FASTAcq`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODe:AUTOmatic:FASTAcq?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:AUTOmatic:FASTAcq?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.recordlength``: The ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._recordlength = HorizontalModeAutomaticFastacqRecordlength(
            device, f"{self._cmd_syntax}:RECOrdlength"
        )

    @property
    def recordlength(self) -> HorizontalModeAutomaticFastacqRecordlength:
        """Return the ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength?`` query and raise an AssertionError
              if the returned value does not match ``value``.

        Sub-properties:
            - ``.maximum``: The ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength:MAXimum`` command
              tree.
        """
        return self._recordlength


class HorizontalModeAutomatic(SCPICmdRead):
    """The ``HORizontal:MODe:AUTOmatic`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODe:AUTOmatic?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:AUTOmatic?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.fastacq``: The ``HORizontal:MODe:AUTOmatic:FASTAcq`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._fastacq = HorizontalModeAutomaticFastacq(device, f"{self._cmd_syntax}:FASTAcq")

    @property
    def fastacq(self) -> HorizontalModeAutomaticFastacq:
        """Return the ``HORizontal:MODe:AUTOmatic:FASTAcq`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODe:AUTOmatic:FASTAcq?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:MODe:AUTOmatic:FASTAcq?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.recordlength``: The ``HORizontal:MODe:AUTOmatic:FASTAcq:RECOrdlength`` command
              tree.
        """
        return self._fastacq


class HorizontalMode(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODe`` command.

    Description:
        - This command set or queries the horizontal operating mode.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODe value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MODe {AUTO|MANual}
        - HORizontal:MODe?
        ```

    Info:
        - ``AUTO`` selects the automatic horizontal model. Auto mode automatically adjusts the
          sample rate and record length to provide a high acquisition rate in Fast Acq or signal
          fidelity in analysis. Record length is read only.
        - ``MANUAL`` selects the manual horizontal model. Manual mode lets you change the sample
          rate, horizontal scale, and record length. These values interact. For example, when you
          change record length then the horizontal scale also changes.

    Properties:
        - ``.automatic``: The ``HORizontal:MODe:AUTOmatic`` command tree.
        - ``.manual``: The ``HORizontal:MODe:MANual`` command tree.
        - ``.recordlength``: The ``HORizontal:MODe:RECOrdlength`` command.
        - ``.samplerate``: The ``HORizontal:MODe:SAMPLERate`` command.
        - ``.scale``: The ``HORizontal:MODe:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._automatic = HorizontalModeAutomatic(device, f"{self._cmd_syntax}:AUTOmatic")
        self._manual = HorizontalModeManual(device, f"{self._cmd_syntax}:MANual")
        self._recordlength = HorizontalModeRecordlength(device, f"{self._cmd_syntax}:RECOrdlength")
        self._samplerate = HorizontalModeSamplerate(device, f"{self._cmd_syntax}:SAMPLERate")
        self._scale = HorizontalModeScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def automatic(self) -> HorizontalModeAutomatic:
        """Return the ``HORizontal:MODe:AUTOmatic`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODe:AUTOmatic?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:AUTOmatic?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.fastacq``: The ``HORizontal:MODe:AUTOmatic:FASTAcq`` command tree.
        """
        return self._automatic

    @property
    def manual(self) -> HorizontalModeManual:
        """Return the ``HORizontal:MODe:MANual`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODe:MANual?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:MANual?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.configure``: The ``HORizontal:MODe:MANual:CONFIGure`` command.
        """
        return self._manual

    @property
    def recordlength(self) -> HorizontalModeRecordlength:
        """Return the ``HORizontal:MODe:RECOrdlength`` command.

        Description:
            - This command sets or queries the record length.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODe:RECOrdlength?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:RECOrdlength?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:MODe:RECOrdlength value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MODe:RECOrdlength <NR1>
            - HORizontal:MODe:RECOrdlength?
            ```

        Info:
            - ``<NR1>`` is the record length in samples. Manual mode lets you change the record
              length, while the record length is read only for Automatic mode.
        """
        return self._recordlength

    @property
    def samplerate(self) -> HorizontalModeSamplerate:
        """Return the ``HORizontal:MODe:SAMPLERate`` command.

        Description:
            - This command sets or queries the sample rate.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODe:SAMPLERate?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:SAMPLERate?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MODe:SAMPLERate value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:MODe:SAMPLERate <NR1>
            - HORizontal:MODe:SAMPLERate?
            ```

        Info:
            - ``<NR1>`` is the sample rate in samples per second.
        """
        return self._samplerate

    @property
    def scale(self) -> HorizontalModeScale:
        """Return the ``HORizontal:MODe:SCAle`` command.

        Description:
            - This command sets or queries the horizontal scale.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODe:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODe:SCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MODe:SCAle value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:MODe:SCAle <NR1>
            - HORizontal:MODe:SCAle?
            ```

        Info:
            - ``<NR1>`` is the horizontal scale in seconds per division.
        """
        return self._scale


class HorizontalMainInterpratio(SCPICmdRead):
    """The ``HORizontal:MAIn:INTERPRatio`` command.

    Description:
        - This query-only command returns the Horizontal interpolation ratio.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:INTERPRatio?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:INTERPRatio?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:INTERPRatio?
        ```
    """


class HorizontalMain(SCPICmdRead):
    """The ``HORizontal:MAIn`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.interpratio``: The ``HORizontal:MAIn:INTERPRatio`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._interpratio = HorizontalMainInterpratio(device, f"{self._cmd_syntax}:INTERPRatio")

    @property
    def interpratio(self) -> HorizontalMainInterpratio:
        """Return the ``HORizontal:MAIn:INTERPRatio`` command.

        Description:
            - This query-only command returns the Horizontal interpolation ratio.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:INTERPRatio?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:INTERPRatio?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:INTERPRatio?
            ```
        """
        return self._interpratio


class HorizontalHistoryTimestampSelected(SCPICmdRead):
    """The ``HORizontal:HISTory:TIMEStamp:SELECTED`` command.

    Description:
        - This query-only command returns the timestamp of the history selected acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory:TIMEStamp:SELECTED?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:HISTory:TIMEStamp:SELECTED?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:HISTory:TIMEStamp:SELECTED?
        ```
    """


class HorizontalHistoryTimestampReference(SCPICmdRead):
    """The ``HORizontal:HISTory:TIMEStamp:REFerence`` command.

    Description:
        - This query-only command returns the timestamp of the history reference acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory:TIMEStamp:REFerence?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:HISTory:TIMEStamp:REFerence?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:HISTory:TIMEStamp:REFerence?
        ```
    """


class HorizontalHistoryTimestampDelta(SCPICmdRead):
    """The ``HORizontal:HISTory:TIMEStamp:DELTa`` command.

    Description:
        - This query-only command returns the difference between the timestamps of the history
          reference acquisition and the history selected acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory:TIMEStamp:DELTa?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:TIMEStamp:DELTa?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:HISTory:TIMEStamp:DELTa?
        ```
    """


class HorizontalHistoryTimestamp(SCPICmdRead):
    """The ``HORizontal:HISTory:TIMEStamp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory:TIMEStamp?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:TIMEStamp?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delta``: The ``HORizontal:HISTory:TIMEStamp:DELTa`` command.
        - ``.reference``: The ``HORizontal:HISTory:TIMEStamp:REFerence`` command.
        - ``.selected``: The ``HORizontal:HISTory:TIMEStamp:SELECTED`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delta = HorizontalHistoryTimestampDelta(device, f"{self._cmd_syntax}:DELTa")
        self._reference = HorizontalHistoryTimestampReference(
            device, f"{self._cmd_syntax}:REFerence"
        )
        self._selected = HorizontalHistoryTimestampSelected(device, f"{self._cmd_syntax}:SELECTED")

    @property
    def delta(self) -> HorizontalHistoryTimestampDelta:
        """Return the ``HORizontal:HISTory:TIMEStamp:DELTa`` command.

        Description:
            - This query-only command returns the difference between the timestamps of the history
              reference acquisition and the history selected acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:HISTory:TIMEStamp:DELTa?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:HISTory:TIMEStamp:DELTa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:HISTory:TIMEStamp:DELTa?
            ```
        """
        return self._delta

    @property
    def reference(self) -> HorizontalHistoryTimestampReference:
        """Return the ``HORizontal:HISTory:TIMEStamp:REFerence`` command.

        Description:
            - This query-only command returns the timestamp of the history reference acquisition.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:HISTory:TIMEStamp:REFerence?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:HISTory:TIMEStamp:REFerence?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:HISTory:TIMEStamp:REFerence?
            ```
        """
        return self._reference

    @property
    def selected(self) -> HorizontalHistoryTimestampSelected:
        """Return the ``HORizontal:HISTory:TIMEStamp:SELECTED`` command.

        Description:
            - This query-only command returns the timestamp of the history selected acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:HISTory:TIMEStamp:SELECTED?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:HISTory:TIMEStamp:SELECTED?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:HISTory:TIMEStamp:SELECTED?
            ```
        """
        return self._selected


class HorizontalHistoryState(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:HISTory:STATe`` command.

    Description:
        - This command sets or returns the state of History. Acquisition modes Peak Detect, Envelope
          and Average are not compatible with History. If History is on, an attempted set to those
          acquisition modes will fail and revert to Sample mode. If History is turned on while in
          one of those acquisition modes, the acquisition mode is changed to Sample.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:STATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:HISTory:STATe value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:HISTory:STATe {OFF|ON|1|0}
        - HORizontal:HISTory:STATe?
        ```

    Info:
        - ``ON`` enables History.
        - ``OFF`` disables History.
        - ``1`` enables History.
        - ``0`` disables History; any other number value turns this feature on.
    """


class HorizontalHistorySelected(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:HISTory:SELected`` command.

    Description:
        - This command sets or queries the selected acquisition in History. By default this is the
          most recent acquisition in History.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory:SELected?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:SELected?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:HISTory:SELected value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:HISTory:SELected <NR1>
        - HORizontal:HISTory:SELected?
        ```

    Info:
        - ``<NR1>`` is the acquisition number to set. Must be between 1 and the total number of
          acquisitions in History.
    """


class HorizontalHistoryRefInclude(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:HISTory:REF:INClude`` command.

    Description:
        - This command sets or returns whether the history reference acquisition is included in the
          user interface history badge or not.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory:REF:INClude?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:REF:INClude?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:HISTory:REF:INClude value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:HISTory:REF:INClude {ON|OFF}
        - HORizontal:HISTory:REF:INClude?
        ```

    Info:
        - ``ON`` includes the reference acquisition.
        - ``OFF`` does not include the reference acquisition.
    """


class HorizontalHistoryRefAcq(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:HISTory:REF:ACQ`` command.

    Description:
        - This command sets or queries the reference acquisition in History. By default this is the
          first acquisition in History.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory:REF:ACQ?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:REF:ACQ?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:HISTory:REF:ACQ value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:HISTory:REF:ACQ <NR1>
        - HORizontal:HISTory:REF:ACQ?
        ```

    Info:
        - ``<NR1>`` is the acquisition number to set. Must be between 1 and the total number of
          acquisitions in History.
    """


class HorizontalHistoryRef(SCPICmdRead):
    """The ``HORizontal:HISTory:REF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory:REF?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:REF?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.acq``: The ``HORizontal:HISTory:REF:ACQ`` command.
        - ``.include``: The ``HORizontal:HISTory:REF:INClude`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._acq = HorizontalHistoryRefAcq(device, f"{self._cmd_syntax}:ACQ")
        self._include = HorizontalHistoryRefInclude(device, f"{self._cmd_syntax}:INClude")

    @property
    def acq(self) -> HorizontalHistoryRefAcq:
        """Return the ``HORizontal:HISTory:REF:ACQ`` command.

        Description:
            - This command sets or queries the reference acquisition in History. By default this is
              the first acquisition in History.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:HISTory:REF:ACQ?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:REF:ACQ?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:HISTory:REF:ACQ value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:HISTory:REF:ACQ <NR1>
            - HORizontal:HISTory:REF:ACQ?
            ```

        Info:
            - ``<NR1>`` is the acquisition number to set. Must be between 1 and the total number of
              acquisitions in History.
        """
        return self._acq

    @property
    def include(self) -> HorizontalHistoryRefInclude:
        """Return the ``HORizontal:HISTory:REF:INClude`` command.

        Description:
            - This command sets or returns whether the history reference acquisition is included in
              the user interface history badge or not.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:HISTory:REF:INClude?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:REF:INClude?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:HISTory:REF:INClude value`` command.

        SCPI Syntax:
            ```
            - HORizontal:HISTory:REF:INClude {ON|OFF}
            - HORizontal:HISTory:REF:INClude?
            ```

        Info:
            - ``ON`` includes the reference acquisition.
            - ``OFF`` does not include the reference acquisition.
        """
        return self._include


class HorizontalHistoryOverlay(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:HISTory:OVERlay`` command.

    Description:
        - This command sets or returns whether all acquisitions in history are overlaid in the
          waveform view.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory:OVERlay?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:OVERlay?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:HISTory:OVERlay value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:HISTory:OVERlay {ON|OFF}
        - HORizontal:HISTory:OVERlay?
        ```

    Info:
        - ``ON`` overlays all acquisitions in history in the waveform view.
        - ``OFF`` only shows the current acquisition in the waveform view.
    """


class HorizontalHistoryCstats(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:HISTory:CSTAts`` command.

    Description:
        - This command sets or returns the history cumulative statistics type. When in All
          Acquisitions mode, statistics and plots reflect all acquisitions since the scope began
          acquiring. This may include results from acquisitions that go further back in time than
          those captured in history. When in History Only mode, statistics and plots only include
          acquisitions in history. The cumulative statistics type is set to All Acquisitions by
          default.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory:CSTAts?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:CSTAts?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:HISTory:CSTAts value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:HISTory:CSTAts {AACQs|HONLy}
        - HORizontal:HISTory:CSTAts?
        ```

    Info:
        - ``AACQs`` sets the history cumulative statistics type to all acquisitions.
        - ``HONLy`` sets the history cumulative statistics type to history only.
    """


class HorizontalHistory(SCPICmdRead):
    """The ``HORizontal:HISTory`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:HISTory?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.cstats``: The ``HORizontal:HISTory:CSTAts`` command.
        - ``.overlay``: The ``HORizontal:HISTory:OVERlay`` command.
        - ``.ref``: The ``HORizontal:HISTory:REF`` command tree.
        - ``.selected``: The ``HORizontal:HISTory:SELected`` command.
        - ``.state``: The ``HORizontal:HISTory:STATe`` command.
        - ``.timestamp``: The ``HORizontal:HISTory:TIMEStamp`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cstats = HorizontalHistoryCstats(device, f"{self._cmd_syntax}:CSTAts")
        self._overlay = HorizontalHistoryOverlay(device, f"{self._cmd_syntax}:OVERlay")
        self._ref = HorizontalHistoryRef(device, f"{self._cmd_syntax}:REF")
        self._selected = HorizontalHistorySelected(device, f"{self._cmd_syntax}:SELected")
        self._state = HorizontalHistoryState(device, f"{self._cmd_syntax}:STATe")
        self._timestamp = HorizontalHistoryTimestamp(device, f"{self._cmd_syntax}:TIMEStamp")

    @property
    def cstats(self) -> HorizontalHistoryCstats:
        """Return the ``HORizontal:HISTory:CSTAts`` command.

        Description:
            - This command sets or returns the history cumulative statistics type. When in All
              Acquisitions mode, statistics and plots reflect all acquisitions since the scope began
              acquiring. This may include results from acquisitions that go further back in time
              than those captured in history. When in History Only mode, statistics and plots only
              include acquisitions in history. The cumulative statistics type is set to All
              Acquisitions by default.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:HISTory:CSTAts?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:CSTAts?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:HISTory:CSTAts value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:HISTory:CSTAts {AACQs|HONLy}
            - HORizontal:HISTory:CSTAts?
            ```

        Info:
            - ``AACQs`` sets the history cumulative statistics type to all acquisitions.
            - ``HONLy`` sets the history cumulative statistics type to history only.
        """
        return self._cstats

    @property
    def overlay(self) -> HorizontalHistoryOverlay:
        """Return the ``HORizontal:HISTory:OVERlay`` command.

        Description:
            - This command sets or returns whether all acquisitions in history are overlaid in the
              waveform view.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:HISTory:OVERlay?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:OVERlay?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:HISTory:OVERlay value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:HISTory:OVERlay {ON|OFF}
            - HORizontal:HISTory:OVERlay?
            ```

        Info:
            - ``ON`` overlays all acquisitions in history in the waveform view.
            - ``OFF`` only shows the current acquisition in the waveform view.
        """
        return self._overlay

    @property
    def ref(self) -> HorizontalHistoryRef:
        """Return the ``HORizontal:HISTory:REF`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:HISTory:REF?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:REF?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.acq``: The ``HORizontal:HISTory:REF:ACQ`` command.
            - ``.include``: The ``HORizontal:HISTory:REF:INClude`` command.
        """
        return self._ref

    @property
    def selected(self) -> HorizontalHistorySelected:
        """Return the ``HORizontal:HISTory:SELected`` command.

        Description:
            - This command sets or queries the selected acquisition in History. By default this is
              the most recent acquisition in History.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:HISTory:SELected?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:SELected?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:HISTory:SELected value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:HISTory:SELected <NR1>
            - HORizontal:HISTory:SELected?
            ```

        Info:
            - ``<NR1>`` is the acquisition number to set. Must be between 1 and the total number of
              acquisitions in History.
        """
        return self._selected

    @property
    def state(self) -> HorizontalHistoryState:
        """Return the ``HORizontal:HISTory:STATe`` command.

        Description:
            - This command sets or returns the state of History. Acquisition modes Peak Detect,
              Envelope and Average are not compatible with History. If History is on, an attempted
              set to those acquisition modes will fail and revert to Sample mode. If History is
              turned on while in one of those acquisition modes, the acquisition mode is changed to
              Sample.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:HISTory:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:STATe?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:HISTory:STATe value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:HISTory:STATe {OFF|ON|1|0}
            - HORizontal:HISTory:STATe?
            ```

        Info:
            - ``ON`` enables History.
            - ``OFF`` disables History.
            - ``1`` enables History.
            - ``0`` disables History; any other number value turns this feature on.
        """
        return self._state

    @property
    def timestamp(self) -> HorizontalHistoryTimestamp:
        """Return the ``HORizontal:HISTory:TIMEStamp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:HISTory:TIMEStamp?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory:TIMEStamp?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delta``: The ``HORizontal:HISTory:TIMEStamp:DELTa`` command.
            - ``.reference``: The ``HORizontal:HISTory:TIMEStamp:REFerence`` command.
            - ``.selected``: The ``HORizontal:HISTory:TIMEStamp:SELECTED`` command.
        """
        return self._timestamp


class HorizontalFastframeXzeroSelected(SCPICmdRead):
    """The ``HORizontal:FASTframe:XZEro:SELECTED`` command.

    Description:
        - This query-only command returns the sub-sample time between the trigger sample (designated
          by ``PT_OFF``) and the occurrence of the actual trigger for the waveform specified by the
          ``DATa:SOUrce`` command for the selected frame. This value is in units of
          ``WFMOutpre:XUNit``.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:SELECTED?``
          query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro:SELECTED?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:XZEro:SELECTED?
        ```
    """


class HorizontalFastframeXzeroRef(SCPICmdRead):
    """The ``HORizontal:FASTframe:XZEro:REF`` command.

    Description:
        - This query-only command returns the sub-sample time between the trigger sample (designated
          by ``PT_OFF``) and the occurrence of the actual trigger for the waveform specified by the
          ``DATa:SOUrce`` command for the reference frame. This value is in units of
          ``WFMOutpre:XUNit``.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:REF?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro:REF?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:XZEro:REF?
        ```
    """


class HorizontalFastframeXzeroAll(SCPICmdRead):
    """The ``HORizontal:FASTframe:XZEro:ALL`` command.

    Description:
        - This query-only command returns the sub-sample time between the trigger sample (designated
          by ``PT_OFF``) and the occurrence of the actual trigger for the waveform specified by the
          ``DATa:SOUrce`` command for all frames. This value is in units of ``WFMOutpre:XUNit``. The
          format is a string of the form (frame #``:zxero``, frame #``:xzero``, and so on).

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:ALL?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro:ALL?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:XZEro:ALL?
        ```
    """


class HorizontalFastframeXzero(SCPICmdRead):
    """The ``HORizontal:FASTframe:XZEro`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.all``: The ``HORizontal:FASTframe:XZEro:ALL`` command.
        - ``.ref``: The ``HORizontal:FASTframe:XZEro:REF`` command.
        - ``.selected``: The ``HORizontal:FASTframe:XZEro:SELECTED`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._all = HorizontalFastframeXzeroAll(device, f"{self._cmd_syntax}:ALL")
        self._ref = HorizontalFastframeXzeroRef(device, f"{self._cmd_syntax}:REF")
        self._selected = HorizontalFastframeXzeroSelected(device, f"{self._cmd_syntax}:SELECTED")

    @property
    def all(self) -> HorizontalFastframeXzeroAll:
        """Return the ``HORizontal:FASTframe:XZEro:ALL`` command.

        Description:
            - This query-only command returns the sub-sample time between the trigger sample
              (designated by ``PT_OFF``) and the occurrence of the actual trigger for the waveform
              specified by the ``DATa:SOUrce`` command for all frames. This value is in units of
              ``WFMOutpre:XUNit``. The format is a string of the form (frame #``:zxero``, frame
              #``:xzero``, and so on).

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:ALL?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro:ALL?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:XZEro:ALL?
            ```
        """
        return self._all

    @property
    def ref(self) -> HorizontalFastframeXzeroRef:
        """Return the ``HORizontal:FASTframe:XZEro:REF`` command.

        Description:
            - This query-only command returns the sub-sample time between the trigger sample
              (designated by ``PT_OFF``) and the occurrence of the actual trigger for the waveform
              specified by the ``DATa:SOUrce`` command for the reference frame. This value is in
              units of ``WFMOutpre:XUNit``.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:REF?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro:REF?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:XZEro:REF?
            ```
        """
        return self._ref

    @property
    def selected(self) -> HorizontalFastframeXzeroSelected:
        """Return the ``HORizontal:FASTframe:XZEro:SELECTED`` command.

        Description:
            - This query-only command returns the sub-sample time between the trigger sample
              (designated by ``PT_OFF``) and the occurrence of the actual trigger for the waveform
              specified by the ``DATa:SOUrce`` command for the selected frame. This value is in
              units of ``WFMOutpre:XUNit``.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro:SELECTED?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:XZEro:SELECTED?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:XZEro:SELECTED?
            ```
        """
        return self._selected


class HorizontalFastframeTimestampSelected(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:SELECTED`` command.

    Description:
        - This query returns the time-stamp of the FastFrame Selected acquired frame.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:SELECTED?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:SELECTED?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:SELECTED?
        ```
    """


class HorizontalFastframeTimestampReference(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:REFerence`` command.

    Description:
        - This query returns the time-stamp of the FastFrame Reference frame.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:REFerence?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:REFerence?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:REFerence?
        ```
    """


class HorizontalFastframeTimestampDelta(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:DELTa`` command.

    Description:
        - This query returns the time difference between the Selected and Reference time-stamps.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:DELTa?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:TIMEStamp:DELTa?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:DELTa?
        ```
    """


class HorizontalFastframeTimestampAll(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp:ALL`` command.

    Description:
        - This query-only command returns the time stamp of all frames. The format is (Frame #:
          TimeStamp, Frame #: TimeStamp, and so on). Each time-stamp string is of the form
          DD.MM.YYYY.``HH:MM``:``:SS``.xxxxxxxxxxxx.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:ALL?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:TIMEStamp:ALL?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:TIMEStamp:ALL?
        ```
    """


class HorizontalFastframeTimestamp(SCPICmdRead):
    """The ``HORizontal:FASTframe:TIMEStamp`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:TIMEStamp?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.all``: The ``HORizontal:FASTframe:TIMEStamp:ALL`` command.
        - ``.delta``: The ``HORizontal:FASTframe:TIMEStamp:DELTa`` command.
        - ``.reference``: The ``HORizontal:FASTframe:TIMEStamp:REFerence`` command.
        - ``.selected``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._all = HorizontalFastframeTimestampAll(device, f"{self._cmd_syntax}:ALL")
        self._delta = HorizontalFastframeTimestampDelta(device, f"{self._cmd_syntax}:DELTa")
        self._reference = HorizontalFastframeTimestampReference(
            device, f"{self._cmd_syntax}:REFerence"
        )
        self._selected = HorizontalFastframeTimestampSelected(
            device, f"{self._cmd_syntax}:SELECTED"
        )

    @property
    def all(self) -> HorizontalFastframeTimestampAll:
        """Return the ``HORizontal:FASTframe:TIMEStamp:ALL`` command.

        Description:
            - This query-only command returns the time stamp of all frames. The format is (Frame #:
              TimeStamp, Frame #: TimeStamp, and so on). Each time-stamp string is of the form
              DD.MM.YYYY.``HH:MM``:``:SS``.xxxxxxxxxxxx.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:ALL?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:ALL?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:ALL?
            ```
        """
        return self._all

    @property
    def delta(self) -> HorizontalFastframeTimestampDelta:
        """Return the ``HORizontal:FASTframe:TIMEStamp:DELTa`` command.

        Description:
            - This query returns the time difference between the Selected and Reference time-stamps.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp:DELTa?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:DELTa?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:DELTa?
            ```
        """
        return self._delta

    @property
    def reference(self) -> HorizontalFastframeTimestampReference:
        """Return the ``HORizontal:FASTframe:TIMEStamp:REFerence`` command.

        Description:
            - This query returns the time-stamp of the FastFrame Reference frame.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:REFerence?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:REFerence?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:REFerence?
            ```
        """
        return self._reference

    @property
    def selected(self) -> HorizontalFastframeTimestampSelected:
        """Return the ``HORizontal:FASTframe:TIMEStamp:SELECTED`` command.

        Description:
            - This query returns the time-stamp of the FastFrame Selected acquired frame.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:TIMEStamp:SELECTED?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:TIMEStamp:SELECTED?
            ```
        """
        return self._selected


class HorizontalFastframeSumframeState(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:SUMFrame:STATE`` command.

    Description:
        - This command sets or returns the state of FastFrame summary frame. Summary frame mode is
          set automatically based on the acquisition mode. When in Sample mode, the summary frame
          type is set to Average. When in Peak Detect mode, the summary frame type is set to
          Envelope. When in High Res mode, the summary frame type is set to Average.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SUMFrame:STATE?``
          query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SUMFrame:STATE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:SUMFrame:STATE value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:SUMFrame:STATE {ON|OFF|<NR1>}
        - HORizontal:FASTframe:SUMFrame:STATE?
        ```

    Info:
        - ``ON`` indicates summary frame is active.
        - ``OFF`` indicates that summary frame is off.
        - ``<NR1>`` a 0 turns off summary frame; any other value activates the summary frame.
    """


class HorizontalFastframeSumframe(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:SUMFrame`` command.

    Description:
        - This command sets or returns the summary frame type. Turning on Summary Frame does not
          adjust the numberFrames value as long as there is room for an additional frame. If there
          is not enough room then numberFrames will be reduced by 1. The numberFrames value is
          always the number of frames to acquire.

    Usage:
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:SUMFrame value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:SUMFrame {NONe|AVErage|ENVelope}
        ```

    Info:
        - ``NONe`` sets the Summary frame to off.
        - ``AVErage`` sets the Summary frame to average of all acquired frames.
        - ``ENVelope`` sets the Summary frame to envelope of all acquired frames.

    Properties:
        - ``.state``: The ``HORizontal:FASTframe:SUMFrame:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = HorizontalFastframeSumframeState(device, f"{self._cmd_syntax}:STATE")

    @property
    def state(self) -> HorizontalFastframeSumframeState:
        """Return the ``HORizontal:FASTframe:SUMFrame:STATE`` command.

        Description:
            - This command sets or returns the state of FastFrame summary frame. Summary frame mode
              is set automatically based on the acquisition mode. When in Sample mode, the summary
              frame type is set to Average. When in Peak Detect mode, the summary frame type is set
              to Envelope. When in High Res mode, the summary frame type is set to Average.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SUMFrame:STATE?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:SUMFrame:STATE?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:SUMFrame:STATE value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:SUMFrame:STATE {ON|OFF|<NR1>}
            - HORizontal:FASTframe:SUMFrame:STATE?
            ```

        Info:
            - ``ON`` indicates summary frame is active.
            - ``OFF`` indicates that summary frame is off.
            - ``<NR1>`` a 0 turns off summary frame; any other value activates the summary frame.
        """
        return self._state


class HorizontalFastframeState(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:STATE`` command.

    Description:
        - This command sets or returns the state of FastFrame. Acquisition modes Envelope and
          Average are not compatible with FastFrame. If FastFrame is on, an attempted set to those
          acquisition modes will fail and revert to Sample mode. If FastFrame is turned on while in
          one of those acquisition modes, the acquisition mode is changed to Sample.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:STATE?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:STATE value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:STATE {ON|OFF|<NR1>}
        - HORizontal:FASTframe:STATE?
        ```

    Info:
        - ``ON`` indicates FastFrame is active.
        - ``OFF`` indicates that FastFrame is off.
        - ``<NR1>`` A 0 turns off FastFrame; any other value activates FastFrame.
    """


class HorizontalFastframeSelected(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:SELECTED`` command.

    Description:
        - This command sets or returns the selected frame number for acquired frames. Refs have
          their own selected frames.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SELECTED?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:SELECTED value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:SELECTED <NR1>
        - HORizontal:FASTframe:SELECTED?
        ```

    Info:
        - ``<NR1>`` is the selected frame number for acquired frames.
    """


class HorizontalFastframeRefInclude(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:REF:INCLUde`` command.

    Description:
        - This command sets or returns whether the reference frame delta information is shown in the
          display.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF:INCLUde?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:REF:INCLUde?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:REF:INCLUde value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:REF:INCLUde {ON|OFF|<NR1>}
        - HORizontal:FASTframe:REF:INCLUde?
        ```

    Info:
        - ``ON`` displays the delta information.
        - ``OFF`` does not display the delta information.
        - ``<NR1>`` a 0 indicates the delta information is off; any other value displays the delta
          information.
    """


class HorizontalFastframeRefFrame(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:REF:FRAme`` command.

    Description:
        - This command sets or returns the reference frame number.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF:FRAme?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:REF:FRAme?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:REF:FRAme value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:REF:FRAme <NR1>
        - HORizontal:FASTframe:REF:FRAme?
        ```

    Info:
        - ``<NR1>`` is the reference frame number.
    """


class HorizontalFastframeRef(SCPICmdRead):
    """The ``HORizontal:FASTframe:REF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:REF?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.frame``: The ``HORizontal:FASTframe:REF:FRAme`` command.
        - ``.include``: The ``HORizontal:FASTframe:REF:INCLUde`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._frame = HorizontalFastframeRefFrame(device, f"{self._cmd_syntax}:FRAme")
        self._include = HorizontalFastframeRefInclude(device, f"{self._cmd_syntax}:INCLUde")

    @property
    def frame(self) -> HorizontalFastframeRefFrame:
        """Return the ``HORizontal:FASTframe:REF:FRAme`` command.

        Description:
            - This command sets or returns the reference frame number.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF:FRAme?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:REF:FRAme?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:REF:FRAme value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:REF:FRAme <NR1>
            - HORizontal:FASTframe:REF:FRAme?
            ```

        Info:
            - ``<NR1>`` is the reference frame number.
        """
        return self._frame

    @property
    def include(self) -> HorizontalFastframeRefInclude:
        """Return the ``HORizontal:FASTframe:REF:INCLUde`` command.

        Description:
            - This command sets or returns whether the reference frame delta information is shown in
              the display.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF:INCLUde?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:REF:INCLUde?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:REF:INCLUde value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:REF:INCLUde {ON|OFF|<NR1>}
            - HORizontal:FASTframe:REF:INCLUde?
            ```

        Info:
            - ``ON`` displays the delta information.
            - ``OFF`` does not display the delta information.
            - ``<NR1>`` a 0 indicates the delta information is off; any other value displays the
              delta information.
        """
        return self._include


class HorizontalFastframeMultipleframesMode(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:MULtipleframes:MODe`` command.

    Description:
        - This command sets or returns the overlay display type.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:MULtipleframes:MODe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:MODe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:FASTframe:MULtipleframes:MODe value`` command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MULtipleframes:MODe {OFF|OVERlay}
        - HORizontal:FASTframe:MULtipleframes:MODe?
        ```

    Info:
        - ``OFF`` specifies only displaying the selected frame.
        - ``OVERlay`` specifies overlaying all frames with the temperature palette. The summary
          frame is not included in the overlay. The selected frame is drawn in blue on top of all
          other frames.
    """


class HorizontalFastframeMultipleframes(SCPICmdRead):
    """The ``HORizontal:FASTframe:MULtipleframes`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:MULtipleframes?``
          query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:MULtipleframes?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``HORizontal:FASTframe:MULtipleframes:MODe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = HorizontalFastframeMultipleframesMode(device, f"{self._cmd_syntax}:MODe")

    @property
    def mode(self) -> HorizontalFastframeMultipleframesMode:
        """Return the ``HORizontal:FASTframe:MULtipleframes:MODe`` command.

        Description:
            - This command sets or returns the overlay display type.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:MODe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:MODe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes:MODe value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MULtipleframes:MODe {OFF|OVERlay}
            - HORizontal:FASTframe:MULtipleframes:MODe?
            ```

        Info:
            - ``OFF`` specifies only displaying the selected frame.
            - ``OVERlay`` specifies overlaying all frames with the temperature palette. The summary
              frame is not included in the overlay. The selected frame is drawn in blue on top of
              all other frames.
        """
        return self._mode


class HorizontalFastframeMaxframes(SCPICmdRead):
    """The ``HORizontal:FASTframe:MAXFRames`` command.

    Description:
        - This query returns the maximum number of frames.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:MAXFRames?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:MAXFRames?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:MAXFRames?
        ```
    """


class HorizontalFastframeCount(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:FASTframe:COUNt`` command.

    Description:
        - This command sets or returns the number of frames.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe:COUNt?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:COUNt?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:COUNt value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe:COUNt <NR1>
        - HORizontal:FASTframe:COUNt?
        ```

    Info:
        - ``<NR1>`` is the number of frames.
    """


#  pylint: disable=too-many-instance-attributes
class HorizontalFastframe(SCPICmdRead):
    """The ``HORizontal:FASTframe`` command.

    Description:
        - This query returns all information under ``horizontal:fastframe``.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:FASTframe?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:FASTframe?
        ```

    Properties:
        - ``.count``: The ``HORizontal:FASTframe:COUNt`` command.
        - ``.maxframes``: The ``HORizontal:FASTframe:MAXFRames`` command.
        - ``.multipleframes``: The ``HORizontal:FASTframe:MULtipleframes`` command tree.
        - ``.ref``: The ``HORizontal:FASTframe:REF`` command tree.
        - ``.selected``: The ``HORizontal:FASTframe:SELECTED`` command.
        - ``.state``: The ``HORizontal:FASTframe:STATE`` command.
        - ``.sumframe``: The ``HORizontal:FASTframe:SUMFrame`` command.
        - ``.timestamp``: The ``HORizontal:FASTframe:TIMEStamp`` command tree.
        - ``.xzero``: The ``HORizontal:FASTframe:XZEro`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._count = HorizontalFastframeCount(device, f"{self._cmd_syntax}:COUNt")
        self._maxframes = HorizontalFastframeMaxframes(device, f"{self._cmd_syntax}:MAXFRames")
        self._multipleframes = HorizontalFastframeMultipleframes(
            device, f"{self._cmd_syntax}:MULtipleframes"
        )
        self._ref = HorizontalFastframeRef(device, f"{self._cmd_syntax}:REF")
        self._selected = HorizontalFastframeSelected(device, f"{self._cmd_syntax}:SELECTED")
        self._state = HorizontalFastframeState(device, f"{self._cmd_syntax}:STATE")
        self._sumframe = HorizontalFastframeSumframe(device, f"{self._cmd_syntax}:SUMFrame")
        self._timestamp = HorizontalFastframeTimestamp(device, f"{self._cmd_syntax}:TIMEStamp")
        self._xzero = HorizontalFastframeXzero(device, f"{self._cmd_syntax}:XZEro")

    @property
    def count(self) -> HorizontalFastframeCount:
        """Return the ``HORizontal:FASTframe:COUNt`` command.

        Description:
            - This command sets or returns the number of frames.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:COUNt?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:COUNt?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:COUNt value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:COUNt <NR1>
            - HORizontal:FASTframe:COUNt?
            ```

        Info:
            - ``<NR1>`` is the number of frames.
        """
        return self._count

    @property
    def maxframes(self) -> HorizontalFastframeMaxframes:
        """Return the ``HORizontal:FASTframe:MAXFRames`` command.

        Description:
            - This query returns the maximum number of frames.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:MAXFRames?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:MAXFRames?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:MAXFRames?
            ```
        """
        return self._maxframes

    @property
    def multipleframes(self) -> HorizontalFastframeMultipleframes:
        """Return the ``HORizontal:FASTframe:MULtipleframes`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:MULtipleframes?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:FASTframe:MULtipleframes?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``HORizontal:FASTframe:MULtipleframes:MODe`` command.
        """
        return self._multipleframes

    @property
    def ref(self) -> HorizontalFastframeRef:
        """Return the ``HORizontal:FASTframe:REF`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:REF?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:REF?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.frame``: The ``HORizontal:FASTframe:REF:FRAme`` command.
            - ``.include``: The ``HORizontal:FASTframe:REF:INCLUde`` command.
        """
        return self._ref

    @property
    def selected(self) -> HorizontalFastframeSelected:
        """Return the ``HORizontal:FASTframe:SELECTED`` command.

        Description:
            - This command sets or returns the selected frame number for acquired frames. Refs have
              their own selected frames.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:SELECTED?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:SELECTED?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:SELECTED value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:SELECTED <NR1>
            - HORizontal:FASTframe:SELECTED?
            ```

        Info:
            - ``<NR1>`` is the selected frame number for acquired frames.
        """
        return self._selected

    @property
    def state(self) -> HorizontalFastframeState:
        """Return the ``HORizontal:FASTframe:STATE`` command.

        Description:
            - This command sets or returns the state of FastFrame. Acquisition modes Envelope and
              Average are not compatible with FastFrame. If FastFrame is on, an attempted set to
              those acquisition modes will fail and revert to Sample mode. If FastFrame is turned on
              while in one of those acquisition modes, the acquisition mode is changed to Sample.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:STATE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:FASTframe:STATE value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:STATE {ON|OFF|<NR1>}
            - HORizontal:FASTframe:STATE?
            ```

        Info:
            - ``ON`` indicates FastFrame is active.
            - ``OFF`` indicates that FastFrame is off.
            - ``<NR1>`` A 0 turns off FastFrame; any other value activates FastFrame.
        """
        return self._state

    @property
    def sumframe(self) -> HorizontalFastframeSumframe:
        """Return the ``HORizontal:FASTframe:SUMFrame`` command.

        Description:
            - This command sets or returns the summary frame type. Turning on Summary Frame does not
              adjust the numberFrames value as long as there is room for an additional frame. If
              there is not enough room then numberFrames will be reduced by 1. The numberFrames
              value is always the number of frames to acquire.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``HORizontal:FASTframe:SUMFrame value`` command.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe:SUMFrame {NONe|AVErage|ENVelope}
            ```

        Info:
            - ``NONe`` sets the Summary frame to off.
            - ``AVErage`` sets the Summary frame to average of all acquired frames.
            - ``ENVelope`` sets the Summary frame to envelope of all acquired frames.

        Sub-properties:
            - ``.state``: The ``HORizontal:FASTframe:SUMFrame:STATE`` command.
        """
        return self._sumframe

    @property
    def timestamp(self) -> HorizontalFastframeTimestamp:
        """Return the ``HORizontal:FASTframe:TIMEStamp`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:TIMEStamp?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:TIMEStamp?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.all``: The ``HORizontal:FASTframe:TIMEStamp:ALL`` command.
            - ``.delta``: The ``HORizontal:FASTframe:TIMEStamp:DELTa`` command.
            - ``.reference``: The ``HORizontal:FASTframe:TIMEStamp:REFerence`` command.
            - ``.selected``: The ``HORizontal:FASTframe:TIMEStamp:SELECTED`` command.
        """
        return self._timestamp

    @property
    def xzero(self) -> HorizontalFastframeXzero:
        """Return the ``HORizontal:FASTframe:XZEro`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe:XZEro?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe:XZEro?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.all``: The ``HORizontal:FASTframe:XZEro:ALL`` command.
            - ``.ref``: The ``HORizontal:FASTframe:XZEro:REF`` command.
            - ``.selected``: The ``HORizontal:FASTframe:XZEro:SELECTED`` command.
        """
        return self._xzero


class HorizontalDivisions(SCPICmdRead):
    """The ``HORizontal:DIVisions`` command.

    Description:
        - This query-only command returns the number of graticule divisions.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIVisions?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIVisions?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIVisions?
        ```
    """


class HorizontalDelayTime(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:DELay:TIMe`` command.

    Description:
        - This command sets or queries the horizontal delay time that is used when delay mode is on.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DELay:TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DELay:TIMe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:DELay:TIMe value`` command.

    SCPI Syntax:
        ```
        - HORizontal:DELay:TIMe <NR3>
        - HORizontal:DELay:TIMe?
        ```

    Info:
        - ``NR3`` is the delay in seconds.
    """


class HorizontalDelayMode(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:DELay:MODe`` command.

    Description:
        - This command sets or queries the horizontal delay mode.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DELay:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DELay:MODe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:DELay:MODe value`` command.

    SCPI Syntax:
        ```
        - HORizontal:DELay:MODe {ON|OFF|<NR1>}
        - HORizontal:DELay:MODe?
        ```

    Info:
        - ``OFF`` sets the Horizontal Delay Mode to off. This causes the ``HORizontal:POSition``
          command to operate like the HORIZONTAL POSITION knob on the front panel.
        - ``ON`` sets the Horizontal Delay Mode to on. This causes the ``HORizontal:DELay:TIMe``
          command to operate like the HORIZONTAL POSITION knob on the front panel.
        - ``<NR1>`` = 0 sets the Horizontal Delay Mode to off; any other value sets this mode to on.
    """


class HorizontalDelay(SCPICmdRead):
    """The ``HORizontal:DELay`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DELay?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DELay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``HORizontal:DELay:MODe`` command.
        - ``.time``: The ``HORizontal:DELay:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = HorizontalDelayMode(device, f"{self._cmd_syntax}:MODe")
        self._time = HorizontalDelayTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def mode(self) -> HorizontalDelayMode:
        """Return the ``HORizontal:DELay:MODe`` command.

        Description:
            - This command sets or queries the horizontal delay mode.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DELay:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DELay:MODe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:DELay:MODe value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:DELay:MODe {ON|OFF|<NR1>}
            - HORizontal:DELay:MODe?
            ```

        Info:
            - ``OFF`` sets the Horizontal Delay Mode to off. This causes the ``HORizontal:POSition``
              command to operate like the HORIZONTAL POSITION knob on the front panel.
            - ``ON`` sets the Horizontal Delay Mode to on. This causes the ``HORizontal:DELay:TIMe``
              command to operate like the HORIZONTAL POSITION knob on the front panel.
            - ``<NR1>`` = 0 sets the Horizontal Delay Mode to off; any other value sets this mode to
              on.
        """
        return self._mode

    @property
    def time(self) -> HorizontalDelayTime:
        """Return the ``HORizontal:DELay:TIMe`` command.

        Description:
            - This command sets or queries the horizontal delay time that is used when delay mode is
              on.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DELay:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DELay:TIMe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:DELay:TIMe value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:DELay:TIMe <NR3>
            - HORizontal:DELay:TIMe?
            ```

        Info:
            - ``NR3`` is the delay in seconds.
        """
        return self._time


class HorizontalAcqduration(SCPICmdRead):
    """The ``HORizontal:ACQDURATION`` command.

    Description:
        - This query returns the timebase duration.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:ACQDURATION?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:ACQDURATION?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:ACQDURATION?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Horizontal(SCPICmdRead):
    """The ``HORizontal`` command.

    Description:
        - Queries the current horizontal settings.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal?
        ```

    Properties:
        - ``.acqduration``: The ``HORizontal:ACQDURATION`` command.
        - ``.delay``: The ``HORizontal:DELay`` command tree.
        - ``.divisions``: The ``HORizontal:DIVisions`` command.
        - ``.fastframe``: The ``HORizontal:FASTframe`` command.
        - ``.history``: The ``HORizontal:HISTory`` command tree.
        - ``.main``: The ``HORizontal:MAIn`` command tree.
        - ``.mode``: The ``HORizontal:MODe`` command.
        - ``.position``: The ``HORizontal:POSition`` command.
        - ``.previewstate``: The ``HORizontal:PREViewstate`` command.
        - ``.recordlength``: The ``HORizontal:RECOrdlength`` command.
        - ``.roll``: The ``HORizontal:ROLL`` command.
        - ``.samplerate``: The ``HORizontal:SAMPLERate`` command.
        - ``.scale``: The ``HORizontal:SCAle`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "HORizontal"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._acqduration = HorizontalAcqduration(device, f"{self._cmd_syntax}:ACQDURATION")
        self._delay = HorizontalDelay(device, f"{self._cmd_syntax}:DELay")
        self._divisions = HorizontalDivisions(device, f"{self._cmd_syntax}:DIVisions")
        self._fastframe = HorizontalFastframe(device, f"{self._cmd_syntax}:FASTframe")
        self._history = HorizontalHistory(device, f"{self._cmd_syntax}:HISTory")
        self._main = HorizontalMain(device, f"{self._cmd_syntax}:MAIn")
        self._mode = HorizontalMode(device, f"{self._cmd_syntax}:MODe")
        self._position = HorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._previewstate = HorizontalPreviewstate(device, f"{self._cmd_syntax}:PREViewstate")
        self._recordlength = HorizontalRecordlength(device, f"{self._cmd_syntax}:RECOrdlength")
        self._roll = HorizontalRoll(device, f"{self._cmd_syntax}:ROLL")
        self._samplerate = HorizontalSamplerate(device, f"{self._cmd_syntax}:SAMPLERate")
        self._scale = HorizontalScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def acqduration(self) -> HorizontalAcqduration:
        """Return the ``HORizontal:ACQDURATION`` command.

        Description:
            - This query returns the timebase duration.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:ACQDURATION?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:ACQDURATION?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:ACQDURATION?
            ```
        """
        return self._acqduration

    @property
    def delay(self) -> HorizontalDelay:
        """Return the ``HORizontal:DELay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DELay?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``HORizontal:DELay:MODe`` command.
            - ``.time``: The ``HORizontal:DELay:TIMe`` command.
        """
        return self._delay

    @property
    def divisions(self) -> HorizontalDivisions:
        """Return the ``HORizontal:DIVisions`` command.

        Description:
            - This query-only command returns the number of graticule divisions.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIVisions?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DIVisions?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIVisions?
            ```
        """
        return self._divisions

    @property
    def fastframe(self) -> HorizontalFastframe:
        """Return the ``HORizontal:FASTframe`` command.

        Description:
            - This query returns all information under ``horizontal:fastframe``.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:FASTframe?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:FASTframe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:FASTframe?
            ```

        Sub-properties:
            - ``.count``: The ``HORizontal:FASTframe:COUNt`` command.
            - ``.maxframes``: The ``HORizontal:FASTframe:MAXFRames`` command.
            - ``.multipleframes``: The ``HORizontal:FASTframe:MULtipleframes`` command tree.
            - ``.ref``: The ``HORizontal:FASTframe:REF`` command tree.
            - ``.selected``: The ``HORizontal:FASTframe:SELECTED`` command.
            - ``.state``: The ``HORizontal:FASTframe:STATE`` command.
            - ``.sumframe``: The ``HORizontal:FASTframe:SUMFrame`` command.
            - ``.timestamp``: The ``HORizontal:FASTframe:TIMEStamp`` command tree.
            - ``.xzero``: The ``HORizontal:FASTframe:XZEro`` command tree.
        """
        return self._fastframe

    @property
    def history(self) -> HorizontalHistory:
        """Return the ``HORizontal:HISTory`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:HISTory?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:HISTory?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.cstats``: The ``HORizontal:HISTory:CSTAts`` command.
            - ``.overlay``: The ``HORizontal:HISTory:OVERlay`` command.
            - ``.ref``: The ``HORizontal:HISTory:REF`` command tree.
            - ``.selected``: The ``HORizontal:HISTory:SELected`` command.
            - ``.state``: The ``HORizontal:HISTory:STATe`` command.
            - ``.timestamp``: The ``HORizontal:HISTory:TIMEStamp`` command tree.
        """
        return self._history

    @property
    def main(self) -> HorizontalMain:
        """Return the ``HORizontal:MAIn`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.interpratio``: The ``HORizontal:MAIn:INTERPRatio`` command.
        """
        return self._main

    @property
    def mode(self) -> HorizontalMode:
        """Return the ``HORizontal:MODe`` command.

        Description:
            - This command set or queries the horizontal operating mode.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODe?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MODe value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MODe {AUTO|MANual}
            - HORizontal:MODe?
            ```

        Info:
            - ``AUTO`` selects the automatic horizontal model. Auto mode automatically adjusts the
              sample rate and record length to provide a high acquisition rate in Fast Acq or signal
              fidelity in analysis. Record length is read only.
            - ``MANUAL`` selects the manual horizontal model. Manual mode lets you change the sample
              rate, horizontal scale, and record length. These values interact. For example, when
              you change record length then the horizontal scale also changes.

        Sub-properties:
            - ``.automatic``: The ``HORizontal:MODe:AUTOmatic`` command tree.
            - ``.manual``: The ``HORizontal:MODe:MANual`` command tree.
            - ``.recordlength``: The ``HORizontal:MODe:RECOrdlength`` command.
            - ``.samplerate``: The ``HORizontal:MODe:SAMPLERate`` command.
            - ``.scale``: The ``HORizontal:MODe:SCAle`` command.
        """
        return self._mode

    @property
    def position(self) -> HorizontalPosition:
        """Return the ``HORizontal:POSition`` command.

        Description:
            - This command sets or queries the horizontal position as a percent of screen width.
              When Horizontal Delay Mode is turned off, this command is equivalent to adjusting the
              HORIZONTAL POSITION knob on the front panel. When Horizontal Delay Mode is turned on,
              the horizontal position is forced to 50%.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:POSition?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:POSition value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:POSition <NR3>
            - HORizontal:POSition?
            ```

        Info:
            - ``<NR3>`` is from 0 to ≈100 and is the position of the trigger point on the screen (0
              = left edge, 100 = right edge).
        """
        return self._position

    @property
    def previewstate(self) -> HorizontalPreviewstate:
        """Return the ``HORizontal:PREViewstate`` command.

        Description:
            - This query returns the display system preview state.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:PREViewstate?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:PREViewstate?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:PREViewstate?
            ```
        """
        return self._previewstate

    @property
    def recordlength(self) -> HorizontalRecordlength:
        """Return the ``HORizontal:RECOrdlength`` command.

        Description:
            - This command sets or queries the horizontal record length. To change the record length
              the Horizontal Mode must be set to Manual.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:RECOrdlength?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:RECOrdlength?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:RECOrdlength value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:RECOrdlength <NR1>
            - HORizontal:RECOrdlength?
            ```

        Info:
            - ``<NR1>`` is the horizontal record length.
        """
        return self._recordlength

    @property
    def roll(self) -> HorizontalRoll:
        """Return the ``HORizontal:ROLL`` command.

        Description:
            - Queries the horizontal roll mode status.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:ROLL?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:ROLL?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:ROLL?
            ```
        """
        return self._roll

    @property
    def samplerate(self) -> HorizontalSamplerate:
        """Return the ``HORizontal:SAMPLERate`` command.

        Description:
            - This command sets or queries the horizontal sample rate.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:SAMPLERate?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:SAMPLERate?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:SAMPLERate value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:SAMPLERate <NR3>
            - HORizontal:SAMPLERate?
            ```

        Info:
            - ``<NR3>`` is the horizontal sample rate in samples per second.

        Sub-properties:
            - ``.analyzemode``: The ``HORizontal:SAMPLERate:ANALYZemode`` command tree.
        """
        return self._samplerate

    @property
    def scale(self) -> HorizontalScale:
        """Return the ``HORizontal:SCAle`` command.

        Description:
            - This command sets or queries the horizontal scale.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:SCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:SCAle value`` command.

        SCPI Syntax:
            ```
            - HORizontal:SCAle <NR3>
            - HORizontal:SCAle?
            ```

        Info:
            - ``<NR3>`` is the horizontal scale in time per division.
        """
        return self._scale
