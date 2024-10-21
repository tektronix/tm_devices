"""The synchronize commands module.

These commands are used in the following models:
AWG5200

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - SYNChronize:ADJust:STARt
    - SYNChronize:DESKew:ABORt
    - SYNChronize:DESKew:STARt
    - SYNChronize:DESKew:STATe?
    - SYNChronize:ENABle {0|1|OFF|ON}
    - SYNChronize:ENABle?
    - SYNChronize:TYPE {MASTer|SLAVe}
    - SYNChronize:TYPE?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class SynchronizeType(SCPICmdWrite, SCPICmdRead):
    """The ``SYNChronize:TYPE`` command.

    Description:
        - This command sets or returns the instrument type (master or slave) when synchronization is
          enabled.

    Usage:
        - Using the ``.query()`` method will send the ``SYNChronize:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:TYPE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYNChronize:TYPE value`` command.

    SCPI Syntax:
        ```
        - SYNChronize:TYPE {MASTer|SLAVe}
        - SYNChronize:TYPE?
        ```
    """


class SynchronizeEnable(SCPICmdWrite, SCPICmdRead):
    """The ``SYNChronize:ENABle`` command.

    Description:
        - This command sets or returns the synchronization state (enabled or disabled). When
          enabled, the instrument can be used as part of a synchronized system of other AWG5200
          series instruments.

    Usage:
        - Using the ``.query()`` method will send the ``SYNChronize:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:ENABle?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYNChronize:ENABle value`` command.

    SCPI Syntax:
        ```
        - SYNChronize:ENABle {0|1|OFF|ON}
        - SYNChronize:ENABle?
        ```
    """


class SynchronizeDeskewState(SCPICmdRead):
    """The ``SYNChronize:DESKew:STATe`` command.

    Description:
        - This command returns the state of the system deskew condition.

    Usage:
        - Using the ``.query()`` method will send the ``SYNChronize:DESKew:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:DESKew:STATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - SYNChronize:DESKew:STATe?
        ```
    """


class SynchronizeDeskewStart(SCPICmdWriteNoArguments):
    """The ``SYNChronize:DESKew:STARt`` command.

    Description:
        - This command only performs a system deskew calibration.

    Usage:
        - Using the ``.write()`` method will send the ``SYNChronize:DESKew:STARt`` command.

    SCPI Syntax:
        ```
        - SYNChronize:DESKew:STARt
        ```
    """


class SynchronizeDeskewAbort(SCPICmdWriteNoArguments):
    """The ``SYNChronize:DESKew:ABORt`` command.

    Description:
        - This command cancels a system deskew calibration.

    Usage:
        - Using the ``.write()`` method will send the ``SYNChronize:DESKew:ABORt`` command.

    SCPI Syntax:
        ```
        - SYNChronize:DESKew:ABORt
        ```
    """


class SynchronizeDeskew(SCPICmdRead):
    """The ``SYNChronize:DESKew`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYNChronize:DESKew?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:DESKew?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.abort``: The ``SYNChronize:DESKew:ABORt`` command.
        - ``.state``: The ``SYNChronize:DESKew:STATe`` command.
        - ``.start``: The ``SYNChronize:DESKew:STARt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._abort = SynchronizeDeskewAbort(device, f"{self._cmd_syntax}:ABORt")
        self._state = SynchronizeDeskewState(device, f"{self._cmd_syntax}:STATe")
        self._start = SynchronizeDeskewStart(device, f"{self._cmd_syntax}:STARt")

    @property
    def abort(self) -> SynchronizeDeskewAbort:
        """Return the ``SYNChronize:DESKew:ABORt`` command.

        Description:
            - This command cancels a system deskew calibration.

        Usage:
            - Using the ``.write()`` method will send the ``SYNChronize:DESKew:ABORt`` command.

        SCPI Syntax:
            ```
            - SYNChronize:DESKew:ABORt
            ```
        """
        return self._abort

    @property
    def state(self) -> SynchronizeDeskewState:
        """Return the ``SYNChronize:DESKew:STATe`` command.

        Description:
            - This command returns the state of the system deskew condition.

        Usage:
            - Using the ``.query()`` method will send the ``SYNChronize:DESKew:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:DESKew:STATe?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - SYNChronize:DESKew:STATe?
            ```
        """
        return self._state

    @property
    def start(self) -> SynchronizeDeskewStart:
        """Return the ``SYNChronize:DESKew:STARt`` command.

        Description:
            - This command only performs a system deskew calibration.

        Usage:
            - Using the ``.write()`` method will send the ``SYNChronize:DESKew:STARt`` command.

        SCPI Syntax:
            ```
            - SYNChronize:DESKew:STARt
            ```
        """
        return self._start


