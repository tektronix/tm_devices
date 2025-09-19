"""The fgen commands module.

These commands are used in the following models:
AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FGEN:CHANnel[n]:AMPLitude:POWer <NRf>
    - FGEN:CHANnel[n]:AMPLitude:POWer?
    - FGEN:CHANnel[n]:AMPLitude:VOLTage <NRf>
    - FGEN:CHANnel[n]:AMPLitude:VOLTage?
    - FGEN:CHANnel[n]:DCLevel <NRf>
    - FGEN:CHANnel[n]:DCLevel?
    - FGEN:CHANnel[n]:FREQuency <NRf>
    - FGEN:CHANnel[n]:FREQuency?
    - FGEN:CHANnel[n]:HIGH <NRf>
    - FGEN:CHANnel[n]:HIGH?
    - FGEN:CHANnel[n]:LOW <NRf>
    - FGEN:CHANnel[n]:LOW?
    - FGEN:CHANnel[n]:OFFSet <NR3>
    - FGEN:CHANnel[n]:OFFSet?
    - FGEN:CHANnel[n]:PATH {DIRect|DCAMplified|AC}
    - FGEN:CHANnel[n]:PATH?
    - FGEN:CHANnel[n]:PERiod?
    - FGEN:CHANnel[n]:PHASe <NRf>
    - FGEN:CHANnel[n]:PHASe?
    - FGEN:CHANnel[n]:SYMMetry <NR1>
    - FGEN:CHANnel[n]:SYMMetry?
    - FGEN:CHANnel[n]:TYPE {SINE|SQUare|TRIangle|NOISe|DC|GAUSsian|EXPRise|EXPDecay|NONE}
    - FGEN:CHANnel[n]:TYPE?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import DefaultDictPassKeyToFactory, SCPICmdRead, SCPICmdWrite, ValidatedChannel

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class FgenChannelItemType(SCPICmdWrite, SCPICmdRead):
    """The ``FGEN:CHANnel[n]:TYPE`` command.

    Description:
        - This command sets or returns the function generator's waveform type (shape) for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:TYPE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:TYPE value`` command.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:TYPE {SINE|SQUare|TRIangle|NOISe|DC|GAUSsian|EXPRise|EXPDecay|NONE}
        - FGEN:CHANnel[n]:TYPE?
        ```

    Info:
        - ``*RST`` sets this to SINE.
    """


class FgenChannelItemSymmetry(SCPICmdWrite, SCPICmdRead):
    """The ``FGEN:CHANnel[n]:SYMMetry`` command.

    Description:
        - This command sets or returns the function generator's triangle waveform symmetry value for
          the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:SYMMetry?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:SYMMetry?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:SYMMetry value``
          command.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:SYMMetry <NR1>
        - FGEN:CHANnel[n]:SYMMetry?
        ```

    Info:
        - ``*RST`` sets this to 100.
    """


class FgenChannelItemPhase(SCPICmdWrite, SCPICmdRead):
    """The ``FGEN:CHANnel[n]:PHASe`` command.

    Description:
        - This command sets or returns the function generator's waveform phase value for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:PHASe?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:PHASe?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:PHASe value`` command.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:PHASe <NRf>
        - FGEN:CHANnel[n]:PHASe?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class FgenChannelItemPeriod(SCPICmdRead):
    """The ``FGEN:CHANnel[n]:PERiod`` command.

    Description:
        - This command returns the function generator's waveform period for the specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:PERiod?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:PERiod?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:PERiod?
        ```
    """


class FgenChannelItemPath(SCPICmdWrite, SCPICmdRead):
    """The ``FGEN:CHANnel[n]:PATH`` command.

    Description:
        - This command sets or returns the function generator's signal path for the specified
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:PATH?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:PATH?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:PATH value`` command.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:PATH {DIRect|DCAMplified|AC}
        - FGEN:CHANnel[n]:PATH?
        ```
    """


