"""The diggrp commands module.

These commands are used in the following models:
LPD6, MSO4, MSO4B, MSO5, MSO5B, MSO5LP, MSO6, MSO6B

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DIGGRP<x>:D<x>:THReshold <NR3>
    - DIGGRP<x>:D<x>:THReshold?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDigitalBit,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DiggrpItemDigitalBitThreshold(SCPICmdWrite, SCPICmdRead):
    """The ``DIGGRP<x>:D<x>:THReshold`` command.

    Description:
        - Sets or queries the threshold level in volts for the specified digital channel. If the
          source channel doesn't exist, a hardware missing error event is set.

    Usage:
        - Using the ``.query()`` method will send the ``DIGGRP<x>:D<x>:THReshold?`` query.
        - Using the ``.verify(value)`` method will send the ``DIGGRP<x>:D<x>:THReshold?`` query and
          raise an AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``DIGGRP<x>:D<x>:THReshold value``
          command.

    SCPI Syntax:
        ```
        - DIGGRP<x>:D<x>:THReshold <NR3>
        - DIGGRP<x>:D<x>:THReshold?
        ```

    Info:
        - ``DIGGRP<x>`` is the channel number.
        - ``D<x>`` is the digital channel bit number (0-7).
        - ``<NR3>`` is the threshold level in volts for the specified digital channel.
    """


class DiggrpItemDigitalBit(ValidatedDigitalBit, SCPICmdRead):
    """The ``DIGGRP<x>:D<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIGGRP<x>:D<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DIGGRP<x>:D<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``DIGGRP<x>`` is the channel number.
        - ``D<x>`` is the digital channel bit number (0-7).

    Properties:
        - ``.threshold``: The ``DIGGRP<x>:D<x>:THReshold`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._threshold = DiggrpItemDigitalBitThreshold(device, f"{self._cmd_syntax}:THReshold")

    @property
    def threshold(self) -> DiggrpItemDigitalBitThreshold:
        """Return the ``DIGGRP<x>:D<x>:THReshold`` command.

        Description:
            - Sets or queries the threshold level in volts for the specified digital channel. If the
              source channel doesn't exist, a hardware missing error event is set.

        Usage:
            - Using the ``.query()`` method will send the ``DIGGRP<x>:D<x>:THReshold?`` query.
            - Using the ``.verify(value)`` method will send the ``DIGGRP<x>:D<x>:THReshold?`` query
              and raise an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``DIGGRP<x>:D<x>:THReshold value``
              command.

        SCPI Syntax:
            ```
            - DIGGRP<x>:D<x>:THReshold <NR3>
            - DIGGRP<x>:D<x>:THReshold?
            ```

        Info:
            - ``DIGGRP<x>`` is the channel number.
            - ``D<x>`` is the digital channel bit number (0-7).
            - ``<NR3>`` is the threshold level in volts for the specified digital channel.
        """
        return self._threshold


class DiggrpItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``DIGGRP<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIGGRP<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``DIGGRP<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Info:
        - ``DIGGRP<x>`` is the channel number.

    Properties:
        - ``.d``: The ``DIGGRP<x>:D<x>`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DIGGRP<x>") -> None:
        super().__init__(device, cmd_syntax)
        self._d: Dict[int, DiggrpItemDigitalBit] = DefaultDictPassKeyToFactory(
            lambda x: DiggrpItemDigitalBit(device, f"{self._cmd_syntax}:D{x}")
        )

    @property
    def d(self) -> Dict[int, DiggrpItemDigitalBit]:
        """Return the ``DIGGRP<x>:D<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``DIGGRP<x>:D<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``DIGGRP<x>:D<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Info:
            - ``DIGGRP<x>`` is the channel number.
            - ``D<x>`` is the digital channel bit number (0-7).

        Sub-properties:
            - ``.threshold``: The ``DIGGRP<x>:D<x>:THReshold`` command.
        """
        return self._d