class SynchronizeAdjustStart(SCPICmdWriteNoArguments):
    """The ``SYNChronize:ADJust:STARt`` command.

    Description:
        - This command only performs a system sample rate calibration on the synchronized system.
          This command may take up to 3 minutes to complete.

    Usage:
        - Using the ``.write()`` method will send the ``SYNChronize:ADJust:STARt`` command.

    SCPI Syntax:
        ```
        - SYNChronize:ADJust:STARt
        ```
    """


class SynchronizeAdjust(SCPICmdRead):
    """The ``SYNChronize:ADJust`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYNChronize:ADJust?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:ADJust?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.start``: The ``SYNChronize:ADJust:STARt`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._start = SynchronizeAdjustStart(device, f"{self._cmd_syntax}:STARt")

    @property
    def start(self) -> SynchronizeAdjustStart:
        """Return the ``SYNChronize:ADJust:STARt`` command.

        Description:
            - This command only performs a system sample rate calibration on the synchronized
              system. This command may take up to 3 minutes to complete.

        Usage:
            - Using the ``.write()`` method will send the ``SYNChronize:ADJust:STARt`` command.

        SCPI Syntax:
            ```
            - SYNChronize:ADJust:STARt
            ```
        """
        return self._start


class Synchronize(SCPICmdRead):
    """The ``SYNChronize`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``SYNChronize?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.adjust``: The ``SYNChronize:ADJust`` command tree.
        - ``.deskew``: The ``SYNChronize:DESKew`` command tree.
        - ``.enable``: The ``SYNChronize:ENABle`` command.
        - ``.type``: The ``SYNChronize:TYPE`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "SYNChronize"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._adjust = SynchronizeAdjust(device, f"{self._cmd_syntax}:ADJust")
        self._deskew = SynchronizeDeskew(device, f"{self._cmd_syntax}:DESKew")
        self._enable = SynchronizeEnable(device, f"{self._cmd_syntax}:ENABle")
        self._type = SynchronizeType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def adjust(self) -> SynchronizeAdjust:
        """Return the ``SYNChronize:ADJust`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYNChronize:ADJust?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:ADJust?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.start``: The ``SYNChronize:ADJust:STARt`` command.
        """
        return self._adjust

    @property
    def deskew(self) -> SynchronizeDeskew:
        """Return the ``SYNChronize:DESKew`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``SYNChronize:DESKew?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:DESKew?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.abort``: The ``SYNChronize:DESKew:ABORt`` command.
            - ``.state``: The ``SYNChronize:DESKew:STATe`` command.
            - ``.start``: The ``SYNChronize:DESKew:STARt`` command.
        """
        return self._deskew

    @property
    def enable(self) -> SynchronizeEnable:
        """Return the ``SYNChronize:ENABle`` command.

        Description:
            - This command sets or returns the synchronization state (enabled or disabled). When
              enabled, the instrument can be used as part of a synchronized system of other AWG5200
              series instruments.

        Usage:
            - Using the ``.query()`` method will send the ``SYNChronize:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:ENABle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYNChronize:ENABle value`` command.

        SCPI Syntax:
            ```
            - SYNChronize:ENABle {0|1|OFF|ON}
            - SYNChronize:ENABle?
            ```
        """
        return self._enable

    @property
    def type(self) -> SynchronizeType:
        """Return the ``SYNChronize:TYPE`` command.

        Description:
            - This command sets or returns the instrument type (master or slave) when
              synchronization is enabled.

        Usage:
            - Using the ``.query()`` method will send the ``SYNChronize:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:TYPE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYNChronize:TYPE value`` command.

        SCPI Syntax:
            ```
            - SYNChronize:TYPE {MASTer|SLAVe}
            - SYNChronize:TYPE?
            ```
        """
        return self._type
