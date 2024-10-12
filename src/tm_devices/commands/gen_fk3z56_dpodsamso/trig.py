"""The trig commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TRIG:A:PLOCK:STANDARD {<STANDARD>}
    - TRIG:A:PLOCK:STANDARD?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class TrigAPlockStandard(SCPICmdWrite, SCPICmdRead):
    """The ``TRIG:A:PLOCK:STANDARD`` command.

    Description:
        - This command sets or queries the communication standard used by the pattern lock trigger.

    Usage:
        - Using the ``.query()`` method will send the ``TRIG:A:PLOCK:STANDARD?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIG:A:PLOCK:STANDARD?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TRIG:A:PLOCK:STANDARD value`` command.

    SCPI Syntax:
        ```
        - TRIG:A:PLOCK:STANDARD {<STANDARD>}
        - TRIG:A:PLOCK:STANDARD?
        ```

    Info:
        - ``STANDARD`` communication standard used by the pattern lock trigger. See
          ``TRIGGER:A:COMMUNICATION:STANDARD`` for a list of standards.
    """


class TrigAPlock(SCPICmdRead):
    """The ``TRIG:A:PLOCK`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIG:A:PLOCK?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIG:A:PLOCK?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.standard``: The ``TRIG:A:PLOCK:STANDARD`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._standard = TrigAPlockStandard(device, f"{self._cmd_syntax}:STANDARD")

    @property
    def standard(self) -> TrigAPlockStandard:
        """Return the ``TRIG:A:PLOCK:STANDARD`` command.

        Description:
            - This command sets or queries the communication standard used by the pattern lock
              trigger.

        Usage:
            - Using the ``.query()`` method will send the ``TRIG:A:PLOCK:STANDARD?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIG:A:PLOCK:STANDARD?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``TRIG:A:PLOCK:STANDARD value``
              command.

        SCPI Syntax:
            ```
            - TRIG:A:PLOCK:STANDARD {<STANDARD>}
            - TRIG:A:PLOCK:STANDARD?
            ```

        Info:
            - ``STANDARD`` communication standard used by the pattern lock trigger. See
              ``TRIGGER:A:COMMUNICATION:STANDARD`` for a list of standards.
        """
        return self._standard


class TrigA(SCPICmdRead):
    """The ``TRIG:A`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIG:A?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIG:A?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.plock``: The ``TRIG:A:PLOCK`` command tree.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._plock = TrigAPlock(device, f"{self._cmd_syntax}:PLOCK")

    @property
    def plock(self) -> TrigAPlock:
        """Return the ``TRIG:A:PLOCK`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIG:A:PLOCK?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIG:A:PLOCK?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.standard``: The ``TRIG:A:PLOCK:STANDARD`` command.
        """
        return self._plock


class Trig(SCPICmdRead):
    """The ``TRIG`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``TRIG?`` query.
        - Using the ``.verify(value)`` method will send the ``TRIG?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.a``: The ``TRIG:A`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "TRIG") -> None:
        super().__init__(device, cmd_syntax)
        self._a = TrigA(device, f"{self._cmd_syntax}:A")

    @property
    def a(self) -> TrigA:
        """Return the ``TRIG:A`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``TRIG:A?`` query.
            - Using the ``.verify(value)`` method will send the ``TRIG:A?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.plock``: The ``TRIG:A:PLOCK`` command tree.
        """
        return self._a
