"""The horizontal commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HORizontal:DELay:MODe {ON|OFF|<NR1>}
    - HORizontal:DELay:MODe?
    - HORizontal:DELay:TIMe <NR3>
    - HORizontal:DELay:TIMe?
    - HORizontal:DIGital:RECOrdlength:MAGnivu?
    - HORizontal:DIGital:RECOrdlength:MAIn?
    - HORizontal:DIGital:SAMPLERate:MAGnivu?
    - HORizontal:DIGital:SAMPLERate:MAIn?
    - HORizontal:POSition <NR3>
    - HORizontal:POSition?
    - HORizontal:PREViewstate?
    - HORizontal:RECOrdlength <NR1>
    - HORizontal:RECOrdlength?
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


class HorizontalDigitalSamplerateMain(SCPICmdRead):
    """The ``HORizontal:DIGital:SAMPLERate:MAIn`` command.

    Description:
        - Returns the sample rate of the main digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate:MAIn?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal:DIGital:SAMPLERate:MAIn?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:SAMPLERate:MAIn?
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
        - ``.main``: The ``HORizontal:DIGital:SAMPLERate:MAIn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._magnivu = HorizontalDigitalSamplerateMagnivu(device, f"{self._cmd_syntax}:MAGnivu")
        self._main = HorizontalDigitalSamplerateMain(device, f"{self._cmd_syntax}:MAIn")

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
        """Return the ``HORizontal:DIGital:SAMPLERate:MAIn`` command.

        Description:
            - Returns the sample rate of the main digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:SAMPLERate:MAIn?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:DIGital:SAMPLERate:MAIn?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:SAMPLERate:MAIn?
            ```
        """
        return self._main


class HorizontalDigitalRecordlengthMain(SCPICmdRead):
    """The ``HORizontal:DIGital:RECOrdlength:MAIn`` command.

    Description:
        - Returns the record length of the main digital acquisition.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength:MAIn?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``HORizontal:DIGital:RECOrdlength:MAIn?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - HORizontal:DIGital:RECOrdlength:MAIn?
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
        - ``.main``: The ``HORizontal:DIGital:RECOrdlength:MAIn`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._magnivu = HorizontalDigitalRecordlengthMagnivu(device, f"{self._cmd_syntax}:MAGnivu")
        self._main = HorizontalDigitalRecordlengthMain(device, f"{self._cmd_syntax}:MAIn")

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
        """Return the ``HORizontal:DIGital:RECOrdlength:MAIn`` command.

        Description:
            - Returns the record length of the main digital acquisition.

        Usage:
            - Using the ``.query()`` method will send the ``HORizontal:DIGital:RECOrdlength:MAIn?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``HORizontal:DIGital:RECOrdlength:MAIn?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - HORizontal:DIGital:RECOrdlength:MAIn?
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
            - ``.main``: The ``HORizontal:DIGital:RECOrdlength:MAIn`` command.
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
            - ``.main``: The ``HORizontal:DIGital:SAMPLERate:MAIn`` command.
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
        - ``.delay``: The ``HORizontal:DELay`` command tree.
        - ``.digital``: The ``HORizontal:DIGital`` command tree.
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
        self._delay = HorizontalDelay(device, f"{self._cmd_syntax}:DELay")
        self._digital = HorizontalDigital(device, f"{self._cmd_syntax}:DIGital")
        self._position = HorizontalPosition(device, f"{self._cmd_syntax}:POSition")
        self._previewstate = HorizontalPreviewstate(device, f"{self._cmd_syntax}:PREViewstate")
        self._recordlength = HorizontalRecordlength(device, f"{self._cmd_syntax}:RECOrdlength")
        self._samplerate = HorizontalSamplerate(device, f"{self._cmd_syntax}:SAMPLERate")
        self._scale = HorizontalScale(device, f"{self._cmd_syntax}:SCAle")

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
