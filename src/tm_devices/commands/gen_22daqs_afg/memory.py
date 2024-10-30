"""The memory commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - *RCL {0|1|2|3|4}
    - *SAV {0|1|2|3|4}
    - MEMory:STATe:DELete {0|1|2|3|4}
    - MEMory:STATe:LOCK {1|2|3|4},{ON|OFF|<NR1>}
    - MEMory:STATe:LOCK? {1|2|3|4}
    - MEMory:STATe:RECall:AUTo {ON|OFF|<NR1>}
    - MEMory:STATe:RECall:AUTo?
    - MEMory:STATe:VALid? {0|1|2|3|4}
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdReadWithArguments, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class MemoryStateValid(SCPICmdReadWithArguments):
    """The ``MEMory:STATe:VALid`` command.

    Description:
        - This command returns the availability of a setup memory.

    Usage:
        - Using the ``.query(argument)`` method will send the ``MEMory:STATe:VALid? argument``
          query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEMory:STATe:VALid? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.

    SCPI Syntax:
        ```
        - MEMory:STATe:VALid? {0|1|2|3|4}
        ```
    """


class MemoryStateRecallAuto(SCPICmdWrite, SCPICmdRead):
    """The ``MEMory:STATe:RECall:AUTo`` command.

    Description:
        - This command sets or queries whether to enable the automatic recall of last setup memory
          when powered-on. The next time you apply the power, the arbitrary function generator will
          automatically recall the settings you used when you powered off the instrument. If you
          select OFF, the default setups are recalled when you power on the instrument.

    Usage:
        - Using the ``.query()`` method will send the ``MEMory:STATe:RECall:AUTo?`` query.
        - Using the ``.verify(value)`` method will send the ``MEMory:STATe:RECall:AUTo?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEMory:STATe:RECall:AUTo value``
          command.

    SCPI Syntax:
        ```
        - MEMory:STATe:RECall:AUTo {ON|OFF|<NR1>}
        - MEMory:STATe:RECall:AUTo?
        ```
    """


class MemoryStateRecall(SCPICmdRead):
    """The ``MEMory:STATe:RECall`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEMory:STATe:RECall?`` query.
        - Using the ``.verify(value)`` method will send the ``MEMory:STATe:RECall?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.auto``: The ``MEMory:STATe:RECall:AUTo`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._auto = MemoryStateRecallAuto(device, f"{self._cmd_syntax}:AUTo")

    @property
    def auto(self) -> MemoryStateRecallAuto:
        """Return the ``MEMory:STATe:RECall:AUTo`` command.

        Description:
            - This command sets or queries whether to enable the automatic recall of last setup
              memory when powered-on. The next time you apply the power, the arbitrary function
              generator will automatically recall the settings you used when you powered off the
              instrument. If you select OFF, the default setups are recalled when you power on the
              instrument.

        Usage:
            - Using the ``.query()`` method will send the ``MEMory:STATe:RECall:AUTo?`` query.
            - Using the ``.verify(value)`` method will send the ``MEMory:STATe:RECall:AUTo?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEMory:STATe:RECall:AUTo value``
              command.

        SCPI Syntax:
            ```
            - MEMory:STATe:RECall:AUTo {ON|OFF|<NR1>}
            - MEMory:STATe:RECall:AUTo?
            ```
        """
        return self._auto


class MemoryStateLock(SCPICmdWrite, SCPICmdReadWithArguments):
    """The ``MEMory:STATe:LOCK`` command.

    Description:
        - This command sets or queries whether to lock the specified setup memory. If you lock a
          setup memory, you cannot overwrite or delete the setup file. You cannot execute this
          command for the setup memory of location number 0 (last setup memory).

    Usage:
        - Using the ``.query(argument)`` method will send the ``MEMory:STATe:LOCK? argument`` query.
        - Using the ``.verify(argument, value)`` method will send the
          ``MEMory:STATe:LOCK? argument`` query and raise an AssertionError if the returned value
          does not match ``value``.
        - Using the ``.write(value)`` method will send the ``MEMory:STATe:LOCK value`` command.

    SCPI Syntax:
        ```
        - MEMory:STATe:LOCK {1|2|3|4},{ON|OFF|<NR1>}
        - MEMory:STATe:LOCK? {1|2|3|4}
        ```
    """


class MemoryStateDelete(SCPICmdWrite):
    """The ``MEMory:STATe:DELete`` command.

    Description:
        - This command deletes the contents of specified setup memory. If a specified setup memory
          is not allowed to overwrite or delete, this command causes an error.

    Usage:
        - Using the ``.write(value)`` method will send the ``MEMory:STATe:DELete value`` command.

    SCPI Syntax:
        ```
        - MEMory:STATe:DELete {0|1|2|3|4}
        ```
    """


