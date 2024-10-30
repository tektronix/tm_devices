"""The wfmpre commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - WFMPre:NR_FR?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class WfmpreNrFr(SCPICmdRead):
    """The ``WFMPre:NR_FR`` command.

    Description:
        - This query-only command returns the number of frames for the waveform transmitted in
          response to a CURVE? query.

    Usage:
        - Using the ``.query()`` method will send the ``WFMPre:NR_FR?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMPre:NR_FR?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - WFMPre:NR_FR?
        ```
    """


class Wfmpre(SCPICmdRead):
    """The ``WFMPre`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``WFMPre?`` query.
        - Using the ``.verify(value)`` method will send the ``WFMPre?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.nr_fr``: The ``WFMPre:NR_FR`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "WFMPre") -> None:
        super().__init__(device, cmd_syntax)
        self._nr_fr = WfmpreNrFr(device, f"{self._cmd_syntax}:NR_FR")

    @property
    def nr_fr(self) -> WfmpreNrFr:
        """Return the ``WFMPre:NR_FR`` command.

        Description:
            - This query-only command returns the number of frames for the waveform transmitted in
              response to a CURVE? query.

        Usage:
            - Using the ``.query()`` method will send the ``WFMPre:NR_FR?`` query.
            - Using the ``.verify(value)`` method will send the ``WFMPre:NR_FR?`` query and raise an
              AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - WFMPre:NR_FR?
            ```
        """
        return self._nr_fr
