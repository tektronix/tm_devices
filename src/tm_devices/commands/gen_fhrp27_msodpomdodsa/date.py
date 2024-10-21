"""The date commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC,
DSA70KC, DSA70KD, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DATE <QString>
    - DATE?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class Date(SCPICmdWrite, SCPICmdRead):
    """The ``DATE`` command.

    Description:
        - This command specifies the date the oscilloscope displays.

    Usage:
        - Using the ``.query()`` method will send the ``DATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DATE value`` command.

    SCPI Syntax:
        ```
        - DATE <QString>
        - DATE?
        ```

    Info:
        - ``<QString>`` is a date in the form 'yyyy-mm-dd' where yyyy refers to a four-digit year
          number, mm refers to a two-digit month number from 01 to 12, and dd refers to a two-digit
          day number in the month.
    """

    _WRAP_ARG_WITH_QUOTES = True

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DATE") -> None:
        super().__init__(device, cmd_syntax)
