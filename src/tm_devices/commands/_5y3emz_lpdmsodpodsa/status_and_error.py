"""The status_and_error commands module.

These commands are used in the following models:
DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7KC, DSA70KC, DSA70KD, LPD6, MSO2, MSO4, MSO5,
MSO5B, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - *PSC {<NR1>|OFF|ON}
    - *PSC?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Psc(SCPICmdWrite, SCPICmdRead):
    """The ``*PSC`` command.

    **Description:**
        - This command sets and queries the power-on status flag that controls the automatic
          power-on handling of the DESER, SRER, and ESER registers. When ``*PSC`` is true, the DESER
          register is set to 255 and the SRER and ESER registers are set to 0 at power-on. When
          ``*PSC`` is false, the current values in the DESER, SRER, and ESER registers are preserved
          in nonvolatile memory when power is shut off and are restored at power-on.

    **Usage:**
        - Using the ``.query()`` method will send the ``*PSC?`` query.
        - Using the ``.verify(value)`` method will send the ``*PSC?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``*PSC value`` command.

    **SCPI Syntax:**

    ::

        - *PSC {<NR1>|OFF|ON}
        - *PSC?

    **Info:**
        - ``<NR1>`` = 0 sets the power-on status clear flag to false, disables the power-on clear
          and allows the instrument to possibly assert SRQ after power-on; any other value sets the
          power-on status clear flag to true, enabling the power-on status clear and prevents any
          SRQ assertion after power on.
        - ``OFF`` sets the power-on status clear flag to false, disables the power-on clear and
          allows the instrument to possibly assert SRQ after power-on.
        - ``ON`` sets the power-on status clear flag to true, enabling the power-on status clear and
          prevents any SRQ assertion after power on.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "*PSC") -> None:
        super().__init__(device, cmd_syntax)
