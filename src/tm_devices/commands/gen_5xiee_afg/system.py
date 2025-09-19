"""The system commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SYSTem:BEEPer:IMMediate
    - SYSTem:BEEPer:STATe {ON|OFF|<NR1>}
    - SYSTem:BEEPer:STATe?
    - SYSTem:ERRor:NEXT?
    - SYSTem:KCLick:STATe {ON|OFF|<NR1>}
    - SYSTem:KCLick:STATe?
    - SYSTem:KLOCk:STATe {ON|OFF|<NR1>}
    - SYSTem:KLOCk:STATe?
    - SYSTem:PASSword:CDISable <password>
    - SYSTem:PASSword:CENable <password>
    - SYSTem:PASSword:CENable:STATe?
    - SYSTem:PASSword:NEW <current_password>,<new_password>
    - SYSTem:SECurity:IMMediate
    - SYSTem:ULANguage {ENGLish|FRENch|GERMan|JAPanese|KORean|SCHinese|TCHinese|RUSSian}
    - SYSTem:ULANguage?
    - SYSTem:VERSion?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SystemVersion(SCPICmdRead):
    """The ``SYSTem:VERSion`` command.

    Description:
        - This query-only command returns the conformed SCPI version of the instrument.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:VERSion?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:VERSion?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SYSTem:VERSion?
        ```
    """


class SystemUlanguage(SCPICmdWrite, SCPICmdRead):
    """The ``SYSTem:ULANguage`` command.

    Description:
        - This command sets or queries the language that the instrument uses to display information
          on the screen.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ULANguage?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ULANguage?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYSTem:ULANguage value`` command.

    SCPI Syntax:
        ```
        - SYSTem:ULANguage {ENGLish|FRENch|GERMan|JAPanese|KORean|SCHinese|TCHinese|RUSSian}
        - SYSTem:ULANguage?
        ```
    """


class SystemSecurityImmediate(SCPICmdWriteNoArguments):
    """The ``SYSTem:SECurity:IMMediate`` command.

    Description:
        - This command erases all the current instrument setups, setup memory, last setup memory,
          user waveform memory, and log content, and recalls the factory default settings.
          Calibration data is not erased. The communication settings are initialized to the factory
          default settings. This might cause a remote communication error.

    Usage:
        - Using the ``.write()`` method will send the ``SYSTem:SECurity:IMMediate`` command.

    SCPI Syntax:
        ```
        - SYSTem:SECurity:IMMediate
        ```
    """


class SystemSecurity(SCPICmdRead):
    """The ``SYSTem:SECurity`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:SECurity?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:SECurity?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.immediate``: The ``SYSTem:SECurity:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._immediate = SystemSecurityImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def immediate(self) -> SystemSecurityImmediate:
        """Return the ``SYSTem:SECurity:IMMediate`` command.

        Description:
            - This command erases all the current instrument setups, setup memory, last setup
              memory, user waveform memory, and log content, and recalls the factory default
              settings. Calibration data is not erased. The communication settings are initialized
              to the factory default settings. This might cause a remote communication error.

        Usage:
            - Using the ``.write()`` method will send the ``SYSTem:SECurity:IMMediate`` command.

        SCPI Syntax:
            ```
            - SYSTem:SECurity:IMMediate
            ```
        """
        return self._immediate


class SystemPasswordNew(SCPICmdWrite):
    """The ``SYSTem:PASSword:NEW`` command.

    Description:
        - This command changes the password.

    Usage:
        - Using the ``.write(value)`` method will send the ``SYSTem:PASSword:NEW value`` command.

    SCPI Syntax:
        ```
        - SYSTem:PASSword:NEW <current_password>,<new_password>
        ```
    """


class SystemPasswordCenableState(SCPICmdRead):
    """The ``SYSTem:PASSword:CENable:STATe`` command.

    Description:
        - This query-only command returns the security protection state.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:PASSword:CENable:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:PASSword:CENable:STATe?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SYSTem:PASSword:CENable:STATe?
        ```
    """


