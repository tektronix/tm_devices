"""The allocate commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - ALLOcate:WAVEform:REF<x>?
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING

from ..helpers import DefaultDictPassKeyToFactory, SCPICmdRead, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AllocateWaveformRefItem(ValidatedDynamicNumberCmd, SCPICmdRead):
    """The ``ALLOcate:WAVEform:REF<x>`` command.

    Description:
        - This query-only command returns the record length for the specified reference waveform, if
          active, or zero (0) if not active (that is, no slot exists for the reference waveform).

    Usage:
        - Using the ``.query()`` method will send the ``ALLOcate:WAVEform:REF<x>?`` query.
        - Using the ``.verify(value)`` method will send the ``ALLOcate:WAVEform:REF<x>?`` query and
          raise an AssertionError if the returned value does not match ``value``.

    SCPI Syntax:
        ```
        - ALLOcate:WAVEform:REF<x>?
        ```
    """


class AllocateWaveform(SCPICmdRead):
    """The ``ALLOcate:WAVEform`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ALLOcate:WAVEform?`` query.
        - Using the ``.verify(value)`` method will send the ``ALLOcate:WAVEform?`` query and raise
          an AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.ref``: The ``ALLOcate:WAVEform:REF<x>`` command.
    """

    def __init__(self, device: Optional["PIControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._ref: Dict[int, AllocateWaveformRefItem] = DefaultDictPassKeyToFactory(
            lambda x: AllocateWaveformRefItem(device, f"{self._cmd_syntax}:REF{x}")
        )

    @property
    def ref(self) -> Dict[int, AllocateWaveformRefItem]:
        """Return the ``ALLOcate:WAVEform:REF<x>`` command.

        Description:
            - This query-only command returns the record length for the specified reference
              waveform, if active, or zero (0) if not active (that is, no slot exists for the
              reference waveform).

        Usage:
            - Using the ``.query()`` method will send the ``ALLOcate:WAVEform:REF<x>?`` query.
            - Using the ``.verify(value)`` method will send the ``ALLOcate:WAVEform:REF<x>?`` query
              and raise an AssertionError if the returned value does not match ``value``.

        SCPI Syntax:
            ```
            - ALLOcate:WAVEform:REF<x>?
            ```
        """
        return self._ref


class Allocate(SCPICmdRead):
    """The ``ALLOcate`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``ALLOcate?`` query.
        - Using the ``.verify(value)`` method will send the ``ALLOcate?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.waveform``: The ``ALLOcate:WAVEform`` command tree.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "ALLOcate") -> None:
        super().__init__(device, cmd_syntax)
        self._waveform = AllocateWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def waveform(self) -> AllocateWaveform:
        """Return the ``ALLOcate:WAVEform`` command tree.

        Usage:
            - Using the ``.query()`` method will send the ``ALLOcate:WAVEform?`` query.
            - Using the ``.verify(value)`` method will send the ``ALLOcate:WAVEform?`` query and
              raise an AssertionError if the returned value does not match ``value``.

        Sub-properties:
            - ``.ref``: The ``ALLOcate:WAVEform:REF<x>`` command.
        """
        return self._waveform
