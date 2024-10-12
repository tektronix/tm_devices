# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The gpib commands module.

These commands are used in the following models:
DAQ6510, DMM6500, DMM7510, SMU2450, SMU2460, SMU2461, SMU2470, SMU2601B, SMU2601B_Pulse, SMU2602B,
SMU2604B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B, SMU2651A, SMU2657A, SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - gpib.address
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Gpib(BaseTSPCmd):
    """The ``gpib`` command tree.

    Properties and methods:
        - ``.address``: The ``gpib.address`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "gpib") -> None:
        super().__init__(device, cmd_syntax)

    @property
    def address(self) -> str:
        """Access the ``gpib.address`` attribute.

        Description:
            - This attribute contains the GPIB address.

        Usage:
            - Accessing this property will send the ``print(gpib.address)`` query.
            - Setting this property to a value will send the ``gpib.address = value`` command.

        TSP Syntax:
            ```
            - gpib.address = value
            - print(gpib.address)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".address"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.address)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.address`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @address.setter
    def address(self, value: Union[str, float]) -> None:
        """Access the ``gpib.address`` attribute.

        Description:
            - This attribute contains the GPIB address.

        Usage:
            - Accessing this property will send the ``print(gpib.address)`` query.
            - Setting this property to a value will send the ``gpib.address = value`` command.

        TSP Syntax:
            ```
            - gpib.address = value
            - print(gpib.address)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".address", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.address = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.address`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
