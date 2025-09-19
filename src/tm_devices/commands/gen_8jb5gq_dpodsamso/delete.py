"""The delete commands module.

These commands are used in the following models:
DPO5K, DPO5KB, DPO70KC, DPO70KD, DPO70KDX, DPO70KSX, DPO7K, DPO7KC, DSA70KC, DSA70KD, MSO5K, MSO5KB,
MSO70KC, MSO70KDX

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DELEte:SETUp {ALL|<NR1>}
    - DELEte:WAVEform {ALL|REF<x>}
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DeleteWaveform(SCPICmdWrite):
    """The ``DELEte:WAVEform`` command.

    Description:
        - This command (no query form) deletes one or all stored reference waveforms from memory.
          This command is equivalent to selecting Delete from the File menu, and then choosing the
          reference waveform you want to delete; choosing All Refs deletes all of the reference
          waveforms.

    Usage:
        - Using the ``.write(value)`` method will send the ``DELEte:WAVEform value`` command.

    SCPI Syntax:
        ```
        - DELEte:WAVEform {ALL|REF<x>}
        ```

    Info:
        - ``ALL`` specifies to delete all the stored reference waveforms.
        - ``REF<x>`` specifies to delete one of the reference memory locations. Reference memory
          location values range from 1 through 4.
    """


class DeleteSetup(SCPICmdWrite):
    """The ``DELEte:SETUp`` command.

    Description:
        - This command (no query form) changes the setup to reference the factory setup instead of
          the specific user setup slot. The content of the setup slot is unchanged, but the data
          will no longer be accessible to you. This command is equivalent to selecting Delete from
          the File menu, and then clicking the specific setup you want to delete (user setups are
          shown as Setup-User and are ordered in the list from 1 through 10, if defined) or All
          Setups.

    Usage:
        - Using the ``.write(value)`` method will send the ``DELEte:SETUp value`` command.

    SCPI Syntax:
        ```
        - DELEte:SETUp {ALL|<NR1>}
        ```

    Info:
        - ``ALL`` deletes all the stored setups.
        - ``<NR1>`` specifies a setup storage location to delete. Setup storage location values
          range from 1 through 10; using an out-of-range value causes an error.
    """


class Delete(SCPICmdRead):
    """The ``DELEte`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DELEte?`` query.
        - Using the ``.verify(value)`` method will send the ``DELEte?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.setup``: The ``DELEte:SETUp`` command.
        - ``.waveform``: The ``DELEte:WAVEform`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "DELEte") -> None:
        super().__init__(device, cmd_syntax)
        self._setup = DeleteSetup(device, f"{self._cmd_syntax}:SETUp")
        self._waveform = DeleteWaveform(device, f"{self._cmd_syntax}:WAVEform")

    @property
    def setup(self) -> DeleteSetup:
        """Return the ``DELEte:SETUp`` command.

        Description:
            - This command (no query form) changes the setup to reference the factory setup instead
              of the specific user setup slot. The content of the setup slot is unchanged, but the
              data will no longer be accessible to you. This command is equivalent to selecting
              Delete from the File menu, and then clicking the specific setup you want to delete
              (user setups are shown as Setup-User and are ordered in the list from 1 through 10, if
              defined) or All Setups.

        Usage:
            - Using the ``.write(value)`` method will send the ``DELEte:SETUp value`` command.

        SCPI Syntax:
            ```
            - DELEte:SETUp {ALL|<NR1>}
            ```

        Info:
            - ``ALL`` deletes all the stored setups.
            - ``<NR1>`` specifies a setup storage location to delete. Setup storage location values
              range from 1 through 10; using an out-of-range value causes an error.
        """
        return self._setup

    @property
    def waveform(self) -> DeleteWaveform:
        """Return the ``DELEte:WAVEform`` command.

        Description:
            - This command (no query form) deletes one or all stored reference waveforms from
              memory. This command is equivalent to selecting Delete from the File menu, and then
              choosing the reference waveform you want to delete; choosing All Refs deletes all of
              the reference waveforms.

        Usage:
            - Using the ``.write(value)`` method will send the ``DELEte:WAVEform value`` command.

        SCPI Syntax:
            ```
            - DELEte:WAVEform {ALL|REF<x>}
            ```

        Info:
            - ``ALL`` specifies to delete all the stored reference waveforms.
            - ``REF<x>`` specifies to delete one of the reference memory locations. Reference memory
              location values range from 1 through 4.
        """
        return self._waveform
