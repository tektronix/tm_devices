"""The status_and_error commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC, AWG5200, AWG5K, AWG5KC, AWG70KA, AWG70KB, AWG7K, AWG7KC, DPO4K, DPO4KB,
DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7KC, DSA70KC, DSA70KD, LPD6, MDO3, MDO3K, MDO4K,
MDO4KB, MDO4KC, MSO2, MSO4, MSO4K, MSO4KB, MSO5, MSO5B, MSO5KB, MSO5LP, MSO6, MSO6B, MSO70KC,
MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - *OPT?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Opt(SCPICmdRead):
    """The ``*OPT`` command.

    **Description:**
        - This query-only command returns a comma separated list of installed options as an
          arbitrary ASCII string (no quotes) of the form:
          ``<optionCode>:<optionDescription>``,``<optionCode>:<optionDescription>``... The last
          section of each entry (the text following the last hyphen) indicates the license type. If
          no options are found, NONE is returned.

    **Usage:**
        - Using the ``.query()`` method will send the ``*OPT?`` query.
        - Using the ``.verify(value)`` method will send the ``*OPT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    **SCPI Syntax:**

    ::

        - *OPT?
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "*OPT") -> None:
        super().__init__(device, cmd_syntax)
