"""The curve commands module.

These commands are used in the following models:
MSO2, TekScopePC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CURVe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Curve(SCPICmdRead):
    """The ``CURVe`` command.

    Description:
        - This command transfers waveform data from the instrument. Each waveform that is
          transferred has an associated waveform preamble that contains information such as data
          format and scale. The ``CURVe?`` query transfers data from the instrument. The data source
          is specified by the ``DATA:SOURCE`` command. The first and last data points are specified
          by the ``DATA:START`` and ``DATA:STOP`` commands. For MATH sources, only 8-byte double
          precision floating point data is returned in ``:CURVe?`` queries.

    Usage:
        - Using the ``.query()`` method will send the ``CURVe?`` query.
        - Using the ``.verify(value)`` method will send the ``CURVe?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - CURVe?
        ```
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CURVe") -> None:
        super().__init__(device, cmd_syntax)
