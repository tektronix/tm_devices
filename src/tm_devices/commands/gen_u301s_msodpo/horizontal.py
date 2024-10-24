"""The horizontal commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HORizontal:ACQLENGTH?
    - HORizontal:DELay:MODe {ON|OFF|<NR1>}
    - HORizontal:DELay:MODe?
    - HORizontal:DELay:POSition
    - HORizontal:DELay:POSition?
    - HORizontal:DELay:TIMe <NR3>
    - HORizontal:DELay:TIMe?
    - HORizontal:DIGital:RECOrdlength:MAGnivu?
    - HORizontal:DIGital:RECOrdlength:MAIN?
    - HORizontal:DIGital:SAMPLERate:MAGnivu?
    - HORizontal:DIGital:SAMPLERate:MAIN?
    - HORizontal:MAIn:SAMPLERate
    - HORizontal:MAIn:SCAle
    - HORizontal:MAIn:SCAle?
    - HORizontal:MAIn:UNIts:STRing?
    - HORizontal:MAIn:UNIts?
    - HORizontal:MAIn?
    - HORizontal:POSition <NR3>
    - HORizontal:POSition?
    - HORizontal:PREViewstate?
    - HORizontal:RECOrdlength <NR1>
    - HORizontal:RECOrdlength?
    - HORizontal:RESOlution <NR1>
    - HORizontal:RESOlution?
    - HORizontal:SAMPLERate?
    - HORizontal:SCAle <NR3>
    - HORizontal:SCAle?
    - HORizontal:TRIGger:POSition
    - HORizontal:TRIGger:POSition?
    - HORizontal?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class HorizontalTriggerPosition(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``HORizontal:TRIGger:POSition`` command.

    Description:
        - Sets the horizontal position when delay mode is OFF. It is similar to
          ``HORIZONTAL:POSITION``.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:TRIGger:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:TRIGger:POSition?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``HORizontal:TRIGger:POSition`` command.

    SCPI Syntax:
        ```
        - HORizontal:TRIGger:POSition
        - HORizontal:TRIGger:POSition?
        ```
    """


class HorizontalTrigger(SCPICmdRead):
    """The ``HORizontal:TRIGger`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:TRIGger?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:TRIGger?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.position``: The ``HORizontal:TRIGger:POSition`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._position = HorizontalTriggerPosition(device, f"{self._cmd_syntax}:POSition")

    @property
    def position(self) -> HorizontalTriggerPosition:
        """Return the ``HORizontal:TRIGger:POSition`` command.

        Description:
            - Sets the horizontal position when delay mode is OFF. It is similar to
              ``HORIZONTAL:POSITION``.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:TRIGger:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:TRIGger:POSition?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``HORizontal:TRIGger:POSition`` command.

        SCPI Syntax:
            ```
            - HORizontal:TRIGger:POSition
            - HORizontal:TRIGger:POSition?
            ```
        """
        return self._position


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


class HorizontalSamplerate(SCPICmdRead):
    """The ``HORizontal:SAMPLERate`` command.

    Description:
        - The command form is ignored. The query returns the sample rate for analog channels in
          samples per second.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:SAMPLERate?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:SAMPLERate?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:SAMPLERate?
        ```
    """


class HorizontalResolution(SCPICmdWrite, SCPICmdRead):
    """The ``HORizontal:RESOlution`` command.

    Description:
        - Sets or returns the horizontal record length of acquired waveforms. The sample rate is
          automatically adjusted at the same time to maintain a constant time per division. The
          query form of this command returns the current horizontal record length.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:RESOlution?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:RESOlution?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HORizontal:RESOlution value`` command.

    SCPI Syntax:
        ```
        - HORizontal:RESOlution <NR1>
        - HORizontal:RESOlution?
        ```

    Info:
        - ``<NR1>`` represents the supported values for horizontal record lengths.
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


class HorizontalMainUnitsString(SCPICmdRead):
    """The ``HORizontal:MAIn:UNIts:STRing`` command.

    Description:
        - Returns the units string for the horizontal time base.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:UNIts:STRing?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:UNIts:STRing?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:UNIts:STRing?
        ```
    """


class HorizontalMainUnits(SCPICmdRead):
    """The ``HORizontal:MAIn:UNIts`` command.

    Description:
        - Returns the units string for the horizontal time base.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:UNIts?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:UNIts?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:UNIts?
        ```

    Properties:
        - ``.string``: The ``HORizontal:MAIn:UNIts:STRing`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._string = HorizontalMainUnitsString(device, f"{self._cmd_syntax}:STRing")

    @property
    def string(self) -> HorizontalMainUnitsString:
        """Return the ``HORizontal:MAIn:UNIts:STRing`` command.

        Description:
            - Returns the units string for the horizontal time base.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:UNIts:STRing?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:UNIts:STRing?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:UNIts:STRing?
            ```
        """
        return self._string


