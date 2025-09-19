"""The display commands module.

These commands are used in the following models:
DPO2K, DPO2KB, MSO2K, MSO2KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DISplay:CLOCk {DATEOnly|TIMEOnly|DATETIME|NONe|ON|OFF|<NR1>}
    - DISplay:CLOCk?
    - DISplay:DIGital:HEIght {SMAll|MEDium|LARge}
    - DISplay:DIGital:HEIght?
    - DISplay:FORMat {YT|XY}
    - DISplay:FORMat?
    - DISplay:GLITch {ON|OFF|<NR1>}
    - DISplay:GLITch?
    - DISplay:GRAticule {CROSSHair|FRAme|FULl|GRId}
    - DISplay:GRAticule?
    - DISplay:INTENSITy:BACKLight {LOW|MEDium|HIGH}
    - DISplay:INTENSITy:BACKLight?
    - DISplay:INTENSITy:GLITch {<NR1>}
    - DISplay:INTENSITy:GRAticule <NR1>
    - DISplay:INTENSITy:GRAticule?
    - DISplay:INTENSITy:WAVEform <NR1>
    - DISplay:INTENSITy:WAVEform?
    - DISplay:INTENSITy?
    - DISplay:PERSistence {<NR3>|CLEAR|AUTO|MINImum|INFInite}
    - DISplay:PERSistence?
    - DISplay:STYle:DOTsonly {ON|OFF|<NR1>}
    - DISplay:STYle:DOTsonly?
    - DISplay?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


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
        - Sets or returns the display persistence. This affects the display only.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:PERSistence?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:PERSistence?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:PERSistence value`` command.

    SCPI Syntax:
        ```
        - DISplay:PERSistence {<NR3>|CLEAR|AUTO|MINImum|INFInite}
        - DISplay:PERSistence?
        ```

    Info:
        - ``<NR3>`` specifies the time of the persistence.
        - ``CLEAR`` resets the persist time count down and clears the display of acquired points.
        - ``INFInite`` displays waveform points until a control change resets the acquisition
          system. When persistence is set to infinite, it does not mean that the brightness of any
          pixel should never decrease. The brightness of a pixel is proportionally dependent on the
          ratio between its intensity, which does NOT decrease at infinite persistence, and the
          maximum value of intensity of any pixel on the screen. Thus, if a particular pixel gets
          hit less often than others, its brightness will decrease over time. It will become less
          bright relative to the pixels that get hit often.
        - ``AUTO`` specifies that the oscilloscope automatically determines the best waveform
          persistence based on the value of waveform intensity (``DISPLAY:INTEnsITY:WAVEFORM``).
        - ``MINImum`` specifies that the waveform persistence is set to the minimum value of 0.0E0.
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


class DisplayIntensityGlitch(SCPICmdWrite):
    """The ``DISplay:INTENSITy:GLITch`` command.

    Description:
        - Sets the intensity of the glitch capture background of the waveform display. The intensity
          can be set from 5 to 100% in increments of 5%. The intensity of the glitch capture
          background can only be adjusted when the glitch capture background is displayed and
          FilterVu filtering is in use. Otherwise, the intensity is fixed. Use ``DISPLAY:GLITCH`` to
          turn the glitch capture background ON and OFF. Use ``FILTERVU:FREQUENCY`` to enable
          filtering. Filtering is enabled if the frequency chosen is different than the
          oscilloscope's full bandwidth.

    Usage:
        - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:GLITch value``
          command.

    SCPI Syntax:
        ```
        - DISplay:INTENSITy:GLITch {<NR1>}
        ```

    Info:
        - ``<NR1>`` is the glitch intensity and ranges from 5 to 100 percent.
    """


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
    """


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
        - ``.glitch``: The ``DISplay:INTENSITy:GLITch`` command.
        - ``.graticule``: The ``DISplay:INTENSITy:GRAticule`` command.
        - ``.waveform``: The ``DISplay:INTENSITy:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._backlight = DisplayIntensityBacklight(device, f"{self._cmd_syntax}:BACKLight")
        self._glitch = DisplayIntensityGlitch(device, f"{self._cmd_syntax}:GLITch")
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
        """
        return self._backlight

    @property
    def glitch(self) -> DisplayIntensityGlitch:
        """Return the ``DISplay:INTENSITy:GLITch`` command.

        Description:
            - Sets the intensity of the glitch capture background of the waveform display. The
              intensity can be set from 5 to 100% in increments of 5%. The intensity of the glitch
              capture background can only be adjusted when the glitch capture background is
              displayed and FilterVu filtering is in use. Otherwise, the intensity is fixed. Use
              ``DISPLAY:GLITCH`` to turn the glitch capture background ON and OFF. Use
              ``FILTERVU:FREQUENCY`` to enable filtering. Filtering is enabled if the frequency
              chosen is different than the oscilloscope's full bandwidth.

        Usage:
            - Using the ``.write(value)`` method will send the ``DISplay:INTENSITy:GLITch value``
              command.

        SCPI Syntax:
            ```
            - DISplay:INTENSITy:GLITch {<NR1>}
            ```

        Info:
            - ``<NR1>`` is the glitch intensity and ranges from 5 to 100 percent.
        """
        return self._glitch

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
        - Selects or queries the type of graticule the oscilloscope displays.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GRAticule?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GRAticule?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:GRAticule value`` command.

    SCPI Syntax:
        ```
        - DISplay:GRAticule {CROSSHair|FRAme|FULl|GRId}
        - DISplay:GRAticule?
        ```

    Info:
        - ``CROSSHair`` specifies a frame and cross hairs.
        - ``FRAme`` specifies a frame only.
        - ``FULl`` specifies a frame, a grid and cross hairs.
        - ``GRId`` specifies a frame and grid only.
    """


