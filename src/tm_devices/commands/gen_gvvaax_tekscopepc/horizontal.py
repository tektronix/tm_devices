"""The horizontal commands module.

These commands are used in the following models:
TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - HORizontal:DELay:MODe {ON|OFF|<NR1>}
    - HORizontal:DELay:MODe?
    - HORizontal:DELay:TIMe <NR3>
    - HORizontal:DELay:TIMe?
    - HORizontal:MODe {AUTO|MANual}
    - HORizontal:MODe:MANual:CONFIGure {HORIZontalscale|RECORDLength}
    - HORizontal:MODe:MANual:CONFIGure?
    - HORizontal:MODe?
    - HORizontal:POSition <NR3>
    - HORizontal:POSition?
    - HORizontal:SAMPLERate <NR3>
    - HORizontal:SAMPLERate?
    - HORizontal:SCAle <NR3>
    - HORizontal:SCAle?
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
        - ``.manual``: The ``HORizontal:MODe:MANual`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._manual = HorizontalModeManual(device, f"{self._cmd_syntax}:MANual")

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
    """The ``HORizontal`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``HORizontal?`` query.
        - Using the ``.verify(value)`` method will send the ``HORizontal?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delay``: The ``HORizontal:DELay`` command tree.
        - ``.mode``: The ``HORizontal:MODe`` command.
        - ``.position``: The ``HORizontal:POSition`` command.
        - ``.samplerate``: The ``HORizontal:SAMPLERate`` command.
        - ``.scale``: The ``HORizontal:SCAle`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "HORizontal"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._delay = HorizontalDelay(device, f"{self._cmd_syntax}:DELay")
        self._mode = HorizontalMode(device, f"{self._cmd_syntax}:MODe")
        self._position = HorizontalPosition(device, f"{self._cmd_syntax}:POSition")
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
            - ``.manual``: The ``HORizontal:MODe:MANual`` command tree.
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
