"""The calibrate commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CALibrate:CALProbe:CH<x>?
    - CALibrate:INTERNal
    - CALibrate:INTERNal:STARt
    - CALibrate:INTERNal:STATus?
    - CALibrate:PRObestate:CH<x>?
    - CALibrate:RESults:SPC?
    - CALibrate:RESults?
    - CALibrate?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWriteNoArguments,
    ValidatedChannel,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CalibrateResultsSpc(SCPICmdRead):
    """The ``CALibrate:RESults:SPC`` command.

    Description:
        - Returns the status of the SPC operation. This query does not initiate a SPC.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:RESults:SPC?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:SPC?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:RESults:SPC?
        ```
    """


class CalibrateResults(SCPICmdRead):
    """The ``CALibrate:RESults`` command.

    Description:
        - Returns the status of internal and factory calibrations, without performing any
          calibration operations. The results returned do not include the calibration status of
          attached probes. The query is intended to support GO/NoGO testing of the oscilloscope
          calibration readiness: all returned results should indicate PASS status if the
          oscilloscope is 'fit for duty'. It is quite common, however, to use uncalibrated probes
          (particularly when the oscilloscope inputs are connected into a test system with coaxial
          cables).

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:RESults?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:RESults?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:RESults?
        ```

    Properties:
        - ``.spc``: The ``CALibrate:RESults:SPC`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._spc = CalibrateResultsSpc(device, f"{self._cmd_syntax}:SPC")

    @property
    def spc(self) -> CalibrateResultsSpc:
        """Return the ``CALibrate:RESults:SPC`` command.

        Description:
            - Returns the status of the SPC operation. This query does not initiate a SPC.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:RESults:SPC?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:RESults:SPC?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:RESults:SPC?
            ```
        """
        return self._spc


class CalibrateProbestateChannel(ValidatedChannel, SCPICmdRead):
    """The ``CALibrate:PRObestate:CH<x>`` command.

    Description:
        - This query-only command returns the probe calibration status for the probe of the selected
          channel, 1 through 4.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:PRObestate:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:PRObestate:CH<x>?`` query
          and raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:PRObestate:CH<x>?
        ```
    """


class CalibrateProbestate(SCPICmdRead):
    """The ``CALibrate:PRObestate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:PRObestate?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:PRObestate?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``CALibrate:PRObestate:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, CalibrateProbestateChannel] = DefaultDictPassKeyToFactory(
            lambda x: CalibrateProbestateChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, CalibrateProbestateChannel]:
        """Return the ``CALibrate:PRObestate:CH<x>`` command.

        Description:
            - This query-only command returns the probe calibration status for the probe of the
              selected channel, 1 through 4.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:PRObestate:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:PRObestate:CH<x>?``
              query and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:PRObestate:CH<x>?
            ```
        """
        return self._ch


class CalibrateInternalStatus(SCPICmdRead):
    """The ``CALibrate:INTERNal:STATus`` command.

    Description:
        - This query-only command returns the current status of the signal path calibration.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:INTERNal:STATus?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:INTERNal:STATus?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:INTERNal:STATus?
        ```
    """


class CalibrateInternalStart(SCPICmdWriteNoArguments):
    """The ``CALibrate:INTERNal:STARt`` command.

    Description:
        - This command (no query form) starts the signal path calibration (SPC) of the analog
          channels. This command is the same as the ``CALIBRATE:INTERNAL`` command. You can use the
          ``CALIBRATE:INTERNAL:STATUS`` query to return the current status of the signal path
          calibration of the instrument.

    Usage:
        - Using the ``.write()`` method will send the ``CALibrate:INTERNal:STARt`` command.

    SCPI Syntax:
        ```
        - CALibrate:INTERNal:STARt
        ```
    """


class CalibrateInternal(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``CALibrate:INTERNal`` command.

    Description:
        - This command (no query form) starts the signal path calibration (SPC) of the instrument.
          You can use the ``CALIBRATE:INTERNAL:STATUS`` query to return the current status of the
          signal path calibration of the instrument.

    Usage:
        - Using the ``.write()`` method will send the ``CALibrate:INTERNal`` command.

    SCPI Syntax:
        ```
        - CALibrate:INTERNal
        ```

    Properties:
        - ``.start``: The ``CALibrate:INTERNal:STARt`` command.
        - ``.status``: The ``CALibrate:INTERNal:STATus`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._start = CalibrateInternalStart(device, f"{self._cmd_syntax}:STARt")
        self._status = CalibrateInternalStatus(device, f"{self._cmd_syntax}:STATus")

    @property
    def start(self) -> CalibrateInternalStart:
        """Return the ``CALibrate:INTERNal:STARt`` command.

        Description:
            - This command (no query form) starts the signal path calibration (SPC) of the analog
              channels. This command is the same as the ``CALIBRATE:INTERNAL`` command. You can use
              the ``CALIBRATE:INTERNAL:STATUS`` query to return the current status of the signal
              path calibration of the instrument.

        Usage:
            - Using the ``.write()`` method will send the ``CALibrate:INTERNal:STARt`` command.

        SCPI Syntax:
            ```
            - CALibrate:INTERNal:STARt
            ```
        """
        return self._start

    @property
    def status(self) -> CalibrateInternalStatus:
        """Return the ``CALibrate:INTERNal:STATus`` command.

        Description:
            - This query-only command returns the current status of the signal path calibration.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:INTERNal:STATus?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:INTERNal:STATus?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:INTERNal:STATus?
            ```
        """
        return self._status


