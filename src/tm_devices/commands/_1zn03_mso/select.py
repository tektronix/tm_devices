"""The select commands module.

These commands are used in the following models:
MSO2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:

::

    - SELect:DCH<x>:DAll {ON|OFF|<NR1>}
    - SELect:DCH<x>:DAll?
"""
from typing import Dict, Optional, TYPE_CHECKING

from .._helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.drivers.pi.pi_device import PIDevice


class SelectDchItemDall(SCPICmdWrite, SCPICmdRead):
    """The ``SELect:DCH<x>:DAll`` command.

    **Description:**
        - This command turns on or off all constituent digital channels.

    **Usage:**
        - Using the ``.query()`` method will send the ``SELect:DCH<x>:DAll?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:DCH<x>:DAll?`` query and raise
          an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``SELect:DCH<x>:DAll value`` command.

    **SCPI Syntax:**

    ::

        - SELect:DCH<x>:DAll {ON|OFF|<NR1>}
        - SELect:DCH<x>:DAll?

    **Info:**
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.
        - ``<NR1>`` = 0 disables the specified digital channel; any other value turns the on the
          digital channel.
        - ``OFF`` turns off the specified digital channel.
        - ``ON`` turns on the specified digital channel.
    """


class SelectDchItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``SELect:DCH<x>`` command tree.

    **Usage:**
        - Using the ``.query()`` method will send the ``SELect:DCH<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect:DCH<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    **Info:**
        - ``DCH<x>`` specifies the digital channel. The supported value is 1.

    Properties:
        - ``.dall``: The ``SELect:DCH<x>:DAll`` command.
    """

    def __init__(self, device: Optional["PIDevice"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._dall = SelectDchItemDall(device, f"{self._cmd_syntax}:DAll")

    @property
    def dall(self) -> SelectDchItemDall:
        """Return the ``SELect:DCH<x>:DAll`` command.

        **Description:**
            - This command turns on or off all constituent digital channels.

        **Usage:**
            - Using the ``.query()`` method will send the ``SELect:DCH<x>:DAll?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:DCH<x>:DAll?`` query and
              raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``SELect:DCH<x>:DAll value`` command.

        **SCPI Syntax:**

        ::

            - SELect:DCH<x>:DAll {ON|OFF|<NR1>}
            - SELect:DCH<x>:DAll?

        **Info:**
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.
            - ``<NR1>`` = 0 disables the specified digital channel; any other value turns the on the
              digital channel.
            - ``OFF`` turns off the specified digital channel.
            - ``ON`` turns on the specified digital channel.
        """
        return self._dall


class Select(SCPICmdRead):
    """The ``SELect`` command tree.

    **Usage:**
        - Using the ``.query()`` method will send the ``SELect?`` query.
        - Using the ``.verify(value)`` method will send the ``SELect?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.dch``: The ``SELect:DCH<x>`` command tree.
    """

    def __init__(self, device: Optional["PIDevice"] = None, cmd_syntax: str = "SELect") -> None:
        super().__init__(device, cmd_syntax)
        self._dch: Dict[int, SelectDchItem] = DefaultDictPassKeyToFactory(
            lambda x: SelectDchItem(device, f"{self._cmd_syntax}:DCH{x}")
        )

    @property
    def dch(self) -> Dict[int, SelectDchItem]:
        """Return the ``SELect:DCH<x>`` command tree.

        **Usage:**
            - Using the ``.query()`` method will send the ``SELect:DCH<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``SELect:DCH<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        **Info:**
            - ``DCH<x>`` specifies the digital channel. The supported value is 1.

        Sub-properties:
            - ``.dall``: The ``SELect:DCH<x>:DAll`` command.
        """
        return self._dch
