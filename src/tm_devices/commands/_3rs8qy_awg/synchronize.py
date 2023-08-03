"""The synchronize commands module.

These commands are used in the following models:
AWG70KA, AWG70KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - SYNChronize:ADJust:STARt
    - SYNChronize:CONFigure <port_configuration>
    - SYNChronize:CONFigure?
    - SYNChronize:DESKew:ABORt
    - SYNChronize:DESKew:STARt
    - SYNChronize:DESKew:STATe?
    - SYNChronize:ENABle {OFF|ON|0|1}
    - SYNChronize:ENABle?
    - SYNChronize:TYPE?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead, SCPICmdWrite, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class SynchronizeType(SCPICmdRead):
    """The ``SYNChronize:TYPE`` command.

    **Description:**
        - This command returns the instrument type (master or slave) in the synchronized system.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYNChronize:TYPE?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:TYPE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - SYNChronize:TYPE?
    """


class SynchronizeEnable(SCPICmdWrite, SCPICmdRead):
    """The ``SYNChronize:ENABle`` command.

    **Description:**
        - This command enables or disables synchronization in the instrument.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYNChronize:ENABle?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:ENABle?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYNChronize:ENABle value`` command.

    **SCPI Syntax:**

    ::

        - SYNChronize:ENABle {OFF|ON|0|1}
        - SYNChronize:ENABle?
    """


class SynchronizeDeskewState(SCPICmdRead):
    """The ``SYNChronize:DESKew:STATe`` command.

    **Description:**
        - This command returns the state of the system deskew condition.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYNChronize:DESKew:STATe?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:DESKew:STATe?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - SYNChronize:DESKew:STATe?
    """


class SynchronizeDeskewStart(SCPICmdWriteNoArguments):
    """The ``SYNChronize:DESKew:STARt`` command.

    **Description:**
        - This command only performs a system deskew calibration.

    **Usage:**
        - Using the ``.write()`` method will send the ``SYNChronize:DESKew:STARt`` command.

    **SCPI Syntax:**

    ::

        - SYNChronize:DESKew:STARt
    """


class SynchronizeDeskewAbort(SCPICmdWriteNoArguments):
    """The ``SYNChronize:DESKew:ABORt`` command.

    **Description:**
        - This command cancels a system deskew calibration.

    **Usage:**
        - Using the ``.write()`` method will send the ``SYNChronize:DESKew:ABORt`` command.

    **SCPI Syntax:**

    ::

        - SYNChronize:DESKew:ABORt
    """


class SynchronizeDeskew(SCPICmdRead):
    """The ``SYNChronize:DESKew`` command tree.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYNChronize:DESKew?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:DESKew?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.abort``: The ``SYNChronize:DESKew:ABORt`` command.
        - ``.state``: The ``SYNChronize:DESKew:STATe`` command.
        - ``.start``: The ``SYNChronize:DESKew:STARt`` command.
    """

    def __init__(self, device: Optional["PIDevice"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._abort = SynchronizeDeskewAbort(device, f"{self._cmd_syntax}:ABORt")
        self._state = SynchronizeDeskewState(device, f"{self._cmd_syntax}:STATe")
        self._start = SynchronizeDeskewStart(device, f"{self._cmd_syntax}:STARt")

    @property
    def abort(self) -> SynchronizeDeskewAbort:
        """Return the ``SYNChronize:DESKew:ABORt`` command.

        **Description:**
            - This command cancels a system deskew calibration.

        **Usage:**
            - Using the ``.write()`` method will send the ``SYNChronize:DESKew:ABORt`` command.

        **SCPI Syntax:**

        ::

            - SYNChronize:DESKew:ABORt
        """
        return self._abort

    @property
    def state(self) -> SynchronizeDeskewState:
        """Return the ``SYNChronize:DESKew:STATe`` command.

        **Description:**
            - This command returns the state of the system deskew condition.

        **Usage:**
            - Using the ``.query()`` method will send the ``SYNChronize:DESKew:STATe?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:DESKew:STATe?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - SYNChronize:DESKew:STATe?
        """
        return self._state

    @property
    def start(self) -> SynchronizeDeskewStart:
        """Return the ``SYNChronize:DESKew:STARt`` command.

        **Description:**
            - This command only performs a system deskew calibration.

        **Usage:**
            - Using the ``.write()`` method will send the ``SYNChronize:DESKew:STARt`` command.

        **SCPI Syntax:**

        ::

            - SYNChronize:DESKew:STARt
        """
        return self._start


class SynchronizeConfigure(SCPICmdWrite, SCPICmdRead):
    """The ``SYNChronize:CONFigure`` command.

    **Description:**
        - This command configures the ports in a synchronized system and forces an initialization
          within the selected configuration.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYNChronize:CONFigure?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:CONFigure?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYNChronize:CONFigure value`` command.

    **SCPI Syntax:**

    ::

        - SYNChronize:CONFigure <port_configuration>
        - SYNChronize:CONFigure?
    """


class SynchronizeAdjustStart(SCPICmdWriteNoArguments):
    """The ``SYNChronize:ADJust:STARt`` command.

    **Description:**
        - This command only performs a system sample rate calibration on the synchronized system.
          This command may take up to 3 minutes to complete.

    **Usage:**
        - Using the ``.write()`` method will send the ``SYNChronize:ADJust:STARt`` command.

    **SCPI Syntax:**

    ::

        - SYNChronize:ADJust:STARt
    """


class SynchronizeAdjust(SCPICmdRead):
    """The ``SYNChronize:ADJust`` command tree.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYNChronize:ADJust?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize:ADJust?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.start``: The ``SYNChronize:ADJust:STARt`` command.
    """

    def __init__(self, device: Optional["PIDevice"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._start = SynchronizeAdjustStart(device, f"{self._cmd_syntax}:STARt")

    @property
    def start(self) -> SynchronizeAdjustStart:
        """Return the ``SYNChronize:ADJust:STARt`` command.

        **Description:**
            - This command only performs a system sample rate calibration on the synchronized
              system. This command may take up to 3 minutes to complete.

        **Usage:**
            - Using the ``.write()`` method will send the ``SYNChronize:ADJust:STARt`` command.

        **SCPI Syntax:**

        ::

            - SYNChronize:ADJust:STARt
        """
        return self._start


class Synchronize(SCPICmdRead):
    """The ``SYNChronize`` command tree.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYNChronize?`` query.
        - Using the ``.verify(value)`` method will send the ``SYNChronize?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.adjust``: The ``SYNChronize:ADJust`` command tree.
        - ``.configure``: The ``SYNChronize:CONFigure`` command.
        - ``.deskew``: The ``SYNChronize:DESKew`` command tree.
        - ``.enable``: The ``SYNChronize:ENABle`` command.
        - ``.type``: The ``SYNChronize:TYPE`` command.
    """

    def __init__(
        self, device: Optional["PIDevice"] = None, cmd_syntax: str = "SYNChronize"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._adjust = SynchronizeAdjust(device, f"{self._cmd_syntax}:ADJust")
        self._configure = SynchronizeConfigure(device, f"{self._cmd_syntax}:CONFigure")
        self._deskew = SynchronizeDeskew(device, f"{self._cmd_syntax}:DESKew")
        self._enable = SynchronizeEnable(device, f"{self._cmd_syntax}:ENABle")
        self._type = SynchronizeType(device, f"{self._cmd_syntax}:TYPE")

    @property
    def adjust(self) -> SynchronizeAdjust:
        """Return the ``SYNChronize:ADJust`` command tree.

        **Usage:**
            - Using the ``.query()`` method will send the ``SYNChronize:ADJust?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:ADJust?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.start``: The ``SYNChronize:ADJust:STARt`` command.
        """
        return self._adjust

    @property
    def configure(self) -> SynchronizeConfigure:
        """Return the ``SYNChronize:CONFigure`` command.

        **Description:**
            - This command configures the ports in a synchronized system and forces an
              initialization within the selected configuration.

        **Usage:**
            - Using the ``.query()`` method will send the ``SYNChronize:CONFigure?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:CONFigure?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYNChronize:CONFigure value``
              command.

        **SCPI Syntax:**

        ::

            - SYNChronize:CONFigure <port_configuration>
            - SYNChronize:CONFigure?
        """
        return self._configure

    @property
    def deskew(self) -> SynchronizeDeskew:
        """Return the ``SYNChronize:DESKew`` command tree.

        **Usage:**
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

        **Description:**
            - This command enables or disables synchronization in the instrument.

        **Usage:**
            - Using the ``.query()`` method will send the ``SYNChronize:ENABle?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:ENABle?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYNChronize:ENABle value`` command.

        **SCPI Syntax:**

        ::

            - SYNChronize:ENABle {OFF|ON|0|1}
            - SYNChronize:ENABle?
        """
        return self._enable

    @property
    def type(self) -> SynchronizeType:
        """Return the ``SYNChronize:TYPE`` command.

        **Description:**
            - This command returns the instrument type (master or slave) in the synchronized system.

        **Usage:**
            - Using the ``.query()`` method will send the ``SYNChronize:TYPE?`` query.
            - Using the ``.verify(value)`` method will send the ``SYNChronize:TYPE?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        **SCPI Syntax:**

        ::

            - SYNChronize:TYPE?
        """
        return self._type
