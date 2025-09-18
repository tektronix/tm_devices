"""The status_and_error commands module.

These commands are used in the following models:
DPO7AX, LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *ESE <NR1>
    - *ESE?
    - *OPC
    - *OPC?
    - *RST
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Rst(SCPICmdWriteNoArguments):
    """The ``*RST`` command.

    Description:
        - This command (no query form) resets the instrument to the factory default settings. This
          command does the following: Recalls the default instrument setup. Clears the current
          ``*DDT`` command. Disables aliases (``:ALIAS:STATE 0``). Disables the user password (for
          the ``*PUD`` command). The ``*RST`` command does not change the following: The current
          working directory (: ``FILESystem:CWD`` command). The state of command headers (: HEADer
          command). The state of keyword and enumeration verbosity (: VERBose command). The Power-on
          Status Clear Flag ( ``*PSC`` command). The Event Status Enable Register ( ``*ESE``
          command). The Service Request Enable Register ( ``*SRE`` command). The Event Status Enable
          Register ( ``*ESE`` command). The Service Request Enable Register ( ``*SRE`` command). The
          Device Event Status Enable Register ( DESE command). The user password for protected user
          data (: PASSWord command). The content of protected user data ( ``*PUD`` command). The
          enabled state of the socket server (: ``SOCKETServer:ENAble`` command). The socket server
          port number (: ``SOCKETServer:PORT`` command). The socket server protocol (:
          ``SOCKETServer:PROTOCol`` command). The USBTMC port configuration (:
          ``USBDevice:CONFigure`` command). The destination reference waveform or file path for the
          : CURVe command (: ``DATa:DESTination`` command). The source waveform for the : CURVe? or
          : WAVFrm? queries (: ``DATa:SOUrce`` command). The source waveform for the : CURVe? or :
          WAVFrm? queries (: ``DATa:SOUrce`` command). The waveform data encoding for the : CURVe
          command or query or the : WAVFrm? query (: ``DATa:ENCdg`` command). The starting point for
          : CURVe? queries (: ``DATa:STARt`` command). The ending point for : CURVe? queries (:
          ``DATa:STOP`` command). All settings associated the : WFMInpre commands. All user settable
          settings associated with the WFMOutpre commands. ``*RST`` only resets the programmable
          interface settings, it does not change the user interface settings.

    Usage:
        - Using the ``.write()`` method will send the ``*RST`` command.

    SCPI Syntax:
        ```
        - *RST
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*RST") -> None:
        super().__init__(device, cmd_syntax)


class Opc(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``*OPC`` command.

    Description:
        - This command generates the operation complete message in the Standard Event Status
          Register (SESR) when all pending commands that generate an OPC message are complete. The
          ``*OPC?`` query places the ASCII character '1' into the output queue when all such OPC
          commands are complete. The ``*OPC?`` response is not available to read until all pending
          operations finish. For a complete discussion of the use of these registers and the output
          queue, see Registers and Queues. The ``*OPC`` command allows you to synchronize the
          operation of the instrument with your application program. For more information, see
          Synchronization Methods. Refer to the Oscilloscope operations that can generate OPC table
          for a list of commands that generate an OPC message. (See Table 3-3.)

    Usage:
        - Using the ``.query()`` method will send the ``*OPC?`` query.
        - Using the ``.verify(value)`` method will send the ``*OPC?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``*OPC`` command.

    SCPI Syntax:
        ```
        - *OPC
        - *OPC?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*OPC") -> None:
        super().__init__(device, cmd_syntax)


class Ese(SCPICmdWrite, SCPICmdRead):
    """The ``*ESE`` command.

    Description:
        - This command sets and queries the bits in the Event Status Enable Register (ESER). The
          ESER prevents events from being reported to the Status Byte Register (STB). For a more
          detailed discussion of the use of these registers, see Registers. Note: Setting the DESER
          and the ESER to the same values allows only those codes to be entered into the Event Queue
          and summarized on the ESB bit (bit 5) of the Status Byte Register. Use the DESE command to
          set the DESER.

    Usage:
        - Using the ``.query()`` method will send the ``*ESE?`` query.
        - Using the ``.verify(value)`` method will send the ``*ESE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*ESE value`` command.

    SCPI Syntax:
        ```
        - *ESE <NR1>
        - *ESE?
        ```

    Info:
        - ``<NR1>`` specifies the binary bits of the ESER according to this value, which ranges from
          0 through 255. The power-on default for the ESER is 0 if ``*PSC`` is 1. If ``*PSC`` is 0,
          the ESER maintains the previous power cycle value through the current power cycle.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*ESE") -> None:
        super().__init__(device, cmd_syntax)
