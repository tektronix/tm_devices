# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The slot commands module.

These commands are used in the following models:
DMM6500

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - slot[1].idn
    - slot[1].maxvoltage
    - slot[1].pseudocard
    - slot[1].voltage.endchannel
    - slot[1].voltage.startchannel
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class SlotItemVoltage(BaseTSPCmd):
    """The ``slot[1].voltage`` command tree.

    Properties and methods:
        - ``.endchannel``: The ``slot[1].voltage.endchannel`` attribute.
        - ``.startchannel``: The ``slot[1].voltage.startchannel`` attribute.
    """

    @property
    def endchannel(self) -> str:
        """Access the ``slot[1].voltage.endchannel`` attribute.

        Description:
            - This attribute indicates the last channel in the specified slot that supports voltage.

        Usage:
            - Accessing this property will send the ``print(slot[1].voltage.endchannel)`` query.

        TSP Syntax:
            ```
            - print(slot[1].voltage.endchannel)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".endchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.endchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.endchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def startchannel(self) -> str:
        """Access the ``slot[1].voltage.startchannel`` attribute.

        Description:
            - This attribute indicates the first channel in the specified slot that supports
              voltage.

        Usage:
            - Accessing this property will send the ``print(slot[1].voltage.startchannel)`` query.

        TSP Syntax:
            ```
            - print(slot[1].voltage.startchannel)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".startchannel"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.startchannel)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.startchannel`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SlotItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``slot[1]`` command tree.

    Properties and methods:
        - ``.idn``: The ``slot[1].idn`` attribute.
        - ``.maxvoltage``: The ``slot[1].maxvoltage`` attribute.
        - ``.pseudocard``: The ``slot[1].pseudocard`` attribute.
        - ``.voltage``: The ``slot[1].voltage`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "slot[1]") -> None:
        super().__init__(device, cmd_syntax)
        self._voltage = SlotItemVoltage(device, f"{self._cmd_syntax}.voltage")

    @property
    def idn(self) -> str:
        """Access the ``slot[1].idn`` attribute.

        Description:
            - This attribute returns a string that contains information about the .

        Usage:
            - Accessing this property will send the ``print(slot[1].idn)`` query.

        TSP Syntax:
            ```
            - print(slot[1].idn)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".idn"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.idn)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.idn`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def maxvoltage(self) -> str:
        """Access the ``slot[1].maxvoltage`` attribute.

        Description:
            - This attribute returns the maximum voltage of all channels on a  in the specified slot
              on a  in the specified slot.

        Usage:
            - Accessing this property will send the ``print(slot[1].maxvoltage)`` query.

        TSP Syntax:
            ```
            - print(slot[1].maxvoltage)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".maxvoltage"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.maxvoltage)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.maxvoltage`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def pseudocard(self) -> str:
        """Access the ``slot[1].pseudocard`` attribute.

        Description:
            - This attribute specifies a pseudocard to use.

        Usage:
            - Accessing this property will send the ``print(slot[1].pseudocard)`` query.
            - Setting this property to a value will send the ``slot[1].pseudocard = value`` command.

        TSP Syntax:
            ```
            - slot[1].pseudocard = value
            - print(slot[1].pseudocard)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".pseudocard"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.pseudocard)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.pseudocard`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @pseudocard.setter
    def pseudocard(self, value: Union[str, float]) -> None:
        """Access the ``slot[1].pseudocard`` attribute.

        Description:
            - This attribute specifies a pseudocard to use.

        Usage:
            - Accessing this property will send the ``print(slot[1].pseudocard)`` query.
            - Setting this property to a value will send the ``slot[1].pseudocard = value`` command.

        TSP Syntax:
            ```
            - slot[1].pseudocard = value
            - print(slot[1].pseudocard)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".pseudocard", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.pseudocard = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.pseudocard`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def voltage(self) -> SlotItemVoltage:
        """Return the ``slot[1].voltage`` command tree.

        Sub-properties and sub-methods:
            - ``.endchannel``: The ``slot[1].voltage.endchannel`` attribute.
            - ``.startchannel``: The ``slot[1].voltage.startchannel`` attribute.
        """
        return self._voltage
