"""The configuration commands module.

These commands are used in the following models:
MDO3

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CONFIGuration:ADVMATH?
    - CONFIGuration:AFG?
    - CONFIGuration:ANALOg:BANDWidth?
    - CONFIGuration:ANALOg:MAXBANDWidth?
    - CONFIGuration:ANALOg:MAXSAMPLERate?
    - CONFIGuration:ANALOg:NUMCHANnels?
    - CONFIGuration:ANALOg:RECLENS?
    - CONFIGuration:ANALOg:VERTINVert?
    - CONFIGuration:APPLications:CUSTOMMask?
    - CONFIGuration:APPLications:LIMITMask?
    - CONFIGuration:APPLications:POWer?
    - CONFIGuration:APPLications:STANDARDMask?
    - CONFIGuration:APPLications:VIDPIC?
    - CONFIGuration:ARB?
    - CONFIGuration:AUXIN?
    - CONFIGuration:BUSWAVEFORMS:ARINC429A?
    - CONFIGuration:BUSWAVEFORMS:AUDIO?
    - CONFIGuration:BUSWAVEFORMS:CAN?
    - CONFIGuration:BUSWAVEFORMS:CANFD?
    - CONFIGuration:BUSWAVEFORMS:ETHERNET?
    - CONFIGuration:BUSWAVEFORMS:FLEXRAY?
    - CONFIGuration:BUSWAVEFORMS:I2C?
    - CONFIGuration:BUSWAVEFORMS:LIN?
    - CONFIGuration:BUSWAVEFORMS:MIL1553B?
    - CONFIGuration:BUSWAVEFORMS:NUMBUS?
    - CONFIGuration:BUSWAVEFORMS:PARallel?
    - CONFIGuration:BUSWAVEFORMS:RS232C?
    - CONFIGuration:BUSWAVEFORMS:SPI?
    - CONFIGuration:BUSWAVEFORMS:USB:HS?
    - CONFIGuration:BUSWAVEFORMS:USB?
    - CONFIGuration:DIGITAl:MAGnivu?
    - CONFIGuration:DIGITAl:MAXSAMPLERate?
    - CONFIGuration:DIGITAl:NUMCHANnels?
    - CONFIGuration:DVM?
    - CONFIGuration:EXTVIDEO?
    - CONFIGuration:HISTOGRAM?
    - CONFIGuration:NETWORKDRIVES?
    - CONFIGuration:NUMMEAS?
    - CONFIGuration:REFS:NUMREFS?
    - CONFIGuration:RF:ADVTRIG?
    - CONFIGuration:RF:BANDWidth?
    - CONFIGuration:RF:MAXBANDWidth?
    - CONFIGuration:RF:NUMCHANnels?
    - CONFIGuration:ROSC?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class ConfigurationRosc(SCPICmdRead):
    """The ``CONFIGuration:ROSC`` command.

    Description:
        - This query returns a boolean value to indicate whether the instrument has an external
          reference oscillator (ROSC) input.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ROSC?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ROSC?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:ROSC?
        ```
    """


class ConfigurationRfNumchannels(SCPICmdRead):
    """The ``CONFIGuration:RF:NUMCHANnels`` command.

    Description:
        - This query returns the number of RF channels present. If no RF channels are present, the
          query returns 0. )

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:RF:NUMCHANnels?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:RF:NUMCHANnels?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:RF:NUMCHANnels?
        ```
    """


class ConfigurationRfMaxbandwidth(SCPICmdRead):
    """The ``CONFIGuration:RF:MAXBANDWidth`` command.

    Description:
        - This query returns the maximum bandwidth, in hertz, for RF channels. If no RF channels are
          present, the query returns 0. Enabling this feature requires an MDO4000/B/C Series
          oscilloscope and installation of a MDO4TRIG option.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:RF:MAXBANDWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:RF:MAXBANDWidth?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:RF:MAXBANDWidth?
        ```
    """


class ConfigurationRfBandwidth(SCPICmdRead):
    """The ``CONFIGuration:RF:BANDWidth`` command.

    Description:
        - This query returns the bandwidth, in Hz, for the RF channel(s). If there are no RF
          channels, the value returned is 0.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:RF:BANDWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:RF:BANDWidth?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:RF:BANDWidth?
        ```
    """


class ConfigurationRfAdvtrig(SCPICmdRead):
    """The ``CONFIGuration:RF:ADVTRIG`` command.

    Description:
        - This query returns a boolean value to indicate whether the advanced RF trigger and
          analysis feature is present. (Enabling this feature requires an MDO4000/B/C Series
          oscilloscope and installation of a MDO4TRIG application option.)

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:RF:ADVTRIG?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:RF:ADVTRIG?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:RF:ADVTRIG?
        ```
    """


class ConfigurationRf(SCPICmdRead):
    """The ``CONFIGuration:RF`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:RF?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:RF?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.advtrig``: The ``CONFIGuration:RF:ADVTRIG`` command.
        - ``.bandwidth``: The ``CONFIGuration:RF:BANDWidth`` command.
        - ``.maxbandwidth``: The ``CONFIGuration:RF:MAXBANDWidth`` command.
        - ``.numchannels``: The ``CONFIGuration:RF:NUMCHANnels`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._advtrig = ConfigurationRfAdvtrig(device, f"{self._cmd_syntax}:ADVTRIG")
        self._bandwidth = ConfigurationRfBandwidth(device, f"{self._cmd_syntax}:BANDWidth")
        self._maxbandwidth = ConfigurationRfMaxbandwidth(device, f"{self._cmd_syntax}:MAXBANDWidth")
        self._numchannels = ConfigurationRfNumchannels(device, f"{self._cmd_syntax}:NUMCHANnels")

    @property
    def advtrig(self) -> ConfigurationRfAdvtrig:
        """Return the ``CONFIGuration:RF:ADVTRIG`` command.

        Description:
            - This query returns a boolean value to indicate whether the advanced RF trigger and
              analysis feature is present. (Enabling this feature requires an MDO4000/B/C Series
              oscilloscope and installation of a MDO4TRIG application option.)

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:RF:ADVTRIG?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:RF:ADVTRIG?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:RF:ADVTRIG?
            ```
        """
        return self._advtrig

    @property
    def bandwidth(self) -> ConfigurationRfBandwidth:
        """Return the ``CONFIGuration:RF:BANDWidth`` command.

        Description:
            - This query returns the bandwidth, in Hz, for the RF channel(s). If there are no RF
              channels, the value returned is 0.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:RF:BANDWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:RF:BANDWidth?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:RF:BANDWidth?
            ```
        """
        return self._bandwidth

    @property
    def maxbandwidth(self) -> ConfigurationRfMaxbandwidth:
        """Return the ``CONFIGuration:RF:MAXBANDWidth`` command.

        Description:
            - This query returns the maximum bandwidth, in hertz, for RF channels. If no RF channels
              are present, the query returns 0. Enabling this feature requires an MDO4000/B/C Series
              oscilloscope and installation of a MDO4TRIG option.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:RF:MAXBANDWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:RF:MAXBANDWidth?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:RF:MAXBANDWidth?
            ```
        """
        return self._maxbandwidth

    @property
    def numchannels(self) -> ConfigurationRfNumchannels:
        """Return the ``CONFIGuration:RF:NUMCHANnels`` command.

        Description:
            - This query returns the number of RF channels present. If no RF channels are present,
              the query returns 0. )

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:RF:NUMCHANnels?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:RF:NUMCHANnels?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:RF:NUMCHANnels?
            ```
        """
        return self._numchannels


class ConfigurationRefsNumrefs(SCPICmdRead):
    """The ``CONFIGuration:REFS:NUMREFS`` command.

    Description:
        - This query returns the number of reference waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:REFS:NUMREFS?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:REFS:NUMREFS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:REFS:NUMREFS?
        ```
    """


class ConfigurationRefs(SCPICmdRead):
    """The ``CONFIGuration:REFS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:REFS?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:REFS?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.numrefs``: The ``CONFIGuration:REFS:NUMREFS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._numrefs = ConfigurationRefsNumrefs(device, f"{self._cmd_syntax}:NUMREFS")

    @property
    def numrefs(self) -> ConfigurationRefsNumrefs:
        """Return the ``CONFIGuration:REFS:NUMREFS`` command.

        Description:
            - This query returns the number of reference waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:REFS:NUMREFS?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:REFS:NUMREFS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:REFS:NUMREFS?
            ```
        """
        return self._numrefs


