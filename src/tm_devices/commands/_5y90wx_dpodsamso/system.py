"""The system commands module.

These commands are used in the following models:
DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7KC, DSA70KC, DSA70KD, MSO5KB, MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - SYSTem:SETup <Data Block>
    - SYSTem:SETup?
"""
from typing import Optional, TYPE_CHECKING

from .._helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class SystemSetup(SCPICmdWrite, SCPICmdRead):
    """The ``SYSTem:SETup`` command.

    **Description:**
        - This command configures the oscilloscope's data block as defined by the IEEE 488.2
          standard. The data block contains a compressed zip file. The query form of this command
          queries the block data containing the oscilloscope's current setup.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYSTem:SETup?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem:SETup?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SYSTem:SETup value`` command.

    **SCPI Syntax:**

    ::

        - SYSTem:SETup <Data Block>
        - SYSTem:SETup?
    """


class System(SCPICmdRead):
    """The ``SYSTem`` command tree.

    **Usage:**
        - Using the ``.query()`` method will send the ``SYSTem?`` query.
        - Using the ``.verify(value)`` method will send the ``SYSTem?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.setup``: The ``SYSTem:SETup`` command.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "SYSTem") -> None:
        super().__init__(device, cmd_syntax)
        self._setup = SystemSetup(device, f"{self._cmd_syntax}:SETup")

    @property
    def setup(self) -> SystemSetup:
        """Return the ``SYSTem:SETup`` command.

        **Description:**
            - This command configures the oscilloscope's data block as defined by the IEEE 488.2
              standard. The data block contains a compressed zip file. The query form of this
              command queries the block data containing the oscilloscope's current setup.

        **Usage:**
            - Using the ``.query()`` method will send the ``SYSTem:SETup?`` query.
            - Using the ``.verify(value)`` method will send the ``SYSTem:SETup?`` query and raise an
              AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SYSTem:SETup value`` command.

        **SCPI Syntax:**

        ::

            - SYSTem:SETup <Data Block>
            - SYSTem:SETup?
        """
        return self._setup