class DisplayGlitch(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:GLITch`` command.

    Description:
        - Controls the display of the glitch capture background of the waveform. Set the intensity
          with ``DISPLAY:INTENSITY:GLITCH``.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:GLITch?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:GLITch?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:GLITch value`` command.

    SCPI Syntax:
        ```
        - DISplay:GLITch {ON|OFF|<NR1>}
        - DISplay:GLITch?
        ```

    Info:
        - ``ON`` or <NR1> ≠ 0 turns on the glitch capture waveform display.
        - ``OFF`` or <NR1> = 0 turns off the glitch capture waveform display.
    """


class DisplayFormat(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:FORMat`` command.

    Description:
        - Sets or returns the display format.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:FORMat?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:FORMat?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:FORMat value`` command.

    SCPI Syntax:
        ```
        - DISplay:FORMat {YT|XY}
        - DISplay:FORMat?
        ```

    Info:
        - ``YT`` sets the display to a voltage versus time format and is the default mode.
        - ``XY`` argument displays one waveform against another. Selecting one source causes its
          corresponding source to be implicitly selected, producing a single trace from the two
          input waveforms.
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


class DisplayDigital(SCPICmdRead):
    """The ``DISplay:DIGital`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:DIGital?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:DIGital?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.height``: The ``DISplay:DIGital:HEIght`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._height = DisplayDigitalHeight(device, f"{self._cmd_syntax}:HEIght")

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


class DisplayClock(SCPICmdWrite, SCPICmdRead):
    """The ``DISplay:CLOCk`` command.

    Description:
        - Sets or returns whether the oscilloscope displays the date and time. The query form of
          this command returns an ON (1) or an OFF (0).

    Usage:
        - Using the ``.query()`` method will send the ``DISplay:CLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``DISplay:CLOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DISplay:CLOCk value`` command.

    SCPI Syntax:
        ```
        - DISplay:CLOCk {DATEOnly|TIMEOnly|DATETIME|NONe|ON|OFF|<NR1>}
        - DISplay:CLOCk?
        ```

    Info:
        - ``DATEOnly`` enables the display of date.
        - ``TIMEOnly`` enables the display of time.
        - ``DATETIME or ON`` enables the display of both date and time.
        - ``NONe or OFF`` disables the display of date and time.
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
        - ``.digital``: The ``DISplay:DIGital`` command tree.
        - ``.format``: The ``DISplay:FORMat`` command.
        - ``.glitch``: The ``DISplay:GLITch`` command.
        - ``.graticule``: The ``DISplay:GRAticule`` command.
        - ``.intensity``: The ``DISplay:INTENSITy`` command.
        - ``.persistence``: The ``DISplay:PERSistence`` command.
        - ``.style``: The ``DISplay:STYle`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DISplay") -> None:
        super().__init__(device, cmd_syntax)
        self._clock = DisplayClock(device, f"{self._cmd_syntax}:CLOCk")
        self._digital = DisplayDigital(device, f"{self._cmd_syntax}:DIGital")
        self._format = DisplayFormat(device, f"{self._cmd_syntax}:FORMat")
        self._glitch = DisplayGlitch(device, f"{self._cmd_syntax}:GLITch")
        self._graticule = DisplayGraticule(device, f"{self._cmd_syntax}:GRAticule")
        self._intensity = DisplayIntensity(device, f"{self._cmd_syntax}:INTENSITy")
        self._persistence = DisplayPersistence(device, f"{self._cmd_syntax}:PERSistence")
        self._style = DisplayStyle(device, f"{self._cmd_syntax}:STYle")

    @property
    def clock(self) -> DisplayClock:
        """Return the ``DISplay:CLOCk`` command.

        Description:
            - Sets or returns whether the oscilloscope displays the date and time. The query form of
              this command returns an ON (1) or an OFF (0).

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:CLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:CLOCk?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:CLOCk value`` command.

        SCPI Syntax:
            ```
            - DISplay:CLOCk {DATEOnly|TIMEOnly|DATETIME|NONe|ON|OFF|<NR1>}
            - DISplay:CLOCk?
            ```

        Info:
            - ``DATEOnly`` enables the display of date.
            - ``TIMEOnly`` enables the display of time.
            - ``DATETIME or ON`` enables the display of both date and time.
            - ``NONe or OFF`` disables the display of date and time.
            - ``<NR1>`` = 0 disables the display of date and time; any other value enables the
              display of date and time.
        """
        return self._clock

    @property
    def digital(self) -> DisplayDigital:
        """Return the ``DISplay:DIGital`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:DIGital?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:DIGital?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.height``: The ``DISplay:DIGital:HEIght`` command.
        """
        return self._digital

    @property
    def format(self) -> DisplayFormat:
        """Return the ``DISplay:FORMat`` command.

        Description:
            - Sets or returns the display format.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:FORMat?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:FORMat?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:FORMat value`` command.

        SCPI Syntax:
            ```
            - DISplay:FORMat {YT|XY}
            - DISplay:FORMat?
            ```

        Info:
            - ``YT`` sets the display to a voltage versus time format and is the default mode.
            - ``XY`` argument displays one waveform against another. Selecting one source causes its
              corresponding source to be implicitly selected, producing a single trace from the two
              input waveforms.
        """
        return self._format

    @property
    def glitch(self) -> DisplayGlitch:
        """Return the ``DISplay:GLITch`` command.

        Description:
            - Controls the display of the glitch capture background of the waveform. Set the
              intensity with ``DISPLAY:INTENSITY:GLITCH``.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GLITch?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GLITch?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:GLITch value`` command.

        SCPI Syntax:
            ```
            - DISplay:GLITch {ON|OFF|<NR1>}
            - DISplay:GLITch?
            ```

        Info:
            - ``ON`` or <NR1> ≠ 0 turns on the glitch capture waveform display.
            - ``OFF`` or <NR1> = 0 turns off the glitch capture waveform display.
        """
        return self._glitch

    @property
    def graticule(self) -> DisplayGraticule:
        """Return the ``DISplay:GRAticule`` command.

        Description:
            - Selects or queries the type of graticule the oscilloscope displays.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:GRAticule?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:GRAticule?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:GRAticule value`` command.

        SCPI Syntax:
            ```
            - DISplay:GRAticule {CROSSHair|FRAme|FULl|GRId}
            - DISplay:GRAticule?
            ```

        Info:
            - ``CROSSHair`` specifies a frame and cross hairs.
            - ``FRAme`` specifies a frame only.
            - ``FULl`` specifies a frame, a grid and cross hairs.
            - ``GRId`` specifies a frame and grid only.
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
            - ``.glitch``: The ``DISplay:INTENSITy:GLITch`` command.
            - ``.graticule``: The ``DISplay:INTENSITy:GRAticule`` command.
            - ``.waveform``: The ``DISplay:INTENSITy:WAVEform`` command.
        """
        return self._intensity

    @property
    def persistence(self) -> DisplayPersistence:
        """Return the ``DISplay:PERSistence`` command.

        Description:
            - Sets or returns the display persistence. This affects the display only.

        Usage:
            - Using the ``.query()`` method will send the ``DISplay:PERSistence?`` query.
            - Using the ``.verify(value)`` method will send the ``DISplay:PERSistence?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DISplay:PERSistence value``
              command.

        SCPI Syntax:
            ```
            - DISplay:PERSistence {<NR3>|CLEAR|AUTO|MINImum|INFInite}
            - DISplay:PERSistence?
            ```

        Info:
            - ``<NR3>`` specifies the time of the persistence.
            - ``CLEAR`` resets the persist time count down and clears the display of acquired
              points.
            - ``INFInite`` displays waveform points until a control change resets the acquisition
              system. When persistence is set to infinite, it does not mean that the brightness of
              any pixel should never decrease. The brightness of a pixel is proportionally dependent
              on the ratio between its intensity, which does NOT decrease at infinite persistence,
              and the maximum value of intensity of any pixel on the screen. Thus, if a particular
              pixel gets hit less often than others, its brightness will decrease over time. It will
              become less bright relative to the pixels that get hit often.
            - ``AUTO`` specifies that the oscilloscope automatically determines the best waveform
              persistence based on the value of waveform intensity (``DISPLAY:INTEnsITY:WAVEFORM``).
            - ``MINImum`` specifies that the waveform persistence is set to the minimum value of
              0.0E0.
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
