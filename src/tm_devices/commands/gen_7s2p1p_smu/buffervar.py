# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The buffervar commands module.

These commands are used in the following models:
SMU2601B_Pulse

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - bufferVar.capacity
    - bufferVar.statuses[N]
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, DefaultDictDeviceCommunication, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Buffervar(BaseTSPCmd):
    """The ``bufferVar`` command tree.

    Info:
        - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer or a
          dedicated reading buffer.

    Properties and methods:
        - ``.capacity``: The ``bufferVar.capacity`` attribute.
        - ``.statuses``: The ``bufferVar.statuses[N]`` attribute.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "bufferVar"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._statuses: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.statuses[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.statuses[{{key}}])",
            device=self._device,
        )

    @property
    def capacity(self) -> str:
        """Access the ``bufferVar.capacity`` attribute.

        Description:
            - This attribute sets the number of readings a buffer can store.

        Usage:
            - Accessing this property will send the ``print(bufferVar.capacity)`` query.

        TSP Syntax:
            ```
            - print(bufferVar.capacity)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".capacity"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.capacity)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.capacity`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def statuses(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.statuses[N]`` attribute.

        Description:
            - This attribute contains the status values of readings in the reading buffer.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.statuses[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.statuses[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._statuses
