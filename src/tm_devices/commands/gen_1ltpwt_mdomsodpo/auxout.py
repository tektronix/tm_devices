"""The auxout commands module.

These commands are used in the following models:
DPO4K, DPO4KB, MDO3, MDO3K, MDO4K, MDO4KB, MDO4KC, MSO4K, MSO4KB

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AUXOut:SOUrce {ATRIGger|MAIn|REFOut|EVENT|AFG}
    - AUXOut:SOUrce?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AuxoutSource(SCPICmdWrite, SCPICmdRead):
    """The ``AUXOut:SOUrce`` command.

    Description:
        - This command sets (or queries) the source for the Auxiliary Output port.

    Usage:
        - Using the ``.query()`` method will send the ``AUXOut:SOUrce?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXOut:SOUrce?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write(value)`` method will send the ``AUXOut:SOUrce value`` command.

    SCPI Syntax:
        ```
        - AUXOut:SOUrce {ATRIGger|MAIn|REFOut|EVENT|AFG}
        - AUXOut:SOUrce?
        ```

    Info:
        - ``ATRIGger`` is the default signal output of the auxiliary out port. MAIn is synonymous
          with ATRIGger.
        - ``REFOut`` specifies the reference oscillator output as the source for the auxiliary
          output.
        - ``EVENT`` refers to an internally generated oscilloscope event. The Mask and Act on Event
          commands can cause an event output, such as a mask test completion notification event.
        - ``AFG`` specifies the AFG sync out pulse. (Only available for models with the 3-AFG option
          installed.).
    """


class Auxout(SCPICmdRead):
    """The ``AUXOut`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AUXOut?`` query.
        - Using the ``.verify(value)`` method will send the ``AUXOut?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.source``: The ``AUXOut:SOUrce`` command.
    """

    def __init__(self, device: Optional["PIControl"] = None, cmd_syntax: str = "AUXOut") -> None:
        super().__init__(device, cmd_syntax)
        self._source = AuxoutSource(device, f"{self._cmd_syntax}:SOUrce")

    @property
    def source(self) -> AuxoutSource:
        """Return the ``AUXOut:SOUrce`` command.

        Description:
            - This command sets (or queries) the source for the Auxiliary Output port.

        Usage:
            - Using the ``.query()`` method will send the ``AUXOut:SOUrce?`` query.
            - Using the ``.verify(value)`` method will send the ``AUXOut:SOUrce?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write(value)`` method will send the ``AUXOut:SOUrce value`` command.

        SCPI Syntax:
            ```
            - AUXOut:SOUrce {ATRIGger|MAIn|REFOut|EVENT|AFG}
            - AUXOut:SOUrce?
            ```

        Info:
            - ``ATRIGger`` is the default signal output of the auxiliary out port. MAIn is
              synonymous with ATRIGger.
            - ``REFOut`` specifies the reference oscillator output as the source for the auxiliary
              output.
            - ``EVENT`` refers to an internally generated oscilloscope event. The Mask and Act on
              Event commands can cause an event output, such as a mask test completion notification
              event.
            - ``AFG`` specifies the AFG sync out pulse. (Only available for models with the 3-AFG
              option installed.).
        """
        return self._source
