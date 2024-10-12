"""The autoset commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUTOSet {EXECute|UNDo}
    - AUTOSet:ENAble {OFF|ON|0|1}
    - AUTOSet:ENAble?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AutosetEnable(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSet:ENAble`` command.

    Description:
        - Enables or disables the autoset feature. This is useful for classroom purposes where the
          instructor wants the students to achieve the desired instrument settings without the
          benefit of the autoset feature. This setting is not saved in setup files or SET? or
          ``*LRN?`` queries. The default state is 1 (autoset enabled).

    Usage:
        - Using the ``.query()`` method will send the ``AUTOSet:ENAble?`` query.
        - Using the ``.verify(value)`` method will send the ``AUTOSet:ENAble?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUTOSet:ENAble value`` command.

    SCPI Syntax:
        ```
        - AUTOSet:ENAble {OFF|ON|0|1}
        - AUTOSet:ENAble?
        ```

    Info:
        - ``OFF or 0`` disables autoset.
        - ``ON or 1`` enables autoset.
    """


class Autoset(SCPICmdWrite, SCPICmdRead):
    """The ``AUTOSet`` command.

    Description:
        - Sets the vertical, horizontal, and trigger controls of the oscilloscope to automatically
          acquire and display the selected waveform.

    Usage:
        - Using the ``.write(value)`` method will send the ``AUTOSet value`` command.

    SCPI Syntax:
        ```
        - AUTOSet {EXECute|UNDo}
        ```

    Info:
        - ``EXECute`` autosets the displayed waveform.
        - ``UNDo`` restores the oscilloscope settings to those present prior to the autoset
          execution.

    Properties:
        - ``.enable``: The ``AUTOSet:ENAble`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUTOSet") -> None:
        super().__init__(device, cmd_syntax)
        self._enable = AutosetEnable(device, f"{self._cmd_syntax}:ENAble")

    @property
    def enable(self) -> AutosetEnable:
        """Return the ``AUTOSet:ENAble`` command.

        Description:
            - Enables or disables the autoset feature. This is useful for classroom purposes where
              the instructor wants the students to achieve the desired instrument settings without
              the benefit of the autoset feature. This setting is not saved in setup files or SET?
              or ``*LRN?`` queries. The default state is 1 (autoset enabled).

        Usage:
            - Using the ``.query()`` method will send the ``AUTOSet:ENAble?`` query.
            - Using the ``.verify(value)`` method will send the ``AUTOSet:ENAble?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUTOSet:ENAble value`` command.

        SCPI Syntax:
            ```
            - AUTOSet:ENAble {OFF|ON|0|1}
            - AUTOSet:ENAble?
            ```

        Info:
            - ``OFF or 0`` disables autoset.
            - ``ON or 1`` enables autoset.
        """
        return self._enable
