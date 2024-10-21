# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The format commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - format.asciiprecision
    - format.byteorder
    - format.data
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Format(BaseTSPCmd):
    """The ``format`` command tree.

    Properties and methods:
        - ``.asciiprecision``: The ``format.asciiprecision`` attribute.
        - ``.byteorder``: The ``format.byteorder`` attribute.
        - ``.data``: The ``format.data`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "format") -> None:
        super().__init__(device, cmd_syntax)

    @property
    def asciiprecision(self) -> str:
        """Access the ``format.asciiprecision`` attribute.

        Description:
            - This attribute sets the precision (number of digits) for all numbers returned in the
              ASCII format.

        Usage:
            - Accessing this property will send the ``print(format.asciiprecision)`` query.
            - Setting this property to a value will send the ``format.asciiprecision = value``
              command.

        TSP Syntax:
            ```
            - format.asciiprecision = value
            - print(format.asciiprecision)
            ```

        Info:
            - ``precision``, a number representing the number of digits to be printed for numbers
              printed with the print(), printbuffer(), and printnumber() functions; must be a number
              from 1 to 16; set to 0 to have the instrument select the precision automatically based
              on the number that is being formatted.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".asciiprecision"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.asciiprecision)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.asciiprecision`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @asciiprecision.setter
    def asciiprecision(self, value: Union[str, float]) -> None:
        """Access the ``format.asciiprecision`` attribute.

        Description:
            - This attribute sets the precision (number of digits) for all numbers returned in the
              ASCII format.

        Usage:
            - Accessing this property will send the ``print(format.asciiprecision)`` query.
            - Setting this property to a value will send the ``format.asciiprecision = value``
              command.

        TSP Syntax:
            ```
            - format.asciiprecision = value
            - print(format.asciiprecision)
            ```

        Info:
            - ``precision``, a number representing the number of digits to be printed for numbers
              printed with the print(), printbuffer(), and printnumber() functions; must be a number
              from 1 to 16; set to 0 to have the instrument select the precision automatically based
              on the number that is being formatted.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".asciiprecision", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.asciiprecision = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.asciiprecision`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def byteorder(self) -> str:
        """Access the ``format.byteorder`` attribute.

        Description:
            - This attribute sets the binary byte order for the data that is printed using the
              printnumber() and printbuffer() functions.

        Usage:
            - Accessing this property will send the ``print(format.byteorder)`` query.
            - Setting this property to a value will send the ``format.byteorder = value`` command.

        TSP Syntax:
            ```
            - format.byteorder = value
            - print(format.byteorder)
            ```

        Info:
            - ``order``, the byte order value as follows:

                * Most significant byte first: 0, format.NORMAL, format.NETWORK, or format.BIGENDIAN
                * Least significant byte first: 1, format.SWAPPED or format.LITTLEENDIAN.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".byteorder"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.byteorder)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.byteorder`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @byteorder.setter
    def byteorder(self, value: Union[str, float]) -> None:
        """Access the ``format.byteorder`` attribute.

        Description:
            - This attribute sets the binary byte order for the data that is printed using the
              printnumber() and printbuffer() functions.

        Usage:
            - Accessing this property will send the ``print(format.byteorder)`` query.
            - Setting this property to a value will send the ``format.byteorder = value`` command.

        TSP Syntax:
            ```
            - format.byteorder = value
            - print(format.byteorder)
            ```

        Info:
            - ``order``, the byte order value as follows:

                * Most significant byte first: 0, format.NORMAL, format.NETWORK, or format.BIGENDIAN
                * Least significant byte first: 1, format.SWAPPED or format.LITTLEENDIAN.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".byteorder", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.byteorder = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.byteorder`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def data(self) -> str:
        """Access the ``format.data`` attribute.

        Description:
            - This attribute sets the data format for data that is printed using the printnumber()
              and printbuffer() functions.

        Usage:
            - Accessing this property will send the ``print(format.data)`` query.
            - Setting this property to a value will send the ``format.data = value`` command.

        TSP Syntax:
            ```
            - format.data = value
            - print(format.data)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".data"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.data)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.data`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @data.setter
    def data(self, value: Union[str, float]) -> None:
        """Access the ``format.data`` attribute.

        Description:
            - This attribute sets the data format for data that is printed using the printnumber()
              and printbuffer() functions.

        Usage:
            - Accessing this property will send the ``print(format.data)`` query.
            - Setting this property to a value will send the ``format.data = value`` command.

        TSP Syntax:
            ```
            - format.data = value
            - print(format.data)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".data", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.data = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.data`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
