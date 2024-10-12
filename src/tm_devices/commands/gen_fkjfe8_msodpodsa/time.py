"""The time commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD,
MSO2K, MSO2KB, MSO5K, MSO5KB, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TIME <QString>
    - TIME?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Time(SCPICmdWrite, SCPICmdRead):
    """The ``TIME`` command.

    Description:
        - This command sets or queries the time that the instrument displays. This command is
          equivalent to selecting Set Time & Date from the Utilities menu and then setting the
          fields in the Time group box.

    Usage:
        - Using the ``.query()`` method will send the ``TIME?`` query.
        - Using the ``.verify(value)`` method will send the ``TIME?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TIME value`` command.

    SCPI Syntax:
        ```
        - TIME <QString>
        - TIME?
        ```

    Info:
        - ``<QString>`` is a time in the form '``hh:mm:ss``' where hh refers to a two-digit hour
          number, mm refers to a two-digit minute number from 01 to 60, and ss refers to a two-digit
          second number from 01 to 60.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "TIME") -> None:
        super().__init__(device, cmd_syntax)
