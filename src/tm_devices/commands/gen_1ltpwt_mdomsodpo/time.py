"""The time commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - TIMe <QString>
    - TIMe?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Time(SCPICmdWrite, SCPICmdRead):
    """The ``TIMe`` command.

    Description:
        - This command sets the time in the form ``hh:mm:ss`` where hh refers to a two-digit hour
          number, mm refers to a two-digit minute number from 01 to 60, and ss refers to a two-digit
          second number from 01 to 60.

    Usage:
        - Using the ``.query()`` method will send the ``TIMe?`` query.
        - Using the ``.verify(value)`` method will send the ``TIMe?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``TIMe value`` command.

    SCPI Syntax:
        ```
        - TIMe <QString>
        - TIMe?
        ```

    Info:
        - ``<QString>`` is a quoted string representing the desired time.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "TIMe") -> None:
        super().__init__(device, cmd_syntax)
