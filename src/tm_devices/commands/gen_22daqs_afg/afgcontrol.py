"""The afgcontrol commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - AFGControl:CSCopy {CH1|CH2},{CH1|CH2}
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWrite

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class AfgcontrolCscopy(SCPICmdWrite):
    """The ``AFGControl:CSCopy`` command.

    Description:
        - This command copies setup parameters for one channel to another channel. If your arbitrary
          function generator is a single-channel model, this command is not supported.

    Usage:
        - Using the ``.write(value)`` method will send the ``AFGControl:CSCopy value`` command.

    SCPI Syntax:
        ```
        - AFGControl:CSCopy {CH1|CH2},{CH1|CH2}
        ```
    """


class Afgcontrol(SCPICmdRead):
    """The ``AFGControl`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``AFGControl?`` query.
        - Using the ``.verify(value)`` method will send the ``AFGControl?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.cscopy``: The ``AFGControl:CSCopy`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "AFGControl"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._cscopy = AfgcontrolCscopy(device, f"{self._cmd_syntax}:CSCopy")

    @property
    def cscopy(self) -> AfgcontrolCscopy:
        """Return the ``AFGControl:CSCopy`` command.

        Description:
            - This command copies setup parameters for one channel to another channel. If your
              arbitrary function generator is a single-channel model, this command is not supported.

        Usage:
            - Using the ``.write(value)`` method will send the ``AFGControl:CSCopy value`` command.

        SCPI Syntax:
            ```
            - AFGControl:CSCopy {CH1|CH2},{CH1|CH2}
            ```
        """
        return self._cscopy
