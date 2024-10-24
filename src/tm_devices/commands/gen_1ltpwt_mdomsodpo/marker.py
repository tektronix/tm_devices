"""The marker commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - MARKER:M<x>:AMPLitude:ABSolute?
    - MARKER:M<x>:AMPLitude:DELTa?
    - MARKER:M<x>:FREQuency:ABSolute <NR3>
    - MARKER:M<x>:FREQuency:ABSolute?
    - MARKER:M<x>:FREQuency:DELTa?
    - MARKER:M<x>:NOISEDensity?
    - MARKER:M<x>:PHASENoise?
    - MARKER:MANual {OFF|ON|0|1}
    - MARKER:MANual?
    - MARKER:PEAK:EXCURsion <NR3>
    - MARKER:PEAK:EXCURsion?
    - MARKER:PEAK:MAXimum <NR1>
    - MARKER:PEAK:MAXimum?
    - MARKER:PEAK:STATE {OFF|ON|0|1}
    - MARKER:PEAK:STATE?
    - MARKER:PEAK:THReshold <NR3>
    - MARKER:PEAK:THReshold?
    - MARKER:REFERence CENTER
    - MARKER:REFERence:AMPlitude?
    - MARKER:REFERence:FREQuency?
    - MARKER:TYPe {DELTa|ABSolute}
    - MARKER:TYPe?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MarkerType(SCPICmdWrite, SCPICmdRead):
    """The ``MARKER:TYPe`` command.

    Description:
        - This command specifies the marker type (either DELTa or ABSolute). An absolute marker
          shows the frequency and amplitude at the location of the marker. A delta marker shows the
          frequency and amplitude of the marker relative to the Reference Marker. The Reference
          Marker shows the absolute frequency and amplitude, regardless of this command. The marker
          amplitude measurements are in dBm for absolute, or in dBc (dB below carrier amplitude) for
          delta.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:TYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:TYPe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MARKER:TYPe value`` command.

    SCPI Syntax:
        ```
        - MARKER:TYPe {DELTa|ABSolute}
        - MARKER:TYPe?
        ```

    Info:
        - ``DELTa`` specifies to display the frequency and amplitude of the markers relative to the
          Reference Marker. The relative amplitude is in dBc (dB below carrier amplitude); the
          relative frequency is in Hz.
        - ``ABSolute`` specifies to display the actual frequency and amplitude of each marker. The
          absolute amplitude is in user-set units; the absolute frequency is in Hz.
    """


class MarkerReferenceFrequency(SCPICmdRead):
    """The ``MARKER:REFERence:FREQuency`` command.

    Description:
        - This query returns the frequency of the Reference Marker, in Hz, when the frequency domain
          trace markers are on (using either the command ``MARKER:PEAK:STATE`` or
          ``MARKER:MANUAL``). This data is equivalent to the number that appears on the display next
          to the red R inside a triangle when markers areon. If all markers are off, the value
          returned will be the last value displayed.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:REFERence:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:REFERence:FREQuency?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARKER:REFERence:FREQuency?
        ```
    """


class MarkerReferenceAmplitude(SCPICmdRead):
    """The ``MARKER:REFERence:AMPlitude`` command.

    Description:
        - This query returns the actual amplitude (vertical) value of the Reference Marker in
          user-set units. This value indicates the absolute amplitude of the Reference Marker,
          regardless of whether the other markers are manual or automatic. This data is equivalent
          to the number that appears on the display next to the red R inside a triangle when markers
          are turned on. If all markers are turned off, the value returned will be the last value
          displayed.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:REFERence:AMPlitude?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:REFERence:AMPlitude?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARKER:REFERence:AMPlitude?
        ```
    """


class MarkerReference(SCPICmdWrite, SCPICmdRead):
    """The ``MARKER:REFERence`` command.

    Description:
        - This command changes the Center Frequency to the frequency indicated by the Reference
          Marker, in effect moving the Reference Marker to the center of the screen. This applies
          when markers are turned on (using the command ``MARKER:PEAK:STATE`` or ``MARKER:MANUAL``).
          This is equivalent to the 'R' to Center side menu button in the front panel Markers menu.

    Usage:
        - Using the ``.write(value)`` method will send the ``MARKER:REFERence value`` command.

    SCPI Syntax:
        ```
        - MARKER:REFERence CENTER
        ```

    Properties:
        - ``.amplitude``: The ``MARKER:REFERence:AMPlitude`` command.
        - ``.frequency``: The ``MARKER:REFERence:FREQuency`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = MarkerReferenceAmplitude(device, f"{self._cmd_syntax}:AMPlitude")
        self._frequency = MarkerReferenceFrequency(device, f"{self._cmd_syntax}:FREQuency")

    @property
    def amplitude(self) -> MarkerReferenceAmplitude:
        """Return the ``MARKER:REFERence:AMPlitude`` command.

        Description:
            - This query returns the actual amplitude (vertical) value of the Reference Marker in
              user-set units. This value indicates the absolute amplitude of the Reference Marker,
              regardless of whether the other markers are manual or automatic. This data is
              equivalent to the number that appears on the display next to the red R inside a
              triangle when markers are turned on. If all markers are turned off, the value returned
              will be the last value displayed.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:REFERence:AMPlitude?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:REFERence:AMPlitude?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARKER:REFERence:AMPlitude?
            ```
        """
        return self._amplitude

    @property
    def frequency(self) -> MarkerReferenceFrequency:
        """Return the ``MARKER:REFERence:FREQuency`` command.

        Description:
            - This query returns the frequency of the Reference Marker, in Hz, when the frequency
              domain trace markers are on (using either the command ``MARKER:PEAK:STATE`` or
              ``MARKER:MANUAL``). This data is equivalent to the number that appears on the display
              next to the red R inside a triangle when markers areon. If all markers are off, the
              value returned will be the last value displayed.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:REFERence:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:REFERence:FREQuency?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARKER:REFERence:FREQuency?
            ```
        """
        return self._frequency


class MarkerPeakThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``MARKER:PEAK:THReshold`` command.

    Description:
        - This command specifies the threshold value of the automatic peak markers available for
          frequency domain traces. (Use the ``RF:UNITS`` command to specify the units.) Only peaks
          with an amplitude greater than the threshold value will qualify for automatic peak marker
          placement. To set the excursion value for the automatic markers, use the command
          ``MARKER:PEAK:EXCURSION``. To switch the automatic marker readout between absolute and
          delta, use the command ``MARKER:TYPE``. To turn on and set the number of automatic
          markers, use the commands ``MARKER:PEAK:STATE`` and ``MARKER:PEAK:MAXIMUM``. To list all
          of the peak markers, use the command ``SEARCH:SPECTRAL:LIST``

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:PEAK:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:PEAK:THReshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MARKER:PEAK:THReshold value`` command.

    SCPI Syntax:
        ```
        - MARKER:PEAK:THReshold <NR3>
        - MARKER:PEAK:THReshold?
        ```

    Info:
        - ``<NR3>`` is a floating point number that indicates the automatic marker threshold value.
    """


class MarkerPeakState(SCPICmdWrite, SCPICmdRead):
    """The ``MARKER:PEAK:STATE`` command.

    Description:
        - This command switches on or off the automatic peak markers that are available for
          frequency domain traces. There are up to 11 automatic markers. The maximum number of
          markers can be set using the command ``MARKER:PEAK:MAXIMUM``. The automatic peak markers
          find amplitude peaks based upon user threshold and excursion settings (set with the
          ``MARKER:PEAK:EXCURSION`` and ``MARKER:PEAK:THRESHOLD`` commands.) Each automatic marker
          has a readout associated with it. These can be absolute or delta readouts (set with the
          ``MARKER:TYPE`` command.) To list all of the peak markers, use the command
          ``SEARCH:SPECTRAL:LIST``

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:PEAK:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:PEAK:STATE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MARKER:PEAK:STATE value`` command.

    SCPI Syntax:
        ```
        - MARKER:PEAK:STATE {OFF|ON|0|1}
        - MARKER:PEAK:STATE?
        ```

    Info:
        - ``OFF`` or 0 turns the automatic peak markers off.
        - ``ON`` or 1 turns the automatic peak markers on.
    """


class MarkerPeakMaximum(SCPICmdWrite, SCPICmdRead):
    """The ``MARKER:PEAK:MAXimum`` command.

    Description:
        - This command specifies the maximum number of frequency domain trace peaks that could have
          automatic markers placed on them. This can be a number between 1 and 11. The default is 5.
          To turn on the automatic peak markers, use the command ``MARKER:PEAK:STATE``. To list all
          of the peak markers, use the command ``SEARCH:SPECTRAL:LIST The`` actual number of
          automatic markers may be less than the maximum, depending on the threshold and excursion
          values and the spectral content of the RF signal. If more peaks than the maximum are
          detected that meet the threshold and excursion criteria, only the highest amplitude peaks
          will have automatic markers placed on them.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:PEAK:MAXimum?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:PEAK:MAXimum?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MARKER:PEAK:MAXimum value`` command.

    SCPI Syntax:
        ```
        - MARKER:PEAK:MAXimum <NR1>
        - MARKER:PEAK:MAXimum?
        ```

    Info:
        - ``<NR1>`` is an integer that represents the maximum number of peaks that could have
          automatic markers.
    """


class MarkerPeakExcursion(SCPICmdWrite, SCPICmdRead):
    """The ``MARKER:PEAK:EXCURsion`` command.

    Description:
        - This command specifies the peak excursion value, in dB, for the frequency domain trace
          automatic peak markers. Peak excursion refers to how far an RF signal needs to fall in
          amplitude between marked peaks, in order to be considered another valid peak. If the peak
          excursion value is low, more peaks will tend to qualify as valid peaks and have associated
          markers. If the peak excursion value is high, fewer peaks will tend to qualify as valid
          peaks and have associated markers.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:PEAK:EXCURsion?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:PEAK:EXCURsion?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MARKER:PEAK:EXCURsion value`` command.

    SCPI Syntax:
        ```
        - MARKER:PEAK:EXCURsion <NR3>
        - MARKER:PEAK:EXCURsion?
        ```

    Info:
        - ``<NR3>`` is a floating point number that specifies the automatic marker excursion value.
    """


class MarkerPeak(SCPICmdRead):
    """The ``MARKER:PEAK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:PEAK?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:PEAK?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.excursion``: The ``MARKER:PEAK:EXCURsion`` command.
        - ``.maximum``: The ``MARKER:PEAK:MAXimum`` command.
        - ``.state``: The ``MARKER:PEAK:STATE`` command.
        - ``.threshold``: The ``MARKER:PEAK:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._excursion = MarkerPeakExcursion(device, f"{self._cmd_syntax}:EXCURsion")
        self._maximum = MarkerPeakMaximum(device, f"{self._cmd_syntax}:MAXimum")
        self._state = MarkerPeakState(device, f"{self._cmd_syntax}:STATE")
        self._threshold = MarkerPeakThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def excursion(self) -> MarkerPeakExcursion:
        """Return the ``MARKER:PEAK:EXCURsion`` command.

        Description:
            - This command specifies the peak excursion value, in dB, for the frequency domain trace
              automatic peak markers. Peak excursion refers to how far an RF signal needs to fall in
              amplitude between marked peaks, in order to be considered another valid peak. If the
              peak excursion value is low, more peaks will tend to qualify as valid peaks and have
              associated markers. If the peak excursion value is high, fewer peaks will tend to
              qualify as valid peaks and have associated markers.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:PEAK:EXCURsion?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:PEAK:EXCURsion?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MARKER:PEAK:EXCURsion value``
              command.

        SCPI Syntax:
            ```
            - MARKER:PEAK:EXCURsion <NR3>
            - MARKER:PEAK:EXCURsion?
            ```

        Info:
            - ``<NR3>`` is a floating point number that specifies the automatic marker excursion
              value.
        """
        return self._excursion

    @property
    def maximum(self) -> MarkerPeakMaximum:
        """Return the ``MARKER:PEAK:MAXimum`` command.

        Description:
            - This command specifies the maximum number of frequency domain trace peaks that could
              have automatic markers placed on them. This can be a number between 1 and 11. The
              default is 5. To turn on the automatic peak markers, use the command
              ``MARKER:PEAK:STATE``. To list all of the peak markers, use the command
              ``SEARCH:SPECTRAL:LIST The`` actual number of automatic markers may be less than the
              maximum, depending on the threshold and excursion values and the spectral content of
              the RF signal. If more peaks than the maximum are detected that meet the threshold and
              excursion criteria, only the highest amplitude peaks will have automatic markers
              placed on them.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:PEAK:MAXimum?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:PEAK:MAXimum?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MARKER:PEAK:MAXimum value``
              command.

        SCPI Syntax:
            ```
            - MARKER:PEAK:MAXimum <NR1>
            - MARKER:PEAK:MAXimum?
            ```

        Info:
            - ``<NR1>`` is an integer that represents the maximum number of peaks that could have
              automatic markers.
        """
        return self._maximum

    @property
    def state(self) -> MarkerPeakState:
        """Return the ``MARKER:PEAK:STATE`` command.

        Description:
            - This command switches on or off the automatic peak markers that are available for
              frequency domain traces. There are up to 11 automatic markers. The maximum number of
              markers can be set using the command ``MARKER:PEAK:MAXIMUM``. The automatic peak
              markers find amplitude peaks based upon user threshold and excursion settings (set
              with the ``MARKER:PEAK:EXCURSION`` and ``MARKER:PEAK:THRESHOLD`` commands.) Each
              automatic marker has a readout associated with it. These can be absolute or delta
              readouts (set with the ``MARKER:TYPE`` command.) To list all of the peak markers, use
              the command ``SEARCH:SPECTRAL:LIST``

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:PEAK:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:PEAK:STATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MARKER:PEAK:STATE value`` command.

        SCPI Syntax:
            ```
            - MARKER:PEAK:STATE {OFF|ON|0|1}
            - MARKER:PEAK:STATE?
            ```

        Info:
            - ``OFF`` or 0 turns the automatic peak markers off.
            - ``ON`` or 1 turns the automatic peak markers on.
        """
        return self._state

    @property
    def threshold(self) -> MarkerPeakThreshold:
        """Return the ``MARKER:PEAK:THReshold`` command.

        Description:
            - This command specifies the threshold value of the automatic peak markers available for
              frequency domain traces. (Use the ``RF:UNITS`` command to specify the units.) Only
              peaks with an amplitude greater than the threshold value will qualify for automatic
              peak marker placement. To set the excursion value for the automatic markers, use the
              command ``MARKER:PEAK:EXCURSION``. To switch the automatic marker readout between
              absolute and delta, use the command ``MARKER:TYPE``. To turn on and set the number of
              automatic markers, use the commands ``MARKER:PEAK:STATE`` and ``MARKER:PEAK:MAXIMUM``.
              To list all of the peak markers, use the command ``SEARCH:SPECTRAL:LIST``

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:PEAK:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:PEAK:THReshold?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MARKER:PEAK:THReshold value``
              command.

        SCPI Syntax:
            ```
            - MARKER:PEAK:THReshold <NR3>
            - MARKER:PEAK:THReshold?
            ```

        Info:
            - ``<NR3>`` is a floating point number that indicates the automatic marker threshold
              value.
        """
        return self._threshold


class MarkerManual(SCPICmdWrite, SCPICmdRead):
    """The ``MARKER:MANual`` command.

    Description:
        - This command switches on or off the manual markers a and b that are available for
          frequency domain traces. Two manual markers are available for measuring non-peak areas of
          interest. The absolute measurements are in dBm; the relative measurements (relative to the
          Reference Marker) are in dBc (dB relative to the carrier). When the manual markers are
          turned off, and the peak markers are turned on, the Reference Marker is placed on the
          highest amplitude peak. With manual markers on, the Reference Marker is placed at the a
          manual marker. The manual markers use the units specified with the command ``RF:UNITS``.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:MANual?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:MANual?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MARKER:MANual value`` command.

    SCPI Syntax:
        ```
        - MARKER:MANual {OFF|ON|0|1}
        - MARKER:MANual?
        ```

    Info:
        - ``OFF`` or 0 turns the manual markers off.
        - ``ON`` or 1 turns the manual markers on.
    """


class MarkerMItemPhasenoise(SCPICmdRead):
    """The ``MARKER:M<x>:PHASENoise`` command.

    Description:
        - This command returns the phase noise of the ``RF_NORMal`` trace at the specified marker
          position in dBc/Hz units.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:M<x>:PHASENoise?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:PHASENoise?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARKER:M<x>:PHASENoise?
        ```
    """


class MarkerMItemNoisedensity(SCPICmdRead):
    """The ``MARKER:M<x>:NOISEDensity`` command.

    Description:
        - This command returns the noise density of the ``RF_NORMal`` trace at the specified marker
          position in <RF Units>/Hz units, where <RF Units> are the units specified by the command
          ``RF:UNITS``.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:M<x>:NOISEDensity?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:NOISEDensity?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARKER:M<x>:NOISEDensity?
        ```
    """


class MarkerMItemFrequencyDelta(SCPICmdRead):
    """The ``MARKER:M<x>:FREQuency:DELTa`` command.

    Description:
        - This query returns the delta frequency (horizontal) value of either of the two manual
          markers that are available for frequency domain traces, in relation to the Reference
          Marker. M<x> can be either M1, which specifies manual marker a, or M2, which specifies
          manual marker b. The manual marker readouts use the units specified with the command
          ``RF:UNITS``.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:M<x>:FREQuency:DELTa?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:FREQuency:DELTa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARKER:M<x>:FREQuency:DELTa?
        ```
    """


class MarkerMItemFrequencyAbsolute(SCPICmdWrite, SCPICmdRead):
    """The ``MARKER:M<x>:FREQuency:ABSolute`` command.

    Description:
        - This command specifies the actual frequency (horizontal) value of either of the two manual
          markers that are available for frequency domain traces. M<x> can be either M1, which
          specifies manual marker a, or M2, which specifies manual marker b.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:M<x>:FREQuency:ABSolute?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:FREQuency:ABSolute?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MARKER:M<x>:FREQuency:ABSolute value``
          command.

    SCPI Syntax:
        ```
        - MARKER:M<x>:FREQuency:ABSolute <NR3>
        - MARKER:M<x>:FREQuency:ABSolute?
        ```

    Info:
        - ``<NR3>`` is a floating point value that indicates the actual frequency of either of the
          two manual markers.
    """


class MarkerMItemFrequency(SCPICmdRead):
    """The ``MARKER:M<x>:FREQuency`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:M<x>:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:FREQuency?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absolute``: The ``MARKER:M<x>:FREQuency:ABSolute`` command.
        - ``.delta``: The ``MARKER:M<x>:FREQuency:DELTa`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = MarkerMItemFrequencyAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._delta = MarkerMItemFrequencyDelta(device, f"{self._cmd_syntax}:DELTa")

    @property
    def absolute(self) -> MarkerMItemFrequencyAbsolute:
        """Return the ``MARKER:M<x>:FREQuency:ABSolute`` command.

        Description:
            - This command specifies the actual frequency (horizontal) value of either of the two
              manual markers that are available for frequency domain traces. M<x> can be either M1,
              which specifies manual marker a, or M2, which specifies manual marker b.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:M<x>:FREQuency:ABSolute?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:FREQuency:ABSolute?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``MARKER:M<x>:FREQuency:ABSolute value`` command.

        SCPI Syntax:
            ```
            - MARKER:M<x>:FREQuency:ABSolute <NR3>
            - MARKER:M<x>:FREQuency:ABSolute?
            ```

        Info:
            - ``<NR3>`` is a floating point value that indicates the actual frequency of either of
              the two manual markers.
        """
        return self._absolute

    @property
    def delta(self) -> MarkerMItemFrequencyDelta:
        """Return the ``MARKER:M<x>:FREQuency:DELTa`` command.

        Description:
            - This query returns the delta frequency (horizontal) value of either of the two manual
              markers that are available for frequency domain traces, in relation to the Reference
              Marker. M<x> can be either M1, which specifies manual marker a, or M2, which specifies
              manual marker b. The manual marker readouts use the units specified with the command
              ``RF:UNITS``.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:M<x>:FREQuency:DELTa?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:FREQuency:DELTa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARKER:M<x>:FREQuency:DELTa?
            ```
        """
        return self._delta


