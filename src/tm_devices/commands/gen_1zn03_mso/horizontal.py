"""The horizontal commands module.

These commands are used in the following models:
MSO2

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
    - HORizontal:MAIn:INTERPRatio?
    - HORizontal:MODE {AUTO|MANual}
    - HORizontal:MODE:MANual:CONFIGure {HORIZontalscale|RECORDLength}
    - HORizontal:MODE:MANual:CONFIGure?
    - HORizontal:MODE:RECOrdlength <NR1>
    - HORizontal:MODE:RECOrdlength?
    - HORizontal:MODE:SAMPLERate <NR1>
    - HORizontal:MODE:SAMPLERate?
    - HORizontal:MODE:SCAle <NR1>
    - HORizontal:MODE:SCAle?
    - HORizontal:MODE?
    - HORizontal:POSition <NR3>
    - HORizontal:POSition?
    - HORizontal:PREViewstate?
    - HORizontal:RECOrdlength <NR1>
    - HORizontal:RECOrdlength?
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
    """The ``HORizontal:MODE:SCAle`` command.

    Description:
        - This command sets or queries the horizontal scale.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODE:SCAle value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MODE:SCAle <NR1>
        - HORizontal:MODE:SCAle?
        ```

    Info:
        - ``<NR1>`` is the horizontal scale in seconds per division.
    """


class HorizontalModeSamplerate(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODE:SAMPLERate`` command.

    Description:
        - This command sets or queries the sample rate.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE:SAMPLERate?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:SAMPLERate?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODE:SAMPLERate value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:MODE:SAMPLERate <NR1>
        - HORizontal:MODE:SAMPLERate?
        ```

    Info:
        - ``<NR1>`` is the sample rate in samples per second.
    """


class HorizontalModeRecordlength(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODE:RECOrdlength`` command.

    Description:
        - This command sets or queries the record length.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE:RECOrdlength?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:RECOrdlength?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODE:RECOrdlength value``
          command.

    SCPI Syntax:
        ```
        - HORizontal:MODE:RECOrdlength <NR1>
        - HORizontal:MODE:RECOrdlength?
        ```

    Info:
        - ``<NR1>`` is the record length in samples. Manual mode lets you change the record length,
          while the record length is read only for Automatic mode.
    """