class MemoryState(SCPICmdRead):
    """The ``MEMory:STATe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEMory:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``MEMory:STATe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.delete``: The ``MEMory:STATe:DELete`` command.
        - ``.lock``: The ``MEMory:STATe:LOCK`` command.
        - ``.recall``: The ``MEMory:STATe:RECall`` command tree.
        - ``.valid``: The ``MEMory:STATe:VALid`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._delete = MemoryStateDelete(device, f"{self._cmd_syntax}:DELete")
        self._lock = MemoryStateLock(device, f"{self._cmd_syntax}:LOCK")
        self._recall = MemoryStateRecall(device, f"{self._cmd_syntax}:RECall")
        self._valid = MemoryStateValid(device, f"{self._cmd_syntax}:VALid")

    @property
    def delete(self) -> MemoryStateDelete:
        """Return the ``MEMory:STATe:DELete`` command.

        Description:
            - This command deletes the contents of specified setup memory. If a specified setup
              memory is not allowed to overwrite or delete, this command causes an error.

        Usage:
            - Using the ``.write(value)`` method will send the ``MEMory:STATe:DELete value``
              command.

        SCPI Syntax:
            ```
            - MEMory:STATe:DELete {0|1|2|3|4}
            ```
        """
        return self._delete

    @property
    def lock(self) -> MemoryStateLock:
        """Return the ``MEMory:STATe:LOCK`` command.

        Description:
            - This command sets or queries whether to lock the specified setup memory. If you lock a
              setup memory, you cannot overwrite or delete the setup file. You cannot execute this
              command for the setup memory of location number 0 (last setup memory).

        Usage:
            - Using the ``.query(argument)`` method will send the ``MEMory:STATe:LOCK? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEMory:STATe:LOCK? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``MEMory:STATe:LOCK value`` command.

        SCPI Syntax:
            ```
            - MEMory:STATe:LOCK {1|2|3|4},{ON|OFF|<NR1>}
            - MEMory:STATe:LOCK? {1|2|3|4}
            ```
        """
        return self._lock

    @property
    def recall(self) -> MemoryStateRecall:
        """Return the ``MEMory:STATe:RECall`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEMory:STATe:RECall?`` query.
            - Using the ``.verify(value)`` method will send the ``MEMory:STATe:RECall?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.auto``: The ``MEMory:STATe:RECall:AUTo`` command.
        """
        return self._recall

    @property
    def valid(self) -> MemoryStateValid:
        """Return the ``MEMory:STATe:VALid`` command.

        Description:
            - This command returns the availability of a setup memory.

        Usage:
            - Using the ``.query(argument)`` method will send the ``MEMory:STATe:VALid? argument``
              query.
            - Using the ``.verify(argument, value)`` method will send the
              ``MEMory:STATe:VALid? argument`` query and raise an AssertionError if the returned
              value does not match ``value``.

        SCPI Syntax:
            ```
            - MEMory:STATe:VALid? {0|1|2|3|4}
            ```
        """
        return self._valid


class Memory(SCPICmdRead):
    """The ``MEMory`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``MEMory?`` query.
        - Using the ``.verify(value)`` method will send the ``MEMory?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.state``: The ``MEMory:STATe`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "MEMory") -> None:
        super().__init__(device, cmd_syntax)
        self._state = MemoryState(device, f"{self._cmd_syntax}:STATe")

    @property
    def state(self) -> MemoryState:
        """Return the ``MEMory:STATe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``MEMory:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``MEMory:STATe?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.delete``: The ``MEMory:STATe:DELete`` command.
            - ``.lock``: The ``MEMory:STATe:LOCK`` command.
            - ``.recall``: The ``MEMory:STATe:RECall`` command tree.
            - ``.valid``: The ``MEMory:STATe:VALid`` command.
        """
        return self._state


class Sav(SCPICmdWrite):
    """The ``*SAV`` command.

    Description:
        - This command stores the current settings of the arbitrary function generator to a
          specified setup memory location. A setup memory location numbered 0 ( last setup memory)
          is automatically overwritten by the setups when you power off the instrument. If a
          specified numbered setup memory is locked, this command causes an error.

    Usage:
        - Using the ``.write(value)`` method will send the ``*SAV value`` command.

    SCPI Syntax:
        ```
        - *SAV {0|1|2|3|4}
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*SAV") -> None:
        super().__init__(device, cmd_syntax)


class Rcl(SCPICmdWrite):
    """The ``*RCL`` command.

    Description:
        - This command restores the state of the instrument from a copy of the settings stored in
          the setup memory. The settings are stored using the ``*SAV`` command. If the specified
          setup memory is deleted, this command causes an error.

    Usage:
        - Using the ``.write(value)`` method will send the ``*RCL value`` command.

    SCPI Syntax:
        ```
        - *RCL {0|1|2|3|4}
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "*RCL") -> None:
        super().__init__(device, cmd_syntax)
