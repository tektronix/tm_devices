"""The header commands module.

These commands are used in the following models:
DPO2K, DPO2KB, DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO2K, MSO2KB, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - HEADer {OFF|ON|<NR1>}
    - HEADer?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class Header(SCPICmdWrite, SCPICmdRead):
    """The ``HEADer`` command.

    **Description:**
        - This command specifies the Response Header Enable State that causes the oscilloscope to
          either include or omit headers on query responses.

    **Usage:**
        - Using the ``.query()`` method will send the ``HEADer?`` query.
        - Using the ``.verify(value)`` method will send the ``HEADer?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``HEADer value`` command.

    **SCPI Syntax:**

    ::

        - HEADer {OFF|ON|<NR1>}
        - HEADer?

    **Info:**
        - ``OFF`` sets the Response Header Enable State to false. This causes the oscilloscope to
          omit headers on query responses, so that only the argument is returned.
        - ``ON`` sets the Response Header Enable State to true. This causes the oscilloscope to
          include headers on applicable query responses. You can then use the query response as a
          command.
        - ``<NR1>`` = 0 sets the Response Header Enable State to false; any other value sets this
          state to true.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "HEADer") -> None:
        super().__init__(device, cmd_syntax)
