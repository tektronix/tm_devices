"""The status_and_error commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - *PSC {OFF|ON|NR1>}
    - *PSC?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Psc(SCPICmdWrite, SCPICmdRead):
    """The ``*PSC`` command.

    **Description:**
        - This command specifies the power-on status flag that controls the automatic power-on
          handling of the DESER, SRER, and ESER registers. When ``*PSC`` is true, the DESER register
          is set to 255 and the SRER and ESER registers are set to 0 at power-on. When ``*PSC`` is
          false, the current values in the DESER, SRER, and ESER registers are preserved in
          nonvolatile memory when power is shut off and are restored at power-on.

    **Usage:**
        - Using the ``.query()`` method will send the ``*PSC?`` query.
        - Using the ``.verify(value)`` method will send the ``*PSC?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*PSC value`` command.

    **SCPI Syntax:**

    ::

        - *PSC {OFF|ON|NR1>}
        - *PSC?

    **Info:**
        - ``OFF`` sets the power-on status clear flag to false.
        - ``ON`` sets the power-on status clear flag to true.
        - ``<NR1>`` = 0 sets the power-on status clear flag to false. This disables the power-on
          clear allowing the oscilloscope to possibly assert SRQ after power-on; any other value
          sets the power-on status clear flag to true, enabling the power-on status clear preventing
          any SRQ assertion after power on.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "*PSC") -> None:
        super().__init__(device, cmd_syntax)