class SystemPasswordCenable(SCPICmdWrite, SCPICmdRead):
    """The ``SYSTem:PASSword:CENable`` command.

    Description:
        - This command enables protected commands to function. The instrument security protection is
          deactivated. In the AFG3000 Series Arbitrary Function Generators, no remote commands are
          under the control of ``SYSTem:PASSword`` commands.

    Usage:
        - Using the ``.write(value)`` method will send the ``SYSTem:PASSword:CENable value``
          command.

    SCPI Syntax:
        ```
        - SYSTem:PASSword:CENable <password>
        ```

    Properties:
        - ``.state``: The ``SYSTem:PASSword:CENable:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = SystemPasswordCenableState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> SystemPasswordCenableState:
        """Return the ``SYSTem:PASSword:CENable:STATe`` command.

        Description:
            - This query-only command returns the security protection state.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:PASSword:CENable:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:PASSword:CENable:STATe?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SYSTem:PASSword:CENable:STATe?
            ```
        """
        return self._state


class SystemPasswordCdisable(SCPICmdWrite):
    """The ``SYSTem:PASSword:CDISable`` command.

    Description:
        - This command disables protected commands. The instrument security protection is activated.
          In the AFG3000 Series Arbitrary Function Generators, no remote commands are under the
          control of ``SYSTem:PASSword`` commands.

    Usage:
        - Using the ``.write(value)`` method will send the ``SYSTem:PASSword:CDISable value``
          command.

    SCPI Syntax:
        ```
        - SYSTem:PASSword:CDISable <password>
        ```
    """


class SystemPassword(SCPICmdRead):
    """The ``SYSTem:PASSword`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:PASSword?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:PASSword?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.cdisable``: The ``SYSTem:PASSword:CDISable`` command.
        - ``.new``: The ``SYSTem:PASSword:NEW`` command.
        - ``.cenable``: The ``SYSTem:PASSword:CENable`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._cdisable = SystemPasswordCdisable(device, f"{self._cmd_syntax}:CDISable")
        self._new = SystemPasswordNew(device, f"{self._cmd_syntax}:NEW")
        self._cenable = SystemPasswordCenable(device, f"{self._cmd_syntax}:CENable")

    @property
    def cdisable(self) -> SystemPasswordCdisable:
        """Return the ``SYSTem:PASSword:CDISable`` command.

        Description:
            - This command disables protected commands. The instrument security protection is
              activated. In the AFG3000 Series Arbitrary Function Generators, no remote commands are
              under the control of ``SYSTem:PASSword`` commands.

        Usage:
            - Using the ``.write(value)`` method will send the ``SYSTem:PASSword:CDISable value``
              command.

        SCPI Syntax:
            ```
            - SYSTem:PASSword:CDISable <password>
            ```
        """
        return self._cdisable

    @property
    def new(self) -> SystemPasswordNew:
        """Return the ``SYSTem:PASSword:NEW`` command.

        Description:
            - This command changes the password.

        Usage:
            - Using the ``.write(value)`` method will send the ``SYSTem:PASSword:NEW value``
              command.

        SCPI Syntax:
            ```
            - SYSTem:PASSword:NEW <current_password>,<new_password>
            ```
        """
        return self._new

    @property
    def cenable(self) -> SystemPasswordCenable:
        """Return the ``SYSTem:PASSword:CENable`` command.

        Description:
            - This command enables protected commands to function. The instrument security
              protection is deactivated. In the AFG3000 Series Arbitrary Function Generators, no
              remote commands are under the control of ``SYSTem:PASSword`` commands.

        Usage:
            - Using the ``.write(value)`` method will send the ``SYSTem:PASSword:CENable value``
              command.

        SCPI Syntax:
            ```
            - SYSTem:PASSword:CENable <password>
            ```

        Sub-properties:
            - ``.state``: The ``SYSTem:PASSword:CENable:STATe`` command.
        """
        return self._cenable


class SystemKlockState(SCPICmdWrite, SCPICmdRead):
    """The ``SYSTem:KLOCk:STATe`` command.

    Description:
        - This command locks or unlocks the instrument front panel controls. The query command
          returns '0' (OFF) or '1' (ON).

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:KLOCk:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:KLOCk:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYSTem:KLOCk:STATe value`` command.

    SCPI Syntax:
        ```
        - SYSTem:KLOCk:STATe {ON|OFF|<NR1>}
        - SYSTem:KLOCk:STATe?
        ```
    """


class SystemKlock(SCPICmdRead):
    """The ``SYSTem:KLOCk`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:KLOCk?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:KLOCk?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``SYSTem:KLOCk:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = SystemKlockState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> SystemKlockState:
        """Return the ``SYSTem:KLOCk:STATe`` command.

        Description:
            - This command locks or unlocks the instrument front panel controls. The query command
              returns '0' (OFF) or '1' (ON).

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:KLOCk:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:KLOCk:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYSTem:KLOCk:STATe value`` command.

        SCPI Syntax:
            ```
            - SYSTem:KLOCk:STATe {ON|OFF|<NR1>}
            - SYSTem:KLOCk:STATe?
            ```
        """
        return self._state