class ConfigurationNummeas(SCPICmdRead):
    """The ``CONFIGuration:NUMMEAS`` command.

    Description:
        - This query returns the maximum number of periodic measurements.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:NUMMEAS?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:NUMMEAS?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:NUMMEAS?
        ```
    """


class ConfigurationNetworkdrives(SCPICmdRead):
    """The ``CONFIGuration:NETWORKDRIVES`` command.

    Description:
        - This query returns a boolean value to indicate whether network drives are supported.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:NETWORKDRIVES?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:NETWORKDRIVES?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:NETWORKDRIVES?
        ```
    """


class ConfigurationHistogram(SCPICmdRead):
    """The ``CONFIGuration:HISTOGRAM`` command.

    Description:
        - This query returns a boolean value to indicate whether the waveform histogram feature is
          present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:HISTOGRAM?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:HISTOGRAM?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:HISTOGRAM?
        ```
    """


class ConfigurationExtvideo(SCPICmdRead):
    """The ``CONFIGuration:EXTVIDEO`` command.

    Description:
        - This query returns a boolean value to indicate whether the extended video trigger features
          are present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:EXTVIDEO?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:EXTVIDEO?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:EXTVIDEO?
        ```
    """


class ConfigurationDvm(SCPICmdRead):
    """The ``CONFIGuration:DVM`` command.

    Description:
        - Indicates whether the Digital Voltmeter hardware is present, and the DVM feature is
          enabled.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:DVM?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:DVM?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:DVM?
        ```
    """


class ConfigurationDigitalNumchannels(SCPICmdRead):
    """The ``CONFIGuration:DIGITAl:NUMCHANnels`` command.

    Description:
        - This query returns the number of digital channels.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:DIGITAl:NUMCHANnels?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:DIGITAl:NUMCHANnels?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:DIGITAl:NUMCHANnels?
        ```
    """


class ConfigurationDigitalMaxsamplerate(SCPICmdRead):
    """The ``CONFIGuration:DIGITAl:MAXSAMPLERate`` command.

    Description:
        - This query returns the maximum sample rate for digital channels, in samples per second. If
          there are no digital channels, the value returned is 0.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:DIGITAl:MAXSAMPLERate?``
          query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:DIGITAl:MAXSAMPLERate?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:DIGITAl:MAXSAMPLERate?
        ```
    """


class ConfigurationDigitalMagnivu(SCPICmdRead):
    """The ``CONFIGuration:DIGITAl:MAGnivu`` command.

    Description:
        - This query returns a boolean value to indicate whether the instrument supports the MagniVu
          feature for digital channels. If there are no digital channels, the value returned is 0.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:DIGITAl:MAGnivu?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:DIGITAl:MAGnivu?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:DIGITAl:MAGnivu?
        ```
    """


