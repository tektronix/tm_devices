"""The instrument commands module.

These commands are used in the following models:
AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - INSTrument:COUPle:SOURce {0|1|OFF|ON}
    - INSTrument:COUPle:SOURce?
    - INSTrument:MODE {AWG|FGEN}
    - INSTrument:MODE?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class InstrumentMode(SCPICmdWrite, SCPICmdRead):
    """The ``INSTrument:MODE`` command.

    Description:
        - This command sets or returns the AWG mode, either the AWG mode or the Function generator
          mode.

    Usage:
        - Using the ``.query()`` method will send the ``INSTrument:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``INSTrument:MODE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``INSTrument:MODE value`` command.

    SCPI Syntax:
        ```
        - INSTrument:MODE {AWG|FGEN}
        - INSTrument:MODE?
        ```

    Info:
        - ``AWG`` sets the instrument to the Arbitrary Waveform Generator mode.FGEN sets the
          instrument to the Function generator mode.
        - ``*RST`` sets this to AWG.
    """


class InstrumentCoupleSource(SCPICmdWrite, SCPICmdRead):
    """The ``INSTrument:COUPle:SOURce`` command.

    Description:
        - This command sets or returns the coupled state of the channel's Analog and Marker output
          controls of multi channel instruments. The set form of this command forces channel 2 to
          match channel 1. After the initial coupling of the settings, changes made to either
          channel 1 or channel 2 amplitude settings affect both channels.

    Usage:
        - Using the ``.query()`` method will send the ``INSTrument:COUPle:SOURce?`` query.
        - Using the ``.verify(value)`` method will send the ``INSTrument:COUPle:SOURce?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``INSTrument:COUPle:SOURce value``
          command.

    SCPI Syntax:
        ```
        - INSTrument:COUPle:SOURce {0|1|OFF|ON}
        - INSTrument:COUPle:SOURce?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class InstrumentCouple(SCPICmdRead):
    """The ``INSTrument:COUPle`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``INSTrument:COUPle?`` query.
        - Using the ``.verify(value)`` method will send the ``INSTrument:COUPle?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``INSTrument:COUPle:SOURce`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = InstrumentCoupleSource(device, f"{self._cmd_syntax}:SOURce")

    @property
    def source(self) -> InstrumentCoupleSource:
        """Return the ``INSTrument:COUPle:SOURce`` command.

        Description:
            - This command sets or returns the coupled state of the channel's Analog and Marker
              output controls of multi channel instruments. The set form of this command forces
              channel 2 to match channel 1. After the initial coupling of the settings, changes made
              to either channel 1 or channel 2 amplitude settings affect both channels.

        Usage:
            - Using the ``.query()`` method will send the ``INSTrument:COUPle:SOURce?`` query.
            - Using the ``.verify(value)`` method will send the ``INSTrument:COUPle:SOURce?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``INSTrument:COUPle:SOURce value``
              command.

        SCPI Syntax:
            ```
            - INSTrument:COUPle:SOURce {0|1|OFF|ON}
            - INSTrument:COUPle:SOURce?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._source


class Instrument(SCPICmdRead):
    """The ``INSTrument`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``INSTrument?`` query.
        - Using the ``.verify(value)`` method will send the ``INSTrument?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.couple``: The ``INSTrument:COUPle`` command tree.
        - ``.mode``: The ``INSTrument:MODE`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "INSTrument"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._couple = InstrumentCouple(device, f"{self._cmd_syntax}:COUPle")
        self._mode = InstrumentMode(device, f"{self._cmd_syntax}:MODE")

    @property
    def couple(self) -> InstrumentCouple:
        """Return the ``INSTrument:COUPle`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``INSTrument:COUPle?`` query.
            - Using the ``.verify(value)`` method will send the ``INSTrument:COUPle?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``INSTrument:COUPle:SOURce`` command.
        """
        return self._couple

    @property
    def mode(self) -> InstrumentMode:
        """Return the ``INSTrument:MODE`` command.

        Description:
            - This command sets or returns the AWG mode, either the AWG mode or the Function
              generator mode.

        Usage:
            - Using the ``.query()`` method will send the ``INSTrument:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``INSTrument:MODE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``INSTrument:MODE value`` command.

        SCPI Syntax:
            ```
            - INSTrument:MODE {AWG|FGEN}
            - INSTrument:MODE?
            ```

        Info:
            - ``AWG`` sets the instrument to the Arbitrary Waveform Generator mode.FGEN sets the
              instrument to the Function generator mode.
            - ``*RST`` sets this to AWG.
        """
        return self._mode