class FgenChannelItemOffset(SCPICmdWrite, SCPICmdRead):
    """The ``FGEN:CHANnel[n]:OFFSet`` command.

    Description:
        - This command sets or returns the function generator's waveform offset value for the
          specified channel. If the offset value is higher than the designated maximum offset or
          lower than the designated minimum offset, then the respective max/min values are used.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:OFFSet?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:OFFSet?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:OFFSet value`` command.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:OFFSet <NR3>
        - FGEN:CHANnel[n]:OFFSet?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class FgenChannelItemLow(SCPICmdWrite, SCPICmdRead):
    """The ``FGEN:CHANnel[n]:LOW`` command.

    Description:
        - This command sets or returns the function generator's waveform low voltage value for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:LOW?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:LOW?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:LOW value`` command.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:LOW <NRf>
        - FGEN:CHANnel[n]:LOW?
        ```

    Info:
        - ``*RST`` sets this to -250 mV.
    """


class FgenChannelItemHigh(SCPICmdWrite, SCPICmdRead):
    """The ``FGEN:CHANnel[n]:HIGH`` command.

    Description:
        - This command sets or returns the function generator's waveform high voltage value for the
          specified channel.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:HIGH?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:HIGH?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:HIGH value`` command.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:HIGH <NRf>
        - FGEN:CHANnel[n]:HIGH?
        ```

    Info:
        - ``*RST`` sets this to 250 mV.
    """


class FgenChannelItemFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``FGEN:CHANnel[n]:FREQuency`` command.

    Description:
        - This command sets or returns the function generator's waveform frequency for the specified
          channel. All channels on a multi-channel instrument use the same frequency setting.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:FREQuency?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:FREQuency value``
          command.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:FREQuency <NRf>
        - FGEN:CHANnel[n]:FREQuency?
        ```

    Info:
        - ``*RST`` sets this to 1.2 MHz.
    """


class FgenChannelItemDclevel(SCPICmdWrite, SCPICmdRead):
    """The ``FGEN:CHANnel[n]:DCLevel`` command.

    Description:
        - This command sets or returns the DC level of the generated waveform for the specified
          channel.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:DCLevel?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:DCLevel?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:DCLevel value``
          command.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:DCLevel <NRf>
        - FGEN:CHANnel[n]:DCLevel?
        ```

    Info:
        - ``*RST`` sets this to 0.
    """


class FgenChannelItemAmplitudeVoltage(SCPICmdWrite, SCPICmdRead):
    """The ``FGEN:CHANnel[n]:AMPLitude:VOLTage`` command.

    Description:
        - This command sets or returns the function generator's waveform amplitude value for the
          specified channel in units of volts.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:AMPLitude:VOLTage?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:AMPLitude:VOLTage?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``FGEN:CHANnel[n]:AMPLitude:VOLTage value`` command.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:AMPLitude:VOLTage <NRf>
        - FGEN:CHANnel[n]:AMPLitude:VOLTage?
        ```

    Info:
        - ``*RST`` sets this to 500 mV.
    """


class FgenChannelItemAmplitudePower(SCPICmdWrite, SCPICmdRead):
    """The ``FGEN:CHANnel[n]:AMPLitude:POWer`` command.

    Description:
        - This command sets or returns the function generator's waveform amplitude value for the
          specified channel in units of dBm.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:AMPLitude:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:AMPLitude:POWer?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:AMPLitude:POWer value``
          command.

    SCPI Syntax:
        ```
        - FGEN:CHANnel[n]:AMPLitude:POWer <NRf>
        - FGEN:CHANnel[n]:AMPLitude:POWer?
        ```
    """


