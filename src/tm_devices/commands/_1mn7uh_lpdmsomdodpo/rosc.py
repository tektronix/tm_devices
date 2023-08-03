"""The rosc commands module.

These commands are used in the following models:
DPO4K, DPO4KB, LPD6, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2, MSO4, MSO4K, MSO4KB, MSO5, MSO5B,
MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - ROSc:SOUrce {INTERnal|EXTernal}
    - ROSc:SOUrce?
    - ROSc:STATE?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class RoscState(SCPICmdRead):
    """The ``ROSc:STATE`` command.

    **Description:**
        - This query-only command returns whether the time base reference oscillator is locked. This
          command will return either LOCKED or UNLOCKED.

    **Usage:**
        - Using the ``.query()`` method will send the ``ROSc:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``ROSc:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - ROSc:STATE?
    """


class RoscSource(SCPICmdWrite, SCPICmdRead):
    """The ``ROSc:SOUrce`` command.

    **Description:**
        - This command sets or queries the selected source for the time base reference oscillator.
          The reference oscillator locks to this source. Depending on the command argument that you
          specify, you can use an external reference or use the internal crystal oscillator as the
          time base reference.

    **Usage:**
        - Using the ``.query()`` method will send the ``ROSc:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``ROSc:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``ROSc:SOUrce value`` command.

    **SCPI Syntax:**

    ::

        - ROSc:SOUrce {INTERnal|EXTernal}
        - ROSc:SOUrce?

    **Info:**
        - ``INTERnal`` specifies the internal 10 MHz crystal oscillator as the time base reference.
        - ``EXTernal`` specifies the user-supplied external signal as the time base reference.
    """


class Rosc(SCPICmdRead):
    """The ``ROSc`` command tree.

    **Usage:**
        - Using the ``.query()`` method will send the ``ROSc?`` query.
        - Using the ``.verify(value)`` method will send the ``ROSc?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``ROSc:SOUrce`` command.
        - ``.state``: The ``ROSc:STATE`` command.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "ROSc") -> None:
        super().__init__(device, cmd_syntax)
        self._source = RoscSource(device, f"{self._cmd_syntax}:SOUrce")
        self._state = RoscState(device, f"{self._cmd_syntax}:STATE")

    @property
    def source(self) -> RoscSource:
        """Return the ``ROSc:SOUrce`` command.

        **Description:**
            - This command sets or queries the selected source for the time base reference
              oscillator. The reference oscillator locks to this source. Depending on the command
              argument that you specify, you can use an external reference or use the internal
              crystal oscillator as the time base reference.

        **Usage:**
            - Using the ``.query()`` method will send the ``ROSc:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``ROSc:SOUrce?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``ROSc:SOUrce value`` command.

        **SCPI Syntax:**

        ::

            - ROSc:SOUrce {INTERnal|EXTernal}
            - ROSc:SOUrce?

        **Info:**
            - ``INTERnal`` specifies the internal 10 MHz crystal oscillator as the time base
              reference.
            - ``EXTernal`` specifies the user-supplied external signal as the time base reference.
        """
        return self._source

    @property
    def state(self) -> RoscState:
        """Return the ``ROSc:STATE`` command.

        **Description:**
            - This query-only command returns whether the time base reference oscillator is locked.
              This command will return either LOCKED or UNLOCKED.

        **Usage:**
            - Using the ``.query()`` method will send the ``ROSc:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``ROSc:STATE?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - ROSc:STATE?
        """
        return self._state
