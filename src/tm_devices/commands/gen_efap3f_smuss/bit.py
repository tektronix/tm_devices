# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The bit commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2604B, SMU2606B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B,
SMU2651A, SMU2657A, SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - bit.bitand()
    - bit.bitor()
    - bit.bitxor()
    - bit.clear()
    - bit.get()
    - bit.getfield()
    - bit.set()
    - bit.setfield()
    - bit.test()
    - bit.toggle()
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Bit(BaseTSPCmd):
    """The ``bit`` command tree.

    Properties and methods:
        - ``.bitand()``: The ``bit.bitand()`` function.
        - ``.bitor()``: The ``bit.bitor()`` function.
        - ``.bitxor()``: The ``bit.bitxor()`` function.
        - ``.clear()``: The ``bit.clear()`` function.
        - ``.get()``: The ``bit.get()`` function.
        - ``.getfield()``: The ``bit.getfield()`` function.
        - ``.set()``: The ``bit.set()`` function.
        - ``.setfield()``: The ``bit.setfield()`` function.
        - ``.test()``: The ``bit.test()`` function.
        - ``.toggle()``: The ``bit.toggle()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "bit") -> None:
        super().__init__(device, cmd_syntax)

    def bitand(self, value1: str, value2: str) -> str:
        """Run the ``bit.bitand()`` function.

        Description:
            - This function performs a bitwise logical AND operation on two numbers.

        TSP Syntax:
            ```
            - bit.bitand()
            ```

        Args:
            value1: Operand for the logical AND operation.
            value2: Operand for the logical AND operation.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.bitand({value1}, {value2}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.bitand()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def bitor(self, value1: str, value2: str) -> str:
        """Run the ``bit.bitor()`` function.

        Description:
            - This function performs a bitwise logical OR operation on two numbers.

        TSP Syntax:
            ```
            - bit.bitor()
            ```

        Args:
            value1: Operand for the logical OR operation.
            value2: Operand for the logical OR operation.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.bitor({value1}, {value2}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.bitor()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def bitxor(self, value1: str, value2: str) -> str:
        """Run the ``bit.bitxor()`` function.

        Description:
            - This function performs a bitwise logical XOR (exclusive OR) operation on two numbers.

        TSP Syntax:
            ```
            - bit.bitxor()
            ```

        Args:
            value1: Operand for the logical XOR operation.
            value2: Operand for the logical XOR operation.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.bitxor({value1}, {value2}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.bitxor()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def clear(self, value: str, index: int) -> str:
        """Run the ``bit.clear()`` function.

        Description:
            - This function clears a bit at a specified index position.

        TSP Syntax:
            ```
            - bit.clear()
            ```

        Args:
            value: Specified number.
            index: One-based bit position within value to clear (1 to 32).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.clear({value}, {index}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.clear()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def get(self, value: str, index: int) -> str:
        """Run the ``bit.get()`` function.

        Description:
            - This function retrieves the weighted value of a bit at a specified index position.

        TSP Syntax:
            ```
            - bit.get()
            ```

        Args:
            value: Specified number.
            index: One-based bit position within value to get (1 to 32).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.get({value}, {index}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.get()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getfield(self, value: str, index: int, width: int) -> str:
        """Run the ``bit.getfield()`` function.

        Description:
            - This function returns a field of bits from the value starting at the specified index
              position.

        TSP Syntax:
            ```
            - bit.getfield()
            ```

        Args:
            value: Specified number.
            index: One-based bit position within value to get (1 to 32).
            width: The number of bits to include in the field (1 to 32).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getfield({value}, {index}, {width}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getfield()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def set_(self, value: str, index: int) -> str:
        """Run the ``bit.set()`` function.

        Description:
            - This function sets a bit at the specified index position.

        TSP Syntax:
            ```
            - bit.set()
            ```

        Args:
            value: Specified number.
            index: One-based bit position within value to set (1 to 32).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.set({value}, {index}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.set()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setfield(self, value: str, index: int, width: int, field_value: str) -> str:
        """Run the ``bit.setfield()`` function.

        Description:
            - This function overwrites a bit field at a specified index position.

        TSP Syntax:
            ```
            - bit.setfield()
            ```

        Args:
            value: Specified number.
            index: One-based bit position in value to set (1 to 32).
            width: The number of bits to include in the field (1 to 32).
            field_value: Value to write to the field.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.setfield({value}, {index}, {width}, {field_value}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setfield()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def test(self, value: str, index: int) -> str:
        """Run the ``bit.test()`` function.

        Description:
            - This function returns the Boolean value (true or false) of a bit at the specified
              index position.

        TSP Syntax:
            ```
            - bit.test()
            ```

        Args:
            value: Specified number.
            index: One-based bit position within value to test (1 to 32).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.test({value}, {index}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.test()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def toggle(self, value: str, index: int) -> str:
        """Run the ``bit.toggle()`` function.

        Description:
            - This function toggles the value of a bit at a specified index position.

        TSP Syntax:
            ```
            - bit.toggle()
            ```

        Args:
            value: Specified number.
            index: One-based bit position within value to toggle (1 to 32).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.toggle({value}, {index}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.toggle()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
