"""The autoset commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUTOSet {EXECute|UNDo|VFields|VIDeo|VLines}
    - AUTOSet:OVErlay {ON|OFF}
    - AUTOSet:PERcent <NR3>
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AutosetPercent(SCPICmdWrite):
    """The ``AUTOSet:PERcent`` command.

    Description:
        - Sets or queries the percent of the full vertical scale that the signal should cover after
          Autoset is run when Overlay is turned on.

    Usage:
        - Using the ``.write(value)`` method will send the ``AUTOSet:PERcent value`` command.

    SCPI Syntax:
        ```
        - AUTOSet:PERcent <NR3>
        ```
    """


class AutosetOverlay(SCPICmdWrite):
    """The ``AUTOSet:OVErlay`` command.

    Description:
        - Sets or queries the autoset overlay feature. If Autoset Overlay is turned on, Autoset will
          place all signals center vertically on-screen with the vertical settings on each channel
          configured so that the amplitude of the signal occupies n divisions = Percent/10
          divisions.

    Usage:
        - Using the ``.write(value)`` method will send the ``AUTOSet:OVErlay value`` command.

    SCPI Syntax:
        ```
        - AUTOSet:OVErlay {ON|OFF}
        ```
    """


class Autoset(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSet`` command.

    Description:
        - This command (no query format) sets the vertical, horizontal, and trigger controls of the
          instrument to automatically acquire and display the selected waveform. (To autoset a video
          waveform, the video trigger must be set to video standard, not custom. Video arguments
          require video hardware.) This is equivalent to pressing the front panel AUTOSET button.
          For a detailed description of autoset functionality, see Autoset in the index of the
          online help for your instrument.

    Usage:
        - Using the ``.write(value)`` method will send the ``AUTOSet value`` command.

    SCPI Syntax:
        ```
        - AUTOSet {EXECute|UNDo|VFields|VIDeo|VLines}
        ```

    Info:
        - ``EXECute`` runs the autoset routine; this is equivalent to pressing the front panel
          AUTOSET button. If the display is set to a PAL, MV, or IRE graticule, this argument forces
          the graticule display to full mode (frame, grid, and cross hair).
        - ``UNDo`` returns the instrument to the setting prior to executing an autoset.
        - ``VFields`` autosets the displayed waveform.
        - ``VIDeo`` autosets the displayed waveform.
        - ``VLines`` autosets the displayed waveform.

    Properties:
        - ``.overlay``: The ``AUTOSet:OVErlay`` command.
        - ``.percent``: The ``AUTOSet:PERcent`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUTOSet") -> None:
        super().__init__(device, cmd_syntax)
        self._overlay = AutosetOverlay(device, f"{self._cmd_syntax}:OVErlay")
        self._percent = AutosetPercent(device, f"{self._cmd_syntax}:PERcent")

    @property
    def overlay(self) -> AutosetOverlay:
        """Return the ``AUTOSet:OVErlay`` command.

        Description:
            - Sets or queries the autoset overlay feature. If Autoset Overlay is turned on, Autoset
              will place all signals center vertically on-screen with the vertical settings on each
              channel configured so that the amplitude of the signal occupies n divisions =
              Percent/10 divisions.

        Usage:
            - Using the ``.write(value)`` method will send the ``AUTOSet:OVErlay value`` command.

        SCPI Syntax:
            ```
            - AUTOSet:OVErlay {ON|OFF}
            ```
        """
        return self._overlay

    @property
    def percent(self) -> AutosetPercent:
        """Return the ``AUTOSet:PERcent`` command.

        Description:
            - Sets or queries the percent of the full vertical scale that the signal should cover
              after Autoset is run when Overlay is turned on.

        Usage:
            - Using the ``.write(value)`` method will send the ``AUTOSet:PERcent value`` command.

        SCPI Syntax:
            ```
            - AUTOSet:PERcent <NR3>
            ```
        """
        return self._percent
