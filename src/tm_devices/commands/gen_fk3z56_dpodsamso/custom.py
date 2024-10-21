"""The custom commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CUSTOM:GATE<x>:SOUrce { CH1|CH2|CH3|CH4|MATH1|MATH2|MATH3|MATH4|REF1|REF2|REF3|REF4 }
    - CUSTOM:GATE<x>:START <NR3>
    - CUSTOM:GATE<x>:WIDth <NR3>
    - CUSTOM:SELECT:GATE<x> {1|0|ON|OFF}
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import (
    DefaultDictPassKeyToFactory,
    SCPICmdRead,
    SCPICmdWrite,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CustomSelectGateItem(ValidatedDynamicNumberCmd, SCPICmdWrite):
    """The ``CUSTOM:SELECT:GATE<x>`` command.

    Description:
        - Sets or queries wether or not the selected gate is displayed on the screen.

    Usage:
        - Using the ``.write(value)`` method will send the ``CUSTOM:SELECT:GATE<x> value`` command.

    SCPI Syntax:
        ```
        - CUSTOM:SELECT:GATE<x> {1|0|ON|OFF}
        ```

    Info:
        - ``1`` sets the specified gate to be displayed.
        - ``0`` sets the specified gate to be hidden.
        - ``ON`` sets the specified gate to be displayed.
        - ``OFF`` sets the specified gate to be hidden.
    """


class CustomSelect(SCPICmdRead):
    """The ``CUSTOM:SELECT`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CUSTOM:SELECT?`` query.
        - Using the ``.verify(value)`` method will send the ``CUSTOM:SELECT?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.gate``: The ``CUSTOM:SELECT:GATE<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._gate: Dict[int, CustomSelectGateItem] = DefaultDictPassKeyToFactory(
            lambda x: CustomSelectGateItem(device, f"{self._cmd_syntax}:GATE{x}")
        )

    @property
    def gate(self) -> Dict[int, CustomSelectGateItem]:
        """Return the ``CUSTOM:SELECT:GATE<x>`` command.

        Description:
            - Sets or queries wether or not the selected gate is displayed on the screen.

        Usage:
            - Using the ``.write(value)`` method will send the ``CUSTOM:SELECT:GATE<x> value``
              command.

        SCPI Syntax:
            ```
            - CUSTOM:SELECT:GATE<x> {1|0|ON|OFF}
            ```

        Info:
            - ``1`` sets the specified gate to be displayed.
            - ``0`` sets the specified gate to be hidden.
            - ``ON`` sets the specified gate to be displayed.
            - ``OFF`` sets the specified gate to be hidden.
        """
        return self._gate


class CustomGateItemWidth(SCPICmdWrite):
    """The ``CUSTOM:GATE<x>:WIDth`` command.

    Description:
        - Sets or queries the width of the specified gate.

    Usage:
        - Using the ``.write(value)`` method will send the ``CUSTOM:GATE<x>:WIDth value`` command.

    SCPI Syntax:
        ```
        - CUSTOM:GATE<x>:WIDth <NR3>
        ```
    """


class CustomGateItemStart(SCPICmdWrite):
    """The ``CUSTOM:GATE<x>:START`` command.

    Description:
        - Sets or queries the start position of the specified gate.

    Usage:
        - Using the ``.write(value)`` method will send the ``CUSTOM:GATE<x>:START value`` command.

    SCPI Syntax:
        ```
        - CUSTOM:GATE<x>:START <NR3>
        ```
    """


class CustomGateItemSource(SCPICmdWrite):
    """The ``CUSTOM:GATE<x>:SOUrce`` command.

    Description:
        - Sets or queries the source for the specified gate.

    Usage:
        - Using the ``.write(value)`` method will send the ``CUSTOM:GATE<x>:SOUrce value`` command.

    SCPI Syntax:
        ```
        - CUSTOM:GATE<x>:SOUrce { CH1|CH2|CH3|CH4|MATH1|MATH2|MATH3|MATH4|REF1|REF2|REF3|REF4 }
        ```
    """


class CustomGateItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``CUSTOM:GATE<x>`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CUSTOM:GATE<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``CUSTOM:GATE<x>?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``CUSTOM:GATE<x>:SOUrce`` command.
        - ``.start``: The ``CUSTOM:GATE<x>:START`` command.
        - ``.width``: The ``CUSTOM:GATE<x>:WIDth`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._source = CustomGateItemSource(device, f"{self._cmd_syntax}:SOUrce")
        self._start = CustomGateItemStart(device, f"{self._cmd_syntax}:START")
        self._width = CustomGateItemWidth(device, f"{self._cmd_syntax}:WIDth")

    @property
    def source(self) -> CustomGateItemSource:
        """Return the ``CUSTOM:GATE<x>:SOUrce`` command.

        Description:
            - Sets or queries the source for the specified gate.

        Usage:
            - Using the ``.write(value)`` method will send the ``CUSTOM:GATE<x>:SOUrce value``
              command.

        SCPI Syntax:
            ```
            - CUSTOM:GATE<x>:SOUrce { CH1|CH2|CH3|CH4|MATH1|MATH2|MATH3|MATH4|REF1|REF2|REF3|REF4 }
            ```
        """
        return self._source

    @property
    def start(self) -> CustomGateItemStart:
        """Return the ``CUSTOM:GATE<x>:START`` command.

        Description:
            - Sets or queries the start position of the specified gate.

        Usage:
            - Using the ``.write(value)`` method will send the ``CUSTOM:GATE<x>:START value``
              command.

        SCPI Syntax:
            ```
            - CUSTOM:GATE<x>:START <NR3>
            ```
        """
        return self._start

    @property
    def width(self) -> CustomGateItemWidth:
        """Return the ``CUSTOM:GATE<x>:WIDth`` command.

        Description:
            - Sets or queries the width of the specified gate.

        Usage:
            - Using the ``.write(value)`` method will send the ``CUSTOM:GATE<x>:WIDth value``
              command.

        SCPI Syntax:
            ```
            - CUSTOM:GATE<x>:WIDth <NR3>
            ```
        """
        return self._width


class Custom(SCPICmdRead):
    """The ``CUSTOM`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CUSTOM?`` query.
        - Using the ``.verify(value)`` method will send the ``CUSTOM?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.gate``: The ``CUSTOM:GATE<x>`` command tree.
        - ``.select``: The ``CUSTOM:SELECT`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "CUSTOM") -> None:
        super().__init__(device, cmd_syntax)
        self._gate: Dict[int, CustomGateItem] = DefaultDictPassKeyToFactory(
            lambda x: CustomGateItem(device, f"{self._cmd_syntax}:GATE{x}")
        )
        self._select = CustomSelect(device, f"{self._cmd_syntax}:SELECT")

    @property
    def gate(self) -> Dict[int, CustomGateItem]:
        """Return the ``CUSTOM:GATE<x>`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CUSTOM:GATE<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``CUSTOM:GATE<x>?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.source``: The ``CUSTOM:GATE<x>:SOUrce`` command.
            - ``.start``: The ``CUSTOM:GATE<x>:START`` command.
            - ``.width``: The ``CUSTOM:GATE<x>:WIDth`` command.
        """
        return self._gate

    @property
    def select(self) -> CustomSelect:
        """Return the ``CUSTOM:SELECT`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``CUSTOM:SELECT?`` query.
            - Using the ``.verify(value)`` method will send the ``CUSTOM:SELECT?`` query and raise
              an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.gate``: The ``CUSTOM:SELECT:GATE<x>`` command.
        """
        return self._select