class CalibrateCalprobeChannel(ValidatedChannel, SCPICmdRead):
    """The ``CALibrate:CALProbe:CH<x>`` command.

    Description:
        - This query-only command instructs the instrument to perform a probe calibration for the
          selected channel and returns the calibration status. The Channel <x> range is 1 through 4.
          This command is equivalent to selecting Probe Cal from the Vertical menu. You must warm up
          the instrument for at least 20 minutes before running this command.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:CALProbe:CH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:CALProbe:CH<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate:CALProbe:CH<x>?
        ```
    """


class CalibrateCalprobe(SCPICmdRead):
    """The ``CALibrate:CALProbe`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate:CALProbe?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate:CALProbe?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ch``: The ``CALibrate:CALProbe:CH<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ch: Dict[int, CalibrateCalprobeChannel] = DefaultDictPassKeyToFactory(
            lambda x: CalibrateCalprobeChannel(device, f"{self._cmd_syntax}:CH{x}")
        )

    @property
    def ch(self) -> Dict[int, CalibrateCalprobeChannel]:
        """Return the ``CALibrate:CALProbe:CH<x>`` command.

        Description:
            - This query-only command instructs the instrument to perform a probe calibration for
              the selected channel and returns the calibration status. The Channel <x> range is 1
              through 4. This command is equivalent to selecting Probe Cal from the Vertical menu.
              You must warm up the instrument for at least 20 minutes before running this command.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:CALProbe:CH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:CALProbe:CH<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:CALProbe:CH<x>?
            ```
        """
        return self._ch


class Calibrate(SCPICmdRead):
    """The ``CALibrate`` command.

    Description:
        - This query returns the status of signal path calibration.

    Usage:
        - Using the ``.query()`` method will send the ``CALibrate?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibrate?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CALibrate?
        ```

    Properties:
        - ``.calprobe``: The ``CALibrate:CALProbe`` command tree.
        - ``.internal``: The ``CALibrate:INTERNal`` command.
        - ``.probestate``: The ``CALibrate:PRObestate`` command tree.
        - ``.results``: The ``CALibrate:RESults`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CALibrate") -> None:
        super().__init__(device, cmd_syntax)
        self._calprobe = CalibrateCalprobe(device, f"{self._cmd_syntax}:CALProbe")
        self._internal = CalibrateInternal(device, f"{self._cmd_syntax}:INTERNal")
        self._probestate = CalibrateProbestate(device, f"{self._cmd_syntax}:PRObestate")
        self._results = CalibrateResults(device, f"{self._cmd_syntax}:RESults")

    @property
    def calprobe(self) -> CalibrateCalprobe:
        """Return the ``CALibrate:CALProbe`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:CALProbe?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:CALProbe?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``CALibrate:CALProbe:CH<x>`` command.
        """
        return self._calprobe

    @property
    def internal(self) -> CalibrateInternal:
        """Return the ``CALibrate:INTERNal`` command.

        Description:
            - This command (no query form) starts the signal path calibration (SPC) of the
              instrument. You can use the ``CALIBRATE:INTERNAL:STATUS`` query to return the current
              status of the signal path calibration of the instrument.

        Usage:
            - Using the ``.write()`` method will send the ``CALibrate:INTERNal`` command.

        SCPI Syntax:
            ```
            - CALibrate:INTERNal
            ```

        Sub-properties:
            - ``.start``: The ``CALibrate:INTERNal:STARt`` command.
            - ``.status``: The ``CALibrate:INTERNal:STATus`` command.
        """
        return self._internal

    @property
    def probestate(self) -> CalibrateProbestate:
        """Return the ``CALibrate:PRObestate`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:PRObestate?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:PRObestate?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ch``: The ``CALibrate:PRObestate:CH<x>`` command.
        """
        return self._probestate

    @property
    def results(self) -> CalibrateResults:
        """Return the ``CALibrate:RESults`` command.

        Description:
            - Returns the status of internal and factory calibrations, without performing any
              calibration operations. The results returned do not include the calibration status of
              attached probes. The query is intended to support GO/NoGO testing of the oscilloscope
              calibration readiness: all returned results should indicate PASS status if the
              oscilloscope is 'fit for duty'. It is quite common, however, to use uncalibrated
              probes (particularly when the oscilloscope inputs are connected into a test system
              with coaxial cables).

        Usage:
            - Using the ``.query()`` method will send the ``CALibrate:RESults?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibrate:RESults?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - CALibrate:RESults?
            ```

        Sub-properties:
            - ``.spc``: The ``CALibrate:RESults:SPC`` command.
        """
        return self._results