class MarkerMItemAmplitudeDelta(SCPICmdRead):
    """The ``MARKER:M<x>:AMPLitude:DELTa`` command.

    Description:
        - This query returns the delta amplitude (vertical) value of either of the two manual
          markers that are available for frequency domain traces, in relation to the Reference
          Marker. M<x> can be either M1, which specifies manual marker a, or M2, which specifies
          manual marker b.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:M<x>:AMPLitude:DELTa?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:AMPLitude:DELTa?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARKER:M<x>:AMPLitude:DELTa?
        ```
    """


class MarkerMItemAmplitudeAbsolute(SCPICmdRead):
    """The ``MARKER:M<x>:AMPLitude:ABSolute`` command.

    Description:
        - This query returns the actual amplitude (vertical) value of either of the two manual
          markers that are available for frequency domain traces, in user-set units. M<x> can be
          either M1, which specifies manual marker a, or M2, which specifies manual marker b. (Use
          ``RF:UNITS`` to specify the units.)

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:M<x>:AMPLitude:ABSolute?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:AMPLitude:ABSolute?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - MARKER:M<x>:AMPLitude:ABSolute?
        ```
    """


class MarkerMItemAmplitude(SCPICmdRead):
    """The ``MARKER:M<x>:AMPLitude`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:M<x>:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:AMPLitude?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.absolute``: The ``MARKER:M<x>:AMPLitude:ABSolute`` command.
        - ``.delta``: The ``MARKER:M<x>:AMPLitude:DELTa`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._absolute = MarkerMItemAmplitudeAbsolute(device, f"{self._cmd_syntax}:ABSolute")
        self._delta = MarkerMItemAmplitudeDelta(device, f"{self._cmd_syntax}:DELTa")

    @property
    def absolute(self) -> MarkerMItemAmplitudeAbsolute:
        """Return the ``MARKER:M<x>:AMPLitude:ABSolute`` command.

        Description:
            - This query returns the actual amplitude (vertical) value of either of the two manual
              markers that are available for frequency domain traces, in user-set units. M<x> can be
              either M1, which specifies manual marker a, or M2, which specifies manual marker b.
              (Use ``RF:UNITS`` to specify the units.)

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:M<x>:AMPLitude:ABSolute?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:AMPLitude:ABSolute?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARKER:M<x>:AMPLitude:ABSolute?
            ```
        """
        return self._absolute

    @property
    def delta(self) -> MarkerMItemAmplitudeDelta:
        """Return the ``MARKER:M<x>:AMPLitude:DELTa`` command.

        Description:
            - This query returns the delta amplitude (vertical) value of either of the two manual
              markers that are available for frequency domain traces, in relation to the Reference
              Marker. M<x> can be either M1, which specifies manual marker a, or M2, which specifies
              manual marker b.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:M<x>:AMPLitude:DELTa?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:AMPLitude:DELTa?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARKER:M<x>:AMPLitude:DELTa?
            ```
        """
        return self._delta


class MarkerMItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``MARKER:M<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER:M<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER:M<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``MARKER:M<x>:AMPLitude`` command tree.
        - ``.frequency``: The ``MARKER:M<x>:FREQuency`` command tree.
        - ``.noisedensity``: The ``MARKER:M<x>:NOISEDensity`` command.
        - ``.phasenoise``: The ``MARKER:M<x>:PHASENoise`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = MarkerMItemAmplitude(device, f"{self._cmd_syntax}:AMPLitude")
        self._frequency = MarkerMItemFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._noisedensity = MarkerMItemNoisedensity(device, f"{self._cmd_syntax}:NOISEDensity")
        self._phasenoise = MarkerMItemPhasenoise(device, f"{self._cmd_syntax}:PHASENoise")

    @property
    def amplitude(self) -> MarkerMItemAmplitude:
        """Return the ``MARKER:M<x>:AMPLitude`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:M<x>:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:AMPLitude?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.absolute``: The ``MARKER:M<x>:AMPLitude:ABSolute`` command.
            - ``.delta``: The ``MARKER:M<x>:AMPLitude:DELTa`` command.
        """
        return self._amplitude

    @property
    def frequency(self) -> MarkerMItemFrequency:
        """Return the ``MARKER:M<x>:FREQuency`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:M<x>:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:FREQuency?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.absolute``: The ``MARKER:M<x>:FREQuency:ABSolute`` command.
            - ``.delta``: The ``MARKER:M<x>:FREQuency:DELTa`` command.
        """
        return self._frequency

    @property
    def noisedensity(self) -> MarkerMItemNoisedensity:
        """Return the ``MARKER:M<x>:NOISEDensity`` command.

        Description:
            - This command returns the noise density of the ``RF_NORMal`` trace at the specified
              marker position in <RF Units>/Hz units, where <RF Units> are the units specified by
              the command ``RF:UNITS``.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:M<x>:NOISEDensity?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:NOISEDensity?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARKER:M<x>:NOISEDensity?
            ```
        """
        return self._noisedensity

    @property
    def phasenoise(self) -> MarkerMItemPhasenoise:
        """Return the ``MARKER:M<x>:PHASENoise`` command.

        Description:
            - This command returns the phase noise of the ``RF_NORMal`` trace at the specified
              marker position in dBc/Hz units.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:M<x>:PHASENoise?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:M<x>:PHASENoise?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - MARKER:M<x>:PHASENoise?
            ```
        """
        return self._phasenoise


class Marker(SCPICmdRead):
    """The ``MARKER`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MARKER?`` query.
        - Using the ``.verify(value)`` method will send the ``MARKER?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.m``: The ``MARKER:M<x>`` command tree.
        - ``.manual``: The ``MARKER:MANual`` command.
        - ``.peak``: The ``MARKER:PEAK`` command tree.
        - ``.reference``: The ``MARKER:REFERence`` command.
        - ``.type``: The ``MARKER:TYPe`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MARKER") -> None:
        super().__init__(device, cmd_syntax)
        self._m: Dict[int, MarkerMItem] = DefaultDictPassKeyToFactory(
            lambda x: MarkerMItem(device, f"{self._cmd_syntax}:M{x}")
        )
        self._manual = MarkerManual(device, f"{self._cmd_syntax}:MANual")
        self._peak = MarkerPeak(device, f"{self._cmd_syntax}:PEAK")
        self._reference = MarkerReference(device, f"{self._cmd_syntax}:REFERence")
        self._type = MarkerType(device, f"{self._cmd_syntax}:TYPe")

    @property
    def m(self) -> Dict[int, MarkerMItem]:
        """Return the ``MARKER:M<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:M<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:M<x>?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``MARKER:M<x>:AMPLitude`` command tree.
            - ``.frequency``: The ``MARKER:M<x>:FREQuency`` command tree.
            - ``.noisedensity``: The ``MARKER:M<x>:NOISEDensity`` command.
            - ``.phasenoise``: The ``MARKER:M<x>:PHASENoise`` command.
        """
        return self._m

    @property
    def manual(self) -> MarkerManual:
        """Return the ``MARKER:MANual`` command.

        Description:
            - This command switches on or off the manual markers a and b that are available for
              frequency domain traces. Two manual markers are available for measuring non-peak areas
              of interest. The absolute measurements are in dBm; the relative measurements (relative
              to the Reference Marker) are in dBc (dB relative to the carrier). When the manual
              markers are turned off, and the peak markers are turned on, the Reference Marker is
              placed on the highest amplitude peak. With manual markers on, the Reference Marker is
              placed at the a manual marker. The manual markers use the units specified with the
              command ``RF:UNITS``.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:MANual?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:MANual?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MARKER:MANual value`` command.

        SCPI Syntax:
            ```
            - MARKER:MANual {OFF|ON|0|1}
            - MARKER:MANual?
            ```

        Info:
            - ``OFF`` or 0 turns the manual markers off.
            - ``ON`` or 1 turns the manual markers on.
        """
        return self._manual

    @property
    def peak(self) -> MarkerPeak:
        """Return the ``MARKER:PEAK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:PEAK?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:PEAK?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.excursion``: The ``MARKER:PEAK:EXCURsion`` command.
            - ``.maximum``: The ``MARKER:PEAK:MAXimum`` command.
            - ``.state``: The ``MARKER:PEAK:STATE`` command.
            - ``.threshold``: The ``MARKER:PEAK:THReshold`` command.
        """
        return self._peak

    @property
    def reference(self) -> MarkerReference:
        """Return the ``MARKER:REFERence`` command.

        Description:
            - This command changes the Center Frequency to the frequency indicated by the Reference
              Marker, in effect moving the Reference Marker to the center of the screen. This
              applies when markers are turned on (using the command ``MARKER:PEAK:STATE`` or
              ``MARKER:MANUAL``). This is equivalent to the 'R' to Center side menu button in the
              front panel Markers menu.

        Usage:
            - Using the ``.write(value)`` method will send the ``MARKER:REFERence value`` command.

        SCPI Syntax:
            ```
            - MARKER:REFERence CENTER
            ```

        Sub-properties:
            - ``.amplitude``: The ``MARKER:REFERence:AMPlitude`` command.
            - ``.frequency``: The ``MARKER:REFERence:FREQuency`` command.
        """
        return self._reference

    @property
    def type(self) -> MarkerType:
        """Return the ``MARKER:TYPe`` command.

        Description:
            - This command specifies the marker type (either DELTa or ABSolute). An absolute marker
              shows the frequency and amplitude at the location of the marker. A delta marker shows
              the frequency and amplitude of the marker relative to the Reference Marker. The
              Reference Marker shows the absolute frequency and amplitude, regardless of this
              command. The marker amplitude measurements are in dBm for absolute, or in dBc (dB
              below carrier amplitude) for delta.

        Usage:
            - Using the ``.query()`` method will send the ``MARKER:TYPe?`` query.
            - Using the ``.verify(value)`` method will send the ``MARKER:TYPe?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MARKER:TYPe value`` command.

        SCPI Syntax:
            ```
            - MARKER:TYPe {DELTa|ABSolute}
            - MARKER:TYPe?
            ```

        Info:
            - ``DELTa`` specifies to display the frequency and amplitude of the markers relative to
              the Reference Marker. The relative amplitude is in dBc (dB below carrier amplitude);
              the relative frequency is in Hz.
            - ``ABSolute`` specifies to display the actual frequency and amplitude of each marker.
              The absolute amplitude is in user-set units; the absolute frequency is in Hz.
        """
        return self._type
