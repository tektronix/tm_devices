"""The fastacq commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - FASTAcq:HIACQRATE {ON|OFF|<NR1>}
    - FASTAcq:HIACQRATE?
    - FASTAcq:STATE {ON|OFF|<NR1>}
    - FASTAcq:STATE?
    - FASTAcq?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class FastacqState(SCPICmdWrite, SCPICmdRead):
    """The ``FASTAcq:STATE`` command.

    Description:
        - This command sets or queries the state of Fast Acquisitions. This command is equivalent to
          the FASTACQ button on the front panel.

    Usage:
        - Using the ``.query()`` method will send the ``FASTAcq:STATE?`` query.
        - Using the ``.verify(value)`` method will send the ``FASTAcq:STATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FASTAcq:STATE value`` command.

    SCPI Syntax:
        ```
        - FASTAcq:STATE {ON|OFF|<NR1>}
        - FASTAcq:STATE?
        ```

    Info:
        - ``<NR1>`` = 0 disables Fast Acquisitions mode; any other value enables Fast Acquisitions
          mode.
        - ``ON`` enables Fast Acquisitions mode.
        - ``OFF`` disables Fast Acquisitions mode.
    """


class FastacqHiacqrate(SCPICmdWrite, SCPICmdRead):
    """The ``FASTAcq:HIACQRATE`` command.

    Description:
        - This command sets or queries the state of FastAcq optimization for capturing signal
          details with a higher sample rate.

    Usage:
        - Using the ``.query()`` method will send the ``FASTAcq:HIACQRATE?`` query.
        - Using the ``.verify(value)`` method will send the ``FASTAcq:HIACQRATE?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``FASTAcq:HIACQRATE value`` command.

    SCPI Syntax:
        ```
        - FASTAcq:HIACQRATE {ON|OFF|<NR1>}
        - FASTAcq:HIACQRATE?
        ```

    Info:
        - ``<NR1>`` = 0 sets FastAcq optimization for capturing signal details with a higher sample
          rate; any other value sets FastAcq optimization for capturing rare events with more
          acquisitions.
        - ``OFF`` sets FastAcq optimization for capturing signal details with a higher sample rate.
        - ``ON`` sets FastAcq optimization for capturing rare events with more acquisitions.
    """


class Fastacq(SCPICmdRead):
    """The ``FASTAcq`` command.

    Description:
        - This query-only command returns the state of Fast Acquisitions. This command is equivalent
          to pressing the FASTACQ button on the front panel.

    Usage:
        - Using the ``.query()`` method will send the ``FASTAcq?`` query.
        - Using the ``.verify(value)`` method will send the ``FASTAcq?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - FASTAcq?
        ```

    Properties:
        - ``.hiacqrate``: The ``FASTAcq:HIACQRATE`` command.
        - ``.state``: The ``FASTAcq:STATE`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "FASTAcq") -> None:
        super().__init__(device, cmd_syntax)
        self._hiacqrate = FastacqHiacqrate(device, f"{self._cmd_syntax}:HIACQRATE")
        self._state = FastacqState(device, f"{self._cmd_syntax}:STATE")

    @property
    def hiacqrate(self) -> FastacqHiacqrate:
        """Return the ``FASTAcq:HIACQRATE`` command.

        Description:
            - This command sets or queries the state of FastAcq optimization for capturing signal
              details with a higher sample rate.

        Usage:
            - Using the ``.query()`` method will send the ``FASTAcq:HIACQRATE?`` query.
            - Using the ``.verify(value)`` method will send the ``FASTAcq:HIACQRATE?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FASTAcq:HIACQRATE value`` command.

        SCPI Syntax:
            ```
            - FASTAcq:HIACQRATE {ON|OFF|<NR1>}
            - FASTAcq:HIACQRATE?
            ```

        Info:
            - ``<NR1>`` = 0 sets FastAcq optimization for capturing signal details with a higher
              sample rate; any other value sets FastAcq optimization for capturing rare events with
              more acquisitions.
            - ``OFF`` sets FastAcq optimization for capturing signal details with a higher sample
              rate.
            - ``ON`` sets FastAcq optimization for capturing rare events with more acquisitions.
        """
        return self._hiacqrate

    @property
    def state(self) -> FastacqState:
        """Return the ``FASTAcq:STATE`` command.

        Description:
            - This command sets or queries the state of Fast Acquisitions. This command is
              equivalent to the FASTACQ button on the front panel.

        Usage:
            - Using the ``.query()`` method will send the ``FASTAcq:STATE?`` query.
            - Using the ``.verify(value)`` method will send the ``FASTAcq:STATE?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``FASTAcq:STATE value`` command.

        SCPI Syntax:
            ```
            - FASTAcq:STATE {ON|OFF|<NR1>}
            - FASTAcq:STATE?
            ```

        Info:
            - ``<NR1>`` = 0 disables Fast Acquisitions mode; any other value enables Fast
              Acquisitions mode.
            - ``ON`` enables Fast Acquisitions mode.
            - ``OFF`` disables Fast Acquisitions mode.
        """
        return self._state
