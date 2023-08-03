"""The synchronize commands module.

These commands are used in the following models:
AWG5200

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - SYNChronize:ENABle {0|1|OFF|ON}
    - SYNChronize:ENABle?
    - SYNChronize:TYPE {MASTer|SLAVe}
    - SYNChronize:TYPE?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class SynchronizeType(SCPICmdWrite, SCPICmdRead):
    """The ``SYNChronize:TYPE`` command.

    **Description:**
        - This command sets or returns the instrument type (master or slave) when synchronization is
          enabled.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYNChronize:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:TYPE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYNChronize:TYPE value`` command.

    **SCPI Syntax:**

    ::

        - SYNChronize:TYPE {MASTer|SLAVe}
        - SYNChronize:TYPE?
    """


class SynchronizeEnable(SCPICmdWrite, SCPICmdRead):
    """The ``SYNChronize:ENABle`` command.

    **Description:**
        - This command sets or returns the synchronization state (enabled or disabled). When
          enabled, the instrument can be used as part of a synchronized system of other AWG5200
          series instruments.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYNChronize:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:ENABle?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYNChronize:ENABle value`` command.

    **SCPI Syntax:**

    ::

        - SYNChronize:ENABle {0|1|OFF|ON}
        - SYNChronize:ENABle?
    """


class Synchronize(SCPICmdRead):
    """The ``SYNChronize`` command tree.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYNChronize?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.enable``: The ``SYNChronize:ENABle`` command.
        - ``.type``: The ``SYNChronize:TYPE`` command.
    """

    def __init__(
        self, device: Optional["PIDevice"] = None, cmd_syntax: str = "SYNChronize"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._enable = SynchronizeEnable(device, f"{self._cmd_syntax}:ENABle")
        self._type = SynchronizeType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def enable(self) -> SynchronizeEnable:
        """Return the ``SYNChronize:ENABle`` command.

        **Description:**
            - This command sets or returns the synchronization state (enabled or disabled). When
              enabled, the instrument can be used as part of a synchronized system of other AWG5200
              series instruments.

        **Usage:**
            - Using the ``.query()`` method will send the ``SYNChronize:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:ENABle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYNChronize:ENABle value`` command.

        **SCPI Syntax:**

        ::

            - SYNChronize:ENABle {0|1|OFF|ON}
            - SYNChronize:ENABle?
        """
        return self._enable

    @property
    def type(self) -> SynchronizeType:
        """Return the ``SYNChronize:TYPE`` command.

        **Description:**
            - This command sets or returns the instrument type (master or slave) when
              synchronization is enabled.

        **Usage:**
            - Using the ``.query()`` method will send the ``SYNChronize:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:TYPE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYNChronize:TYPE value`` command.

        **SCPI Syntax:**

        ::

            - SYNChronize:TYPE {MASTer|SLAVe}
            - SYNChronize:TYPE?
        """
        return self._type