class HorizontalModeManualConfigure(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODE:MANual:CONFIGure`` command.

    Description:
        - Sets or queries which horizontal control (scale or record length) will primarily change
          when the sample rate is changed in Manual mode. If the selected control (scale or record
          length) reaches a limit then the unselected control (record length or scale) may also
          change.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE:MANual:CONFIGure?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:MANual:CONFIGure?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``HORizontal:MODE:MANual:CONFIGure value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MODE:MANual:CONFIGure {HORIZontalscale|RECORDLength}
        - HORizontal:MODE:MANual:CONFIGure?
        ```

    Info:
        - ``HORIZontalscale`` will change when sample rate is adjusted.
        - ``RECORDLength`` will change when sample rate is adjusted.
    """


class HorizontalModeManual(SCPICmdRead):
    """The ``HORizontal:MODE:MANual`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE:MANual?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:MANual?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.configure``: The ``HORizontal:MODE:MANual:CONFIGure`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._configure = HorizontalModeManualConfigure(device, f"{self._cmd_syntax}:CONFIGure")

    @property
    def configure(self) -> HorizontalModeManualConfigure:
        """Return the ``HORizontal:MODE:MANual:CONFIGure`` command.

        Description:
            - Sets or queries which horizontal control (scale or record length) will primarily
              change when the sample rate is changed in Manual mode. If the selected control (scale
              or record length) reaches a limit then the unselected control (record length or scale)
              may also change.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE:MANual:CONFIGure?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:MODE:MANual:CONFIGure?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:MODE:MANual:CONFIGure value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MODE:MANual:CONFIGure {HORIZontalscale|RECORDLength}
            - HORizontal:MODE:MANual:CONFIGure?
            ```

        Info:
            - ``HORIZontalscale`` will change when sample rate is adjusted.
            - ``RECORDLength`` will change when sample rate is adjusted.
        """
        return self._configure


class HorizontalMode(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:MODE`` command.

    Description:
        - This command set or queries the horizontal operating mode.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MODE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:MODE value`` command.

    SCPI Syntax:
        ```
        - HORizontal:MODE {AUTO|MANual}
        - HORizontal:MODE?
        ```

    Info:
        - ``AUTO`` selects the automatic horizontal model. Auto mode automatically adjusts the
          sample rate and record length to provide a high acquisition rate in Fast Acq or signal
          fidelity in analysis. Record length is read only.
        - ``MANUAL`` selects the manual horizontal model. Manual mode lets you change the sample
          rate, horizontal scale, and record length. These values interact. For example, when you
          change record length then the horizontal scale also changes.

    Properties:
        - ``.manual``: The ``HORizontal:MODE:MANual`` command tree.
        - ``.recordlength``: The ``HORizontal:MODE:RECOrdlength`` command.
        - ``.samplerate``: The ``HORizontal:MODE:SAMPLERate`` command.
        - ``.scale``: The ``HORizontal:MODE:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._manual = HorizontalModeManual(device, f"{self._cmd_syntax}:MANual")
        self._recordlength = HorizontalModeRecordlength(device, f"{self._cmd_syntax}:RECOrdlength")
        self._samplerate = HorizontalModeSamplerate(device, f"{self._cmd_syntax}:SAMPLERate")
        self._scale = HorizontalModeScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def manual(self) -> HorizontalModeManual:
        """Return the ``HORizontal:MODE:MANual`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE:MANual?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:MANual?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.configure``: The ``HORizontal:MODE:MANual:CONFIGure`` command.
        """
        return self._manual

    @property
    def recordlength(self) -> HorizontalModeRecordlength:
        """Return the ``HORizontal:MODE:RECOrdlength`` command.

        Description:
            - This command sets or queries the record length.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE:RECOrdlength?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:RECOrdlength?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``HORizontal:MODE:RECOrdlength value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MODE:RECOrdlength <NR1>
            - HORizontal:MODE:RECOrdlength?
            ```

        Info:
            - ``<NR1>`` is the record length in samples. Manual mode lets you change the record
              length, while the record length is read only for Automatic mode.
        """
        return self._recordlength

    @property
    def samplerate(self) -> HorizontalModeSamplerate:
        """Return the ``HORizontal:MODE:SAMPLERate`` command.

        Description:
            - This command sets or queries the sample rate.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE:SAMPLERate?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:SAMPLERate?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MODE:SAMPLERate value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:MODE:SAMPLERate <NR1>
            - HORizontal:MODE:SAMPLERate?
            ```

        Info:
            - ``<NR1>`` is the sample rate in samples per second.
        """
        return self._samplerate

    @property
    def scale(self) -> HorizontalModeScale:
        """Return the ``HORizontal:MODE:SCAle`` command.

        Description:
            - This command sets or queries the horizontal scale.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODE:SCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MODE:SCAle value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:MODE:SCAle <NR1>
            - HORizontal:MODE:SCAle?
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
        - ``.main``: The ``HORizontal:MAIn`` command tree.
        - ``.mode``: The ``HORizontal:MODE`` command.
        - ``.position``: The ``HORizontal:POSition`` command.
        - ``.previewstate``: The ``HORizontal:PREViewstate`` command.
        - ``.recordlength``: The ``HORizontal:RECOrdlength`` command.
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
        self._main = HorizontalMain(device, f"{self._cmd_syntax}:MAIn")
        self._mode = HorizontalMode(device, f"{self._cmd_syntax}:MODE")
        self._position = HorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._previewstate = HorizontalPreviewstate(device, f"{self._cmd_syntax}:PREViewstate")
        self._recordlength = HorizontalRecordlength(device, f"{self._cmd_syntax}:RECOrdlength")
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
        """Return the ``HORizontal:MODE`` command.

        Description:
            - This command set or queries the horizontal operating mode.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MODE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:MODE value`` command.

        SCPI Syntax:
            ```
            - HORizontal:MODE {AUTO|MANual}
            - HORizontal:MODE?
            ```

        Info:
            - ``AUTO`` selects the automatic horizontal model. Auto mode automatically adjusts the
              sample rate and record length to provide a high acquisition rate in Fast Acq or signal
              fidelity in analysis. Record length is read only.
            - ``MANUAL`` selects the manual horizontal model. Manual mode lets you change the sample
              rate, horizontal scale, and record length. These values interact. For example, when
              you change record length then the horizontal scale also changes.

        Sub-properties:
            - ``.manual``: The ``HORizontal:MODE:MANual`` command tree.
            - ``.recordlength``: The ``HORizontal:MODE:RECOrdlength`` command.
            - ``.samplerate``: The ``HORizontal:MODE:SAMPLERate`` command.
            - ``.scale``: The ``HORizontal:MODE:SCAle`` command.
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