class SystemKclickState(SCPICmdWrite, SCPICmdRead):
    """The ``SYSTem:KCLick:STATe`` command.

    Description:
        - This command enables or disables the click sound when you push the front panel buttons or
          turn the general purpose knob. The query command returns '0' (OFF) or '1' (ON).

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:KCLick:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:KCLick:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYSTem:KCLick:STATe value`` command.

    SCPI Syntax:
        ```
        - SYSTem:KCLick:STATe {ON|OFF|<NR1>}
        - SYSTem:KCLick:STATe?
        ```
    """


class SystemKclick(SCPICmdRead):
    """The ``SYSTem:KCLick`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:KCLick?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:KCLick?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``SYSTem:KCLick:STATe`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = SystemKclickState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> SystemKclickState:
        """Return the ``SYSTem:KCLick:STATe`` command.

        Description:
            - This command enables or disables the click sound when you push the front panel buttons
              or turn the general purpose knob. The query command returns '0' (OFF) or '1' (ON).

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:KCLick:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:KCLick:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYSTem:KCLick:STATe value``
              command.

        SCPI Syntax:
            ```
            - SYSTem:KCLick:STATe {ON|OFF|<NR1>}
            - SYSTem:KCLick:STATe?
            ```
        """
        return self._state


class SystemErrorNext(SCPICmdRead):
    """The ``SYSTem:ERRor:NEXT`` command.

    Description:
        - This query-only command returns the contents of the Error/Event queue.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ERRor:NEXT?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:NEXT?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SYSTem:ERRor:NEXT?
        ```
    """


class SystemErrorCmd(SCPICmdRead):
    """The ``SYSTem:ERRor`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:ERRor?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.next``: The ``SYSTem:ERRor:NEXT`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._next = SystemErrorNext(device, f"{self._cmd_syntax}:NEXT")

    @property
    def next(self) -> SystemErrorNext:
        """Return the ``SYSTem:ERRor:NEXT`` command.

        Description:
            - This query-only command returns the contents of the Error/Event queue.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:ERRor:NEXT?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor:NEXT?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SYSTem:ERRor:NEXT?
            ```
        """
        return self._next


class SystemBeeperState(SCPICmdWrite, SCPICmdRead):
    """The ``SYSTem:BEEPer:STATe`` command.

    Description:
        - The ``SYSTem:BEEPer:STATe`` command sets the beeper ON or OFF. The
          ``SYSTem:BEEPer:STATe?`` command returns '0' (OFF) or '1' (ON). When the beeper is set to
          ON, the instrument will beep when an error message or a warning message is displayed on
          the screen. The instrument does not beep when an error or warning caused by remote command
          execution.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:BEEPer:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:BEEPer:STATe?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYSTem:BEEPer:STATe value`` command.

    SCPI Syntax:
        ```
        - SYSTem:BEEPer:STATe {ON|OFF|<NR1>}
        - SYSTem:BEEPer:STATe?
        ```
    """


class SystemBeeperImmediate(SCPICmdWriteNoArguments):
    """The ``SYSTem:BEEPer:IMMediate`` command.

    Description:
        - This command causes the instrument to beep immediately.

    Usage:
        - Using the ``.write()`` method will send the ``SYSTem:BEEPer:IMMediate`` command.

    SCPI Syntax:
        ```
        - SYSTem:BEEPer:IMMediate
        ```
    """


class SystemBeeper(SCPICmdRead):
    """The ``SYSTem:BEEPer`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem:BEEPer?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:BEEPer?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``SYSTem:BEEPer:STATe`` command.
        - ``.immediate``: The ``SYSTem:BEEPer:IMMediate`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._state = SystemBeeperState(device, f"{self._cmd_syntax}:STATe")
        self._immediate = SystemBeeperImmediate(device, f"{self._cmd_syntax}:IMMediate")

    @property
    def state(self) -> SystemBeeperState:
        """Return the ``SYSTem:BEEPer:STATe`` command.

        Description:
            - The ``SYSTem:BEEPer:STATe`` command sets the beeper ON or OFF. The
              ``SYSTem:BEEPer:STATe?`` command returns '0' (OFF) or '1' (ON). When the beeper is set
              to ON, the instrument will beep when an error message or a warning message is
              displayed on the screen. The instrument does not beep when an error or warning caused
              by remote command execution.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:BEEPer:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:BEEPer:STATe?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYSTem:BEEPer:STATe value``
              command.

        SCPI Syntax:
            ```
            - SYSTem:BEEPer:STATe {ON|OFF|<NR1>}
            - SYSTem:BEEPer:STATe?
            ```
        """
        return self._state

    @property
    def immediate(self) -> SystemBeeperImmediate:
        """Return the ``SYSTem:BEEPer:IMMediate`` command.

        Description:
            - This command causes the instrument to beep immediately.

        Usage:
            - Using the ``.write()`` method will send the ``SYSTem:BEEPer:IMMediate`` command.

        SCPI Syntax:
            ```
            - SYSTem:BEEPer:IMMediate
            ```
        """
        return self._immediate


