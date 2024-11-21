# pylint: disable=line-too-long
"""The wlist commands module.

These commands are used in the following models:
AWG5200

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - WLISt:LAST?
    - WLISt:LIST?
    - WLISt:NAME? <Index>
    - WLISt:SIZE?
    - WLISt:SPARameter:APPLy <file_path>
    - WLISt:SPARameter:BANDwidth {FULL|<bandwidth>}
    - WLISt:SPARameter:BANDwidth:AUTO {0|1|OFF|ON}
    - WLISt:SPARameter:BANDwidth:AUTO?
    - WLISt:SPARameter:BANDwidth?
    - WLISt:SPARameter:CASCading:AGGRessor2:ENABle {0|1|ON|OFF}
    - WLISt:SPARameter:CASCading:AGGRessor2:ENABle?
    - WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude <amplitude>
    - WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude?
    - WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk {NEXT|FEXT|BOTH}
    - WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk?
    - WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe <data_rate>
    - WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe?
    - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal {CLOCk|PRBS|FILE|SAVictim}
    - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE <filepath>
    - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE?
    - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS {PRBS7|PRBS9|PRBS15|PRBS16|PRBS20|PRBS21|PRBS23|PRBS29|PRBS31}
    - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS?
    - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal?
    - WLISt:SPARameter:CASCading:DEEMbed {0|1|OFF|ON}
    - WLISt:SPARameter:CASCading:DEEMbed?
    - WLISt:SPARameter:CASCading:STAGe[m]:DRX[n] <port_number>
    - WLISt:SPARameter:CASCading:STAGe[m]:DRX[n]?
    - WLISt:SPARameter:CASCading:STAGe[m]:DTX[n] <port number>
    - WLISt:SPARameter:CASCading:STAGe[m]:DTX[n]?
    - WLISt:SPARameter:CASCading:STAGe[m]:ENABle {0|1|OFF|ON}
    - WLISt:SPARameter:CASCading:STAGe[m]:ENABle?
    - WLISt:SPARameter:CASCading:STAGe[m]:FILE <filepath>
    - WLISt:SPARameter:CASCading:STAGe[m]:RX[n] <port number>
    - WLISt:SPARameter:CASCading:STAGe[m]:RX[n]?
    - WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme {SENDed|DIFFerential}
    - WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme?
    - WLISt:SPARameter:CASCading:STAGe[m]:TX[n] <port number>
    - WLISt:SPARameter:CASCading:STAGe[m]:TX[n]?
    - WLISt:SPARameter:CASCading:STYPe {VICTim|AGGRessor|BOTH}
    - WLISt:SPARameter:CASCading:STYPe?
    - WLISt:SPARameter:CASCading:TYPE {1|2|4|6|8|12}
    - WLISt:SPARameter:CASCading:TYPE?
    - WLISt:SPARameter:MODE {CASC|NCAS}
    - WLISt:SPARameter:MODE?
    - WLISt:SPARameter:NCAScading:AGGRessor2:ENABle {0|1|ON|OFF}
    - WLISt:SPARameter:NCAScading:AGGRessor2:ENABle?
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude <amplitude>
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude?
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk {NEXT|FEXT|BOTH}
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk?
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe <data_rate>
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe?
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal {CLOCk|PRBS|FILE|SAVictim}
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE <filepath>
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE?
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS {PRBS7|PRBS9|PRBS15|PRBS16|PRBS20|PRBS21|PRBS23|PRBS29|PRBS31}
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS?
    - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal?
    - WLISt:SPARameter:NCAScading:DEEMbed {0|1|OFF|ON}
    - WLISt:SPARameter:NCAScading:DEEMbed?
    - WLISt:SPARameter:NCAScading:DRX[n] <port number>
    - WLISt:SPARameter:NCAScading:DRX[n]?
    - WLISt:SPARameter:NCAScading:DTX[n] <port number>
    - WLISt:SPARameter:NCAScading:DTX[n]?
    - WLISt:SPARameter:NCAScading:FILE <filepath>
    - WLISt:SPARameter:NCAScading:LAYout {TYPical|ALTernate}
    - WLISt:SPARameter:NCAScading:LAYout?
    - WLISt:SPARameter:NCAScading:RX[n] <port number>
    - WLISt:SPARameter:NCAScading:RX[n]?
    - WLISt:SPARameter:NCAScading:SSCHeme {SENDed|DIFFerential}
    - WLISt:SPARameter:NCAScading:SSCHeme?
    - WLISt:SPARameter:NCAScading:STYPe {VICTim|AGGRessor|BOTH}
    - WLISt:SPARameter:NCAScading:STYPe?
    - WLISt:SPARameter:NCAScading:TX[n] <port number>
    - WLISt:SPARameter:NCAScading:TX[n]?
    - WLISt:SPARameter:NCAScading:TYPE {1|2|4|6|8|12}
    - WLISt:SPARameter:SFORmat {REAL|I|Q|IQ}
    - WLISt:SPARameter:SFORmat?
    - WLISt:WAVeform:ACFile <file_path>,<wfm_name>[,<Q_file_path>]
    - WLISt:WAVeform:ACFile:GAUSsian {0|1|OFF|ON}
    - WLISt:WAVeform:ACFile:GAUSsian:BANDwidth <bandwidth>
    - WLISt:WAVeform:ACFile:GAUSsian:BANDwidth?
    - WLISt:WAVeform:ACFile:GAUSsian?
    - WLISt:WAVeform:ACFile:RSINc {0|1|OFF|ON}
    - WLISt:WAVeform:ACFile:RSINc?
    - WLISt:WAVeform:ACFile:SKEW {0|1|OFF|ON}
    - WLISt:WAVeform:ACFile:SKEW?
    - WLISt:WAVeform:AMPLitude <wfm_name>,<amplitude>
    - WLISt:WAVeform:AMPLitude? <wfm_name>
    - WLISt:WAVeform:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
    - WLISt:WAVeform:DATA:I <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
    - WLISt:WAVeform:DATA:I? <wfm_name>[,<StartIndex>[,<Size>]]
    - WLISt:WAVeform:DATA:Q <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
    - WLISt:WAVeform:DATA:Q? <wfm_name>[,<StartIndex>[,<Size>]]
    - WLISt:WAVeform:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
    - WLISt:WAVeform:DELete {<wfm_name>|ALL}
    - WLISt:WAVeform:FREQuency <wfm_name>,<frequency>
    - WLISt:WAVeform:FREQuency?
    - WLISt:WAVeform:GRANularity?
    - WLISt:WAVeform:INVert <wfm_name>
    - WLISt:WAVeform:LENGth? <wfm_name>
    - WLISt:WAVeform:LMAXimum?
    - WLISt:WAVeform:LMINimum?
    - WLISt:WAVeform:MARKer:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
    - WLISt:WAVeform:MARKer:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
    - WLISt:WAVeform:MIQ <I_wfm_name>,<Q_wfm_name>
    - WLISt:WAVeform:NEW <wfm_name>,<Size>[,<format>]
    - WLISt:WAVeform:NORMalize <wfm_name>,{FSCale|ZREFerence}
    - WLISt:WAVeform:OFFSet <wfm_name>,<offset>
    - WLISt:WAVeform:OFFSet? <wfm_name>
    - WLISt:WAVeform:RESample <wfm_name>,<size>
    - WLISt:WAVeform:REVerse <wfm_name>
    - WLISt:WAVeform:ROTate <wfm_name>,<phase>
    - WLISt:WAVeform:SFORmat <wfm_name>,{REAL|I|Q}
    - WLISt:WAVeform:SFORmat? <wfm_name>
    - WLISt:WAVeform:SHIFt <wfm_name>,<phase>
    - WLISt:WAVeform:SRATe <wfm_name>,<sample_rate>
    - WLISt:WAVeform:SRATe? <wfm_name>
    - WLISt:WAVeform:TSTamp? <wfm_name>
    - WLISt:WAVeform:TYPE? <wfm_name>
    ```
"""  # noqa: E501

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdReadWithArguments,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class WlistWaveformType(SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:TYPE`` command.

    Description:
        - This command returns the type of the waveform.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:TYPE? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:TYPE? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:TYPE? <wfm_name>
        ```

    Info:
        - ``<wfm_name>`` ::= <string>.
    """


class WlistWaveformTstamp(SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:TSTamp`` command.

    Description:
        - This command returns the timestamp of the specified waveform in the waveform list.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:TSTamp? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:TSTamp? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:TSTamp? <wfm_name>
        ```
    """


class WlistWaveformSrate(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:SRATe`` command.

    Description:
        - The command sets or returns the Recommended Sampling Rate of the specified waveform in the
          waveform list

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:SRATe? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:SRATe? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:SRATe value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:SRATe <wfm_name>,<sample_rate>
        - WLISt:WAVeform:SRATe? <wfm_name>
        ```
    """


class WlistWaveformShift(SCPICmdWrite):
    """The ``WLISt:WAVeform:SHIFt`` command.

    Description:
        - This command shifts the phase of a waveform in the waveform list.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:SHIFt value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:SHIFt <wfm_name>,<phase>
        ```
    """


class WlistWaveformSformat(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:SFORmat`` command.

    Description:
        - This command sets or returns the signal format of the specified waveform in the waveform
          list.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:SFORmat? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:SFORmat? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:SFORmat value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:SFORmat <wfm_name>,{REAL|I|Q}
        - WLISt:WAVeform:SFORmat? <wfm_name>
        ```
    """


class WlistWaveformRotate(SCPICmdWrite):
    """The ``WLISt:WAVeform:ROTate`` command.

    Description:
        - This command rotates the named waveform (in the waveform list).

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:ROTate value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:ROTate <wfm_name>,<phase>
        ```
    """


class WlistWaveformReverse(SCPICmdWrite):
    """The ``WLISt:WAVeform:REVerse`` command.

    Description:
        - This command reverses the order of the named waveform (in the waveform list).

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:REVerse value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:REVerse <wfm_name>
        ```
    """


class WlistWaveformResample(SCPICmdWrite):
    """The ``WLISt:WAVeform:RESample`` command.

    Description:
        - This command resamples the number of points in a waveform in the waveform list.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:RESample value``
          command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:RESample <wfm_name>,<size>
        ```
    """


class WlistWaveformOffset(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:OFFSet`` command.

    Description:
        - This command sets or returns the Recommended Offset of the specified waveform in the
          waveform list.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:OFFSet? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:OFFSet? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:OFFSet value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:OFFSet <wfm_name>,<offset>
        - WLISt:WAVeform:OFFSet? <wfm_name>
        ```
    """


class WlistWaveformNormalize(SCPICmdWrite):
    """The ``WLISt:WAVeform:NORMalize`` command.

    Description:
        - This command normalizes a waveform in the waveform list.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:NORMalize value``
          command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:NORMalize <wfm_name>,{FSCale|ZREFerence}
        ```
    """


class WlistWaveformNew(SCPICmdWrite):
    """The ``WLISt:WAVeform:NEW`` command.

    Description:
        - This command creates a new empty waveform in the waveform list of the current setup.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:NEW value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:NEW <wfm_name>,<Size>[,<format>]
        ```
    """


class WlistWaveformMiq(SCPICmdWrite):
    """The ``WLISt:WAVeform:MIQ`` command.

    Description:
        - This command creates an IQ waveform from two real waveforms. The name is derived from the
          I waveform name.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:MIQ value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:MIQ <I_wfm_name>,<Q_wfm_name>
        ```
    """


class WlistWaveformMarkerData(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:MARKer:DATA`` command.

    Description:
        - This command sets or returns the waveform marker data. This command has a limit of
          999,999,999 bytes of data. If this limit is insufficient, consider the following
          alternatives: Send a more efficient file format using ``MMEM:DATA``. Use Ethernet (ftp,
          http, or file sharing) to transfer the file.

    Usage:
        - Using the ``.query(argument)`` method will send the
          ``WLISt:WAVeform:MARKer:DATA? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:MARKer:DATA? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:MARKer:DATA value``
          command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:MARKer:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
        - WLISt:WAVeform:MARKer:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
        ```
    """


class WlistWaveformMarker(SCPICmdRead):
    """The ``WLISt:WAVeform:MARKer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform:MARKer?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:MARKer?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.data``: The ``WLISt:WAVeform:MARKer:DATA`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._data = WlistWaveformMarkerData(device, f"{self._cmd_syntax}:DATA")

    @property
    def data(self) -> WlistWaveformMarkerData:
        """Return the ``WLISt:WAVeform:MARKer:DATA`` command.

        Description:
            - This command sets or returns the waveform marker data. This command has a limit of
              999,999,999 bytes of data. If this limit is insufficient, consider the following
              alternatives: Send a more efficient file format using ``MMEM:DATA``. Use Ethernet
              (ftp, http, or file sharing) to transfer the file.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:MARKer:DATA? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:MARKer:DATA? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:MARKer:DATA value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:MARKer:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
            - WLISt:WAVeform:MARKer:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
            ```
        """
        return self._data


class WlistWaveformLminimum(SCPICmdRead):
    """The ``WLISt:WAVeform:LMINimum`` command.

    Description:
        - This command returns the minimum number of waveform sample points required for a valid
          waveform. The number of required sample points is dependent on the instrument model.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform:LMINimum?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:LMINimum?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:LMINimum?
        ```
    """


class WlistWaveformLmaximum(SCPICmdRead):
    """The ``WLISt:WAVeform:LMAXimum`` command.

    Description:
        - This command returns the maximum number of waveform sample points allowed.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform:LMAXimum?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:LMAXimum?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:LMAXimum?
        ```
    """


class WlistWaveformLength(SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:LENGth`` command.

    Description:
        - This command returns the size of the specified waveform in the waveform list. The returned
          value represents data points (not bytes).

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:LENGth? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:LENGth? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:LENGth? <wfm_name>
        ```
    """


class WlistWaveformInvert(SCPICmdWrite):
    """The ``WLISt:WAVeform:INVert`` command.

    Description:
        - This command inverts the named waveform (in the waveform list) and preserves the offset.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:INVert value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:INVert <wfm_name>
        ```
    """


class WlistWaveformGranularity(SCPICmdRead):
    """The ``WLISt:WAVeform:GRANularity`` command.

    Description:
        - This command returns the granularity of sample points required for the waveform to be
          valid. The number of sample points of a single channel instrument must be divisible by 2.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform:GRANularity?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:GRANularity?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:GRANularity?
        ```
    """


class WlistWaveformFrequency(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:WAVeform:FREQuency`` command.

    Description:
        - The command sets or returns the Recommended Center Frequency of the named IQ waveform.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform:FREQuency?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:FREQuency?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:FREQuency value``
          command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:FREQuency <wfm_name>,<frequency>
        - WLISt:WAVeform:FREQuency?
        ```
    """


class WlistWaveformDelete(SCPICmdWrite):
    """The ``WLISt:WAVeform:DELete`` command.

    Description:
        - This command deletes a single waveform from the waveform list or all waveforms. If the
          deleted waveform is currently loaded into waveform memory, it is unloaded. If the RUN
          state of the AWG is ON, the state is turned OFF. If the channel is on, it will be switched
          off.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DELete value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:DELete {<wfm_name>|ALL}
        ```
    """


class WlistWaveformDataQ(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:DATA:Q`` command.

    Description:
        - This command transfers analog waveform data from the external controller into the
          specified waveform or from a waveform to the external control program. This command writes
          the data to Q. The waveform must be of the Signal Format type IQ. To write to I data, use
          the command ``WLIST:WAVEFORM:DATA:I``. This command has a limit of 999,999,999 bytes of
          data. As the IEEE 488.2 is a limitation that the largest read or write that may occur in a
          single command is 999,999,999 bytes as the structure is defined as a '#' followed by a
          byte to determine the number of bytes to read '9'. '9' indicates that we need to read 9
          bytes to determine the length of the following data block: 999,999,999 (separated by
          commas to help separate - they will not be present normally). Because of the size
          limitation, it is suggested that the user make use of the starting index (and size for
          querying) to append data in multiple commands/queries. To set marker data, use the command
          ``WLIST:WAVEFORM:MARKER:DATA``.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:DATA:Q? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:DATA:Q? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DATA:Q value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:DATA:Q <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
        - WLISt:WAVeform:DATA:Q? <wfm_name>[,<StartIndex>[,<Size>]]
        ```
    """


class WlistWaveformDataI(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:DATA:I`` command.

    Description:
        - This command transfers waveform data from the external controller into the specified
          waveform or from a waveform to the external control program. This command writes the data
          to I. The waveform must be of the Signal Format type IQ. To write to Q data, use the
          command ``WLIST:WAVEFORM:DATA:Q``. This command has a limit of 999,999,999 bytes of data.
          As the IEEE 488.2 is a limitation that the largest read or write that may occur in a
          single command is 999,999,999 bytes as the structure is defined as a '#' followed by a
          byte to determine the number of bytes to read '9'. '9' indicates that we need to read 9
          bytes to determine the length of the following data block: 999,999,999 (separated by
          commas to help separate - they will not be present normally). Because of the size
          limitation, it is suggested that the user make use of the starting index (and size for
          querying) to append data in multiple commands/queries. To set marker data, use the command
          ``WLIST:WAVEFORM:MARKER:DATA``.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:DATA:I? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:DATA:I? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DATA:I value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:DATA:I <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
        - WLISt:WAVeform:DATA:I? <wfm_name>[,<StartIndex>[,<Size>]]
        ```
    """


class WlistWaveformData(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:DATA`` command.

    Description:
        - This command transfers waveform data from the external controller into the waveform list
          or from the waveform list to the external control program. This command has a limit of
          650,000,000 bytes of data. If this limit is insufficient, consider the following
          alternatives: Use a more efficient file encoding (WFM or PAT) when sending data. Use
          instrument commands for direct control (``WLIST:WAVEFORM:DATA``, FREQ, VOLT, and so on).
          Use Ethernet (ftp, http, or file sharing) to transfer the file. Refer to the User Online
          Help, AWG Reference > Waveform General Information section for the detailed format
          specification.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:DATA? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:DATA? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DATA value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
        - WLISt:WAVeform:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
        ```

    Info:
        - ``StartIndex, Size,<block_data>``
        - ``<wfm_name>`` ::=<string>.
        - ``<StartIndex>`` ::=<NR1>.
        - ``<Size>`` ::=<NR1>.
        - ``<block_data>`` ::=<IEEE 488.2 block>.

    Properties:
        - ``.i``: The ``WLISt:WAVeform:DATA:I`` command.
        - ``.q``: The ``WLISt:WAVeform:DATA:Q`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._i = WlistWaveformDataI(device, f"{self._cmd_syntax}:I")
        self._q = WlistWaveformDataQ(device, f"{self._cmd_syntax}:Q")

    @property
    def i(self) -> WlistWaveformDataI:
        """Return the ``WLISt:WAVeform:DATA:I`` command.

        Description:
            - This command transfers waveform data from the external controller into the specified
              waveform or from a waveform to the external control program. This command writes the
              data to I. The waveform must be of the Signal Format type IQ. To write to Q data, use
              the command ``WLIST:WAVEFORM:DATA:Q``. This command has a limit of 999,999,999 bytes
              of data. As the IEEE 488.2 is a limitation that the largest read or write that may
              occur in a single command is 999,999,999 bytes as the structure is defined as a '#'
              followed by a byte to determine the number of bytes to read '9'. '9' indicates that we
              need to read 9 bytes to determine the length of the following data block: 999,999,999
              (separated by commas to help separate - they will not be present normally). Because of
              the size limitation, it is suggested that the user make use of the starting index (and
              size for querying) to append data in multiple commands/queries. To set marker data,
              use the command ``WLIST:WAVEFORM:MARKER:DATA``.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:DATA:I? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:DATA:I? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DATA:I value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:DATA:I <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
            - WLISt:WAVeform:DATA:I? <wfm_name>[,<StartIndex>[,<Size>]]
            ```
        """
        return self._i

    @property
    def q(self) -> WlistWaveformDataQ:
        """Return the ``WLISt:WAVeform:DATA:Q`` command.

        Description:
            - This command transfers analog waveform data from the external controller into the
              specified waveform or from a waveform to the external control program. This command
              writes the data to Q. The waveform must be of the Signal Format type IQ. To write to I
              data, use the command ``WLIST:WAVEFORM:DATA:I``. This command has a limit of
              999,999,999 bytes of data. As the IEEE 488.2 is a limitation that the largest read or
              write that may occur in a single command is 999,999,999 bytes as the structure is
              defined as a '#' followed by a byte to determine the number of bytes to read '9'. '9'
              indicates that we need to read 9 bytes to determine the length of the following data
              block: 999,999,999 (separated by commas to help separate - they will not be present
              normally). Because of the size limitation, it is suggested that the user make use of
              the starting index (and size for querying) to append data in multiple
              commands/queries. To set marker data, use the command ``WLIST:WAVEFORM:MARKER:DATA``.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:DATA:Q? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:DATA:Q? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DATA:Q value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:DATA:Q <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
            - WLISt:WAVeform:DATA:Q? <wfm_name>[,<StartIndex>[,<Size>]]
            ```
        """
        return self._q


class WlistWaveformAmplitude(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``WLISt:WAVeform:AMPLitude`` command.

    Description:
        - This command sets or returns the Recommended Amplitude (peak-to-peak) of the specified
          waveform in the waveform list.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:AMPLitude? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``WLISt:WAVeform:AMPLitude? argument`` query and raise an AssertionError if the returned
          value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:AMPLitude value``
          command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:AMPLitude <wfm_name>,<amplitude>
        - WLISt:WAVeform:AMPLitude? <wfm_name>
        ```
    """


class WlistWaveformAcfileSkew(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:WAVeform:ACFile:SKEW`` command.

    Description:
        - This command sets or returns whether the measured Skew will be applied during application
          of a precompensation file (correction coefficients file).

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform:ACFile:SKEW?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:ACFile:SKEW?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:ACFile:SKEW value``
          command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:ACFile:SKEW {0|1|OFF|ON}
        - WLISt:WAVeform:ACFile:SKEW?
        ```
    """


class WlistWaveformAcfileRsinc(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:WAVeform:ACFile:RSINc`` command.

    Description:
        - This command sets or returns whether or not corrections for Sin(x)/x distortions will be
          removed during application of a correction file.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform:ACFile:RSINc?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:ACFile:RSINc?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:ACFile:RSINc value``
          command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:ACFile:RSINc {0|1|OFF|ON}
        - WLISt:WAVeform:ACFile:RSINc?
        ```
    """


class WlistWaveformAcfileGaussianBandwidth(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:WAVeform:ACFile:GAUSsian:BANDwidth`` command.

    Description:
        - This command sets or returns the bandwidth of the gaussian filter that is to be applied
          during application of a precompensation file (correction coefficients file).

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform:ACFile:GAUSsian:BANDwidth?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:WAVeform:ACFile:GAUSsian:BANDwidth?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:WAVeform:ACFile:GAUSsian:BANDwidth value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:ACFile:GAUSsian:BANDwidth <bandwidth>
        - WLISt:WAVeform:ACFile:GAUSsian:BANDwidth?
        ```
    """


class WlistWaveformAcfileGaussian(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:WAVeform:ACFile:GAUSsian`` command.

    Description:
        - This command sets or returns whether a gaussian filter will be applied during the
          application of a precompensation file (correction coefficients file).

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform:ACFile:GAUSsian?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:ACFile:GAUSsian?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:ACFile:GAUSsian value``
          command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:ACFile:GAUSsian {0|1|OFF|ON}
        - WLISt:WAVeform:ACFile:GAUSsian?
        ```

    Properties:
        - ``.bandwidth``: The ``WLISt:WAVeform:ACFile:GAUSsian:BANDwidth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._bandwidth = WlistWaveformAcfileGaussianBandwidth(
            device, f"{self._cmd_syntax}:BANDwidth"
        )

    @property
    def bandwidth(self) -> WlistWaveformAcfileGaussianBandwidth:
        """Return the ``WLISt:WAVeform:ACFile:GAUSsian:BANDwidth`` command.

        Description:
            - This command sets or returns the bandwidth of the gaussian filter that is to be
              applied during application of a precompensation file (correction coefficients file).

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:WAVeform:ACFile:GAUSsian:BANDwidth?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:WAVeform:ACFile:GAUSsian:BANDwidth?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:WAVeform:ACFile:GAUSsian:BANDwidth value`` command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:ACFile:GAUSsian:BANDwidth <bandwidth>
            - WLISt:WAVeform:ACFile:GAUSsian:BANDwidth?
            ```
        """
        return self._bandwidth


class WlistWaveformAcfile(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:WAVeform:ACFile`` command.

    Description:
        - This command applies user supplied correction coefficients from an external
          (precompensation) file to the specified waveform (or waveforms) in the waveform list. If
          the waveform is IQ (complex), you can add individual corrections files to the I and Q
          components of the complex waveform by using the optional syntax component.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:ACFile value`` command.

    SCPI Syntax:
        ```
        - WLISt:WAVeform:ACFile <file_path>,<wfm_name>[,<Q_file_path>]
        ```

    Properties:
        - ``.gaussian``: The ``WLISt:WAVeform:ACFile:GAUSsian`` command.
        - ``.rsinc``: The ``WLISt:WAVeform:ACFile:RSINc`` command.
        - ``.skew``: The ``WLISt:WAVeform:ACFile:SKEW`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._gaussian = WlistWaveformAcfileGaussian(device, f"{self._cmd_syntax}:GAUSsian")
        self._rsinc = WlistWaveformAcfileRsinc(device, f"{self._cmd_syntax}:RSINc")
        self._skew = WlistWaveformAcfileSkew(device, f"{self._cmd_syntax}:SKEW")

    @property
    def gaussian(self) -> WlistWaveformAcfileGaussian:
        """Return the ``WLISt:WAVeform:ACFile:GAUSsian`` command.

        Description:
            - This command sets or returns whether a gaussian filter will be applied during the
              application of a precompensation file (correction coefficients file).

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:WAVeform:ACFile:GAUSsian?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:ACFile:GAUSsian?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:WAVeform:ACFile:GAUSsian value`` command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:ACFile:GAUSsian {0|1|OFF|ON}
            - WLISt:WAVeform:ACFile:GAUSsian?
            ```

        Sub-properties:
            - ``.bandwidth``: The ``WLISt:WAVeform:ACFile:GAUSsian:BANDwidth`` command.
        """
        return self._gaussian

    @property
    def rsinc(self) -> WlistWaveformAcfileRsinc:
        """Return the ``WLISt:WAVeform:ACFile:RSINc`` command.

        Description:
            - This command sets or returns whether or not corrections for Sin(x)/x distortions will
              be removed during application of a correction file.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:WAVeform:ACFile:RSINc?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:ACFile:RSINc?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:ACFile:RSINc value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:ACFile:RSINc {0|1|OFF|ON}
            - WLISt:WAVeform:ACFile:RSINc?
            ```
        """
        return self._rsinc

    @property
    def skew(self) -> WlistWaveformAcfileSkew:
        """Return the ``WLISt:WAVeform:ACFile:SKEW`` command.

        Description:
            - This command sets or returns whether the measured Skew will be applied during
              application of a precompensation file (correction coefficients file).

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:WAVeform:ACFile:SKEW?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:ACFile:SKEW?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:ACFile:SKEW value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:ACFile:SKEW {0|1|OFF|ON}
            - WLISt:WAVeform:ACFile:SKEW?
            ```
        """
        return self._skew


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class WlistWaveform(SCPICmdRead):
    """The ``WLISt:WAVeform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:WAVeform?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.acfile``: The ``WLISt:WAVeform:ACFile`` command.
        - ``.amplitude``: The ``WLISt:WAVeform:AMPLitude`` command.
        - ``.data``: The ``WLISt:WAVeform:DATA`` command.
        - ``.delete``: The ``WLISt:WAVeform:DELete`` command.
        - ``.frequency``: The ``WLISt:WAVeform:FREQuency`` command.
        - ``.granularity``: The ``WLISt:WAVeform:GRANularity`` command.
        - ``.invert``: The ``WLISt:WAVeform:INVert`` command.
        - ``.length``: The ``WLISt:WAVeform:LENGth`` command.
        - ``.lmaximum``: The ``WLISt:WAVeform:LMAXimum`` command.
        - ``.lminimum``: The ``WLISt:WAVeform:LMINimum`` command.
        - ``.marker``: The ``WLISt:WAVeform:MARKer`` command tree.
        - ``.miq``: The ``WLISt:WAVeform:MIQ`` command.
        - ``.new``: The ``WLISt:WAVeform:NEW`` command.
        - ``.normalize``: The ``WLISt:WAVeform:NORMalize`` command.
        - ``.offset``: The ``WLISt:WAVeform:OFFSet`` command.
        - ``.resample``: The ``WLISt:WAVeform:RESample`` command.
        - ``.reverse``: The ``WLISt:WAVeform:REVerse`` command.
        - ``.rotate``: The ``WLISt:WAVeform:ROTate`` command.
        - ``.sformat``: The ``WLISt:WAVeform:SFORmat`` command.
        - ``.shift``: The ``WLISt:WAVeform:SHIFt`` command.
        - ``.srate``: The ``WLISt:WAVeform:SRATe`` command.
        - ``.tstamp``: The ``WLISt:WAVeform:TSTamp`` command.
        - ``.type``: The ``WLISt:WAVeform:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._acfile = WlistWaveformAcfile(device, f"{self._cmd_syntax}:ACFile")
        self._amplitude = WlistWaveformAmplitude(device, f"{self._cmd_syntax}:AMPLitude")
        self._data = WlistWaveformData(device, f"{self._cmd_syntax}:DATA")
        self._delete = WlistWaveformDelete(device, f"{self._cmd_syntax}:DELete")
        self._frequency = WlistWaveformFrequency(device, f"{self._cmd_syntax}:FREQuency")
        self._granularity = WlistWaveformGranularity(device, f"{self._cmd_syntax}:GRANularity")
        self._invert = WlistWaveformInvert(device, f"{self._cmd_syntax}:INVert")
        self._length = WlistWaveformLength(device, f"{self._cmd_syntax}:LENGth")
        self._lmaximum = WlistWaveformLmaximum(device, f"{self._cmd_syntax}:LMAXimum")
        self._lminimum = WlistWaveformLminimum(device, f"{self._cmd_syntax}:LMINimum")
        self._marker = WlistWaveformMarker(device, f"{self._cmd_syntax}:MARKer")
        self._miq = WlistWaveformMiq(device, f"{self._cmd_syntax}:MIQ")
        self._new = WlistWaveformNew(device, f"{self._cmd_syntax}:NEW")
        self._normalize = WlistWaveformNormalize(device, f"{self._cmd_syntax}:NORMalize")
        self._offset = WlistWaveformOffset(device, f"{self._cmd_syntax}:OFFSet")
        self._resample = WlistWaveformResample(device, f"{self._cmd_syntax}:RESample")
        self._reverse = WlistWaveformReverse(device, f"{self._cmd_syntax}:REVerse")
        self._rotate = WlistWaveformRotate(device, f"{self._cmd_syntax}:ROTate")
        self._sformat = WlistWaveformSformat(device, f"{self._cmd_syntax}:SFORmat")
        self._shift = WlistWaveformShift(device, f"{self._cmd_syntax}:SHIFt")
        self._srate = WlistWaveformSrate(device, f"{self._cmd_syntax}:SRATe")
        self._tstamp = WlistWaveformTstamp(device, f"{self._cmd_syntax}:TSTamp")
        self._type = WlistWaveformType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def acfile(self) -> WlistWaveformAcfile:
        """Return the ``WLISt:WAVeform:ACFile`` command.

        Description:
            - This command applies user supplied correction coefficients from an external
              (precompensation) file to the specified waveform (or waveforms) in the waveform list.
              If the waveform is IQ (complex), you can add individual corrections files to the I and
              Q components of the complex waveform by using the optional syntax component.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:ACFile value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:ACFile <file_path>,<wfm_name>[,<Q_file_path>]
            ```

        Sub-properties:
            - ``.gaussian``: The ``WLISt:WAVeform:ACFile:GAUSsian`` command.
            - ``.rsinc``: The ``WLISt:WAVeform:ACFile:RSINc`` command.
            - ``.skew``: The ``WLISt:WAVeform:ACFile:SKEW`` command.
        """
        return self._acfile

    @property
    def amplitude(self) -> WlistWaveformAmplitude:
        """Return the ``WLISt:WAVeform:AMPLitude`` command.

        Description:
            - This command sets or returns the Recommended Amplitude (peak-to-peak) of the specified
              waveform in the waveform list.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:AMPLitude? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:AMPLitude? argument`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:AMPLitude value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:AMPLitude <wfm_name>,<amplitude>
            - WLISt:WAVeform:AMPLitude? <wfm_name>
            ```
        """
        return self._amplitude

    @property
    def data(self) -> WlistWaveformData:
        """Return the ``WLISt:WAVeform:DATA`` command.

        Description:
            - This command transfers waveform data from the external controller into the waveform
              list or from the waveform list to the external control program. This command has a
              limit of 650,000,000 bytes of data. If this limit is insufficient, consider the
              following alternatives: Use a more efficient file encoding (WFM or PAT) when sending
              data. Use instrument commands for direct control (``WLIST:WAVEFORM:DATA``, FREQ, VOLT,
              and so on). Use Ethernet (ftp, http, or file sharing) to transfer the file. Refer to
              the User Online Help, AWG Reference > Waveform General Information section for the
              detailed format specification.

        Usage:
            - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:DATA? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:DATA? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DATA value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:DATA <wfm_name>[,<StartIndex>[,<Size>]],<block_data>
            - WLISt:WAVeform:DATA? <wfm_name>[,<StartIndex>[,<Size>]]
            ```

        Info:
            - ``StartIndex, Size,<block_data>``
            - ``<wfm_name>`` ::=<string>.
            - ``<StartIndex>`` ::=<NR1>.
            - ``<Size>`` ::=<NR1>.
            - ``<block_data>`` ::=<IEEE 488.2 block>.

        Sub-properties:
            - ``.i``: The ``WLISt:WAVeform:DATA:I`` command.
            - ``.q``: The ``WLISt:WAVeform:DATA:Q`` command.
        """
        return self._data

    @property
    def delete(self) -> WlistWaveformDelete:
        """Return the ``WLISt:WAVeform:DELete`` command.

        Description:
            - This command deletes a single waveform from the waveform list or all waveforms. If the
              deleted waveform is currently loaded into waveform memory, it is unloaded. If the RUN
              state of the AWG is ON, the state is turned OFF. If the channel is on, it will be
              switched off.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:DELete value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:DELete {<wfm_name>|ALL}
            ```
        """
        return self._delete

    @property
    def frequency(self) -> WlistWaveformFrequency:
        """Return the ``WLISt:WAVeform:FREQuency`` command.

        Description:
            - The command sets or returns the Recommended Center Frequency of the named IQ waveform.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:WAVeform:FREQuency?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:FREQuency?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:FREQuency value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:FREQuency <wfm_name>,<frequency>
            - WLISt:WAVeform:FREQuency?
            ```
        """
        return self._frequency

    @property
    def granularity(self) -> WlistWaveformGranularity:
        """Return the ``WLISt:WAVeform:GRANularity`` command.

        Description:
            - This command returns the granularity of sample points required for the waveform to be
              valid. The number of sample points of a single channel instrument must be divisible by
              2.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:WAVeform:GRANularity?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:GRANularity?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:GRANularity?
            ```
        """
        return self._granularity

    @property
    def invert(self) -> WlistWaveformInvert:
        """Return the ``WLISt:WAVeform:INVert`` command.

        Description:
            - This command inverts the named waveform (in the waveform list) and preserves the
              offset.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:INVert value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:INVert <wfm_name>
            ```
        """
        return self._invert

    @property
    def length(self) -> WlistWaveformLength:
        """Return the ``WLISt:WAVeform:LENGth`` command.

        Description:
            - This command returns the size of the specified waveform in the waveform list. The
              returned value represents data points (not bytes).

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:LENGth? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:LENGth? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:LENGth? <wfm_name>
            ```
        """
        return self._length

    @property
    def lmaximum(self) -> WlistWaveformLmaximum:
        """Return the ``WLISt:WAVeform:LMAXimum`` command.

        Description:
            - This command returns the maximum number of waveform sample points allowed.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:WAVeform:LMAXimum?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:LMAXimum?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:LMAXimum?
            ```
        """
        return self._lmaximum

    @property
    def lminimum(self) -> WlistWaveformLminimum:
        """Return the ``WLISt:WAVeform:LMINimum`` command.

        Description:
            - This command returns the minimum number of waveform sample points required for a valid
              waveform. The number of required sample points is dependent on the instrument model.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:WAVeform:LMINimum?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:LMINimum?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:LMINimum?
            ```
        """
        return self._lminimum

    @property
    def marker(self) -> WlistWaveformMarker:
        """Return the ``WLISt:WAVeform:MARKer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:WAVeform:MARKer?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform:MARKer?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.data``: The ``WLISt:WAVeform:MARKer:DATA`` command.
        """
        return self._marker

    @property
    def miq(self) -> WlistWaveformMiq:
        """Return the ``WLISt:WAVeform:MIQ`` command.

        Description:
            - This command creates an IQ waveform from two real waveforms. The name is derived from
              the I waveform name.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:MIQ value`` command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:MIQ <I_wfm_name>,<Q_wfm_name>
            ```
        """
        return self._miq

    @property
    def new(self) -> WlistWaveformNew:
        """Return the ``WLISt:WAVeform:NEW`` command.

        Description:
            - This command creates a new empty waveform in the waveform list of the current setup.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:NEW value`` command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:NEW <wfm_name>,<Size>[,<format>]
            ```
        """
        return self._new

    @property
    def normalize(self) -> WlistWaveformNormalize:
        """Return the ``WLISt:WAVeform:NORMalize`` command.

        Description:
            - This command normalizes a waveform in the waveform list.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:NORMalize value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:NORMalize <wfm_name>,{FSCale|ZREFerence}
            ```
        """
        return self._normalize

    @property
    def offset(self) -> WlistWaveformOffset:
        """Return the ``WLISt:WAVeform:OFFSet`` command.

        Description:
            - This command sets or returns the Recommended Offset of the specified waveform in the
              waveform list.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:OFFSet? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:OFFSet? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:OFFSet value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:OFFSet <wfm_name>,<offset>
            - WLISt:WAVeform:OFFSet? <wfm_name>
            ```
        """
        return self._offset

    @property
    def resample(self) -> WlistWaveformResample:
        """Return the ``WLISt:WAVeform:RESample`` command.

        Description:
            - This command resamples the number of points in a waveform in the waveform list.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:RESample value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:RESample <wfm_name>,<size>
            ```
        """
        return self._resample

    @property
    def reverse(self) -> WlistWaveformReverse:
        """Return the ``WLISt:WAVeform:REVerse`` command.

        Description:
            - This command reverses the order of the named waveform (in the waveform list).

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:REVerse value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:REVerse <wfm_name>
            ```
        """
        return self._reverse

    @property
    def rotate(self) -> WlistWaveformRotate:
        """Return the ``WLISt:WAVeform:ROTate`` command.

        Description:
            - This command rotates the named waveform (in the waveform list).

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:ROTate value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:ROTate <wfm_name>,<phase>
            ```
        """
        return self._rotate

    @property
    def sformat(self) -> WlistWaveformSformat:
        """Return the ``WLISt:WAVeform:SFORmat`` command.

        Description:
            - This command sets or returns the signal format of the specified waveform in the
              waveform list.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:SFORmat? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:SFORmat? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:SFORmat value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:SFORmat <wfm_name>,{REAL|I|Q}
            - WLISt:WAVeform:SFORmat? <wfm_name>
            ```
        """
        return self._sformat

    @property
    def shift(self) -> WlistWaveformShift:
        """Return the ``WLISt:WAVeform:SHIFt`` command.

        Description:
            - This command shifts the phase of a waveform in the waveform list.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:SHIFt value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:SHIFt <wfm_name>,<phase>
            ```
        """
        return self._shift

    @property
    def srate(self) -> WlistWaveformSrate:
        """Return the ``WLISt:WAVeform:SRATe`` command.

        Description:
            - The command sets or returns the Recommended Sampling Rate of the specified waveform in
              the waveform list

        Usage:
            - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:SRATe? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:SRATe? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:WAVeform:SRATe value``
              command.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:SRATe <wfm_name>,<sample_rate>
            - WLISt:WAVeform:SRATe? <wfm_name>
            ```
        """
        return self._srate

    @property
    def tstamp(self) -> WlistWaveformTstamp:
        """Return the ``WLISt:WAVeform:TSTamp`` command.

        Description:
            - This command returns the timestamp of the specified waveform in the waveform list.

        Usage:
            - Using the ``.query(argument)`` method will send the
              ``WLISt:WAVeform:TSTamp? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:TSTamp? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:TSTamp? <wfm_name>
            ```
        """
        return self._tstamp

    @property
    def type(self) -> WlistWaveformType:
        """Return the ``WLISt:WAVeform:TYPE`` command.

        Description:
            - This command returns the type of the waveform.

        Usage:
            - Using the ``.query(argument)`` method will send the ``WLISt:WAVeform:TYPE? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``WLISt:WAVeform:TYPE? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:WAVeform:TYPE? <wfm_name>
            ```

        Info:
            - ``<wfm_name>`` ::= <string>.
        """
        return self._type


class WlistSparameterSformat(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:SFORmat`` command.

    Description:
        - This command sets or returns the currently used signal format for setting the S-Parameter
          values.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:SFORmat?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:SFORmat?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:SPARameter:SFORmat value``
          command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:SFORmat {REAL|I|Q|IQ}
        - WLISt:SPARameter:SFORmat?
        ```
    """


class WlistSparameterNcascadingType(SCPICmdWrite):
    """The ``WLISt:SPARameter:NCAScading:TYPE`` command.

    Description:
        - This command sets or returns the S-Parameter number of ports, in Non-Cascading mode.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:TYPE value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:TYPE {1|2|4|6|8|12}
        ```
    """


class WlistSparameterNcascadingTxItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:TX[n]`` command.

    Description:
        - This command sets or returns the S-Parameter port assignment of the channel's specified
          transmission port number (Tx-Port) in Non-Cascading mode and Single-Ended Signalling
          Scheme (where applicable).

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:TX[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:NCAScading:TX[n]?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:TX[n] value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:TX[n] <port number>
        - WLISt:SPARameter:NCAScading:TX[n]?
        ```
    """


class WlistSparameterNcascadingStype(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:STYPe`` command.

    Description:
        - This command sets or returns S-Parameter signal type (victim or aggressor), in
          Non-Cascading mode. The number of ports must be either 8 or 12.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:STYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:NCAScading:STYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:STYPe value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:STYPe {VICTim|AGGRessor|BOTH}
        - WLISt:SPARameter:NCAScading:STYPe?
        ```
    """


class WlistSparameterNcascadingSscheme(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:SSCHeme`` command.

    Description:
        - This command sets or returns the S-Parameter Signalling Scheme, in Non-Cascading mode.
          Signalling Scheme is only available when the Number of Ports is set to 4, 8, or 12.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:SSCHeme?``
          query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:NCAScading:SSCHeme?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:SSCHeme value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:SSCHeme {SENDed|DIFFerential}
        - WLISt:SPARameter:NCAScading:SSCHeme?
        ```
    """


class WlistSparameterNcascadingRxItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:RX[n]`` command.

    Description:
        - This command sets or returns the S-Parameter port assignment of the channel's specified
          receiver port number (Rx-Port) in Non-Cascading mode and Single-Ended Signalling Scheme
          (where applicable).

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:RX[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:NCAScading:RX[n]?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:RX[n] value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:RX[n] <port number>
        - WLISt:SPARameter:NCAScading:RX[n]?
        ```
    """


class WlistSparameterNcascadingLayout(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:LAYout`` command.

    Description:
        - This command sets or returns the 4 port S-Parameter Matrix Configuration, in Non-Cascading
          mode.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:LAYout?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:NCAScading:LAYout?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:LAYout value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:LAYout {TYPical|ALTernate}
        - WLISt:SPARameter:NCAScading:LAYout?
        ```
    """


class WlistSparameterNcascadingFile(SCPICmdWrite):
    """The ``WLISt:SPARameter:NCAScading:FILE`` command.

    Description:
        - This command sets or returns the filepath and file name of the S-Parameter file, in
          Non-Cascading mode.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:FILE value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:FILE <filepath>
        ```
    """


class WlistSparameterNcascadingDtxItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:DTX[n]`` command.

    Description:
        - This command sets or returns the S-Parameter port assignment of the channel's specified
          transmission port number (Tx-Port) in Non-Cascading mode and Differential Signalling
          Scheme (where applicable).

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:DTX[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:NCAScading:DTX[n]?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:DTX[n] value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:DTX[n] <port number>
        - WLISt:SPARameter:NCAScading:DTX[n]?
        ```
    """


class WlistSparameterNcascadingDrxItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:DRX[n]`` command.

    Description:
        - This command sets or returns the S-Parameter port assignment of the channel's specified
          receiver port number (Rx-Port) in Non-Cascading mode and Differential Signalling Scheme
          (where applicable).

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:DRX[n]?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:NCAScading:DRX[n]?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:DRX[n] value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:DRX[n] <port number>
        - WLISt:SPARameter:NCAScading:DRX[n]?
        ```
    """


class WlistSparameterNcascadingDeembed(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:DEEMbed`` command.

    Description:
        - This command sets or returns whether the Non-Cascading S-Parameters is to de-embed
          (invert) the S-Parameters, in Non-Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:DEEMbed?``
          query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:NCAScading:DEEMbed?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:DEEMbed value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:DEEMbed {0|1|OFF|ON}
        - WLISt:SPARameter:NCAScading:DEEMbed?
        ```
    """


class WlistSparameterNcascadingAggressorItemSignalPrbs(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS`` command.

    Description:
        - This command sets or returns the specified Aggressor's PRBS signal type, in Non-Cascading
          mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS {PRBS7|PRBS9|PRBS15|PRBS16|PRBS20|PRBS21|PRBS23|PRBS29|PRBS31}
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS?
        ```
    """  # noqa: E501


class WlistSparameterNcascadingAggressorItemSignalFile(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE`` command.

    Description:
        - This command sets or returns the filepath to the aggressor file for the specified
          Aggressor, in Non-Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE <filepath>
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE?
        ```
    """


class WlistSparameterNcascadingAggressorItemSignal(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal`` command.

    Description:
        - This command sets or returns specified Aggressor's signal type, in Non-Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal {CLOCk|PRBS|FILE|SAVictim}
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal?
        ```

    Properties:
        - ``.file``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE`` command.
        - ``.prbs``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._file = WlistSparameterNcascadingAggressorItemSignalFile(
            device, f"{self._cmd_syntax}:FILE"
        )
        self._prbs = WlistSparameterNcascadingAggressorItemSignalPrbs(
            device, f"{self._cmd_syntax}:PRBS"
        )

    @property
    def file(self) -> WlistSparameterNcascadingAggressorItemSignalFile:
        """Return the ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE`` command.

        Description:
            - This command sets or returns the filepath to the aggressor file for the specified
              Aggressor, in Non-Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE <filepath>
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE?
            ```
        """
        return self._file

    @property
    def prbs(self) -> WlistSparameterNcascadingAggressorItemSignalPrbs:
        """Return the ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS`` command.

        Description:
            - This command sets or returns the specified Aggressor's PRBS signal type, in
              Non-Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS {PRBS7|PRBS9|PRBS15|PRBS16|PRBS20|PRBS21|PRBS23|PRBS29|PRBS31}
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS?
            ```
        """  # noqa: E501
        return self._prbs


class WlistSparameterNcascadingAggressorItemDrate(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe`` command.

    Description:
        - This command sets or returns the specified Aggressor's data rate, in Non-Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe <data_rate>
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe?
        ```
    """


class WlistSparameterNcascadingAggressorItemCtalk(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk`` command.

    Description:
        - This command sets or returns the specified Aggressor's crosstalk type, in Non-Cascading
          mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk {NEXT|FEXT|BOTH}
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk?
        ```
    """


class WlistSparameterNcascadingAggressorItemAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude`` command.

    Description:
        - This command sets or returns the specified Aggressor's amplitude, in Non-Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude <amplitude>
        - WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude?
        ```
    """


class WlistSparameterNcascadingAggressorItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:AGGRessor[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:AGGRessor[n]?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor[n]?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude`` command.
        - ``.ctalk``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk`` command.
        - ``.drate``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe`` command.
        - ``.signal``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = WlistSparameterNcascadingAggressorItemAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )
        self._ctalk = WlistSparameterNcascadingAggressorItemCtalk(
            device, f"{self._cmd_syntax}:CTALk"
        )
        self._drate = WlistSparameterNcascadingAggressorItemDrate(
            device, f"{self._cmd_syntax}:DRATe"
        )
        self._signal = WlistSparameterNcascadingAggressorItemSignal(
            device, f"{self._cmd_syntax}:SIGNal"
        )

    @property
    def amplitude(self) -> WlistSparameterNcascadingAggressorItemAmplitude:
        """Return the ``WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude`` command.

        Description:
            - This command sets or returns the specified Aggressor's amplitude, in Non-Cascading
              mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude <amplitude>
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude?
            ```
        """
        return self._amplitude

    @property
    def ctalk(self) -> WlistSparameterNcascadingAggressorItemCtalk:
        """Return the ``WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk`` command.

        Description:
            - This command sets or returns the specified Aggressor's crosstalk type, in
              Non-Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk {NEXT|FEXT|BOTH}
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk?
            ```
        """
        return self._ctalk

    @property
    def drate(self) -> WlistSparameterNcascadingAggressorItemDrate:
        """Return the ``WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe`` command.

        Description:
            - This command sets or returns the specified Aggressor's data rate, in Non-Cascading
              mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe <data_rate>
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe?
            ```
        """
        return self._drate

    @property
    def signal(self) -> WlistSparameterNcascadingAggressorItemSignal:
        """Return the ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal`` command.

        Description:
            - This command sets or returns specified Aggressor's signal type, in Non-Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal {CLOCk|PRBS|FILE|SAVictim}
            - WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal?
            ```

        Sub-properties:
            - ``.file``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:FILE`` command.
            - ``.prbs``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal:PRBS`` command.
        """
        return self._signal


class WlistSparameterNcascadingAggressor2Enable(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:AGGRessor2:ENABle`` command.

    Description:
        - This command sets or returns the aggressor 2 signal type state (enabled or disabled) in
          Non-Cascading mode. Aggressor2 signals are available when the number of ports is set to
          12.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor2:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor2:ENABle?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor2:ENABle value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:NCAScading:AGGRessor2:ENABle {0|1|ON|OFF}
        - WLISt:SPARameter:NCAScading:AGGRessor2:ENABle?
        ```
    """


class WlistSparameterNcascadingAggressor2(SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading:AGGRessor2`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:AGGRessor2?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:NCAScading:AGGRessor2?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``WLISt:SPARameter:NCAScading:AGGRessor2:ENABle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = WlistSparameterNcascadingAggressor2Enable(
            device, f"{self._cmd_syntax}:ENABle"
        )

    @property
    def enable(self) -> WlistSparameterNcascadingAggressor2Enable:
        """Return the ``WLISt:SPARameter:NCAScading:AGGRessor2:ENABle`` command.

        Description:
            - This command sets or returns the aggressor 2 signal type state (enabled or disabled)
              in Non-Cascading mode. Aggressor2 signals are available when the number of ports is
              set to 12.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor2:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor2:ENABle?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor2:ENABle value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:AGGRessor2:ENABle {0|1|ON|OFF}
            - WLISt:SPARameter:NCAScading:AGGRessor2:ENABle?
            ```
        """
        return self._enable


#  pylint: disable=too-many-instance-attributes
class WlistSparameterNcascading(SCPICmdRead):
    """The ``WLISt:SPARameter:NCAScading`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:NCAScading?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.aggressor2``: The ``WLISt:SPARameter:NCAScading:AGGRessor2`` command tree.
        - ``.aggressor``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]`` command tree.
        - ``.deembed``: The ``WLISt:SPARameter:NCAScading:DEEMbed`` command.
        - ``.drx``: The ``WLISt:SPARameter:NCAScading:DRX[n]`` command.
        - ``.dtx``: The ``WLISt:SPARameter:NCAScading:DTX[n]`` command.
        - ``.file``: The ``WLISt:SPARameter:NCAScading:FILE`` command.
        - ``.layout``: The ``WLISt:SPARameter:NCAScading:LAYout`` command.
        - ``.rx``: The ``WLISt:SPARameter:NCAScading:RX[n]`` command.
        - ``.sscheme``: The ``WLISt:SPARameter:NCAScading:SSCHeme`` command.
        - ``.stype``: The ``WLISt:SPARameter:NCAScading:STYPe`` command.
        - ``.tx``: The ``WLISt:SPARameter:NCAScading:TX[n]`` command.
        - ``.type``: The ``WLISt:SPARameter:NCAScading:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aggressor2 = WlistSparameterNcascadingAggressor2(
            device, f"{self._cmd_syntax}:AGGRessor2"
        )
        self._aggressor: Dict[int, WlistSparameterNcascadingAggressorItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: WlistSparameterNcascadingAggressorItem(
                    device, f"{self._cmd_syntax}:AGGRessor{x}"
                )
            )
        )
        self._deembed = WlistSparameterNcascadingDeembed(device, f"{self._cmd_syntax}:DEEMbed")
        self._drx: Dict[int, WlistSparameterNcascadingDrxItem] = DefaultDictPassKeyToFactory(
            lambda x: WlistSparameterNcascadingDrxItem(device, f"{self._cmd_syntax}:DRX{x}")
        )
        self._dtx: Dict[int, WlistSparameterNcascadingDtxItem] = DefaultDictPassKeyToFactory(
            lambda x: WlistSparameterNcascadingDtxItem(device, f"{self._cmd_syntax}:DTX{x}")
        )
        self._file = WlistSparameterNcascadingFile(device, f"{self._cmd_syntax}:FILE")
        self._layout = WlistSparameterNcascadingLayout(device, f"{self._cmd_syntax}:LAYout")
        self._rx: Dict[int, WlistSparameterNcascadingRxItem] = DefaultDictPassKeyToFactory(
            lambda x: WlistSparameterNcascadingRxItem(device, f"{self._cmd_syntax}:RX{x}")
        )
        self._sscheme = WlistSparameterNcascadingSscheme(device, f"{self._cmd_syntax}:SSCHeme")
        self._stype = WlistSparameterNcascadingStype(device, f"{self._cmd_syntax}:STYPe")
        self._tx: Dict[int, WlistSparameterNcascadingTxItem] = DefaultDictPassKeyToFactory(
            lambda x: WlistSparameterNcascadingTxItem(device, f"{self._cmd_syntax}:TX{x}")
        )
        self._type = WlistSparameterNcascadingType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def aggressor2(self) -> WlistSparameterNcascadingAggressor2:
        """Return the ``WLISt:SPARameter:NCAScading:AGGRessor2`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor2?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor2?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``WLISt:SPARameter:NCAScading:AGGRessor2:ENABle`` command.
        """
        return self._aggressor2

    @property
    def aggressor(self) -> Dict[int, WlistSparameterNcascadingAggressorItem]:
        """Return the ``WLISt:SPARameter:NCAScading:AGGRessor[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:AGGRessor[n]?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:AMPLitude`` command.
            - ``.ctalk``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:CTALk`` command.
            - ``.drate``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:DRATe`` command.
            - ``.signal``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]:SIGNal`` command.
        """
        return self._aggressor

    @property
    def deembed(self) -> WlistSparameterNcascadingDeembed:
        """Return the ``WLISt:SPARameter:NCAScading:DEEMbed`` command.

        Description:
            - This command sets or returns whether the Non-Cascading S-Parameters is to de-embed
              (invert) the S-Parameters, in Non-Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:DEEMbed?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:DEEMbed?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:DEEMbed value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:DEEMbed {0|1|OFF|ON}
            - WLISt:SPARameter:NCAScading:DEEMbed?
            ```
        """
        return self._deembed

    @property
    def drx(self) -> Dict[int, WlistSparameterNcascadingDrxItem]:
        """Return the ``WLISt:SPARameter:NCAScading:DRX[n]`` command.

        Description:
            - This command sets or returns the S-Parameter port assignment of the channel's
              specified receiver port number (Rx-Port) in Non-Cascading mode and Differential
              Signalling Scheme (where applicable).

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:DRX[n]?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:DRX[n]?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:DRX[n] value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:DRX[n] <port number>
            - WLISt:SPARameter:NCAScading:DRX[n]?
            ```
        """
        return self._drx

    @property
    def dtx(self) -> Dict[int, WlistSparameterNcascadingDtxItem]:
        """Return the ``WLISt:SPARameter:NCAScading:DTX[n]`` command.

        Description:
            - This command sets or returns the S-Parameter port assignment of the channel's
              specified transmission port number (Tx-Port) in Non-Cascading mode and Differential
              Signalling Scheme (where applicable).

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:DTX[n]?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:DTX[n]?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:DTX[n] value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:DTX[n] <port number>
            - WLISt:SPARameter:NCAScading:DTX[n]?
            ```
        """
        return self._dtx

    @property
    def file(self) -> WlistSparameterNcascadingFile:
        """Return the ``WLISt:SPARameter:NCAScading:FILE`` command.

        Description:
            - This command sets or returns the filepath and file name of the S-Parameter file, in
              Non-Cascading mode.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:FILE value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:FILE <filepath>
            ```
        """
        return self._file

    @property
    def layout(self) -> WlistSparameterNcascadingLayout:
        """Return the ``WLISt:SPARameter:NCAScading:LAYout`` command.

        Description:
            - This command sets or returns the 4 port S-Parameter Matrix Configuration, in
              Non-Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:LAYout?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:LAYout?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:LAYout value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:LAYout {TYPical|ALTernate}
            - WLISt:SPARameter:NCAScading:LAYout?
            ```
        """
        return self._layout

    @property
    def rx(self) -> Dict[int, WlistSparameterNcascadingRxItem]:
        """Return the ``WLISt:SPARameter:NCAScading:RX[n]`` command.

        Description:
            - This command sets or returns the S-Parameter port assignment of the channel's
              specified receiver port number (Rx-Port) in Non-Cascading mode and Single-Ended
              Signalling Scheme (where applicable).

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:RX[n]?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:RX[n]?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:RX[n] value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:RX[n] <port number>
            - WLISt:SPARameter:NCAScading:RX[n]?
            ```
        """
        return self._rx

    @property
    def sscheme(self) -> WlistSparameterNcascadingSscheme:
        """Return the ``WLISt:SPARameter:NCAScading:SSCHeme`` command.

        Description:
            - This command sets or returns the S-Parameter Signalling Scheme, in Non-Cascading mode.
              Signalling Scheme is only available when the Number of Ports is set to 4, 8, or 12.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:SSCHeme?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:SSCHeme?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:SSCHeme value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:SSCHeme {SENDed|DIFFerential}
            - WLISt:SPARameter:NCAScading:SSCHeme?
            ```
        """
        return self._sscheme

    @property
    def stype(self) -> WlistSparameterNcascadingStype:
        """Return the ``WLISt:SPARameter:NCAScading:STYPe`` command.

        Description:
            - This command sets or returns S-Parameter signal type (victim or aggressor), in
              Non-Cascading mode. The number of ports must be either 8 or 12.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:STYPe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:STYPe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:STYPe value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:STYPe {VICTim|AGGRessor|BOTH}
            - WLISt:SPARameter:NCAScading:STYPe?
            ```
        """
        return self._stype

    @property
    def tx(self) -> Dict[int, WlistSparameterNcascadingTxItem]:
        """Return the ``WLISt:SPARameter:NCAScading:TX[n]`` command.

        Description:
            - This command sets or returns the S-Parameter port assignment of the channel's
              specified transmission port number (Tx-Port) in Non-Cascading mode and Single-Ended
              Signalling Scheme (where applicable).

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading:TX[n]?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:TX[n]?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:TX[n] value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:TX[n] <port number>
            - WLISt:SPARameter:NCAScading:TX[n]?
            ```
        """
        return self._tx

    @property
    def type(self) -> WlistSparameterNcascadingType:
        """Return the ``WLISt:SPARameter:NCAScading:TYPE`` command.

        Description:
            - This command sets or returns the S-Parameter number of ports, in Non-Cascading mode.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:NCAScading:TYPE value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:NCAScading:TYPE {1|2|4|6|8|12}
            ```
        """
        return self._type


class WlistSparameterMode(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:MODE`` command.

    Description:
        - This command sets or returns the S-Parameter mode (Cascading or Non-Cascading).

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:MODE?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:MODE?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:SPARameter:MODE value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:MODE {CASC|NCAS}
        - WLISt:SPARameter:MODE?
        ```

    Info:
        - ``CASCading`` sets the S-Parameter mode to cascading. allowing you to cascade up to six
          S-parameter files and apply the characteristics on the waveform.
        - ``NCASCading`` sets the S-Parameter mode to non-cascading, allowing you to apply
          S-parameter characteristics on the waveform from only one S-parameter file.
    """


class WlistSparameterCascadingType(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:TYPE`` command.

    Description:
        - This command sets or returns the S-Parameter number of ports, in Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:CASCading:TYPE?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:SPARameter:CASCading:TYPE value``
          command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:TYPE {1|2|4|6|8|12}
        - WLISt:SPARameter:CASCading:TYPE?
        ```
    """


class WlistSparameterCascadingStype(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:STYPe`` command.

    Description:
        - This command sets or returns S-Parameter signal type (victim or aggressor), in Cascading
          mode. The number of ports must be either 8 or 12.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:STYPe?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:CASCading:STYPe?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STYPe value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:STYPe {VICTim|AGGRessor|BOTH}
        - WLISt:SPARameter:CASCading:STYPe?
        ```
    """


class WlistSparameterCascadingStageItemTxItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:STAGe[m]:TX[n]`` command.

    Description:
        - This command sets or returns the S-Parameter port assignment of the specified Stage and
          the channel's specified transmission port number (Tx-Port) in Cascading mode and
          Single-Ended Signalling Scheme (where applicable).

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:STAGe[m]:TX[n]?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:TX[n]?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:TX[n] value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:STAGe[m]:TX[n] <port number>
        - WLISt:SPARameter:CASCading:STAGe[m]:TX[n]?
        ```
    """


class WlistSparameterCascadingStageItemSscheme(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme`` command.

    Description:
        - This command sets or returns the S-Parameter Signalling Scheme, in Cascading mode.
          Signalling Scheme is only available when the Number of Ports is set to 4, 8, or 12.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme {SENDed|DIFFerential}
        - WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme?
        ```
    """


class WlistSparameterCascadingStageItemRxItem(ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:STAGe[m]:RX[n]`` command.

    Description:
        - This command sets or returns the S-Parameter port assignment of the specified Stage and
          the channel's specified receiver port number (Rx-Port) in Cascading mode and Single-Ended
          Signalling Scheme (where applicable).

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:STAGe[m]:RX[n]?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:RX[n]?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:RX[n] value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:STAGe[m]:RX[n] <port number>
        - WLISt:SPARameter:CASCading:STAGe[m]:RX[n]?
        ```
    """


class WlistSparameterCascadingStageItemFile(SCPICmdWrite):
    """The ``WLISt:SPARameter:CASCading:STAGe[m]:FILE`` command.

    Description:
        - This command sets or returns the Filepath for the specified S-Parameters Cascading Stage,
          in Cascading mode.

    Usage:
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:FILE value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:STAGe[m]:FILE <filepath>
        ```
    """


class WlistSparameterCascadingStageItemEnable(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:STAGe[m]:ENABle`` command.

    Description:
        - This command sets or returns the state of the specified Cascaded S-Parameter stage
          (enabled or disabled).

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:ENABle?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:ENABle value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:STAGe[m]:ENABle {0|1|OFF|ON}
        - WLISt:SPARameter:CASCading:STAGe[m]:ENABle?
        ```
    """


class WlistSparameterCascadingStageItemDtxItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``WLISt:SPARameter:CASCading:STAGe[m]:DTX[n]`` command.

    Description:
        - This command sets or returns the S-Parameter port assignment of the specified Stage and
          the channel's specified transmission port number (Tx-Port) in Cascading mode and
          Differential Signalling Scheme (where applicable).

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:DTX[n]?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:DTX[n]?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:DTX[n] value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:STAGe[m]:DTX[n] <port number>
        - WLISt:SPARameter:CASCading:STAGe[m]:DTX[n]?
        ```
    """


class WlistSparameterCascadingStageItemDrxItem(
    ValidatedDynamicNumberCmd, SCPICmdWrite, SCPICmdRead
):
    """The ``WLISt:SPARameter:CASCading:STAGe[m]:DRX[n]`` command.

    Description:
        - This command sets or returns the S-Parameter port assignment of the specified Stage and
          the channel's specified receiver port number (Rx-Port) in Cascading mode and Differential
          Signalling Scheme (where applicable).

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:DRX[n]?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:DRX[n]?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:STAGe[m]:DRX[n] value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:STAGe[m]:DRX[n] <port_number>
        - WLISt:SPARameter:CASCading:STAGe[m]:DRX[n]?
        ```
    """


class WlistSparameterCascadingStageItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:STAGe[m]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:STAGe[m]?``
          query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:CASCading:STAGe[m]?``
          query and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.drx``: The ``WLISt:SPARameter:CASCading:STAGe[m]:DRX[n]`` command.
        - ``.dtx``: The ``WLISt:SPARameter:CASCading:STAGe[m]:DTX[n]`` command.
        - ``.enable``: The ``WLISt:SPARameter:CASCading:STAGe[m]:ENABle`` command.
        - ``.file``: The ``WLISt:SPARameter:CASCading:STAGe[m]:FILE`` command.
        - ``.rx``: The ``WLISt:SPARameter:CASCading:STAGe[m]:RX[n]`` command.
        - ``.sscheme``: The ``WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme`` command.
        - ``.tx``: The ``WLISt:SPARameter:CASCading:STAGe[m]:TX[n]`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._drx: Dict[int, WlistSparameterCascadingStageItemDrxItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: WlistSparameterCascadingStageItemDrxItem(
                    device, f"{self._cmd_syntax}:DRX{x}"
                )
            )
        )
        self._dtx: Dict[int, WlistSparameterCascadingStageItemDtxItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: WlistSparameterCascadingStageItemDtxItem(
                    device, f"{self._cmd_syntax}:DTX{x}"
                )
            )
        )
        self._enable = WlistSparameterCascadingStageItemEnable(device, f"{self._cmd_syntax}:ENABle")
        self._file = WlistSparameterCascadingStageItemFile(device, f"{self._cmd_syntax}:FILE")
        self._rx: Dict[int, WlistSparameterCascadingStageItemRxItem] = DefaultDictPassKeyToFactory(
            lambda x: WlistSparameterCascadingStageItemRxItem(device, f"{self._cmd_syntax}:RX{x}")
        )
        self._sscheme = WlistSparameterCascadingStageItemSscheme(
            device, f"{self._cmd_syntax}:SSCHeme"
        )
        self._tx: Dict[int, WlistSparameterCascadingStageItemTxItem] = DefaultDictPassKeyToFactory(
            lambda x: WlistSparameterCascadingStageItemTxItem(device, f"{self._cmd_syntax}:TX{x}")
        )

    @property
    def drx(self) -> Dict[int, WlistSparameterCascadingStageItemDrxItem]:
        """Return the ``WLISt:SPARameter:CASCading:STAGe[m]:DRX[n]`` command.

        Description:
            - This command sets or returns the S-Parameter port assignment of the specified Stage
              and the channel's specified receiver port number (Rx-Port) in Cascading mode and
              Differential Signalling Scheme (where applicable).

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:DRX[n]?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:DRX[n]?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:DRX[n] value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:STAGe[m]:DRX[n] <port_number>
            - WLISt:SPARameter:CASCading:STAGe[m]:DRX[n]?
            ```
        """
        return self._drx

    @property
    def dtx(self) -> Dict[int, WlistSparameterCascadingStageItemDtxItem]:
        """Return the ``WLISt:SPARameter:CASCading:STAGe[m]:DTX[n]`` command.

        Description:
            - This command sets or returns the S-Parameter port assignment of the specified Stage
              and the channel's specified transmission port number (Tx-Port) in Cascading mode and
              Differential Signalling Scheme (where applicable).

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:DTX[n]?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:DTX[n]?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:DTX[n] value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:STAGe[m]:DTX[n] <port number>
            - WLISt:SPARameter:CASCading:STAGe[m]:DTX[n]?
            ```
        """
        return self._dtx

    @property
    def enable(self) -> WlistSparameterCascadingStageItemEnable:
        """Return the ``WLISt:SPARameter:CASCading:STAGe[m]:ENABle`` command.

        Description:
            - This command sets or returns the state of the specified Cascaded S-Parameter stage
              (enabled or disabled).

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:ENABle?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:ENABle value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:STAGe[m]:ENABle {0|1|OFF|ON}
            - WLISt:SPARameter:CASCading:STAGe[m]:ENABle?
            ```
        """
        return self._enable

    @property
    def file(self) -> WlistSparameterCascadingStageItemFile:
        """Return the ``WLISt:SPARameter:CASCading:STAGe[m]:FILE`` command.

        Description:
            - This command sets or returns the Filepath for the specified S-Parameters Cascading
              Stage, in Cascading mode.

        Usage:
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:FILE value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:STAGe[m]:FILE <filepath>
            ```
        """
        return self._file

    @property
    def rx(self) -> Dict[int, WlistSparameterCascadingStageItemRxItem]:
        """Return the ``WLISt:SPARameter:CASCading:STAGe[m]:RX[n]`` command.

        Description:
            - This command sets or returns the S-Parameter port assignment of the specified Stage
              and the channel's specified receiver port number (Rx-Port) in Cascading mode and
              Single-Ended Signalling Scheme (where applicable).

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:RX[n]?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:RX[n]?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:RX[n] value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:STAGe[m]:RX[n] <port number>
            - WLISt:SPARameter:CASCading:STAGe[m]:RX[n]?
            ```
        """
        return self._rx

    @property
    def sscheme(self) -> WlistSparameterCascadingStageItemSscheme:
        """Return the ``WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme`` command.

        Description:
            - This command sets or returns the S-Parameter Signalling Scheme, in Cascading mode.
              Signalling Scheme is only available when the Number of Ports is set to 4, 8, or 12.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme {SENDed|DIFFerential}
            - WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme?
            ```
        """
        return self._sscheme

    @property
    def tx(self) -> Dict[int, WlistSparameterCascadingStageItemTxItem]:
        """Return the ``WLISt:SPARameter:CASCading:STAGe[m]:TX[n]`` command.

        Description:
            - This command sets or returns the S-Parameter port assignment of the specified Stage
              and the channel's specified transmission port number (Tx-Port) in Cascading mode and
              Single-Ended Signalling Scheme (where applicable).

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:TX[n]?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:TX[n]?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]:TX[n] value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:STAGe[m]:TX[n] <port number>
            - WLISt:SPARameter:CASCading:STAGe[m]:TX[n]?
            ```
        """
        return self._tx


class WlistSparameterCascadingDeembed(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:DEEMbed`` command.

    Description:
        - This command sets or returns whether the Cascading S-Parameters is to de-embed (invert)
          the S-Parameters, in Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:DEEMbed?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:CASCading:DEEMbed?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:DEEMbed value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:DEEMbed {0|1|OFF|ON}
        - WLISt:SPARameter:CASCading:DEEMbed?
        ```
    """


class WlistSparameterCascadingAggressorItemSignalPrbs(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS`` command.

    Description:
        - This command sets or returns the specified Aggressor's PRBS signal type, in Cascading
          mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS {PRBS7|PRBS9|PRBS15|PRBS16|PRBS20|PRBS21|PRBS23|PRBS29|PRBS31}
        - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS?
        ```
    """  # noqa: E501


class WlistSparameterCascadingAggressorItemSignalFile(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE`` command.

    Description:
        - This command sets or returns the filepath to the aggressor file for the specified
          Aggressor, in Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE <filepath>
        - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE?
        ```
    """


class WlistSparameterCascadingAggressorItemSignal(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal`` command.

    Description:
        - This command sets or returns specified Aggressor's signal type, in Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal {CLOCk|PRBS|FILE|SAVictim}
        - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal?
        ```

    Properties:
        - ``.file``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE`` command.
        - ``.prbs``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._file = WlistSparameterCascadingAggressorItemSignalFile(
            device, f"{self._cmd_syntax}:FILE"
        )
        self._prbs = WlistSparameterCascadingAggressorItemSignalPrbs(
            device, f"{self._cmd_syntax}:PRBS"
        )

    @property
    def file(self) -> WlistSparameterCascadingAggressorItemSignalFile:
        """Return the ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE`` command.

        Description:
            - This command sets or returns the filepath to the aggressor file for the specified
              Aggressor, in Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE <filepath>
            - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE?
            ```
        """
        return self._file

    @property
    def prbs(self) -> WlistSparameterCascadingAggressorItemSignalPrbs:
        """Return the ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS`` command.

        Description:
            - This command sets or returns the specified Aggressor's PRBS signal type, in Cascading
              mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS {PRBS7|PRBS9|PRBS15|PRBS16|PRBS20|PRBS21|PRBS23|PRBS29|PRBS31}
            - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS?
            ```
        """  # noqa: E501
        return self._prbs


class WlistSparameterCascadingAggressorItemDrate(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe`` command.

    Description:
        - This command sets or returns the specified Aggressor's data rate, in Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe <data_rate>
        - WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe?
        ```
    """


class WlistSparameterCascadingAggressorItemCtalk(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk`` command.

    Description:
        - This command sets or returns the specified Aggressor's crosstalk type, in Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk?`` query and raise an AssertionError if
          the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk {NEXT|FEXT|BOTH}
        - WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk?
        ```
    """


class WlistSparameterCascadingAggressorItemAmplitude(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude`` command.

    Description:
        - This command sets or returns the specified Aggressor's amplitude, in Cascading mode.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude?`` query and raise an AssertionError
          if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude <amplitude>
        - WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude?
        ```
    """


class WlistSparameterCascadingAggressorItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:AGGRessor[n]`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:AGGRessor[n]?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor[n]?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.amplitude``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude`` command.
        - ``.ctalk``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk`` command.
        - ``.drate``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe`` command.
        - ``.signal``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._amplitude = WlistSparameterCascadingAggressorItemAmplitude(
            device, f"{self._cmd_syntax}:AMPLitude"
        )
        self._ctalk = WlistSparameterCascadingAggressorItemCtalk(
            device, f"{self._cmd_syntax}:CTALk"
        )
        self._drate = WlistSparameterCascadingAggressorItemDrate(
            device, f"{self._cmd_syntax}:DRATe"
        )
        self._signal = WlistSparameterCascadingAggressorItemSignal(
            device, f"{self._cmd_syntax}:SIGNal"
        )

    @property
    def amplitude(self) -> WlistSparameterCascadingAggressorItemAmplitude:
        """Return the ``WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude`` command.

        Description:
            - This command sets or returns the specified Aggressor's amplitude, in Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude <amplitude>
            - WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude?
            ```
        """
        return self._amplitude

    @property
    def ctalk(self) -> WlistSparameterCascadingAggressorItemCtalk:
        """Return the ``WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk`` command.

        Description:
            - This command sets or returns the specified Aggressor's crosstalk type, in Cascading
              mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk {NEXT|FEXT|BOTH}
            - WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk?
            ```
        """
        return self._ctalk

    @property
    def drate(self) -> WlistSparameterCascadingAggressorItemDrate:
        """Return the ``WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe`` command.

        Description:
            - This command sets or returns the specified Aggressor's data rate, in Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe <data_rate>
            - WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe?
            ```
        """
        return self._drate

    @property
    def signal(self) -> WlistSparameterCascadingAggressorItemSignal:
        """Return the ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal`` command.

        Description:
            - This command sets or returns specified Aggressor's signal type, in Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal?`` query and raise an AssertionError
              if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal {CLOCk|PRBS|FILE|SAVictim}
            - WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal?
            ```

        Sub-properties:
            - ``.file``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:FILE`` command.
            - ``.prbs``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal:PRBS`` command.
        """
        return self._signal


class WlistSparameterCascadingAggressor2Enable(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:AGGRessor2:ENABle`` command.

    Description:
        - This command sets or returns whether the aggressor 2 signal type state (enabled or
          disabled) in Cascading mode. Aggressor2 signals are available when the number of ports is
          set to 12.

    Usage:
        - Using the ``.query()`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor2:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor2:ENABle?`` query and raise an AssertionError if the
          returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor2:ENABle value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:CASCading:AGGRessor2:ENABle {0|1|ON|OFF}
        - WLISt:SPARameter:CASCading:AGGRessor2:ENABle?
        ```
    """


class WlistSparameterCascadingAggressor2(SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading:AGGRessor2`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:AGGRessor2?``
          query.
        - Using the ``.verify(value)`` method will send the
          ``WLISt:SPARameter:CASCading:AGGRessor2?`` query and raise an AssertionError if the
          returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``WLISt:SPARameter:CASCading:AGGRessor2:ENABle`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = WlistSparameterCascadingAggressor2Enable(
            device, f"{self._cmd_syntax}:ENABle"
        )

    @property
    def enable(self) -> WlistSparameterCascadingAggressor2Enable:
        """Return the ``WLISt:SPARameter:CASCading:AGGRessor2:ENABle`` command.

        Description:
            - This command sets or returns whether the aggressor 2 signal type state (enabled or
              disabled) in Cascading mode. Aggressor2 signals are available when the number of ports
              is set to 12.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor2:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor2:ENABle?`` query and raise an AssertionError if
              the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor2:ENABle value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:AGGRessor2:ENABle {0|1|ON|OFF}
            - WLISt:SPARameter:CASCading:AGGRessor2:ENABle?
            ```
        """
        return self._enable


class WlistSparameterCascading(SCPICmdRead):
    """The ``WLISt:SPARameter:CASCading`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:CASCading?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.aggressor2``: The ``WLISt:SPARameter:CASCading:AGGRessor2`` command tree.
        - ``.aggressor``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]`` command tree.
        - ``.deembed``: The ``WLISt:SPARameter:CASCading:DEEMbed`` command.
        - ``.stage``: The ``WLISt:SPARameter:CASCading:STAGe[m]`` command tree.
        - ``.stype``: The ``WLISt:SPARameter:CASCading:STYPe`` command.
        - ``.type``: The ``WLISt:SPARameter:CASCading:TYPE`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._aggressor2 = WlistSparameterCascadingAggressor2(
            device, f"{self._cmd_syntax}:AGGRessor2"
        )
        self._aggressor: Dict[int, WlistSparameterCascadingAggressorItem] = (
            DefaultDictPassKeyToFactory(
                lambda x: WlistSparameterCascadingAggressorItem(
                    device, f"{self._cmd_syntax}:AGGRessor{x}"
                )
            )
        )
        self._deembed = WlistSparameterCascadingDeembed(device, f"{self._cmd_syntax}:DEEMbed")
        self._stage: Dict[int, WlistSparameterCascadingStageItem] = DefaultDictPassKeyToFactory(
            lambda x: WlistSparameterCascadingStageItem(device, f"{self._cmd_syntax}:STAGe{x}")
        )
        self._stype = WlistSparameterCascadingStype(device, f"{self._cmd_syntax}:STYPe")
        self._type = WlistSparameterCascadingType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def aggressor2(self) -> WlistSparameterCascadingAggressor2:
        """Return the ``WLISt:SPARameter:CASCading:AGGRessor2`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:AGGRessor2?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor2?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.enable``: The ``WLISt:SPARameter:CASCading:AGGRessor2:ENABle`` command.
        """
        return self._aggressor2

    @property
    def aggressor(self) -> Dict[int, WlistSparameterCascadingAggressorItem]:
        """Return the ``WLISt:SPARameter:CASCading:AGGRessor[n]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]?`` query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:AGGRessor[n]?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.amplitude``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:AMPLitude`` command.
            - ``.ctalk``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:CTALk`` command.
            - ``.drate``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:DRATe`` command.
            - ``.signal``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]:SIGNal`` command.
        """
        return self._aggressor

    @property
    def deembed(self) -> WlistSparameterCascadingDeembed:
        """Return the ``WLISt:SPARameter:CASCading:DEEMbed`` command.

        Description:
            - This command sets or returns whether the Cascading S-Parameters is to de-embed
              (invert) the S-Parameters, in Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:DEEMbed?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:DEEMbed?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:DEEMbed value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:DEEMbed {0|1|OFF|ON}
            - WLISt:SPARameter:CASCading:DEEMbed?
            ```
        """
        return self._deembed

    @property
    def stage(self) -> Dict[int, WlistSparameterCascadingStageItem]:
        """Return the ``WLISt:SPARameter:CASCading:STAGe[m]`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:STAGe[m]?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STAGe[m]?`` query and raise an AssertionError if the
              returned value does not match ``value``.

        Sub-properties:
            - ``.drx``: The ``WLISt:SPARameter:CASCading:STAGe[m]:DRX[n]`` command.
            - ``.dtx``: The ``WLISt:SPARameter:CASCading:STAGe[m]:DTX[n]`` command.
            - ``.enable``: The ``WLISt:SPARameter:CASCading:STAGe[m]:ENABle`` command.
            - ``.file``: The ``WLISt:SPARameter:CASCading:STAGe[m]:FILE`` command.
            - ``.rx``: The ``WLISt:SPARameter:CASCading:STAGe[m]:RX[n]`` command.
            - ``.sscheme``: The ``WLISt:SPARameter:CASCading:STAGe[m]:SSCHeme`` command.
            - ``.tx``: The ``WLISt:SPARameter:CASCading:STAGe[m]:TX[n]`` command.
        """
        return self._stage

    @property
    def stype(self) -> WlistSparameterCascadingStype:
        """Return the ``WLISt:SPARameter:CASCading:STYPe`` command.

        Description:
            - This command sets or returns S-Parameter signal type (victim or aggressor), in
              Cascading mode. The number of ports must be either 8 or 12.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:STYPe?``
              query.
            - Using the ``.verify(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STYPe?`` query and raise an AssertionError if the
              returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:STYPe value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:STYPe {VICTim|AGGRessor|BOTH}
            - WLISt:SPARameter:CASCading:STYPe?
            ```
        """
        return self._stype

    @property
    def type(self) -> WlistSparameterCascadingType:
        """Return the ``WLISt:SPARameter:CASCading:TYPE`` command.

        Description:
            - This command sets or returns the S-Parameter number of ports, in Cascading mode.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading:TYPE?``
              query.
            - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:CASCading:TYPE?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:CASCading:TYPE value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:CASCading:TYPE {1|2|4|6|8|12}
            - WLISt:SPARameter:CASCading:TYPE?
            ```
        """
        return self._type


class WlistSparameterBandwidthAuto(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:BANDwidth:AUTO`` command.

    Description:
        - This command sets or returns the S-Parameter automatic bandwidth calculation setting. The
          bandwidth is defined at the point where the signal rolls off to -60 dB. If this results in
          a bandwidth greater than the instrument supports, the bandwidth is set to ½ of the
          waveform's sample rate (i.e. Nyquist Frequency).

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:BANDwidth:AUTO?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:BANDwidth:AUTO?``
          query and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:SPARameter:BANDwidth:AUTO value``
          command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:BANDwidth:AUTO {0|1|OFF|ON}
        - WLISt:SPARameter:BANDwidth:AUTO?
        ```
    """


class WlistSparameterBandwidth(SCPICmdWrite, SCPICmdRead):
    """The ``WLISt:SPARameter:BANDwidth`` command.

    Description:
        - This command sets or returns the S-Parameter bandwidth when setting manually.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter:BANDwidth?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:BANDwidth?`` query
          and raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``WLISt:SPARameter:BANDwidth value``
          command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:BANDwidth {FULL|<bandwidth>}
        - WLISt:SPARameter:BANDwidth?
        ```

    Properties:
        - ``.auto``: The ``WLISt:SPARameter:BANDwidth:AUTO`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._auto = WlistSparameterBandwidthAuto(device, f"{self._cmd_syntax}:AUTO")

    @property
    def auto(self) -> WlistSparameterBandwidthAuto:
        """Return the ``WLISt:SPARameter:BANDwidth:AUTO`` command.

        Description:
            - This command sets or returns the S-Parameter automatic bandwidth calculation setting.
              The bandwidth is defined at the point where the signal rolls off to -60 dB. If this
              results in a bandwidth greater than the instrument supports, the bandwidth is set to ½
              of the waveform's sample rate (i.e. Nyquist Frequency).

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:BANDwidth:AUTO?``
              query.
            - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:BANDwidth:AUTO?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the
              ``WLISt:SPARameter:BANDwidth:AUTO value`` command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:BANDwidth:AUTO {0|1|OFF|ON}
            - WLISt:SPARameter:BANDwidth:AUTO?
            ```
        """
        return self._auto


class WlistSparameterApply(SCPICmdWrite):
    """The ``WLISt:SPARameter:APPLy`` command.

    Description:
        - This command applies S-Parameters to a waveform that exists in the waveform list of the
          current setup.

    Usage:
        - Using the ``.write(value)`` method will send the ``WLISt:SPARameter:APPLy value`` command.

    SCPI Syntax:
        ```
        - WLISt:SPARameter:APPLy <file_path>
        ```
    """


class WlistSparameter(SCPICmdRead):
    """The ``WLISt:SPARameter`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SPARameter?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.apply``: The ``WLISt:SPARameter:APPLy`` command.
        - ``.bandwidth``: The ``WLISt:SPARameter:BANDwidth`` command.
        - ``.cascading``: The ``WLISt:SPARameter:CASCading`` command tree.
        - ``.mode``: The ``WLISt:SPARameter:MODE`` command.
        - ``.ncascading``: The ``WLISt:SPARameter:NCAScading`` command tree.
        - ``.sformat``: The ``WLISt:SPARameter:SFORmat`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._apply = WlistSparameterApply(device, f"{self._cmd_syntax}:APPLy")
        self._bandwidth = WlistSparameterBandwidth(device, f"{self._cmd_syntax}:BANDwidth")
        self._cascading = WlistSparameterCascading(device, f"{self._cmd_syntax}:CASCading")
        self._mode = WlistSparameterMode(device, f"{self._cmd_syntax}:MODE")
        self._ncascading = WlistSparameterNcascading(device, f"{self._cmd_syntax}:NCAScading")
        self._sformat = WlistSparameterSformat(device, f"{self._cmd_syntax}:SFORmat")

    @property
    def apply(self) -> WlistSparameterApply:
        """Return the ``WLISt:SPARameter:APPLy`` command.

        Description:
            - This command applies S-Parameters to a waveform that exists in the waveform list of
              the current setup.

        Usage:
            - Using the ``.write(value)`` method will send the ``WLISt:SPARameter:APPLy value``
              command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:APPLy <file_path>
            ```
        """
        return self._apply

    @property
    def bandwidth(self) -> WlistSparameterBandwidth:
        """Return the ``WLISt:SPARameter:BANDwidth`` command.

        Description:
            - This command sets or returns the S-Parameter bandwidth when setting manually.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:BANDwidth?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:BANDwidth?``
              query and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:SPARameter:BANDwidth value``
              command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:BANDwidth {FULL|<bandwidth>}
            - WLISt:SPARameter:BANDwidth?
            ```

        Sub-properties:
            - ``.auto``: The ``WLISt:SPARameter:BANDwidth:AUTO`` command.
        """
        return self._bandwidth

    @property
    def cascading(self) -> WlistSparameterCascading:
        """Return the ``WLISt:SPARameter:CASCading`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:CASCading?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:CASCading?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.aggressor2``: The ``WLISt:SPARameter:CASCading:AGGRessor2`` command tree.
            - ``.aggressor``: The ``WLISt:SPARameter:CASCading:AGGRessor[n]`` command tree.
            - ``.deembed``: The ``WLISt:SPARameter:CASCading:DEEMbed`` command.
            - ``.stage``: The ``WLISt:SPARameter:CASCading:STAGe[m]`` command tree.
            - ``.stype``: The ``WLISt:SPARameter:CASCading:STYPe`` command.
            - ``.type``: The ``WLISt:SPARameter:CASCading:TYPE`` command.
        """
        return self._cascading

    @property
    def mode(self) -> WlistSparameterMode:
        """Return the ``WLISt:SPARameter:MODE`` command.

        Description:
            - This command sets or returns the S-Parameter mode (Cascading or Non-Cascading).

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:MODE?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:MODE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:SPARameter:MODE value``
              command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:MODE {CASC|NCAS}
            - WLISt:SPARameter:MODE?
            ```

        Info:
            - ``CASCading`` sets the S-Parameter mode to cascading. allowing you to cascade up to
              six S-parameter files and apply the characteristics on the waveform.
            - ``NCASCading`` sets the S-Parameter mode to non-cascading, allowing you to apply
              S-parameter characteristics on the waveform from only one S-parameter file.
        """
        return self._mode

    @property
    def ncascading(self) -> WlistSparameterNcascading:
        """Return the ``WLISt:SPARameter:NCAScading`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:NCAScading?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:NCAScading?``
              query and raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.aggressor2``: The ``WLISt:SPARameter:NCAScading:AGGRessor2`` command tree.
            - ``.aggressor``: The ``WLISt:SPARameter:NCAScading:AGGRessor[n]`` command tree.
            - ``.deembed``: The ``WLISt:SPARameter:NCAScading:DEEMbed`` command.
            - ``.drx``: The ``WLISt:SPARameter:NCAScading:DRX[n]`` command.
            - ``.dtx``: The ``WLISt:SPARameter:NCAScading:DTX[n]`` command.
            - ``.file``: The ``WLISt:SPARameter:NCAScading:FILE`` command.
            - ``.layout``: The ``WLISt:SPARameter:NCAScading:LAYout`` command.
            - ``.rx``: The ``WLISt:SPARameter:NCAScading:RX[n]`` command.
            - ``.sscheme``: The ``WLISt:SPARameter:NCAScading:SSCHeme`` command.
            - ``.stype``: The ``WLISt:SPARameter:NCAScading:STYPe`` command.
            - ``.tx``: The ``WLISt:SPARameter:NCAScading:TX[n]`` command.
            - ``.type``: The ``WLISt:SPARameter:NCAScading:TYPE`` command.
        """
        return self._ncascading

    @property
    def sformat(self) -> WlistSparameterSformat:
        """Return the ``WLISt:SPARameter:SFORmat`` command.

        Description:
            - This command sets or returns the currently used signal format for setting the
              S-Parameter values.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter:SFORmat?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter:SFORmat?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``WLISt:SPARameter:SFORmat value``
              command.

        SCPI Syntax:
            ```
            - WLISt:SPARameter:SFORmat {REAL|I|Q|IQ}
            - WLISt:SPARameter:SFORmat?
            ```
        """
        return self._sformat


class WlistSize(SCPICmdRead):
    """The ``WLISt:SIZE`` command.

    Description:
        - This command returns the number of waveforms in the waveform list.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:SIZE?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:SIZE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:SIZE?
        ```
    """


class WlistName(SCPICmdReadWithArguments):
    """The ``WLISt:NAME`` command.

    Description:
        - This command returns the waveform name from the waveform list at the position specified by
          the index value.

    Usage:
        - Using the ``.query(argument)`` method will send the ``WLISt:NAME? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the ``WLISt:NAME? argument`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:NAME? <Index>
        ```
    """


class WlistList(SCPICmdRead):
    """The ``WLISt:LIST`` command.

    Description:
        - This command returns a list of all waveform names in the waveform list.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:LIST?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:LIST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:LIST?
        ```
    """


class WlistLast(SCPICmdRead):
    """The ``WLISt:LAST`` command.

    Description:
        - This command returns the name of the most recently added waveform in the waveform list.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt:LAST?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt:LAST?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WLISt:LAST?
        ```
    """


class Wlist(SCPICmdRead):
    """The ``WLISt`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WLISt?`` query.
        - Using the ``.verify(value)`` method will send the ``WLISt?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.last``: The ``WLISt:LAST`` command.
        - ``.list``: The ``WLISt:LIST`` command.
        - ``.name``: The ``WLISt:NAME`` command.
        - ``.size``: The ``WLISt:SIZE`` command.
        - ``.sparameter``: The ``WLISt:SPARameter`` command tree.
        - ``.waveform``: The ``WLISt:WAVeform`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "WLISt") -> None:
        super().__init__(device, cmd_syntax)
        self._last = WlistLast(device, f"{self._cmd_syntax}:LAST")
        self._list = WlistList(device, f"{self._cmd_syntax}:LIST")
        self._name = WlistName(device, f"{self._cmd_syntax}:NAME")
        self._size = WlistSize(device, f"{self._cmd_syntax}:SIZE")
        self._sparameter = WlistSparameter(device, f"{self._cmd_syntax}:SPARameter")
        self._waveform = WlistWaveform(device, f"{self._cmd_syntax}:WAVeform")

    @property
    def last(self) -> WlistLast:
        """Return the ``WLISt:LAST`` command.

        Description:
            - This command returns the name of the most recently added waveform in the waveform
              list.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:LAST?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:LAST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:LAST?
            ```
        """
        return self._last

    @property
    def list(self) -> WlistList:
        """Return the ``WLISt:LIST`` command.

        Description:
            - This command returns a list of all waveform names in the waveform list.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:LIST?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:LIST?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:LIST?
            ```
        """
        return self._list

    @property
    def name(self) -> WlistName:
        """Return the ``WLISt:NAME`` command.

        Description:
            - This command returns the waveform name from the waveform list at the position
              specified by the index value.

        Usage:
            - Using the ``.query(argument)`` method will send the ``WLISt:NAME? argument`` query.
            - Using the ``.verify(argument, value)`` method will send the ``WLISt:NAME? argument``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:NAME? <Index>
            ```
        """
        return self._name

    @property
    def size(self) -> WlistSize:
        """Return the ``WLISt:SIZE`` command.

        Description:
            - This command returns the number of waveforms in the waveform list.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SIZE?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:SIZE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WLISt:SIZE?
            ```
        """
        return self._size

    @property
    def sparameter(self) -> WlistSparameter:
        """Return the ``WLISt:SPARameter`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:SPARameter?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:SPARameter?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.apply``: The ``WLISt:SPARameter:APPLy`` command.
            - ``.bandwidth``: The ``WLISt:SPARameter:BANDwidth`` command.
            - ``.cascading``: The ``WLISt:SPARameter:CASCading`` command tree.
            - ``.mode``: The ``WLISt:SPARameter:MODE`` command.
            - ``.ncascading``: The ``WLISt:SPARameter:NCAScading`` command tree.
            - ``.sformat``: The ``WLISt:SPARameter:SFORmat`` command.
        """
        return self._sparameter

    @property
    def waveform(self) -> WlistWaveform:
        """Return the ``WLISt:WAVeform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``WLISt:WAVeform?`` query.
            - Using the ``.verify(value)`` method will send the ``WLISt:WAVeform?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.acfile``: The ``WLISt:WAVeform:ACFile`` command.
            - ``.amplitude``: The ``WLISt:WAVeform:AMPLitude`` command.
            - ``.data``: The ``WLISt:WAVeform:DATA`` command.
            - ``.delete``: The ``WLISt:WAVeform:DELete`` command.
            - ``.frequency``: The ``WLISt:WAVeform:FREQuency`` command.
            - ``.granularity``: The ``WLISt:WAVeform:GRANularity`` command.
            - ``.invert``: The ``WLISt:WAVeform:INVert`` command.
            - ``.length``: The ``WLISt:WAVeform:LENGth`` command.
            - ``.lmaximum``: The ``WLISt:WAVeform:LMAXimum`` command.
            - ``.lminimum``: The ``WLISt:WAVeform:LMINimum`` command.
            - ``.marker``: The ``WLISt:WAVeform:MARKer`` command tree.
            - ``.miq``: The ``WLISt:WAVeform:MIQ`` command.
            - ``.new``: The ``WLISt:WAVeform:NEW`` command.
            - ``.normalize``: The ``WLISt:WAVeform:NORMalize`` command.
            - ``.offset``: The ``WLISt:WAVeform:OFFSet`` command.
            - ``.resample``: The ``WLISt:WAVeform:RESample`` command.
            - ``.reverse``: The ``WLISt:WAVeform:REVerse`` command.
            - ``.rotate``: The ``WLISt:WAVeform:ROTate`` command.
            - ``.sformat``: The ``WLISt:WAVeform:SFORmat`` command.
            - ``.shift``: The ``WLISt:WAVeform:SHIFt`` command.
            - ``.srate``: The ``WLISt:WAVeform:SRATe`` command.
            - ``.tstamp``: The ``WLISt:WAVeform:TSTamp`` command.
            - ``.type``: The ``WLISt:WAVeform:TYPE`` command.
        """
        return self._waveform
