"""The date commands module.

These commands are used in the following models:
LPD6, MSO2, MSO4, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - DATE?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Date(SCPICmdRead):
    """The ``DATE`` command.

    **Description:**
        - This command queries the date that the instrument displays.

    **Usage:**
        - Using the ``.query()`` method will send the ``DATE?`` query.
        - Using the ``.verify(value)`` method will send the ``DATE?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - DATE?
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "DATE") -> None:
        super().__init__(device, cmd_syntax)