#  pylint: disable=too-many-instance-attributes
class System(SCPICmdRead):
    """The ``SYSTem`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYSTem?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.beeper``: The ``SYSTem:BEEPer`` command tree.
        - ``.error``: The ``SYSTem:ERRor`` command tree.
        - ``.kclick``: The ``SYSTem:KCLick`` command tree.
        - ``.klock``: The ``SYSTem:KLOCk`` command tree.
        - ``.password``: The ``SYSTem:PASSword`` command tree.
        - ``.security``: The ``SYSTem:SECurity`` command tree.
        - ``.ulanguage``: The ``SYSTem:ULANguage`` command.
        - ``.version``: The ``SYSTem:VERSion`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "SYSTem") -> None:
        super().__init__(device, cmd_syntax)
        self._beeper = SystemBeeper(device, f"{self._cmd_syntax}:BEEPer")
        self._error = SystemError(device, f"{self._cmd_syntax}:ERRor")
        self._kclick = SystemKclick(device, f"{self._cmd_syntax}:KCLick")
        self._klock = SystemKlock(device, f"{self._cmd_syntax}:KLOCk")
        self._password = SystemPassword(device, f"{self._cmd_syntax}:PASSword")
        self._security = SystemSecurity(device, f"{self._cmd_syntax}:SECurity")
        self._ulanguage = SystemUlanguage(device, f"{self._cmd_syntax}:ULANguage")
        self._version = SystemVersion(device, f"{self._cmd_syntax}:VERSion")

    @property
    def beeper(self) -> SystemBeeper:
        """Return the ``SYSTem:BEEPer`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:BEEPer?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:BEEPer?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``SYSTem:BEEPer:STATe`` command.
            - ``.immediate``: The ``SYSTem:BEEPer:IMMediate`` command.
        """
        return self._beeper

    @property
    def error(self) -> SystemError:
        """Return the ``SYSTem:ERRor`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:ERRor?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:ERRor?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.next``: The ``SYSTem:ERRor:NEXT`` command.
        """
        return self._error

    @property
    def kclick(self) -> SystemKclick:
        """Return the ``SYSTem:KCLick`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:KCLick?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:KCLick?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``SYSTem:KCLick:STATe`` command.
        """
        return self._kclick

    @property
    def klock(self) -> SystemKlock:
        """Return the ``SYSTem:KLOCk`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:KLOCk?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:KLOCk?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.state``: The ``SYSTem:KLOCk:STATe`` command.
        """
        return self._klock

    @property
    def password(self) -> SystemPassword:
        """Return the ``SYSTem:PASSword`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:PASSword?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:PASSword?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.cdisable``: The ``SYSTem:PASSword:CDISable`` command.
            - ``.new``: The ``SYSTem:PASSword:NEW`` command.
            - ``.cenable``: The ``SYSTem:PASSword:CENable`` command.
        """
        return self._password

    @property
    def security(self) -> SystemSecurity:
        """Return the ``SYSTem:SECurity`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:SECurity?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:SECurity?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.immediate``: The ``SYSTem:SECurity:IMMediate`` command.
        """
        return self._security

    @property
    def ulanguage(self) -> SystemUlanguage:
        """Return the ``SYSTem:ULANguage`` command.

        Description:
            - This command sets or queries the language that the instrument uses to display
              information on the screen.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:ULANguage?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:ULANguage?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYSTem:ULANguage value`` command.

        SCPI Syntax:
            ```
            - SYSTem:ULANguage {ENGLish|FRENch|GERMan|JAPanese|KORean|SCHinese|TCHinese|RUSSian}
            - SYSTem:ULANguage?
            ```
        """
        return self._ulanguage

    @property
    def version(self) -> SystemVersion:
        """Return the ``SYSTem:VERSion`` command.

        Description:
            - This query-only command returns the conformed SCPI version of the instrument.

        Usage:
            - Using the ``.query()`` method will send the ``SYSTem:VERSion?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:VERSion?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SYSTem:VERSion?
            ```
        """
        return self._version
