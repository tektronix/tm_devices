"""The status_and_error commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC, AWG5200, AWG5K, AWG5KC, AWG70KA, AWG70KB, AWG7K, AWG7KC, DPO2K, DPO2KB,
DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD,
LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO2K, MSO2KB, MSO4, MSO4B, MSO4K, MSO4KB, MSO5,
MSO5B, MSO5K, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *CLS
    - *ESR?
    - *OPC
    - *OPC?
    - *RST
    - *STB?
    - *WAI
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Wai(SCPICmdWriteNoArguments):
    """The ``*WAI`` command.

    Description:
        - The ``*WAI`` (Wait) command (no query form) prevents the instrument from executing further
          commands or queries until all pending commands that generate an OPC message are complete.
          This command allows you to synchronize the operation of the instrument with your
          application program. For more information, refer to Synchronization Methods.

    Usage:
        - Using the ``.write()`` method will send the ``*WAI`` command.

    SCPI Syntax:
        ```
        - *WAI
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*WAI") -> None:
        super().__init__(device, cmd_syntax)


class Stb(SCPICmdRead):
    """The ``*STB`` command.

    Description:
        - The ``*STB?`` (Read Status Byte) query returns the contents of the Status Byte Register
          (SBR) using the Master Summary Status (MSS) bit. For more information, refer to Registers.

    Usage:
        - Using the ``.query()`` method will send the ``*STB?`` query.
        - Using the ``.verify(value)`` method will send the ``*STB?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - *STB?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*STB") -> None:
        super().__init__(device, cmd_syntax)


class Rst(SCPICmdWriteNoArguments):
    """The ``*RST`` command.

    Description:
        - This command (no query form) resets the instrument to the factory default settings. This
          command does the following: Recalls the default instrument setup. Clears the current
          ``*DDT`` command. Disables aliases (``:ALIAS:STATE 0``). Disables the user password (for
          the ``*PUD`` command). The ``*RST`` command does not change the following: The current
          working directory ( ``:FILESystem:CWD`` command). The state of command headers (
          ``:HEADer`` command). The state of keyword and enumeration verbosity ( ``:VERBose``
          command). The Power-on Status Clear Flag ( ``*PSC`` command). The Event Status Enable
          Register ( ``*ESE`` command). The Service Request Enable Register ( ``*SRE`` command). The
          Device Event Status Enable Register ( DESE command). The user password for protected user
          data ( ``:PASSWord`` command). The content of protected user data ( ``*PUD`` command). The
          enabled state of the socket server ( ``:SOCKETServer:ENAble`` command). The socket server
          port number ( ``:SOCKETServer:PORT`` command). The socket server protocol (
          ``:SOCKETServer:PROTOCol`` command). The USBTMC port configuration (
          ``:USBDevice:CONFigure`` command). The destination reference waveform or file path for the
          ``:CURVe`` command ( ``:DATa:DESTination`` command). The source waveform for the
          ``:CURVe?`` or ``:WAVFrm?`` queries ( ``:DATa:SOUrce`` command). The waveform data
          encoding for the ``:CURVe`` command or query or the ``:WAVFrm?`` query ( ``:DATa:ENCdg``
          command). The starting point for ``:CURVe?`` queries ( ``:DATa:STARt`` command). The
          ending point for ``:CURVe?`` queries ( ``:DATa:STOP`` command). All settings associated
          the ``:WFMInpre`` commands. All user settable settings associated with the WFMOutpre
          commands. ``*RST`` only resets the programmable interface settings, it does not change the
          user interface settings.

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
          for a list of commands that generate an OPC message.

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


class Esr(SCPICmdRead):
    """The ``*ESR`` command.

    Description:
        - This query-only command returns the contents of the Standard Event Status Register (SESR).
          ``*ESR?`` also clears the SESR (since reading the SESR clears it). For a more detailed
          discussion of the use of these registers, see Registers.

    Usage:
        - Using the ``.query()`` method will send the ``*ESR?`` query.
        - Using the ``.verify(value)`` method will send the ``*ESR?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - *ESR?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*ESR") -> None:
        super().__init__(device, cmd_syntax)


class Cls(SCPICmdWriteNoArguments):
    """The ``*CLS`` command.

    Description:
        - This command (no query form) clears the following: Event Queue Standard Event Status
          Register Status Byte Register (except the MAV bit) If the ``*CLS`` command immediately
          follows an <EOI>, the Output Queue and MAV bit (Status Byte Register bit 4) are also
          cleared. MAV indicates that information is in the output queue. The device clear (DCL)
          control message will clear the output queue and thus MAV. ``*CLS`` does not clear the
          output queue or MAV. ``*CLS`` can suppress a Service Request that is to be generated by an
          ``*OPC``. This will happen if a single sequence acquisition operation is still being
          processed when the ``*CLS`` command is executed.

    Usage:
        - Using the ``.write()`` method will send the ``*CLS`` command.

    SCPI Syntax:
        ```
        - *CLS
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*CLS") -> None:
        super().__init__(device, cmd_syntax)
