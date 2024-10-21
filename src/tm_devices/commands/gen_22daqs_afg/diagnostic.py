"""The diagnostic commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - DIAGnostic:ALL
    - DIAGnostic:ALL?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class DiagnosticAll(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``DIAGnostic:ALL`` command.

    Description:
        - The DIAGnostic[``:ALL``] command performs a self-test. The DIAGnostic[``:ALL``]? command
          returns the results after executing the test.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic:ALL?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic:ALL?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``DIAGnostic:ALL`` command.

    SCPI Syntax:
        ```
        - DIAGnostic:ALL
        - DIAGnostic:ALL?
        ```
    """


class Diagnostic(SCPICmdRead):
    """The ``DIAGnostic`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``DIAGnostic?`` query.
        - Using the ``.verify(value)`` method will send the ``DIAGnostic?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.all``: The ``DIAGnostic:ALL`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "DIAGnostic"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._all = DiagnosticAll(device, f"{self._cmd_syntax}:ALL")

    @property
    def all(self) -> DiagnosticAll:
        """Return the ``DIAGnostic:ALL`` command.

        Description:
            - The DIAGnostic[``:ALL``] command performs a self-test. The DIAGnostic[``:ALL``]?
              command returns the results after executing the test.

        Usage:
            - Using the ``.query()`` method will send the ``DIAGnostic:ALL?`` query.
            - Using the ``.verify(value)`` method will send the ``DIAGnostic:ALL?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``DIAGnostic:ALL`` command.

        SCPI Syntax:
            ```
            - DIAGnostic:ALL
            - DIAGnostic:ALL?
            ```
        """
        return self._all
