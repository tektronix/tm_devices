"""The display commands module.

These commands are used in the following models:
MDO3

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DISplay:CLOCk {ON|OFF|<NR1>}
    - DISplay:CLOCk?
    - DISplay:COLor:MODe {NORMal|INVERTed}
    - DISplay:COLor:MODe?
    - DISplay:CONFIGure:READOut {NORMal ! TRANSParent}
    - DISplay:CONFIGure:READOut?
    - DISplay:DIGital:ACTIVity {0|1|OFF|ON}
    - DISplay:DIGital:ACTIVity?
    - DISplay:DIGital:HEIght {SMAll|MEDium|LARge}
    - DISplay:DIGital:HEIght?
    - DISplay:GRAticule {CROSSHair|FRAme|FULl|GRId|SOLid}
    - DISplay:GRAticule?
    - DISplay:INTENSITy:BACKLight {LOW|MEDium|HIGH}
    - DISplay:INTENSITy:BACKLight:AUTODim:ENAble {OFF|ON|0|1}
    - DISplay:INTENSITy:BACKLight:AUTODim:ENAble?
    - DISplay:INTENSITy:BACKLight:AUTODim:TIMe <NR1>
    - DISplay:INTENSITy:BACKLight:AUTODim:TIMe?
    - DISplay:INTENSITy:BACKLight?
    - DISplay:INTENSITy:GRAticule <NR1>
    - DISplay:INTENSITy:GRAticule?
    - DISplay:INTENSITy:WAVEform <NR1>
    - DISplay:INTENSITy:WAVEform?
    - DISplay:INTENSITy?
    - DISplay:PERSistence {<NR3>|CLEAR|AUTO|INFInite|OFF}
    - DISplay:PERSistence?
    - DISplay:STYle:DOTsonly {ON|OFF|<NR1>}
    - DISplay:STYle:DOTsonly?
    - DISplay:TRIGFrequency {OFF|ON|0|1}
    - DISplay:TRIGFrequency?
    - DISplay:XY {OFF|TRIGgered}
    - DISplay:XY:WITHYT {0|1|OFF|ON}
    - DISplay:XY:WITHYT?
    - DISplay:XY?
    - DISplay?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DisplayXyWithyt(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:XY:WITHYT`` command.

    Description:
        - Sets or returns the state of simultaneous display of the XY and YT waveforms when in
          TRIGgered XY display mode. (To set the mode to TRIGgered XY display, first use the command
          ``:DISplay:XY TRIGgered``.) When both the XY and YT waveforms are displayed, the YT
          waveform is displayed in the upper graticule, and the XY waveform is displayed in the
          lower graticule. For this platform, the default state is 0 (XY display only).

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:XY:WITHYT?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:XY:WITHYT?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:XY:WITHYT value`` command.

    SCPI Syntax:
        ```
        - DISplay:XY:WITHYT {0|1|OFF|ON}
        - DISplay:XY:WITHYT?
        ```

    Info:
        - ``1`` or ON turns on simultaneous display of the XY and YT waveforms when in TRIGgered XY
          display mode.
        - ``0`` or OFF turns simultaneous display off.
    """