class HorizontalMainScale(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``HORizontal:MAIn:SCAle`` command.

    Description:
        - Sets or returns the main horizontal scale. The specified scale value is rounded to a valid
          scale setting.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn:SCAle?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:SCAle?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``HORizontal:MAIn:SCAle`` command.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:SCAle
        - HORizontal:MAIn:SCAle?
        ```

    Info:
        - ``<NR3>`` is the time per division. The range is from 400 ps (1 ns) through 1000 s,
          depending on the record length.
    """


class HorizontalMainSamplerate(SCPICmdWriteNoArguments):
    """The ``HORizontal:MAIn:SAMPLERate`` command.

    Description:
        - Sets or returns the current horizontal sample rate.

    Usage:
        - Using the ``.write()`` method will send the ``HORizontal:MAIn:SAMPLERate`` command.

    SCPI Syntax:
        ```
        - HORizontal:MAIn:SAMPLERate
        ```

    Info:
        - ``<NR3>`` specifies the sample rate in seconds.
    """


class HorizontalMain(SCPICmdRead):
    """The ``HORizontal:MAIn`` command.

    Description:
        - This query-only command returns the time per division of the time base. This command is
          equivalent to selecting Position/Scale from the Horiz/Acq menu.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:MAIn?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:MAIn?
        ```

    Properties:
        - ``.samplerate``: The ``HORizontal:MAIn:SAMPLERate`` command.
        - ``.units``: The ``HORizontal:MAIn:UNIts`` command.
        - ``.scale``: The ``HORizontal:MAIn:SCAle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._samplerate = HorizontalMainSamplerate(device, f"{self._cmd_syntax}:SAMPLERate")
        self._units = HorizontalMainUnits(device, f"{self._cmd_syntax}:UNIts")
        self._scale = HorizontalMainScale(device, f"{self._cmd_syntax}:SCAle")

    @property
    def samplerate(self) -> HorizontalMainSamplerate:
        """Return the ``HORizontal:MAIn:SAMPLERate`` command.

        Description:
            - Sets or returns the current horizontal sample rate.

        Usage:
            - Using the ``.write()`` method will send the ``HORizontal:MAIn:SAMPLERate`` command.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:SAMPLERate
            ```

        Info:
            - ``<NR3>`` specifies the sample rate in seconds.
        """
        return self._samplerate

    @property
    def units(self) -> HorizontalMainUnits:
        """Return the ``HORizontal:MAIn:UNIts`` command.

        Description:
            - Returns the units string for the horizontal time base.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:UNIts?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:UNIts?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:UNIts?
            ```

        Sub-properties:
            - ``.string``: The ``HORizontal:MAIn:UNIts:STRing`` command.
        """
        return self._units

    @property
    def scale(self) -> HorizontalMainScale:
        """Return the ``HORizontal:MAIn:SCAle`` command.

        Description:
            - Sets or returns the main horizontal scale. The specified scale value is rounded to a
              valid scale setting.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn:SCAle?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn:SCAle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``HORizontal:MAIn:SCAle`` command.

        SCPI Syntax:
            ```
            - HORizontal:MAIn:SCAle
            - HORizontal:MAIn:SCAle?
            ```

        Info:
            - ``<NR3>`` is the time per division. The range is from 400 ps (1 ns) through 1000 s,
              depending on the record length.
        """
        return self._scale


class HorizontalDigitalSamplerateMain(SCPICmdRead):
    """The ``HORizontal:DIGital:SAMPLERate:MAIN`` command.

    Description:
        - Returns the sample rate of the main digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate:MAIN?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:SAMPLERate:MAIN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:SAMPLERate:MAIN?
        ```
    """


class HorizontalDigitalSamplerateMagnivu(SCPICmdRead):
    """The ``HORizontal:DIGital:SAMPLERate:MAGnivu`` command.

    Description:
        - Returns the sample rate of the MagniVu digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate:MAGnivu?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:DIGital:SAMPLERate:MAGnivu?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:SAMPLERate:MAGnivu?
        ```
    """


class HorizontalDigitalSamplerate(SCPICmdRead):
    """The ``HORizontal:DIGital:SAMPLERate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:SAMPLERate?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.magnivu``: The ``HORizontal:DIGital:SAMPLERate:MAGnivu`` command.
        - ``.main``: The ``HORizontal:DIGital:SAMPLERate:MAIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._magnivu = HorizontalDigitalSamplerateMagnivu(device, f"{self._cmd_syntax}:MAGnivu")
        self._main = HorizontalDigitalSamplerateMain(device, f"{self._cmd_syntax}:MAIN")

    @property
    def magnivu(self) -> HorizontalDigitalSamplerateMagnivu:
        """Return the ``HORizontal:DIGital:SAMPLERate:MAGnivu`` command.

        Description:
            - Returns the sample rate of the MagniVu digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate:MAGnivu?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:DIGital:SAMPLERate:MAGnivu?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:SAMPLERate:MAGnivu?
            ```
        """
        return self._magnivu

    @property
    def main(self) -> HorizontalDigitalSamplerateMain:
        """Return the ``HORizontal:DIGital:SAMPLERate:MAIN`` command.

        Description:
            - Returns the sample rate of the main digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate:MAIN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:DIGital:SAMPLERate:MAIN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:SAMPLERate:MAIN?
            ```
        """
        return self._main


class HorizontalDigitalRecordlengthMain(SCPICmdRead):
    """The ``HORizontal:DIGital:RECOrdlength:MAIN`` command.

    Description:
        - Returns the record length of the main digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength:MAIN?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:DIGital:RECOrdlength:MAIN?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:RECOrdlength:MAIN?
        ```
    """


class HorizontalDigitalRecordlengthMagnivu(SCPICmdRead):
    """The ``HORizontal:DIGital:RECOrdlength:MAGnivu`` command.

    Description:
        - Returns the record length of the MagniVu digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength:MAGnivu?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:DIGital:RECOrdlength:MAGnivu?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:RECOrdlength:MAGnivu?
        ```
    """


class HorizontalDigitalRecordlength(SCPICmdRead):
    """The ``HORizontal:DIGital:RECOrdlength`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:RECOrdlength?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.magnivu``: The ``HORizontal:DIGital:RECOrdlength:MAGnivu`` command.
        - ``.main``: The ``HORizontal:DIGital:RECOrdlength:MAIN`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._magnivu = HorizontalDigitalRecordlengthMagnivu(device, f"{self._cmd_syntax}:MAGnivu")
        self._main = HorizontalDigitalRecordlengthMain(device, f"{self._cmd_syntax}:MAIN")

    @property
    def magnivu(self) -> HorizontalDigitalRecordlengthMagnivu:
        """Return the ``HORizontal:DIGital:RECOrdlength:MAGnivu`` command.

        Description:
            - Returns the record length of the MagniVu digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the
              ``HORizontal:DIGital:RECOrdlength:MAGnivu?`` query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:DIGital:RECOrdlength:MAGnivu?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:RECOrdlength:MAGnivu?
            ```
        """
        return self._magnivu

    @property
    def main(self) -> HorizontalDigitalRecordlengthMain:
        """Return the ``HORizontal:DIGital:RECOrdlength:MAIN`` command.

        Description:
            - Returns the record length of the main digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength:MAIN?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:DIGital:RECOrdlength:MAIN?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:RECOrdlength:MAIN?
            ```
        """
        return self._main


class HorizontalDigital(SCPICmdRead):
    """The ``HORizontal:DIGital`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.recordlength``: The ``HORizontal:DIGital:RECOrdlength`` command tree.
        - ``.samplerate``: The ``HORizontal:DIGital:SAMPLERate`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._recordlength = HorizontalDigitalRecordlength(
            device, f"{self._cmd_syntax}:RECOrdlength"
        )
        self._samplerate = HorizontalDigitalSamplerate(device, f"{self._cmd_syntax}:SAMPLERate")

    @property
    def recordlength(self) -> HorizontalDigitalRecordlength:
        """Return the ``HORizontal:DIGital:RECOrdlength`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength?``
              query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:RECOrdlength?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.magnivu``: The ``HORizontal:DIGital:RECOrdlength:MAGnivu`` command.
            - ``.main``: The ``HORizontal:DIGital:RECOrdlength:MAIN`` command.
        """
        return self._recordlength

    @property
    def samplerate(self) -> HorizontalDigitalSamplerate:
        """Return the ``HORizontal:DIGital:SAMPLERate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:SAMPLERate?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.magnivu``: The ``HORizontal:DIGital:SAMPLERate:MAGnivu`` command.
            - ``.main``: The ``HORizontal:DIGital:SAMPLERate:MAIN`` command.
        """
        return self._samplerate


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


class HorizontalDelayPosition(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``HORizontal:DELay:POSition`` command.

    Description:
        - Sets or returns the horizontal position.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DELay:POSition?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DELay:POSition?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``HORizontal:DELay:POSition`` command.

    SCPI Syntax:
        ```
        - HORizontal:DELay:POSition
        - HORizontal:DELay:POSition?
        ```
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
        - ``.position``: The ``HORizontal:DELay:POSition`` command.
        - ``.time``: The ``HORizontal:DELay:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = HorizontalDelayMode(device, f"{self._cmd_syntax}:MODe")
        self._position = HorizontalDelayPosition(device, f"{self._cmd_syntax}:POSition")
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
    def position(self) -> HorizontalDelayPosition:
        """Return the ``HORizontal:DELay:POSition`` command.

        Description:
            - Sets or returns the horizontal position.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DELay:POSition?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DELay:POSition?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``HORizontal:DELay:POSition`` command.

        SCPI Syntax:
            ```
            - HORizontal:DELay:POSition
            - HORizontal:DELay:POSition?
            ```
        """
        return self._position

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


class HorizontalAcqlength(SCPICmdRead):
    """The ``HORizontal:ACQLENGTH`` command.

    Description:
        - This query returns the record length.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:ACQLENGTH?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:ACQLENGTH?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:ACQLENGTH?
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
        - ``.acqlength``: The ``HORizontal:ACQLENGTH`` command.
        - ``.delay``: The ``HORizontal:DELay`` command tree.
        - ``.digital``: The ``HORizontal:DIGital`` command tree.
        - ``.main``: The ``HORizontal:MAIn`` command.
        - ``.position``: The ``HORizontal:POSition`` command.
        - ``.previewstate``: The ``HORizontal:PREViewstate`` command.
        - ``.recordlength``: The ``HORizontal:RECOrdlength`` command.
        - ``.resolution``: The ``HORizontal:RESOlution`` command.
        - ``.samplerate``: The ``HORizontal:SAMPLERate`` command.
        - ``.scale``: The ``HORizontal:SCAle`` command.
        - ``.trigger``: The ``HORizontal:TRIGger`` command tree.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "HORizontal"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._acqlength = HorizontalAcqlength(device, f"{self._cmd_syntax}:ACQLENGTH")
        self._delay = HorizontalDelay(device, f"{self._cmd_syntax}:DELay")
        self._digital = HorizontalDigital(device, f"{self._cmd_syntax}:DIGital")
        self._position = HorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._previewstate = HorizontalPreviewstate(device, f"{self._cmd_syntax}:PREViewstate")
        self._recordlength = HorizontalRecordlength(device, f"{self._cmd_syntax}:RECOrdlength")
        self._resolution = HorizontalResolution(device, f"{self._cmd_syntax}:RESOlution")
        self._samplerate = HorizontalSamplerate(device, f"{self._cmd_syntax}:SAMPLERate")
        self._scale = HorizontalScale(device, f"{self._cmd_syntax}:SCAle")
        self._trigger = HorizontalTrigger(device, f"{self._cmd_syntax}:TRIGger")
        self._main = HorizontalMain(device, f"{self._cmd_syntax}:MAIn")

    @property
    def acqlength(self) -> HorizontalAcqlength:
        """Return the ``HORizontal:ACQLENGTH`` command.

        Description:
            - This query returns the record length.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:ACQLENGTH?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:ACQLENGTH?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:ACQLENGTH?
            ```
        """
        return self._acqlength

    @property
    def delay(self) -> HorizontalDelay:
        """Return the ``HORizontal:DELay`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DELay?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DELay?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``HORizontal:DELay:MODe`` command.
            - ``.position``: The ``HORizontal:DELay:POSition`` command.
            - ``.time``: The ``HORizontal:DELay:TIMe`` command.
        """
        return self._delay

    @property
    def digital(self) -> HorizontalDigital:
        """Return the ``HORizontal:DIGital`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.recordlength``: The ``HORizontal:DIGital:RECOrdlength`` command tree.
            - ``.samplerate``: The ``HORizontal:DIGital:SAMPLERate`` command tree.
        """
        return self._digital

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
    def resolution(self) -> HorizontalResolution:
        """Return the ``HORizontal:RESOlution`` command.

        Description:
            - Sets or returns the horizontal record length of acquired waveforms. The sample rate is
              automatically adjusted at the same time to maintain a constant time per division. The
              query form of this command returns the current horizontal record length.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:RESOlution?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:RESOlution?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``HORizontal:RESOlution value``
              command.

        SCPI Syntax:
            ```
            - HORizontal:RESOlution <NR1>
            - HORizontal:RESOlution?
            ```

        Info:
            - ``<NR1>`` represents the supported values for horizontal record lengths.
        """
        return self._resolution

    @property
    def samplerate(self) -> HorizontalSamplerate:
        """Return the ``HORizontal:SAMPLERate`` command.

        Description:
            - The command form is ignored. The query returns the sample rate for analog channels in
              samples per second.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:SAMPLERate?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:SAMPLERate?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:SAMPLERate?
            ```
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

    @property
    def trigger(self) -> HorizontalTrigger:
        """Return the ``HORizontal:TRIGger`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:TRIGger?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:TRIGger?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.position``: The ``HORizontal:TRIGger:POSition`` command.
        """
        return self._trigger

    @property
    def main(self) -> HorizontalMain:
        """Return the ``HORizontal:MAIn`` command.

        Description:
            - This query-only command returns the time per division of the time base. This command
              is equivalent to selecting Position/Scale from the Horiz/Acq menu.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:MAIn?`` query.
            - Using the ``.verify(value)`` method will send the ``HORizontal:MAIn?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:MAIn?
            ```

        Sub-properties:
            - ``.samplerate``: The ``HORizontal:MAIn:SAMPLERate`` command.
            - ``.units``: The ``HORizontal:MAIn:UNIts`` command.
            - ``.scale``: The ``HORizontal:MAIn:SCAle`` command.
        """
        return self._main