class ConfigurationDigital(SCPICmdRead):
    """The ``CONFIGuration:DIGITAl`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:DIGITAl?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:DIGITAl?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.magnivu``: The ``CONFIGuration:DIGITAl:MAGnivu`` command.
        - ``.maxsamplerate``: The ``CONFIGuration:DIGITAl:MAXSAMPLERate`` command.
        - ``.numchannels``: The ``CONFIGuration:DIGITAl:NUMCHANnels`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._magnivu = ConfigurationDigitalMagnivu(device, f"{self._cmd_syntax}:MAGnivu")
        self._maxsamplerate = ConfigurationDigitalMaxsamplerate(
            device, f"{self._cmd_syntax}:MAXSAMPLERate"
        )
        self._numchannels = ConfigurationDigitalNumchannels(
            device, f"{self._cmd_syntax}:NUMCHANnels"
        )

    @property
    def magnivu(self) -> ConfigurationDigitalMagnivu:
        """Return the ``CONFIGuration:DIGITAl:MAGnivu`` command.

        Description:
            - This query returns a boolean value to indicate whether the instrument supports the
              MagniVu feature for digital channels. If there are no digital channels, the value
              returned is 0.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:DIGITAl:MAGnivu?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:DIGITAl:MAGnivu?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:DIGITAl:MAGnivu?
            ```
        """
        return self._magnivu

    @property
    def maxsamplerate(self) -> ConfigurationDigitalMaxsamplerate:
        """Return the ``CONFIGuration:DIGITAl:MAXSAMPLERate`` command.

        Description:
            - This query returns the maximum sample rate for digital channels, in samples per
              second. If there are no digital channels, the value returned is 0.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:DIGITAl:MAXSAMPLERate?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:DIGITAl:MAXSAMPLERate?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:DIGITAl:MAXSAMPLERate?
            ```
        """
        return self._maxsamplerate

    @property
    def numchannels(self) -> ConfigurationDigitalNumchannels:
        """Return the ``CONFIGuration:DIGITAl:NUMCHANnels`` command.

        Description:
            - This query returns the number of digital channels.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:DIGITAl:NUMCHANnels?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:DIGITAl:NUMCHANnels?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:DIGITAl:NUMCHANnels?
            ```
        """
        return self._numchannels


class ConfigurationBuswaveformsUsbHs(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:USB:HS`` command.

    Description:
        - This query returns a boolean value to indicate whether the high-speed USB bus triggering
          and analysis feature is present. Depending upon the bandwidth of the instrument, USB bus
          triggering and analysis features may be limited to USB low-speed or full-speed. If the
          instrument bandwidth is sufficient, USB high-speed (HS) triggering and analysis is
          supported as long as the 3-SRUSB2 application option is installed.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:USB:HS?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:USB:HS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:USB:HS?
        ```
    """


class ConfigurationBuswaveformsUsb(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:USB`` command.

    Description:
        - This query returns a boolean value to indicate whether the USB bus triggering and analysis
          feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:USB?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:USB?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:USB?
        ```

    Properties:
        - ``.hs``: The ``CONFIGuration:BUSWAVEFORMS:USB:HS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._hs = ConfigurationBuswaveformsUsbHs(device, f"{self._cmd_syntax}:HS")

    @property
    def hs(self) -> ConfigurationBuswaveformsUsbHs:
        """Return the ``CONFIGuration:BUSWAVEFORMS:USB:HS`` command.

        Description:
            - This query returns a boolean value to indicate whether the high-speed USB bus
              triggering and analysis feature is present. Depending upon the bandwidth of the
              instrument, USB bus triggering and analysis features may be limited to USB low-speed
              or full-speed. If the instrument bandwidth is sufficient, USB high-speed (HS)
              triggering and analysis is supported as long as the 3-SRUSB2 application option is
              installed.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:USB:HS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:BUSWAVEFORMS:USB:HS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:USB:HS?
            ```
        """
        return self._hs


class ConfigurationBuswaveformsSpi(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:SPI`` command.

    Description:
        - This query returns a boolean value to indicate whether the optional SPI bus triggering and
          analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:SPI?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:SPI?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:SPI?
        ```
    """


class ConfigurationBuswaveformsRs232c(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:RS232C`` command.

    Description:
        - This query returns a boolean value to indicate whether the optional RS232 bus triggering
          and analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:RS232C?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:RS232C?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:RS232C?
        ```
    """


