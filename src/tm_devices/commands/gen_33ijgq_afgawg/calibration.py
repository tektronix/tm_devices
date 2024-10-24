"""The calibration commands module.

These commands are used in the following models:
AFG3K, AFG3KB, AFG3KC, AWG5K, AWG5KC, AWG7K, AWG7KC

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Commands and Queries:
    ```
    - CALibration:ALL
    - CALibration:ALL?
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import SCPICmdRead, SCPICmdWriteNoArguments

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.pi_control import PIControl


class CalibrationAll(SCPICmdWriteNoArguments, SCPICmdRead):
    """The ``CALibration:ALL`` command.

    Description:
        - The CALibration[``:ALL``] command performs an internal calibration. The
          CALibration[``:ALL``]? command performs an internal calibration and returns 0 (Pass) or a
          calibration error code.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration:ALL?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration:ALL?`` query and raise an
          AssertionError if the returned value does not match ``value``.
        - Using the ``.write()`` method will send the ``CALibration:ALL`` command.

    SCPI Syntax:
        ```
        - CALibration:ALL
        - CALibration:ALL?
        ```
    """


class Calibration(SCPICmdRead):
    """The ``CALibration`` command tree.

    Usage:
        - Using the ``.query()`` method will send the ``CALibration?`` query.
        - Using the ``.verify(value)`` method will send the ``CALibration?`` query and raise an
          AssertionError if the returned value does not match ``value``.

    Properties:
        - ``.all``: The ``CALibration:ALL`` command.
    """

    def __init__(
        self, device: Optional["PIControl"] = None, cmd_syntax: str = "CALibration"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._all = CalibrationAll(device, f"{self._cmd_syntax}:ALL")

    @property
    def all(self) -> CalibrationAll:
        """Return the ``CALibration:ALL`` command.

        Description:
            - The CALibration[``:ALL``] command performs an internal calibration. The
              CALibration[``:ALL``]? command performs an internal calibration and returns 0 (Pass)
              or a calibration error code.

        Usage:
            - Using the ``.query()`` method will send the ``CALibration:ALL?`` query.
            - Using the ``.verify(value)`` method will send the ``CALibration:ALL?`` query and raise
              an AssertionError if the returned value does not match ``value``.
            - Using the ``.write()`` method will send the ``CALibration:ALL`` command.

        SCPI Syntax:
            ```
            - CALibration:ALL
            - CALibration:ALL?
            ```
        """
        return self._all