class DisplayXy(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:XY`` command.

    Description:
        - This command turns on or off the XY display mode.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:XY?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:XY?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:XY value`` command.

    SCPI Syntax:
        ```
        - DISplay:XY {OFF|TRIGgered}
        - DISplay:XY?
        ```

    Info:
        - ``OFF`` - The channels are displayed individually as a function of time.
        - ``TRIGgered`` - The channels are displayed in 'X-Y' pairs with CH1 being displayed as a
          function of CH2, and so on.

    Properties:
        - ``.withyt``: The ``DISplay:XY:WITHYT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._withyt = DisplayXyWithyt(device, f"{self._cmd_syntax}:WITHYT")

    @property
    def withyt(self) -> DisplayXyWithyt:
        """Return the ``DISplay:XY:WITHYT`` command.

        Description:
            - Sets or returns the state of simultaneous display of the XY and YT waveforms when in
              TRIGgered XY display mode. (To set the mode to TRIGgered XY display, first use the
              command ``:DISplay:XY TRIGgered``.) When both the XY and YT waveforms are displayed,
              the YT waveform is displayed in the upper graticule, and the XY waveform is displayed
              in the lower graticule. For this platform, the default state is 0 (XY display only).

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:XY:WITHYT?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:XY:WITHYT?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:XY:WITHYT value`` command.

        SCPI Syntax:
            ```
            - DISplay:XY:WITHYT {0|1|OFF|ON}
            - DISplay:XY:WITHYT?
            ```

        Info:
            - ``1`` or ON turns on simultaneous display of the XY and YT waveforms when in TRIGgered
              XY display mode.
            - ``0`` or OFF turns simultaneous display off.
        """
        return self._withyt


class DisplayTrigfrequency(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:TRIGFrequency`` command.

    Description:
        - This command switches the trigger frequency readout on or off.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:TRIGFrequency?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:TRIGFrequency?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:TRIGFrequency value`` command.

    SCPI Syntax:
        ```
        - DISplay:TRIGFrequency {OFF|ON|0|1}
        - DISplay:TRIGFrequency?
        ```
    """


class DisplayStyleDotsonly(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:STYle:DOTsonly`` command.

    Description:
        - This command turns on or off the dots-only mode for the waveforms displayed in the time
          domain.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:STYle:DOTsonly?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:STYle:DOTsonly?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:STYle:DOTsonly value`` command.

    SCPI Syntax:
        ```
        - DISplay:STYle:DOTsonly {ON|OFF|<NR1>}
        - DISplay:STYle:DOTsonly?
        ```

    Info:
        - ``ON`` or <NR1> ≠ 0 turns on the dots-only display.
        - ``OFF`` or <NR1> = 0 turns off the dots-only display.
    """


class DisplayStyle(SCPICmdRead):
    """The ``DISplay:STYle`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:STYle?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:STYle?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dotsonly``: The ``DISplay:STYle:DOTsonly`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dotsonly = DisplayStyleDotsonly(device, f"{self._cmd_syntax}:DOTsonly")

    @property
    def dotsonly(self) -> DisplayStyleDotsonly:
        """Return the ``DISplay:STYle:DOTsonly`` command.

        Description:
            - This command turns on or off the dots-only mode for the waveforms displayed in the
              time domain.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:STYle:DOTsonly?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:STYle:DOTsonly?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:STYle:DOTsonly value``
              command.

        SCPI Syntax:
            ```
            - DISplay:STYle:DOTsonly {ON|OFF|<NR1>}
            - DISplay:STYle:DOTsonly?
            ```

        Info:
            - ``ON`` or <NR1> ≠ 0 turns on the dots-only display.
            - ``OFF`` or <NR1> = 0 turns off the dots-only display.
        """
        return self._dotsonly


class DisplayPersistence(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:PERSistence`` command.

    Description:
        - This command specifies the display persistence for analog waveforms. This affects the
          display only.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PERSistence?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PERSistence?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PERSistence value`` command.

    SCPI Syntax:
        ```
        - DISplay:PERSistence {<NR3>|CLEAR|AUTO|INFInite|OFF}
        - DISplay:PERSistence?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the time of the persistence.
        - ``CLEAR`` resets the persist time count down and clears the display of acquired points.
        - ``INFInite`` displays waveform points until a control change resets the acquisition
          system.
        - ``AUTO`` specifies that the oscilloscope automatically determines the best waveform
          persistence based on the value of waveform intensity (``DISPLAY:INTENSITY:WAVEFORM``).
        - ``OFF`` turns off DPO mode (0 seconds of persistence).
    """


class DisplayIntensityWaveform(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:WAVEform`` command.

    Description:
        - Sets and returns the display waveform intensity settings.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:WAVEform?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:WAVEform value``
          command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:WAVEform <NR1>
        - DISplay:INTENSITy:WAVEform?
        ```

    Info:
        - ``<NR1>`` is the waveform intensity and ranges from 1 to 100 percent.
    """


class DisplayIntensityGraticule(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:GRAticule`` command.

    Description:
        - Sets and returns the display graticule intensity settings.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:GRAticule?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:GRAticule?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:GRAticule value``
          command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:GRAticule <NR1>
        - DISplay:INTENSITy:GRAticule?
        ```

    Info:
        - ``<NR1>`` is the graticule intensity and ranges from 0 to 100 percent.
    """


class DisplayIntensityBacklightAutodimTime(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe`` command.

    Description:
        - Sets or queries the amount of time, in minutes, to wait for no user interface activity
          before automatically dimming the display. The time can range from a minimum of 10 minutes
          to a maximum of 1440 minutes (24 hours). The default is 10 minutes.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe value`` command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:BACKLight:AUTODim:TIMe <NR1>
        - DISplay:INTENSITy:BACKLight:AUTODim:TIMe?
        ```

    Info:
        - ``<NR1>`` is the amount of time, in minutes, to wait for no user interface activity before
          automatically dimming the display.
    """


class DisplayIntensityBacklightAutodimEnable(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble`` command.

    Description:
        - Sets or returns the state of the display auto-dim feature. The default is enabled. Once
          the backlight has dimmed, any button push or knob turn returns the backlight value to the
          value set by ``DISPLAY:INTENSITY:BACKLIGHT``.

    Usage:
        - Using the ``.query()`` method will send the
          ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the
          ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble value`` command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:BACKLight:AUTODim:ENAble {OFF|ON|0|1}
        - DISplay:INTENSITy:BACKLight:AUTODim:ENAble?
        ```

    Info:
        - ``OFF`` or 0 turns off the display auto-dim feature.
        - ``ON`` or 1 turns it on.
    """


class DisplayIntensityBacklightAutodim(SCPICmdRead):
    """The ``DISplay:INTENSITy:BACKLight:AUTODim`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight:AUTODim?``
          query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:BACKLight:AUTODim?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble`` command.
        - ``.time``: The ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = DisplayIntensityBacklightAutodimEnable(device, f"{self._cmd_syntax}:ENAble")
        self._time = DisplayIntensityBacklightAutodimTime(device, f"{self._cmd_syntax}:TIMe")

    @property
    def enable(self) -> DisplayIntensityBacklightAutodimEnable:
        """Return the ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble`` command.

        Description:
            - Sets or returns the state of the display auto-dim feature. The default is enabled.
              Once the backlight has dimmed, any button push or knob turn returns the backlight
              value to the value set by ``DISPLAY:INTENSITY:BACKLIGHT``.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble value`` command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:BACKLight:AUTODim:ENAble {OFF|ON|0|1}
            - DISplay:INTENSITy:BACKLight:AUTODim:ENAble?
            ```

        Info:
            - ``OFF`` or 0 turns off the display auto-dim feature.
            - ``ON`` or 1 turns it on.
        """
        return self._enable

    @property
    def time(self) -> DisplayIntensityBacklightAutodimTime:
        """Return the ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe`` command.

        Description:
            - Sets or queries the amount of time, in minutes, to wait for no user interface activity
              before automatically dimming the display. The time can range from a minimum of 10
              minutes to a maximum of 1440 minutes (24 hours). The default is 10 minutes.

        Usage:
            - Using the ``.query()`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe value`` command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:BACKLight:AUTODim:TIMe <NR1>
            - DISplay:INTENSITy:BACKLight:AUTODim:TIMe?
            ```

        Info:
            - ``<NR1>`` is the amount of time, in minutes, to wait for no user interface activity
              before automatically dimming the display.
        """
        return self._time


class DisplayIntensityBacklight(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:INTENSITy:BACKLight`` command.

    Description:
        - This command sets or queries the display backlight intensity setting.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:BACKLight?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:BACKLight value``
          command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:BACKLight {LOW|MEDium|HIGH}
        - DISplay:INTENSITy:BACKLight?
        ```

    Info:
        - ``LOW`` selects a low brightness level.
        - ``MEDium`` selects a moderate brightness level.
        - ``HIGH`` selects a full brightness level.

    Properties:
        - ``.autodim``: The ``DISplay:INTENSITy:BACKLight:AUTODim`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autodim = DisplayIntensityBacklightAutodim(device, f"{self._cmd_syntax}:AUTODim")

    @property
    def autodim(self) -> DisplayIntensityBacklightAutodim:
        """Return the ``DISplay:INTENSITy:BACKLight:AUTODim`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight:AUTODim?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``DISplay:INTENSITy:BACKLight:AUTODim?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``DISplay:INTENSITy:BACKLight:AUTODim:ENAble`` command.
            - ``.time``: The ``DISplay:INTENSITy:BACKLight:AUTODim:TIMe`` command.
        """
        return self._autodim


class DisplayIntensity(SCPICmdRead):
    """The ``DISplay:INTENSITy`` command.

    Description:
        - This query-only command returns the waveform saturation level and screen saver settings.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:INTENSITy?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy?
        ```

    Properties:
        - ``.backlight``: The ``DISplay:INTENSITy:BACKLight`` command.
        - ``.graticule``: The ``DISplay:INTENSITy:GRAticule`` command.
        - ``.waveform``: The ``DISplay:INTENSITy:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._backlight = DisplayIntensityBacklight(device, f"{self._cmd_syntax}:BACKLight")
        self._graticule = DisplayIntensityGraticule(device, f"{self._cmd_syntax}:GRAticule")
        self._waveform = DisplayIntensityWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def backlight(self) -> DisplayIntensityBacklight:
        """Return the ``DISplay:INTENSITy:BACKLight`` command.

        Description:
            - This command sets or queries the display backlight intensity setting.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:BACKLight?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:BACKLight?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:BACKLight value``
              command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:BACKLight {LOW|MEDium|HIGH}
            - DISplay:INTENSITy:BACKLight?
            ```

        Info:
            - ``LOW`` selects a low brightness level.
            - ``MEDium`` selects a moderate brightness level.
            - ``HIGH`` selects a full brightness level.

        Sub-properties:
            - ``.autodim``: The ``DISplay:INTENSITy:BACKLight:AUTODim`` command tree.
        """
        return self._backlight

    @property
    def graticule(self) -> DisplayIntensityGraticule:
        """Return the ``DISplay:INTENSITy:GRAticule`` command.

        Description:
            - Sets and returns the display graticule intensity settings.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:GRAticule?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:GRAticule?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:GRAticule value``
              command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:GRAticule <NR1>
            - DISplay:INTENSITy:GRAticule?
            ```

        Info:
            - ``<NR1>`` is the graticule intensity and ranges from 0 to 100 percent.
        """
        return self._graticule

    @property
    def waveform(self) -> DisplayIntensityWaveform:
        """Return the ``DISplay:INTENSITy:WAVEform`` command.

        Description:
            - Sets and returns the display waveform intensity settings.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy:WAVEform?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:WAVEform value``
              command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:WAVEform <NR1>
            - DISplay:INTENSITy:WAVEform?
            ```

        Info:
            - ``<NR1>`` is the waveform intensity and ranges from 1 to 100 percent.
        """
        return self._waveform


class DisplayGraticule(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:GRAticule`` command.

    Description:
        - This command specifies the type of graticule the oscilloscope displays.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GRAticule?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GRAticule?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:GRAticule value`` command.

    SCPI Syntax:
        ```
        - DISplay:GRAticule {CROSSHair|FRAme|FULl|GRId|SOLid}
        - DISplay:GRAticule?
        ```

    Info:
        - ``CROSSHair`` specifies a frame and cross hairs.
        - ``FRAme`` specifies a frame only.
        - ``FULl`` specifies a frame, a grid and cross hairs.
        - ``GRId`` specifies a frame and grid only.
        - ``SOLid`` specifies a solid graticule.
    """


class DisplayDigitalHeight(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:DIGital:HEIght`` command.

    Description:
        - This command specifies the number of available digital waveform position slots.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:DIGital:HEIght?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:DIGital:HEIght?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:DIGital:HEIght value`` command.

    SCPI Syntax:
        ```
        - DISplay:DIGital:HEIght {SMAll|MEDium|LARge}
        - DISplay:DIGital:HEIght?
        ```

    Info:
        - ``SMAll`` sets the height to display 4 digital waveforms per division.
        - ``MEDium`` sets the height to display 2 digital waveforms per division.
        - ``LARge`` sets the height to display 1 digital waveform per division.
    """


class DisplayDigitalActivity(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:DIGital:ACTIVity`` command.

    Description:
        - Sets or returns the state of the digital channel monitor display. When enabled, the
          digital channel monitor is displayed when one or more of D0-D15 are turned on. The data
          that is summarized in that display can be obtained by querying CURVE with the
          ``DATA:SOURCE`` set to DIGital and one or more digital channels D0-D15 turned on. For more
          information, refer to the description of DIGital in the section entitled 'Transferring a
          Waveform From an Oscilloscope to a Computer'.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:DIGital:ACTIVity?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:DIGital:ACTIVity?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:DIGital:ACTIVity value``
          command.

    SCPI Syntax:
        ```
        - DISplay:DIGital:ACTIVity {0|1|OFF|ON}
        - DISplay:DIGital:ACTIVity?
        ```

    Info:
        - ``1`` or ON turns on the digital channel activity monitor display.
        - ``0`` or OFF turns it off.
    """


class DisplayDigital(SCPICmdRead):
    """The ``DISplay:DIGital`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:DIGital?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:DIGital?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.activity``: The ``DISplay:DIGital:ACTIVity`` command.
        - ``.height``: The ``DISplay:DIGital:HEIght`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._activity = DisplayDigitalActivity(device, f"{self._cmd_syntax}:ACTIVity")
        self._height = DisplayDigitalHeight(device, f"{self._cmd_syntax}:HEIght")

    @property
    def activity(self) -> DisplayDigitalActivity:
        """Return the ``DISplay:DIGital:ACTIVity`` command.

        Description:
            - Sets or returns the state of the digital channel monitor display. When enabled, the
              digital channel monitor is displayed when one or more of D0-D15 are turned on. The
              data that is summarized in that display can be obtained by querying CURVE with the
              ``DATA:SOURCE`` set to DIGital and one or more digital channels D0-D15 turned on. For
              more information, refer to the description of DIGital in the section entitled
              'Transferring a Waveform From an Oscilloscope to a Computer'.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:DIGital:ACTIVity?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:DIGital:ACTIVity?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:DIGital:ACTIVity value``
              command.

        SCPI Syntax:
            ```
            - DISplay:DIGital:ACTIVity {0|1|OFF|ON}
            - DISplay:DIGital:ACTIVity?
            ```

        Info:
            - ``1`` or ON turns on the digital channel activity monitor display.
            - ``0`` or OFF turns it off.
        """
        return self._activity

    @property
    def height(self) -> DisplayDigitalHeight:
        """Return the ``DISplay:DIGital:HEIght`` command.

        Description:
            - This command specifies the number of available digital waveform position slots.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:DIGital:HEIght?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:DIGital:HEIght?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:DIGital:HEIght value``
              command.

        SCPI Syntax:
            ```
            - DISplay:DIGital:HEIght {SMAll|MEDium|LARge}
            - DISplay:DIGital:HEIght?
            ```

        Info:
            - ``SMAll`` sets the height to display 4 digital waveforms per division.
            - ``MEDium`` sets the height to display 2 digital waveforms per division.
            - ``LARge`` sets the height to display 1 digital waveform per division.
        """
        return self._height


class DisplayConfigureReadout(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:CONFIGure:READOut`` command.

    Description:
        - Configures or queries readout backgrounds. NORMal is used for standard opaque, and
          TRANSParent for transparent. This setting applies to all on-screen readouts on the
          waveform area, such as channel, measurements, cursor, math, or bus, etc.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:CONFIGure:READOut?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:CONFIGure:READOut?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:CONFIGure:READOut value``
          command.

    SCPI Syntax:
        ```
        - DISplay:CONFIGure:READOut {NORMal ! TRANSParent}
        - DISplay:CONFIGure:READOut?
        ```

    Info:
        - ``NORMal`` sets all readout backgrounds to the standard opaque background.
        - ``TRANSParent`` sets all readout backgrounds to transparent mode.
    """


class DisplayConfigure(SCPICmdRead):
    """The ``DISplay:CONFIGure`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:CONFIGure?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:CONFIGure?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.readout``: The ``DISplay:CONFIGure:READOut`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._readout = DisplayConfigureReadout(device, f"{self._cmd_syntax}:READOut")

    @property
    def readout(self) -> DisplayConfigureReadout:
        """Return the ``DISplay:CONFIGure:READOut`` command.

        Description:
            - Configures or queries readout backgrounds. NORMal is used for standard opaque, and
              TRANSParent for transparent. This setting applies to all on-screen readouts on the
              waveform area, such as channel, measurements, cursor, math, or bus, etc.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:CONFIGure:READOut?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:CONFIGure:READOut?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:CONFIGure:READOut value``
              command.

        SCPI Syntax:
            ```
            - DISplay:CONFIGure:READOut {NORMal ! TRANSParent}
            - DISplay:CONFIGure:READOut?
            ```

        Info:
            - ``NORMal`` sets all readout backgrounds to the standard opaque background.
            - ``TRANSParent`` sets all readout backgrounds to transparent mode.
        """
        return self._readout


class DisplayColorMode(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:COLor:MODe`` command.

    Description:
        - This command sets or queries the color mode for the graticule and waveform display.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLor:MODe?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLor:MODe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:COLor:MODe value`` command.

    SCPI Syntax:
        ```
        - DISplay:COLor:MODe {NORMal|INVERTed}
        - DISplay:COLor:MODe?
        ```

    Info:
        - ``NORMal`` specifies normal color mode.
        - ``INVERTed`` specifies inverted color mode.
    """


class DisplayColor(SCPICmdRead):
    """The ``DISplay:COLor`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:COLor?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:COLor?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.mode``: The ``DISplay:COLor:MODe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mode = DisplayColorMode(device, f"{self._cmd_syntax}:MODe")

    @property
    def mode(self) -> DisplayColorMode:
        """Return the ``DISplay:COLor:MODe`` command.

        Description:
            - This command sets or queries the color mode for the graticule and waveform display.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLor:MODe?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:COLor:MODe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:COLor:MODe value`` command.

        SCPI Syntax:
            ```
            - DISplay:COLor:MODe {NORMal|INVERTed}
            - DISplay:COLor:MODe?
            ```

        Info:
            - ``NORMal`` specifies normal color mode.
            - ``INVERTed`` specifies inverted color mode.
        """
        return self._mode


class DisplayClock(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:CLOCk`` command.

    Description:
        - This command specifies whether the oscilloscope displays the date and time. The query form
          of this command returns an ON (1) or an OFF (0).

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:CLOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:CLOCk value`` command.

    SCPI Syntax:
        ```
        - DISplay:CLOCk {ON|OFF|<NR1>}
        - DISplay:CLOCk?
        ```

    Info:
        - ``ON`` enables the display of date and time.
        - ``OFF`` disables the display of date and time.
        - ``<NR1>`` = 0 disables the display of date and time; any other value enables the display
          of date and time.
    """


#  pylint: disable=too-many-instance-attributes
class Display(SCPICmdRead):
    """The ``DISplay`` command.

    Description:
        - This query-only command returns the current Display settings.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - DISplay?
        ```

    Properties:
        - ``.clock``: The ``DISplay:CLOCk`` command.
        - ``.color``: The ``DISplay:COLor`` command tree.
        - ``.configure``: The ``DISplay:CONFIGure`` command tree.
        - ``.digital``: The ``DISplay:DIGital`` command tree.
        - ``.graticule``: The ``DISplay:GRAticule`` command.
        - ``.intensity``: The ``DISplay:INTENSITy`` command.
        - ``.persistence``: The ``DISplay:PERSistence`` command.
        - ``.style``: The ``DISplay:STYle`` command tree.
        - ``.trigfrequency``: The ``DISplay:TRIGFrequency`` command.
        - ``.xy``: The ``DISplay:XY`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DISplay") -> None:
        super().__init__(device, cmd_syntax)
        self._clock = DisplayClock(device, f"{self._cmd_syntax}:CLOCk")
        self._color = DisplayColor(device, f"{self._cmd_syntax}:COLor")
        self._configure = DisplayConfigure(device, f"{self._cmd_syntax}:CONFIGure")
        self._digital = DisplayDigital(device, f"{self._cmd_syntax}:DIGital")
        self._graticule = DisplayGraticule(device, f"{self._cmd_syntax}:GRAticule")
        self._intensity = DisplayIntensity(device, f"{self._cmd_syntax}:INTENSITy")
        self._persistence = DisplayPersistence(device, f"{self._cmd_syntax}:PERSistence")
        self._style = DisplayStyle(device, f"{self._cmd_syntax}:STYle")
        self._trigfrequency = DisplayTrigfrequency(device, f"{self._cmd_syntax}:TRIGFrequency")
        self._xy = DisplayXy(device, f"{self._cmd_syntax}:XY")

    @property
    def clock(self) -> DisplayClock:
        """Return the ``DISplay:CLOCk`` command.

        Description:
            - This command specifies whether the oscilloscope displays the date and time. The query
              form of this command returns an ON (1) or an OFF (0).

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:CLOCk?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:CLOCk value`` command.

        SCPI Syntax:
            ```
            - DISplay:CLOCk {ON|OFF|<NR1>}
            - DISplay:CLOCk?
            ```

        Info:
            - ``ON`` enables the display of date and time.
            - ``OFF`` disables the display of date and time.
            - ``<NR1>`` = 0 disables the display of date and time; any other value enables the
              display of date and time.
        """
        return self._clock

    @property
    def color(self) -> DisplayColor:
        """Return the ``DISplay:COLor`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:COLor?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:COLor?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.mode``: The ``DISplay:COLor:MODe`` command.
        """
        return self._color

    @property
    def configure(self) -> DisplayConfigure:
        """Return the ``DISplay:CONFIGure`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:CONFIGure?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:CONFIGure?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.readout``: The ``DISplay:CONFIGure:READOut`` command.
        """
        return self._configure

    @property
    def digital(self) -> DisplayDigital:
        """Return the ``DISplay:DIGital`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:DIGital?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:DIGital?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.activity``: The ``DISplay:DIGital:ACTIVity`` command.
            - ``.height``: The ``DISplay:DIGital:HEIght`` command.
        """
        return self._digital

    @property
    def graticule(self) -> DisplayGraticule:
        """Return the ``DISplay:GRAticule`` command.

        Description:
            - This command specifies the type of graticule the oscilloscope displays.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GRAticule?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GRAticule?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:GRAticule value`` command.

        SCPI Syntax:
            ```
            - DISplay:GRAticule {CROSSHair|FRAme|FULl|GRId|SOLid}
            - DISplay:GRAticule?
            ```

        Info:
            - ``CROSSHair`` specifies a frame and cross hairs.
            - ``FRAme`` specifies a frame only.
            - ``FULl`` specifies a frame, a grid and cross hairs.
            - ``GRId`` specifies a frame and grid only.
            - ``SOLid`` specifies a solid graticule.
        """
        return self._graticule

    @property
    def intensity(self) -> DisplayIntensity:
        """Return the ``DISplay:INTENSITy`` command.

        Description:
            - This query-only command returns the waveform saturation level and screen saver
              settings.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:INTENSITy?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:INTENSITy?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy?
            ```

        Sub-properties:
            - ``.backlight``: The ``DISplay:INTENSITy:BACKLight`` command.
            - ``.graticule``: The ``DISplay:INTENSITy:GRAticule`` command.
            - ``.waveform``: The ``DISplay:INTENSITy:WAVEform`` command.
        """
        return self._intensity

    @property
    def persistence(self) -> DisplayPersistence:
        """Return the ``DISplay:PERSistence`` command.

        Description:
            - This command specifies the display persistence for analog waveforms. This affects the
              display only.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PERSistence?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PERSistence?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:PERSistence value``
              command.

        SCPI Syntax:
            ```
            - DISplay:PERSistence {<NR3>|CLEAR|AUTO|INFInite|OFF}
            - DISplay:PERSistence?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the time of the persistence.
            - ``CLEAR`` resets the persist time count down and clears the display of acquired
              points.
            - ``INFInite`` displays waveform points until a control change resets the acquisition
              system.
            - ``AUTO`` specifies that the oscilloscope automatically determines the best waveform
              persistence based on the value of waveform intensity (``DISPLAY:INTENSITY:WAVEFORM``).
            - ``OFF`` turns off DPO mode (0 seconds of persistence).
        """
        return self._persistence

    @property
    def style(self) -> DisplayStyle:
        """Return the ``DISplay:STYle`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:STYle?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:STYle?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.dotsonly``: The ``DISplay:STYle:DOTsonly`` command.
        """
        return self._style

    @property
    def trigfrequency(self) -> DisplayTrigfrequency:
        """Return the ``DISplay:TRIGFrequency`` command.

        Description:
            - This command switches the trigger frequency readout on or off.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:TRIGFrequency?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:TRIGFrequency?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:TRIGFrequency value``
              command.

        SCPI Syntax:
            ```
            - DISplay:TRIGFrequency {OFF|ON|0|1}
            - DISplay:TRIGFrequency?
            ```
        """
        return self._trigfrequency

    @property
    def xy(self) -> DisplayXy:
        """Return the ``DISplay:XY`` command.

        Description:
            - This command turns on or off the XY display mode.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:XY?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:XY?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:XY value`` command.

        SCPI Syntax:
            ```
            - DISplay:XY {OFF|TRIGgered}
            - DISplay:XY?
            ```

        Info:
            - ``OFF`` - The channels are displayed individually as a function of time.
            - ``TRIGgered`` - The channels are displayed in 'X-Y' pairs with CH1 being displayed as
              a function of CH2, and so on.

        Sub-properties:
            - ``.withyt``: The ``DISplay:XY:WITHYT`` command.
        """
        return self._xy