class FgenChannelItemAmplitude(SCPICmdRead):
    """The ``FGEN:CHANnel[n]:AMPLitude`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:AMPLitude?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.power``: The ``FGEN:CHANnel[n]:AMPLitude:POWer`` command.
        - ``.voltage``: The ``FGEN:CHANnel[n]:AMPLitude:VOLTage`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._power = FgenChannelItemAmplitudePower(device, f"{self._cmd_syntax}:POWer")
        self._voltage = FgenChannelItemAmplitudeVoltage(device, f"{self._cmd_syntax}:VOLTage")

    @property
    def power(self) -> FgenChannelItemAmplitudePower:
        """Return the ``FGEN:CHANnel[n]:AMPLitude:POWer`` command.

        Description:
            - This command sets or returns the function generator's waveform amplitude value for the
              specified channel in units of dBm.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:AMPLitude:POWer?``
              query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:AMPLitude:POWer?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``FGEN:CHANnel[n]:AMPLitude:POWer value`` command.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:AMPLitude:POWer <NRf>
            - FGEN:CHANnel[n]:AMPLitude:POWer?
            ```
        """
        return self._power

    @property
    def voltage(self) -> FgenChannelItemAmplitudeVoltage:
        """Return the ``FGEN:CHANnel[n]:AMPLitude:VOLTage`` command.

        Description:
            - This command sets or returns the function generator's waveform amplitude value for the
              specified channel in units of volts.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:AMPLitude:VOLTage?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``FGEN:CHANnel[n]:AMPLitude:VOLTage?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``FGEN:CHANnel[n]:AMPLitude:VOLTage value`` command.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:AMPLitude:VOLTage <NRf>
            - FGEN:CHANnel[n]:AMPLitude:VOLTage?
            ```

        Info:
            - ``*RST`` sets this to 500 mV.
        """
        return self._voltage


#  pylint: disable=too-many-instance-attributes
class FgenChannelItem(ValidatedChannel, SCPICmdRead):
    """The ``FGEN:CHANnel[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``FGEN:CHANnel[n]:AMPLitude`` command tree.
        - ``.path``: The ``FGEN:CHANnel[n]:PATH`` command.
        - ``.dclevel``: The ``FGEN:CHANnel[n]:DCLevel`` command.
        - ``.frequency``: The ``FGEN:CHANnel[n]:FREQuency`` command.
        - ``.high``: The ``FGEN:CHANnel[n]:HIGH`` command.
        - ``.low``: The ``FGEN:CHANnel[n]:LOW`` command.
        - ``.offset``: The ``FGEN:CHANnel[n]:OFFSet`` command.
        - ``.period``: The ``FGEN:CHANnel[n]:PERiod`` command.
        - ``.phase``: The ``FGEN:CHANnel[n]:PHASe`` command.
        - ``.symmetry``: The ``FGEN:CHANnel[n]:SYMMetry`` command.
        - ``.type``: The ``FGEN:CHANnel[n]:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._path = FgenChannelItemPath(device, f"{self._cmd_syntax}:PATH")
        self._amplitude = FgenChannelItemAmplitude(device, f"{self._cmd_syntax}:AMPLitude")
        self._dclevel = FgenChannelItemDclevel(device, f"{self._cmd_syntax}:DCLevel")
        self._frequency = FgenChannelItemFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._high = FgenChannelItemHigh(device, f"{self._cmd_syntax}:HIGH")
        self._low = FgenChannelItemLow(device, f"{self._cmd_syntax}:LOW")
        self._offset = FgenChannelItemOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._period = FgenChannelItemPeriod(device, f"{self._cmd_syntax}:PERiod")
        self._phase = FgenChannelItemPhase(device, f"{self._cmd_syntax}:PHASe")
        self._symmetry = FgenChannelItemSymmetry(device, f"{self._cmd_syntax}:SYMMetry")
        self._type = FgenChannelItemType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def path(self) -> FgenChannelItemPath:
        """Return the ``FGEN:CHANnel[n]:PATH`` command.

        Description:
            - This command sets or returns the function generator's signal path for the specified
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:PATH?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:PATH?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:PATH value``
              command.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:PATH {DIRect|DCAMplified|AC}
            - FGEN:CHANnel[n]:PATH?
            ```
        """
        return self._path

    @property
    def amplitude(self) -> FgenChannelItemAmplitude:
        """Return the ``FGEN:CHANnel[n]:AMPLitude`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:AMPLitude?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.power``: The ``FGEN:CHANnel[n]:AMPLitude:POWer`` command.
            - ``.voltage``: The ``FGEN:CHANnel[n]:AMPLitude:VOLTage`` command.
        """
        return self._amplitude

    @property
    def dclevel(self) -> FgenChannelItemDclevel:
        """Return the ``FGEN:CHANnel[n]:DCLevel`` command.

        Description:
            - This command sets or returns the DC level of the generated waveform for the specified
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:DCLevel?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:DCLevel?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:DCLevel value``
              command.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:DCLevel <NRf>
            - FGEN:CHANnel[n]:DCLevel?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._dclevel

    @property
    def frequency(self) -> FgenChannelItemFrequency:
        """Return the ``FGEN:CHANnel[n]:FREQuency`` command.

        Description:
            - This command sets or returns the function generator's waveform frequency for the
              specified channel. All channels on a multi-channel instrument use the same frequency
              setting.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:FREQuency?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:FREQuency value``
              command.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:FREQuency <NRf>
            - FGEN:CHANnel[n]:FREQuency?
            ```

        Info:
            - ``*RST`` sets this to 1.2 MHz.
        """
        return self._frequency

    @property
    def high(self) -> FgenChannelItemHigh:
        """Return the ``FGEN:CHANnel[n]:HIGH`` command.

        Description:
            - This command sets or returns the function generator's waveform high voltage value for
              the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:HIGH?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:HIGH?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:HIGH value``
              command.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:HIGH <NRf>
            - FGEN:CHANnel[n]:HIGH?
            ```

        Info:
            - ``*RST`` sets this to 250 mV.
        """
        return self._high

    @property
    def low(self) -> FgenChannelItemLow:
        """Return the ``FGEN:CHANnel[n]:LOW`` command.

        Description:
            - This command sets or returns the function generator's waveform low voltage value for
              the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:LOW?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:LOW?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:LOW value``
              command.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:LOW <NRf>
            - FGEN:CHANnel[n]:LOW?
            ```

        Info:
            - ``*RST`` sets this to -250 mV.
        """
        return self._low

    @property
    def offset(self) -> FgenChannelItemOffset:
        """Return the ``FGEN:CHANnel[n]:OFFSet`` command.

        Description:
            - This command sets or returns the function generator's waveform offset value for the
              specified channel. If the offset value is higher than the designated maximum offset or
              lower than the designated minimum offset, then the respective max/min values are used.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:OFFSet?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:OFFSet?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:OFFSet value``
              command.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:OFFSet <NR3>
            - FGEN:CHANnel[n]:OFFSet?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._offset

    @property
    def period(self) -> FgenChannelItemPeriod:
        """Return the ``FGEN:CHANnel[n]:PERiod`` command.

        Description:
            - This command returns the function generator's waveform period for the specified
              channel.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:PERiod?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:PERiod?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:PERiod?
            ```
        """
        return self._period

    @property
    def phase(self) -> FgenChannelItemPhase:
        """Return the ``FGEN:CHANnel[n]:PHASe`` command.

        Description:
            - This command sets or returns the function generator's waveform phase value for the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:PHASe?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:PHASe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:PHASe value``
              command.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:PHASe <NRf>
            - FGEN:CHANnel[n]:PHASe?
            ```

        Info:
            - ``*RST`` sets this to 0.
        """
        return self._phase

    @property
    def symmetry(self) -> FgenChannelItemSymmetry:
        """Return the ``FGEN:CHANnel[n]:SYMMetry`` command.

        Description:
            - This command sets or returns the function generator's triangle waveform symmetry value
              for the specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:SYMMetry?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:SYMMetry?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:SYMMetry value``
              command.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:SYMMetry <NR1>
            - FGEN:CHANnel[n]:SYMMetry?
            ```

        Info:
            - ``*RST`` sets this to 100.
        """
        return self._symmetry

    @property
    def type(self) -> FgenChannelItemType:
        """Return the ``FGEN:CHANnel[n]:TYPE`` command.

        Description:
            - This command sets or returns the function generator's waveform type (shape) for the
              specified channel.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]:TYPE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FGEN:CHANnel[n]:TYPE value``
              command.

        SCPI Syntax:
            ```
            - FGEN:CHANnel[n]:TYPE {SINE|SQUare|TRIangle|NOISe|DC|GAUSsian|EXPRise|EXPDecay|NONE}
            - FGEN:CHANnel[n]:TYPE?
            ```

        Info:
            - ``*RST`` sets this to SINE.
        """
        return self._type


class Fgen(SCPICmdRead):
    """The ``FGEN`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``FGEN?`` query.
        - Using the ``.verify(value)`` method will send the ``FGEN?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.channel``: The ``FGEN:CHANnel[n]`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "FGEN") -> None:
        super().__init__(device, cmd_syntax)
        self._channel: Dict[int, FgenChannelItem] = DefaultDictPassKeyToFactory(
            lambda x: FgenChannelItem(device, f"{self._cmd_syntax}:CHANnel{x}")
        )

    @property
    def channel(self) -> Dict[int, FgenChannelItem]:
        """Return the ``FGEN:CHANnel[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``FGEN:CHANnel[n]?`` query.
            - Using the ``.verify(value)`` method will send the ``FGEN:CHANnel[n]?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``FGEN:CHANnel[n]:AMPLitude`` command tree.
            - ``.path``: The ``FGEN:CHANnel[n]:PATH`` command.
            - ``.dclevel``: The ``FGEN:CHANnel[n]:DCLevel`` command.
            - ``.frequency``: The ``FGEN:CHANnel[n]:FREQuency`` command.
            - ``.high``: The ``FGEN:CHANnel[n]:HIGH`` command.
            - ``.low``: The ``FGEN:CHANnel[n]:LOW`` command.
            - ``.offset``: The ``FGEN:CHANnel[n]:OFFSet`` command.
            - ``.period``: The ``FGEN:CHANnel[n]:PERiod`` command.
            - ``.phase``: The ``FGEN:CHANnel[n]:PHASe`` command.
            - ``.symmetry``: The ``FGEN:CHANnel[n]:SYMMetry`` command.
            - ``.type``: The ``FGEN:CHANnel[n]:TYPE`` command.
        """
        return self._channel