class ConfigurationBuswaveformsParallel(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:PARallel`` command.

    Description:
        - This query returns a boolean value to indicate whether the parallel bus triggering and
          analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:PARallel?``
          query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:PARallel?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:PARallel?
        ```
    """


class ConfigurationBuswaveformsNumbus(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:NUMBUS`` command.

    Description:
        - This query returns the number of bus waveforms.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:NUMBUS?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:NUMBUS?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:NUMBUS?
        ```
    """


class ConfigurationBuswaveformsMil1553b(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:MIL1553B`` command.

    Description:
        - This query returns a boolean value to indicate whether the optional MIL-STD-1553 bus
          triggering and analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:MIL1553B?``
          query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:MIL1553B?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:MIL1553B?
        ```
    """


class ConfigurationBuswaveformsLin(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:LIN`` command.

    Description:
        - This query returns a boolean value to indicate whether the optional LIN bus triggering and
          analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:LIN?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:LIN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:LIN?
        ```
    """


class ConfigurationBuswaveformsI2c(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:I2C`` command.

    Description:
        - This query returns a boolean value to indicate whether the optional I 2 C bus triggering
          and analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:I2C?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:I2C?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:I2C?
        ```
    """


class ConfigurationBuswaveformsFlexray(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:FLEXRAY`` command.

    Description:
        - This query returns a boolean value to indicate whether the optional FlexRay bus triggering
          and analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:FLEXRAY?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:FLEXRAY?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:FLEXRAY?
        ```
    """


class ConfigurationBuswaveformsEthernet(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:ETHERNET`` command.

    Description:
        - This query returns a boolean value to indicate whether the optional Ethernet triggering
          and analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:ETHERNET?``
          query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:ETHERNET?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:ETHERNET?
        ```
    """


class ConfigurationBuswaveformsCanfd(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:CANFD`` command.

    Description:
        - This query returns a Boolean value to indicate whether the optional CAN FD bus triggering
          and analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:CANFD?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:CANFD?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:CANFD?
        ```
    """


class ConfigurationBuswaveformsCan(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:CAN`` command.

    Description:
        - This query returns a boolean value to indicate whether the optional CAN bus triggering and
          analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:CAN?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:CAN?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:CAN?
        ```
    """


class ConfigurationBuswaveformsAudio(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:AUDIO`` command.

    Description:
        - This query returns a boolean value to indicate whether the optional audio bus triggering
          and analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:AUDIO?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:AUDIO?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:AUDIO?
        ```
    """


class ConfigurationBuswaveformsArinc429a(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS:ARINC429A`` command.

    Description:
        - This query returns a Boolean value to indicate whether the optional CAN-FD bus triggering
          and analysis feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:ARINC429A?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``CONFIGuration:BUSWAVEFORMS:ARINC429A?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:BUSWAVEFORMS:ARINC429A?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class ConfigurationBuswaveforms(SCPICmdRead):
    """The ``CONFIGuration:BUSWAVEFORMS`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.arinc429a``: The ``CONFIGuration:BUSWAVEFORMS:ARINC429A`` command.
        - ``.audio``: The ``CONFIGuration:BUSWAVEFORMS:AUDIO`` command.
        - ``.can``: The ``CONFIGuration:BUSWAVEFORMS:CAN`` command.
        - ``.canfd``: The ``CONFIGuration:BUSWAVEFORMS:CANFD`` command.
        - ``.ethernet``: The ``CONFIGuration:BUSWAVEFORMS:ETHERNET`` command.
        - ``.flexray``: The ``CONFIGuration:BUSWAVEFORMS:FLEXRAY`` command.
        - ``.i2c``: The ``CONFIGuration:BUSWAVEFORMS:I2C`` command.
        - ``.lin``: The ``CONFIGuration:BUSWAVEFORMS:LIN`` command.
        - ``.mil1553b``: The ``CONFIGuration:BUSWAVEFORMS:MIL1553B`` command.
        - ``.numbus``: The ``CONFIGuration:BUSWAVEFORMS:NUMBUS`` command.
        - ``.parallel``: The ``CONFIGuration:BUSWAVEFORMS:PARallel`` command.
        - ``.rs232c``: The ``CONFIGuration:BUSWAVEFORMS:RS232C`` command.
        - ``.spi``: The ``CONFIGuration:BUSWAVEFORMS:SPI`` command.
        - ``.usb``: The ``CONFIGuration:BUSWAVEFORMS:USB`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._arinc429a = ConfigurationBuswaveformsArinc429a(
            device, f"{self._cmd_syntax}:ARINC429A"
        )
        self._audio = ConfigurationBuswaveformsAudio(device, f"{self._cmd_syntax}:AUDIO")
        self._can = ConfigurationBuswaveformsCan(device, f"{self._cmd_syntax}:CAN")
        self._canfd = ConfigurationBuswaveformsCanfd(device, f"{self._cmd_syntax}:CANFD")
        self._ethernet = ConfigurationBuswaveformsEthernet(device, f"{self._cmd_syntax}:ETHERNET")
        self._flexray = ConfigurationBuswaveformsFlexray(device, f"{self._cmd_syntax}:FLEXRAY")
        self._i2c = ConfigurationBuswaveformsI2c(device, f"{self._cmd_syntax}:I2C")
        self._lin = ConfigurationBuswaveformsLin(device, f"{self._cmd_syntax}:LIN")
        self._mil1553b = ConfigurationBuswaveformsMil1553b(device, f"{self._cmd_syntax}:MIL1553B")
        self._numbus = ConfigurationBuswaveformsNumbus(device, f"{self._cmd_syntax}:NUMBUS")
        self._parallel = ConfigurationBuswaveformsParallel(device, f"{self._cmd_syntax}:PARallel")
        self._rs232c = ConfigurationBuswaveformsRs232c(device, f"{self._cmd_syntax}:RS232C")
        self._spi = ConfigurationBuswaveformsSpi(device, f"{self._cmd_syntax}:SPI")
        self._usb = ConfigurationBuswaveformsUsb(device, f"{self._cmd_syntax}:USB")

    @property
    def arinc429a(self) -> ConfigurationBuswaveformsArinc429a:
        """Return the ``CONFIGuration:BUSWAVEFORMS:ARINC429A`` command.

        Description:
            - This query returns a Boolean value to indicate whether the optional CAN-FD bus
              triggering and analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:ARINC429A?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:BUSWAVEFORMS:ARINC429A?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:ARINC429A?
            ```
        """
        return self._arinc429a

    @property
    def audio(self) -> ConfigurationBuswaveformsAudio:
        """Return the ``CONFIGuration:BUSWAVEFORMS:AUDIO`` command.

        Description:
            - This query returns a boolean value to indicate whether the optional audio bus
              triggering and analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:AUDIO?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:BUSWAVEFORMS:AUDIO?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:AUDIO?
            ```
        """
        return self._audio

    @property
    def can(self) -> ConfigurationBuswaveformsCan:
        """Return the ``CONFIGuration:BUSWAVEFORMS:CAN`` command.

        Description:
            - This query returns a boolean value to indicate whether the optional CAN bus triggering
              and analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:CAN?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:CAN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:CAN?
            ```
        """
        return self._can

    @property
    def canfd(self) -> ConfigurationBuswaveformsCanfd:
        """Return the ``CONFIGuration:BUSWAVEFORMS:CANFD`` command.

        Description:
            - This query returns a Boolean value to indicate whether the optional CAN FD bus
              triggering and analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:CANFD?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:BUSWAVEFORMS:CANFD?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:CANFD?
            ```
        """
        return self._canfd

    @property
    def ethernet(self) -> ConfigurationBuswaveformsEthernet:
        """Return the ``CONFIGuration:BUSWAVEFORMS:ETHERNET`` command.

        Description:
            - This query returns a boolean value to indicate whether the optional Ethernet
              triggering and analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:ETHERNET?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:BUSWAVEFORMS:ETHERNET?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:ETHERNET?
            ```
        """
        return self._ethernet

    @property
    def flexray(self) -> ConfigurationBuswaveformsFlexray:
        """Return the ``CONFIGuration:BUSWAVEFORMS:FLEXRAY`` command.

        Description:
            - This query returns a boolean value to indicate whether the optional FlexRay bus
              triggering and analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:FLEXRAY?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:BUSWAVEFORMS:FLEXRAY?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:FLEXRAY?
            ```
        """
        return self._flexray

    @property
    def i2c(self) -> ConfigurationBuswaveformsI2c:
        """Return the ``CONFIGuration:BUSWAVEFORMS:I2C`` command.

        Description:
            - This query returns a boolean value to indicate whether the optional I 2 C bus
              triggering and analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:I2C?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:I2C?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:I2C?
            ```
        """
        return self._i2c

    @property
    def lin(self) -> ConfigurationBuswaveformsLin:
        """Return the ``CONFIGuration:BUSWAVEFORMS:LIN`` command.

        Description:
            - This query returns a boolean value to indicate whether the optional LIN bus triggering
              and analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:LIN?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:LIN?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:LIN?
            ```
        """
        return self._lin

    @property
    def mil1553b(self) -> ConfigurationBuswaveformsMil1553b:
        """Return the ``CONFIGuration:BUSWAVEFORMS:MIL1553B`` command.

        Description:
            - This query returns a boolean value to indicate whether the optional MIL-STD-1553 bus
              triggering and analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:MIL1553B?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:BUSWAVEFORMS:MIL1553B?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:MIL1553B?
            ```
        """
        return self._mil1553b

    @property
    def numbus(self) -> ConfigurationBuswaveformsNumbus:
        """Return the ``CONFIGuration:BUSWAVEFORMS:NUMBUS`` command.

        Description:
            - This query returns the number of bus waveforms.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:NUMBUS?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:BUSWAVEFORMS:NUMBUS?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:NUMBUS?
            ```
        """
        return self._numbus

    @property
    def parallel(self) -> ConfigurationBuswaveformsParallel:
        """Return the ``CONFIGuration:BUSWAVEFORMS:PARallel`` command.

        Description:
            - This query returns a boolean value to indicate whether the parallel bus triggering and
              analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:PARallel?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:BUSWAVEFORMS:PARallel?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:PARallel?
            ```
        """
        return self._parallel

    @property
    def rs232c(self) -> ConfigurationBuswaveformsRs232c:
        """Return the ``CONFIGuration:BUSWAVEFORMS:RS232C`` command.

        Description:
            - This query returns a boolean value to indicate whether the optional RS232 bus
              triggering and analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:RS232C?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:BUSWAVEFORMS:RS232C?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:RS232C?
            ```
        """
        return self._rs232c

    @property
    def spi(self) -> ConfigurationBuswaveformsSpi:
        """Return the ``CONFIGuration:BUSWAVEFORMS:SPI`` command.

        Description:
            - This query returns a boolean value to indicate whether the optional SPI bus triggering
              and analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:SPI?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:SPI?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:SPI?
            ```
        """
        return self._spi

    @property
    def usb(self) -> ConfigurationBuswaveformsUsb:
        """Return the ``CONFIGuration:BUSWAVEFORMS:USB`` command.

        Description:
            - This query returns a boolean value to indicate whether the USB bus triggering and
              analysis feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS:USB?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS:USB?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:BUSWAVEFORMS:USB?
            ```

        Sub-properties:
            - ``.hs``: The ``CONFIGuration:BUSWAVEFORMS:USB:HS`` command.
        """
        return self._usb


class ConfigurationAuxin(SCPICmdRead):
    """The ``CONFIGuration:AUXIN`` command.

    Description:
        - This query returns a boolean value to indicate whether the instrument has an Aux Input
          connector.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:AUXIN?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:AUXIN?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:AUXIN?
        ```
    """


class ConfigurationArb(SCPICmdRead):
    """The ``CONFIGuration:ARB`` command.

    Description:
        - Indicates whether or not the arbitrary function generator hardware is present, and the
          user-defined arbitrary waveform generation feature is enabled. Note that this is different
          than the ``CONFIGuration:AFG?`` query. The ability to generate arbitrary waveforms is an
          extension of the standard AFG features.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ARB?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ARB?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:ARB?
        ```
    """


class ConfigurationApplicationsVidpic(SCPICmdRead):
    """The ``CONFIGuration:APPLications:VIDPIC`` command.

    Description:
        - Indicates whether the Video Picture feature is present and enabled.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:APPLications:VIDPIC?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:APPLications:VIDPIC?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:APPLications:VIDPIC?
        ```
    """


class ConfigurationApplicationsStandardmask(SCPICmdRead):
    """The ``CONFIGuration:APPLications:STANDARDMask`` command.

    Description:
        - Indicates whether the Standard Mask test feature is present and enabled.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:APPLications:STANDARDMask?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``CONFIGuration:APPLications:STANDARDMask?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:APPLications:STANDARDMask?
        ```
    """


class ConfigurationApplicationsPower(SCPICmdRead):
    """The ``CONFIGuration:APPLications:POWer`` command.

    Description:
        - This query returns a boolean value to indicate whether the optional power application
          feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:APPLications:POWer?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:APPLications:POWer?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:APPLications:POWer?
        ```
    """


class ConfigurationApplicationsLimitmask(SCPICmdRead):
    """The ``CONFIGuration:APPLications:LIMITMask`` command.

    Description:
        - This query returns a boolean value to indicate whether the optional mask/limit test
          feature is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:APPLications:LIMITMask?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``CONFIGuration:APPLications:LIMITMask?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:APPLications:LIMITMask?
        ```
    """


class ConfigurationApplicationsCustommask(SCPICmdRead):
    """The ``CONFIGuration:APPLications:CUSTOMMask`` command.

    Description:
        - Indicates whether the Custom Mask test feature is present and enabled.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:APPLications:CUSTOMMask?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``CONFIGuration:APPLications:CUSTOMMask?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:APPLications:CUSTOMMask?
        ```
    """


class ConfigurationApplications(SCPICmdRead):
    """The ``CONFIGuration:APPLications`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:APPLications?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:APPLications?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.custommask``: The ``CONFIGuration:APPLications:CUSTOMMask`` command.
        - ``.limitmask``: The ``CONFIGuration:APPLications:LIMITMask`` command.
        - ``.power``: The ``CONFIGuration:APPLications:POWer`` command.
        - ``.standardmask``: The ``CONFIGuration:APPLications:STANDARDMask`` command.
        - ``.vidpic``: The ``CONFIGuration:APPLications:VIDPIC`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._custommask = ConfigurationApplicationsCustommask(
            device, f"{self._cmd_syntax}:CUSTOMMask"
        )
        self._limitmask = ConfigurationApplicationsLimitmask(
            device, f"{self._cmd_syntax}:LIMITMask"
        )
        self._power = ConfigurationApplicationsPower(device, f"{self._cmd_syntax}:POWer")
        self._standardmask = ConfigurationApplicationsStandardmask(
            device, f"{self._cmd_syntax}:STANDARDMask"
        )
        self._vidpic = ConfigurationApplicationsVidpic(device, f"{self._cmd_syntax}:VIDPIC")

    @property
    def custommask(self) -> ConfigurationApplicationsCustommask:
        """Return the ``CONFIGuration:APPLications:CUSTOMMask`` command.

        Description:
            - Indicates whether the Custom Mask test feature is present and enabled.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:APPLications:CUSTOMMask?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:APPLications:CUSTOMMask?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:APPLications:CUSTOMMask?
            ```
        """
        return self._custommask

    @property
    def limitmask(self) -> ConfigurationApplicationsLimitmask:
        """Return the ``CONFIGuration:APPLications:LIMITMask`` command.

        Description:
            - This query returns a boolean value to indicate whether the optional mask/limit test
              feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:APPLications:LIMITMask?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:APPLications:LIMITMask?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:APPLications:LIMITMask?
            ```
        """
        return self._limitmask

    @property
    def power(self) -> ConfigurationApplicationsPower:
        """Return the ``CONFIGuration:APPLications:POWer`` command.

        Description:
            - This query returns a boolean value to indicate whether the optional power application
              feature is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:APPLications:POWer?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:APPLications:POWer?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:APPLications:POWer?
            ```
        """
        return self._power

    @property
    def standardmask(self) -> ConfigurationApplicationsStandardmask:
        """Return the ``CONFIGuration:APPLications:STANDARDMask`` command.

        Description:
            - Indicates whether the Standard Mask test feature is present and enabled.

        Usage:
            - Using the ``.query()`` method will send the
              ``CONFIGuration:APPLications:STANDARDMask?`` query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:APPLications:STANDARDMask?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:APPLications:STANDARDMask?
            ```
        """
        return self._standardmask

    @property
    def vidpic(self) -> ConfigurationApplicationsVidpic:
        """Return the ``CONFIGuration:APPLications:VIDPIC`` command.

        Description:
            - Indicates whether the Video Picture feature is present and enabled.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:APPLications:VIDPIC?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:APPLications:VIDPIC?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:APPLications:VIDPIC?
            ```
        """
        return self._vidpic


class ConfigurationAnalogVertinvert(SCPICmdRead):
    """The ``CONFIGuration:ANALOg:VERTINVert`` command.

    Description:
        - This query returns a boolean value to indicate whether the vertical invert feature for
          analog channels is present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:VERTINVert?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg:VERTINVert?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:ANALOg:VERTINVert?
        ```
    """


class ConfigurationAnalogReclens(SCPICmdRead):
    """The ``CONFIGuration:ANALOg:RECLENS`` command.

    Description:
        - This query returns a comma-separated list of supported record lengths for the analog
          channels.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:RECLENS?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg:RECLENS?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:ANALOg:RECLENS?
        ```
    """


class ConfigurationAnalogNumchannels(SCPICmdRead):
    """The ``CONFIGuration:ANALOg:NUMCHANnels`` command.

    Description:
        - This query returns the number of analog channels.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:NUMCHANnels?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg:NUMCHANnels?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:ANALOg:NUMCHANnels?
        ```
    """


class ConfigurationAnalogMaxsamplerate(SCPICmdRead):
    """The ``CONFIGuration:ANALOg:MAXSAMPLERate`` command.

    Description:
        - This query returns the maximum sample rate for analog channels.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:MAXSAMPLERate?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg:MAXSAMPLERate?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:ANALOg:MAXSAMPLERate?
        ```
    """


class ConfigurationAnalogMaxbandwidth(SCPICmdRead):
    """The ``CONFIGuration:ANALOg:MAXBANDWidth`` command.

    Description:
        - This query returns the maximum bandwidth for analog channels.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:MAXBANDWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg:MAXBANDWidth?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:ANALOg:MAXBANDWidth?
        ```
    """


class ConfigurationAnalogBandwidth(SCPICmdRead):
    """The ``CONFIGuration:ANALOg:BANDWidth`` command.

    Description:
        - This command queries the maximum licensed bandwidth of the instrument.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:BANDWidth?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg:BANDWidth?``
          query and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:ANALOg:BANDWidth?
        ```
    """


class ConfigurationAnalog(SCPICmdRead):
    """The ``CONFIGuration:ANALOg`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.bandwidth``: The ``CONFIGuration:ANALOg:BANDWidth`` command.
        - ``.maxbandwidth``: The ``CONFIGuration:ANALOg:MAXBANDWidth`` command.
        - ``.maxsamplerate``: The ``CONFIGuration:ANALOg:MAXSAMPLERate`` command.
        - ``.numchannels``: The ``CONFIGuration:ANALOg:NUMCHANnels`` command.
        - ``.reclens``: The ``CONFIGuration:ANALOg:RECLENS`` command.
        - ``.vertinvert``: The ``CONFIGuration:ANALOg:VERTINVert`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bandwidth = ConfigurationAnalogBandwidth(device, f"{self._cmd_syntax}:BANDWidth")
        self._maxbandwidth = ConfigurationAnalogMaxbandwidth(
            device, f"{self._cmd_syntax}:MAXBANDWidth"
        )
        self._maxsamplerate = ConfigurationAnalogMaxsamplerate(
            device, f"{self._cmd_syntax}:MAXSAMPLERate"
        )
        self._numchannels = ConfigurationAnalogNumchannels(
            device, f"{self._cmd_syntax}:NUMCHANnels"
        )
        self._reclens = ConfigurationAnalogReclens(device, f"{self._cmd_syntax}:RECLENS")
        self._vertinvert = ConfigurationAnalogVertinvert(device, f"{self._cmd_syntax}:VERTINVert")

    @property
    def bandwidth(self) -> ConfigurationAnalogBandwidth:
        """Return the ``CONFIGuration:ANALOg:BANDWidth`` command.

        Description:
            - This command queries the maximum licensed bandwidth of the instrument.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:BANDWidth?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg:BANDWidth?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:ANALOg:BANDWidth?
            ```
        """
        return self._bandwidth

    @property
    def maxbandwidth(self) -> ConfigurationAnalogMaxbandwidth:
        """Return the ``CONFIGuration:ANALOg:MAXBANDWidth`` command.

        Description:
            - This query returns the maximum bandwidth for analog channels.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:MAXBANDWidth?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:ANALOg:MAXBANDWidth?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:ANALOg:MAXBANDWidth?
            ```
        """
        return self._maxbandwidth

    @property
    def maxsamplerate(self) -> ConfigurationAnalogMaxsamplerate:
        """Return the ``CONFIGuration:ANALOg:MAXSAMPLERate`` command.

        Description:
            - This query returns the maximum sample rate for analog channels.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:MAXSAMPLERate?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:ANALOg:MAXSAMPLERate?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:ANALOg:MAXSAMPLERate?
            ```
        """
        return self._maxsamplerate

    @property
    def numchannels(self) -> ConfigurationAnalogNumchannels:
        """Return the ``CONFIGuration:ANALOg:NUMCHANnels`` command.

        Description:
            - This query returns the number of analog channels.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:NUMCHANnels?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``CONFIGuration:ANALOg:NUMCHANnels?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:ANALOg:NUMCHANnels?
            ```
        """
        return self._numchannels

    @property
    def reclens(self) -> ConfigurationAnalogReclens:
        """Return the ``CONFIGuration:ANALOg:RECLENS`` command.

        Description:
            - This query returns a comma-separated list of supported record lengths for the analog
              channels.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:RECLENS?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg:RECLENS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:ANALOg:RECLENS?
            ```
        """
        return self._reclens

    @property
    def vertinvert(self) -> ConfigurationAnalogVertinvert:
        """Return the ``CONFIGuration:ANALOg:VERTINVert`` command.

        Description:
            - This query returns a boolean value to indicate whether the vertical invert feature for
              analog channels is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg:VERTINVert?``
              query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg:VERTINVert?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:ANALOg:VERTINVert?
            ```
        """
        return self._vertinvert


class ConfigurationAfg(SCPICmdRead):
    """The ``CONFIGuration:AFG`` command.

    Description:
        - Indicates whether or not the arbitrary function generator hardware is present, and the
          arbitrary function generation feature is enabled.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:AFG?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:AFG?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:AFG?
        ```
    """


class ConfigurationAdvmath(SCPICmdRead):
    """The ``CONFIGuration:ADVMATH`` command.

    Description:
        - This query returns a boolean value to indicate whether the advanced math feature is
          present.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration:ADVMATH?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration:ADVMATH?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CONFIGuration:ADVMATH?
        ```
    """


#  pylint: disable=too-many-instance-attributes
class Configuration(SCPICmdRead):
    """The ``CONFIGuration`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CONFIGuration?`` query.
        - Using the ``.verify(value)`` method will send the ``CONFIGuration?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.advmath``: The ``CONFIGuration:ADVMATH`` command.
        - ``.afg``: The ``CONFIGuration:AFG`` command.
        - ``.analog``: The ``CONFIGuration:ANALOg`` command tree.
        - ``.applications``: The ``CONFIGuration:APPLications`` command tree.
        - ``.arb``: The ``CONFIGuration:ARB`` command.
        - ``.auxin``: The ``CONFIGuration:AUXIN`` command.
        - ``.buswaveforms``: The ``CONFIGuration:BUSWAVEFORMS`` command tree.
        - ``.digital``: The ``CONFIGuration:DIGITAl`` command tree.
        - ``.dvm``: The ``CONFIGuration:DVM`` command.
        - ``.extvideo``: The ``CONFIGuration:EXTVIDEO`` command.
        - ``.histogram``: The ``CONFIGuration:HISTOGRAM`` command.
        - ``.networkdrives``: The ``CONFIGuration:NETWORKDRIVES`` command.
        - ``.nummeas``: The ``CONFIGuration:NUMMEAS`` command.
        - ``.refs``: The ``CONFIGuration:REFS`` command tree.
        - ``.rf``: The ``CONFIGuration:RF`` command tree.
        - ``.rosc``: The ``CONFIGuration:ROSC`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "CONFIGuration"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._advmath = ConfigurationAdvmath(device, f"{self._cmd_syntax}:ADVMATH")
        self._afg = ConfigurationAfg(device, f"{self._cmd_syntax}:AFG")
        self._analog = ConfigurationAnalog(device, f"{self._cmd_syntax}:ANALOg")
        self._applications = ConfigurationApplications(device, f"{self._cmd_syntax}:APPLications")
        self._arb = ConfigurationArb(device, f"{self._cmd_syntax}:ARB")
        self._auxin = ConfigurationAuxin(device, f"{self._cmd_syntax}:AUXIN")
        self._buswaveforms = ConfigurationBuswaveforms(device, f"{self._cmd_syntax}:BUSWAVEFORMS")
        self._digital = ConfigurationDigital(device, f"{self._cmd_syntax}:DIGITAl")
        self._dvm = ConfigurationDvm(device, f"{self._cmd_syntax}:DVM")
        self._extvideo = ConfigurationExtvideo(device, f"{self._cmd_syntax}:EXTVIDEO")
        self._histogram = ConfigurationHistogram(device, f"{self._cmd_syntax}:HISTOGRAM")
        self._networkdrives = ConfigurationNetworkdrives(
            device, f"{self._cmd_syntax}:NETWORKDRIVES"
        )
        self._nummeas = ConfigurationNummeas(device, f"{self._cmd_syntax}:NUMMEAS")
        self._refs = ConfigurationRefs(device, f"{self._cmd_syntax}:REFS")
        self._rf = ConfigurationRf(device, f"{self._cmd_syntax}:RF")
        self._rosc = ConfigurationRosc(device, f"{self._cmd_syntax}:ROSC")

    @property
    def advmath(self) -> ConfigurationAdvmath:
        """Return the ``CONFIGuration:ADVMATH`` command.

        Description:
            - This query returns a boolean value to indicate whether the advanced math feature is
              present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ADVMATH?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:ADVMATH?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:ADVMATH?
            ```
        """
        return self._advmath

    @property
    def afg(self) -> ConfigurationAfg:
        """Return the ``CONFIGuration:AFG`` command.

        Description:
            - Indicates whether or not the arbitrary function generator hardware is present, and the
              arbitrary function generation feature is enabled.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:AFG?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:AFG?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:AFG?
            ```
        """
        return self._afg

    @property
    def analog(self) -> ConfigurationAnalog:
        """Return the ``CONFIGuration:ANALOg`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ANALOg?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:ANALOg?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.bandwidth``: The ``CONFIGuration:ANALOg:BANDWidth`` command.
            - ``.maxbandwidth``: The ``CONFIGuration:ANALOg:MAXBANDWidth`` command.
            - ``.maxsamplerate``: The ``CONFIGuration:ANALOg:MAXSAMPLERate`` command.
            - ``.numchannels``: The ``CONFIGuration:ANALOg:NUMCHANnels`` command.
            - ``.reclens``: The ``CONFIGuration:ANALOg:RECLENS`` command.
            - ``.vertinvert``: The ``CONFIGuration:ANALOg:VERTINVert`` command.
        """
        return self._analog

    @property
    def applications(self) -> ConfigurationApplications:
        """Return the ``CONFIGuration:APPLications`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:APPLications?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:APPLications?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.custommask``: The ``CONFIGuration:APPLications:CUSTOMMask`` command.
            - ``.limitmask``: The ``CONFIGuration:APPLications:LIMITMask`` command.
            - ``.power``: The ``CONFIGuration:APPLications:POWer`` command.
            - ``.standardmask``: The ``CONFIGuration:APPLications:STANDARDMask`` command.
            - ``.vidpic``: The ``CONFIGuration:APPLications:VIDPIC`` command.
        """
        return self._applications

    @property
    def arb(self) -> ConfigurationArb:
        """Return the ``CONFIGuration:ARB`` command.

        Description:
            - Indicates whether or not the arbitrary function generator hardware is present, and the
              user-defined arbitrary waveform generation feature is enabled. Note that this is
              different than the ``CONFIGuration:AFG?`` query. The ability to generate arbitrary
              waveforms is an extension of the standard AFG features.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ARB?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:ARB?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:ARB?
            ```
        """
        return self._arb

    @property
    def auxin(self) -> ConfigurationAuxin:
        """Return the ``CONFIGuration:AUXIN`` command.

        Description:
            - This query returns a boolean value to indicate whether the instrument has an Aux Input
              connector.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:AUXIN?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:AUXIN?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:AUXIN?
            ```
        """
        return self._auxin

    @property
    def buswaveforms(self) -> ConfigurationBuswaveforms:
        """Return the ``CONFIGuration:BUSWAVEFORMS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:BUSWAVEFORMS?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:BUSWAVEFORMS?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.arinc429a``: The ``CONFIGuration:BUSWAVEFORMS:ARINC429A`` command.
            - ``.audio``: The ``CONFIGuration:BUSWAVEFORMS:AUDIO`` command.
            - ``.can``: The ``CONFIGuration:BUSWAVEFORMS:CAN`` command.
            - ``.canfd``: The ``CONFIGuration:BUSWAVEFORMS:CANFD`` command.
            - ``.ethernet``: The ``CONFIGuration:BUSWAVEFORMS:ETHERNET`` command.
            - ``.flexray``: The ``CONFIGuration:BUSWAVEFORMS:FLEXRAY`` command.
            - ``.i2c``: The ``CONFIGuration:BUSWAVEFORMS:I2C`` command.
            - ``.lin``: The ``CONFIGuration:BUSWAVEFORMS:LIN`` command.
            - ``.mil1553b``: The ``CONFIGuration:BUSWAVEFORMS:MIL1553B`` command.
            - ``.numbus``: The ``CONFIGuration:BUSWAVEFORMS:NUMBUS`` command.
            - ``.parallel``: The ``CONFIGuration:BUSWAVEFORMS:PARallel`` command.
            - ``.rs232c``: The ``CONFIGuration:BUSWAVEFORMS:RS232C`` command.
            - ``.spi``: The ``CONFIGuration:BUSWAVEFORMS:SPI`` command.
            - ``.usb``: The ``CONFIGuration:BUSWAVEFORMS:USB`` command.
        """
        return self._buswaveforms

    @property
    def digital(self) -> ConfigurationDigital:
        """Return the ``CONFIGuration:DIGITAl`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:DIGITAl?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:DIGITAl?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.magnivu``: The ``CONFIGuration:DIGITAl:MAGnivu`` command.
            - ``.maxsamplerate``: The ``CONFIGuration:DIGITAl:MAXSAMPLERate`` command.
            - ``.numchannels``: The ``CONFIGuration:DIGITAl:NUMCHANnels`` command.
        """
        return self._digital

    @property
    def dvm(self) -> ConfigurationDvm:
        """Return the ``CONFIGuration:DVM`` command.

        Description:
            - Indicates whether the Digital Voltmeter hardware is present, and the DVM feature is
              enabled.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:DVM?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:DVM?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:DVM?
            ```
        """
        return self._dvm

    @property
    def extvideo(self) -> ConfigurationExtvideo:
        """Return the ``CONFIGuration:EXTVIDEO`` command.

        Description:
            - This query returns a boolean value to indicate whether the extended video trigger
              features are present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:EXTVIDEO?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:EXTVIDEO?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:EXTVIDEO?
            ```
        """
        return self._extvideo

    @property
    def histogram(self) -> ConfigurationHistogram:
        """Return the ``CONFIGuration:HISTOGRAM`` command.

        Description:
            - This query returns a boolean value to indicate whether the waveform histogram feature
              is present.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:HISTOGRAM?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:HISTOGRAM?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:HISTOGRAM?
            ```
        """
        return self._histogram

    @property
    def networkdrives(self) -> ConfigurationNetworkdrives:
        """Return the ``CONFIGuration:NETWORKDRIVES`` command.

        Description:
            - This query returns a boolean value to indicate whether network drives are supported.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:NETWORKDRIVES?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:NETWORKDRIVES?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:NETWORKDRIVES?
            ```
        """
        return self._networkdrives

    @property
    def nummeas(self) -> ConfigurationNummeas:
        """Return the ``CONFIGuration:NUMMEAS`` command.

        Description:
            - This query returns the maximum number of periodic measurements.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:NUMMEAS?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:NUMMEAS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:NUMMEAS?
            ```
        """
        return self._nummeas

    @property
    def refs(self) -> ConfigurationRefs:
        """Return the ``CONFIGuration:REFS`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:REFS?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:REFS?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.numrefs``: The ``CONFIGuration:REFS:NUMREFS`` command.
        """
        return self._refs

    @property
    def rf(self) -> ConfigurationRf:
        """Return the ``CONFIGuration:RF`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:RF?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:RF?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.advtrig``: The ``CONFIGuration:RF:ADVTRIG`` command.
            - ``.bandwidth``: The ``CONFIGuration:RF:BANDWidth`` command.
            - ``.maxbandwidth``: The ``CONFIGuration:RF:MAXBANDWidth`` command.
            - ``.numchannels``: The ``CONFIGuration:RF:NUMCHANnels`` command.
        """
        return self._rf

    @property
    def rosc(self) -> ConfigurationRosc:
        """Return the ``CONFIGuration:ROSC`` command.

        Description:
            - This query returns a boolean value to indicate whether the instrument has an external
              reference oscillator (ROSC) input.

        Usage:
            - Using the ``.query()`` method will send the ``CONFIGuration:ROSC?`` query.
            - Using the ``.verify(value)`` method will send the ``CONFIGuration:ROSC?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CONFIGuration:ROSC?
            ```
        """
        return self._rosc
