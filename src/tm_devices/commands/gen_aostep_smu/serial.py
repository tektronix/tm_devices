# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The serial commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2604B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B, SMU2651A,
SMU2657A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - serial.baud
    - serial.databits
    - serial.flowcontrol
    - serial.parity
    - serial.read()
    - serial.write()
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Serial(BaseTSPCmd):
    """The ``serial`` command tree.

    Constants:
        - ``.FLOW_HARDWARE``: Hardware flow control.
        - ``.FLOW_NONE``: No flow control.
        - ``.PARITY_EVEN``: Select even parity.
        - ``.PARITY_NONE``: Select no parity.
        - ``.PARITY_ODD``: Select odd parity.

    Properties and methods:
        - ``.baud``: The ``serial.baud`` attribute.
        - ``.databits``: The ``serial.databits`` attribute.
        - ``.flowcontrol``: The ``serial.flowcontrol`` attribute.
        - ``.parity``: The ``serial.parity`` attribute.
        - ``.read()``: The ``serial.read()`` function.
        - ``.write()``: The ``serial.write()`` function.
    """

    FLOW_HARDWARE = "serial.FLOW_HARDWARE"
    """str: Hardware flow control."""
    FLOW_NONE = "serial.FLOW_NONE"
    """str: No flow control."""
    PARITY_EVEN = "serial.PARITY_EVEN"
    """str: Select even parity."""
    PARITY_NONE = "serial.PARITY_NONE"
    """str: Select no parity."""
    PARITY_ODD = "serial.PARITY_ODD"
    """str: Select odd parity."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "serial") -> None:
        super().__init__(device, cmd_syntax)

    @property
    def baud(self) -> str:
        """Access the ``serial.baud`` attribute.

        Description:
            - This attribute configures the baud rate for the RS-232 port.

        Usage:
            - Accessing this property will send the ``print(serial.baud)`` query.
            - Setting this property to a value will send the ``serial.baud = value`` command.

        TSP Syntax:
            ```
            - serial.baud = value
            - print(serial.baud)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".baud"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.baud)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.baud`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @baud.setter
    def baud(self, value: Union[str, float]) -> None:
        """Access the ``serial.baud`` attribute.

        Description:
            - This attribute configures the baud rate for the RS-232 port.

        Usage:
            - Accessing this property will send the ``print(serial.baud)`` query.
            - Setting this property to a value will send the ``serial.baud = value`` command.

        TSP Syntax:
            ```
            - serial.baud = value
            - print(serial.baud)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".baud", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.baud = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.baud`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def databits(self) -> str:
        """Access the ``serial.databits`` attribute.

        Description:
            - This attribute configures character width (data bits) for the RS-232 port.

        Usage:
            - Accessing this property will send the ``print(serial.databits)`` query.
            - Setting this property to a value will send the ``serial.databits = value`` command.

        TSP Syntax:
            ```
            - serial.databits = value
            - print(serial.databits)
            ```

        Info:
            - ``bits``, the an integer representing the character width (7 or 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".databits"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.databits)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.databits`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @databits.setter
    def databits(self, value: Union[str, float]) -> None:
        """Access the ``serial.databits`` attribute.

        Description:
            - This attribute configures character width (data bits) for the RS-232 port.

        Usage:
            - Accessing this property will send the ``print(serial.databits)`` query.
            - Setting this property to a value will send the ``serial.databits = value`` command.

        TSP Syntax:
            ```
            - serial.databits = value
            - print(serial.databits)
            ```

        Info:
            - ``bits``, the an integer representing the character width (7 or 8).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".databits", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.databits = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.databits`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def flowcontrol(self) -> str:
        """Access the ``serial.flowcontrol`` attribute.

        Description:
            - This attribute configures flow control for the RS-232 port.

        Usage:
            - Accessing this property will send the ``print(serial.flowcontrol)`` query.
            - Setting this property to a value will send the ``serial.flowcontrol = value`` command.

        TSP Syntax:
            ```
            - serial.flowcontrol = value
            - print(serial.flowcontrol)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".flowcontrol"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.flowcontrol)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.flowcontrol`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @flowcontrol.setter
    def flowcontrol(self, value: Union[str, float]) -> None:
        """Access the ``serial.flowcontrol`` attribute.

        Description:
            - This attribute configures flow control for the RS-232 port.

        Usage:
            - Accessing this property will send the ``print(serial.flowcontrol)`` query.
            - Setting this property to a value will send the ``serial.flowcontrol = value`` command.

        TSP Syntax:
            ```
            - serial.flowcontrol = value
            - print(serial.flowcontrol)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".flowcontrol", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.flowcontrol = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.flowcontrol`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def parity(self) -> str:
        """Access the ``serial.parity`` attribute.

        Description:
            - This attribute configures parity for the RS-232 port.

        Usage:
            - Accessing this property will send the ``print(serial.parity)`` query.
            - Setting this property to a value will send the ``serial.parity = value`` command.

        TSP Syntax:
            ```
            - serial.parity = value
            - print(serial.parity)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".parity"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.parity)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.parity`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @parity.setter
    def parity(self, value: Union[str, float]) -> None:
        """Access the ``serial.parity`` attribute.

        Description:
            - This attribute configures parity for the RS-232 port.

        Usage:
            - Accessing this property will send the ``print(serial.parity)`` query.
            - Setting this property to a value will send the ``serial.parity = value`` command.

        TSP Syntax:
            ```
            - serial.parity = value
            - print(serial.parity)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".parity", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.parity = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.parity`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def read(self, maxchars: str) -> str:
        """Run the ``serial.read()`` function.

        Description:
            - This function reads available characters (data) from the serial port.

        TSP Syntax:
            ```
            - serial.read()
            ```

        Args:
            maxchars: An integer that specifies the maximum number of characters to read.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.read({maxchars}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.read()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def write(self, data: str) -> None:
        """Run the ``serial.write()`` function.

        Description:
            - This function writes data to the serial port.

        TSP Syntax:
            ```
            - serial.write()
            ```

        Args:
            data: A string representing the data to write.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.write("{data}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.write()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
