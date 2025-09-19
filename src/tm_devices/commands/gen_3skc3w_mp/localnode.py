# pyright: reportConstantRedefinition=none
"""The localnode commands module.

These commands are used in the following models:
MP5103

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - localnode.license
    - localnode.linefreq
    - localnode.manufacturer
    - localnode.model
    - localnode.prompts
    - localnode.prompts4882
    - localnode.serialno
    - localnode.showerrors
    - localnode.version
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Localnode(BaseTSPCmd):
    """The ``localnode`` command tree.

    Properties and methods:
        - ``.license``: The ``localnode.license`` attribute.
        - ``.linefreq``: The ``localnode.linefreq`` attribute.
        - ``.manufacturer``: The ``localnode.manufacturer`` attribute.
        - ``.model``: The ``localnode.model`` attribute.
        - ``.prompts``: The ``localnode.prompts`` attribute.
        - ``.prompts4882``: The ``localnode.prompts4882`` attribute.
        - ``.serialno``: The ``localnode.serialno`` attribute.
        - ``.showerrors``: The ``localnode.showerrors`` attribute.
        - ``.version``: The ``localnode.version`` attribute.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "localnode"
    ) -> None:
        super().__init__(device, cmd_syntax)

    @property
    def license(self) -> str:
        """Access the ``localnode.license`` attribute.

        Description:
            - This attribute stores the license of the instrument.

        Usage:
            - Accessing this property will send the ``print(localnode.license)`` query.

        TSP Syntax:
            ```
            - print(localnode.license)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".license"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.license)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.license`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def linefreq(self) -> str:
        """Access the ``localnode.linefreq`` attribute.

        Description:
            - This attribute contains the power line frequency detected at power-on.

        Usage:
            - Accessing this property will send the ``print(localnode.linefreq)`` query.

        TSP Syntax:
            ```
            - print(localnode.linefreq)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".linefreq"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.linefreq)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.linefreq`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def manufacturer(self) -> str:
        """Access the ``localnode.manufacturer`` attribute.

        Description:
            - This attribute stores the manufacturer of the instrument.

        Usage:
            - Accessing this property will send the ``print(localnode.manufacturer)`` query.

        TSP Syntax:
            ```
            - print(localnode.manufacturer)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".manufacturer"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.manufacturer)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.manufacturer`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def model(self) -> str:
        """Access the ``localnode.model`` attribute.

        Description:
            - This attribute stores the model number of the instrument.

        Usage:
            - Accessing this property will send the ``print(localnode.model)`` query.

        TSP Syntax:
            ```
            - print(localnode.model)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".model"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.model)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.model`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def prompts(self) -> str:
        """Access the ``localnode.prompts`` attribute.

        Description:
            - This attribute determines if the instrument generates prompts in response to command
              messages.

        Usage:
            - Accessing this property will send the ``print(localnode.prompts)`` query.
            - Setting this property to a value will send the ``localnode.prompts = value`` command.

        TSP Syntax:
            ```
            - localnode.prompts = value
            - print(localnode.prompts)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".prompts"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.prompts)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.prompts`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @prompts.setter
    def prompts(self, value: Union[str, float]) -> None:
        """Access the ``localnode.prompts`` attribute.

        Description:
            - This attribute determines if the instrument generates prompts in response to command
              messages.

        Usage:
            - Accessing this property will send the ``print(localnode.prompts)`` query.
            - Setting this property to a value will send the ``localnode.prompts = value`` command.

        TSP Syntax:
            ```
            - localnode.prompts = value
            - print(localnode.prompts)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".prompts", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.prompts = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.prompts`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def prompts4882(self) -> str:
        """Access the ``localnode.prompts4882`` attribute.

        Description:
            - This attribute enables or disables the generation of prompts for IEEE Std 488.2 common
              commands.

        Usage:
            - Accessing this property will send the ``print(localnode.prompts4882)`` query.
            - Setting this property to a value will send the ``localnode.prompts4882 = value``
              command.

        TSP Syntax:
            ```
            - localnode.prompts4882 = value
            - print(localnode.prompts4882)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".prompts4882"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.prompts4882)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.prompts4882`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @prompts4882.setter
    def prompts4882(self, value: Union[str, float]) -> None:
        """Access the ``localnode.prompts4882`` attribute.

        Description:
            - This attribute enables or disables the generation of prompts for IEEE Std 488.2 common
              commands.

        Usage:
            - Accessing this property will send the ``print(localnode.prompts4882)`` query.
            - Setting this property to a value will send the ``localnode.prompts4882 = value``
              command.

        TSP Syntax:
            ```
            - localnode.prompts4882 = value
            - print(localnode.prompts4882)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".prompts4882", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.prompts4882 = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.prompts4882`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def serialno(self) -> str:
        """Access the ``localnode.serialno`` attribute.

        Description:
            - This attribute stores the serial number of the instrument.

        Usage:
            - Accessing this property will send the ``print(localnode.serialno)`` query.

        TSP Syntax:
            ```
            - print(localnode.serialno)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".serialno"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.serialno)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.serialno`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def showerrors(self) -> str:
        """Access the ``localnode.showerrors`` attribute.

        Description:
            - This attribute sets whether or not the instrument automatically sends generated
              errors.

        Usage:
            - Accessing this property will send the ``print(localnode.showerrors)`` query.
            - Setting this property to a value will send the ``localnode.showerrors = value``
              command.

        TSP Syntax:
            ```
            - localnode.showerrors = value
            - print(localnode.showerrors)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".showerrors"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.showerrors)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.showerrors`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @showerrors.setter
    def showerrors(self, value: Union[str, float]) -> None:
        """Access the ``localnode.showerrors`` attribute.

        Description:
            - This attribute sets whether or not the instrument automatically sends generated
              errors.

        Usage:
            - Accessing this property will send the ``print(localnode.showerrors)`` query.
            - Setting this property to a value will send the ``localnode.showerrors = value``
              command.

        TSP Syntax:
            ```
            - localnode.showerrors = value
            - print(localnode.showerrors)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".showerrors", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.showerrors = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.showerrors`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def version(self) -> str:
        """Access the ``localnode.version`` attribute.

        Description:
            - This attribute stores the firmware revision level.

        Usage:
            - Accessing this property will send the ``print(localnode.version)`` query.

        TSP Syntax:
            ```
            - print(localnode.version)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".version"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.version)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.version`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
