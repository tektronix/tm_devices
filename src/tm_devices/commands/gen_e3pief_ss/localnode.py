# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The localnode commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - localnode.description
    - localnode.emulation
    - localnode.license
    - localnode.linefreq
    - localnode.model
    - localnode.password
    - localnode.passwordmode
    - localnode.prompts
    - localnode.prompts4882
    - localnode.reset()
    - localnode.revision
    - localnode.serialno
    - localnode.showerrors
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Localnode(BaseTSPCmd):
    """The ``localnode`` command tree.

    Properties and methods:
        - ``.description``: The ``localnode.description`` attribute.
        - ``.emulation``: The ``localnode.emulation`` attribute.
        - ``.license``: The ``localnode.license`` attribute.
        - ``.linefreq``: The ``localnode.linefreq`` attribute.
        - ``.model``: The ``localnode.model`` attribute.
        - ``.password``: The ``localnode.password`` attribute.
        - ``.passwordmode``: The ``localnode.passwordmode`` attribute.
        - ``.prompts``: The ``localnode.prompts`` attribute.
        - ``.prompts4882``: The ``localnode.prompts4882`` attribute.
        - ``.reset()``: The ``localnode.reset()`` function.
        - ``.revision``: The ``localnode.revision`` attribute.
        - ``.serialno``: The ``localnode.serialno`` attribute.
        - ``.showerrors``: The ``localnode.showerrors`` attribute.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "localnode"
    ) -> None:
        super().__init__(device, cmd_syntax)

    @property
    def description(self) -> str:
        """Access the ``localnode.description`` attribute.

        Description:
            - This attribute stores a user-defined description and mDNS service name of the
              instrument.

        Usage:
            - Accessing this property will send the ``print(localnode.description)`` query.
            - Setting this property to a value will send the ``localnode.description = value``
              command.

        TSP Syntax:
            ```
            - localnode.description = value
            - print(localnode.description)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".description"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.description)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.description`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @description.setter
    def description(self, value: Union[str, float]) -> None:
        """Access the ``localnode.description`` attribute.

        Description:
            - This attribute stores a user-defined description and mDNS service name of the
              instrument.

        Usage:
            - Accessing this property will send the ``print(localnode.description)`` query.
            - Setting this property to a value will send the ``localnode.description = value``
              command.

        TSP Syntax:
            ```
            - localnode.description = value
            - print(localnode.description)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".description", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.description = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.description`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def emulation(self) -> str:
        """Access the ``localnode.emulation`` attribute.

        Description:
            - This attribute sets the instrument to report the model number as 3706 instead of
              3706A.

        Usage:
            - Accessing this property will send the ``print(localnode.emulation)`` query.
            - Setting this property to a value will send the ``localnode.emulation = value``
              command.

        TSP Syntax:
            ```
            - localnode.emulation = value
            - print(localnode.emulation)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".emulation"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.emulation)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.emulation`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @emulation.setter
    def emulation(self, value: Union[str, float]) -> None:
        """Access the ``localnode.emulation`` attribute.

        Description:
            - This attribute sets the instrument to report the model number as 3706 instead of
              3706A.

        Usage:
            - Accessing this property will send the ``print(localnode.emulation)`` query.
            - Setting this property to a value will send the ``localnode.emulation = value``
              command.

        TSP Syntax:
            ```
            - localnode.emulation = value
            - print(localnode.emulation)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".emulation", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.emulation = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.emulation`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def license(self) -> str:
        """Access the ``localnode.license`` attribute.

        Description:
            - This attribute returns the product license agreements.

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
            - This attribute contains the power line frequency setting used for NPLC calculations.

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
    def model(self) -> str:
        """Access the ``localnode.model`` attribute.

        Description:
            - This attribute stores the model number.

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
    def password(self) -> str:
        """Access the ``localnode.password`` attribute.

        Description:
            - This attribute stores the remote access password.

        Usage:
            - Setting this property to a value will send the ``localnode.password = value`` command.

        TSP Syntax:
            ```
            - localnode.password = value
            ```

        Raises:
            AttributeError: Indicates that this attribute is write-only.
        """
        if self._device.command_syntax_enabled:  # type: ignore[union-attr]
            return self._cmd_syntax + ".password"
        msg = f"``{self._cmd_syntax}.password`` is a write-only attribute."
        raise AttributeError(msg)

    @password.setter
    def password(self, value: Union[str, float]) -> None:
        """Access the ``localnode.password`` attribute.

        Description:
            - This attribute stores the remote access password.

        Usage:
            - Setting this property to a value will send the ``localnode.password = value`` command.

        TSP Syntax:
            ```
            - localnode.password = value
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.password = {value}"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.password`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def passwordmode(self) -> str:
        """Access the ``localnode.passwordmode`` attribute.

        Description:
            - This attribute stores the password enable mode for remote access to the instrument.

        Usage:
            - Accessing this property will send the ``print(localnode.passwordmode)`` query.
            - Setting this property to a value will send the ``localnode.passwordmode = value``
              command.

        TSP Syntax:
            ```
            - localnode.passwordmode = value
            - print(localnode.passwordmode)
            ```

        Info:
            - ``mode``, the remote password enable mode.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".passwordmode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.passwordmode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.passwordmode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @passwordmode.setter
    def passwordmode(self, value: Union[str, float]) -> None:
        """Access the ``localnode.passwordmode`` attribute.

        Description:
            - This attribute stores the password enable mode for remote access to the instrument.

        Usage:
            - Accessing this property will send the ``print(localnode.passwordmode)`` query.
            - Setting this property to a value will send the ``localnode.passwordmode = value``
              command.

        TSP Syntax:
            ```
            - localnode.passwordmode = value
            - print(localnode.passwordmode)
            ```

        Info:
            - ``mode``, the remote password enable mode.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".passwordmode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.passwordmode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.passwordmode`` attribute."  # noqa: E501
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
            - This attribute enables and disables the generation of prompts for IEEE Std 488.2
              common commands.

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
            - This attribute enables and disables the generation of prompts for IEEE Std 488.2
              common commands.

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
    def revision(self) -> str:
        """Access the ``localnode.revision`` attribute.

        Description:
            - This attribute stores the firmware revision level.

        Usage:
            - Accessing this property will send the ``print(localnode.revision)`` query.

        TSP Syntax:
            ```
            - print(localnode.revision)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".revision"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.revision)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.revision`` attribute."  # noqa: E501
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

    def reset(self) -> None:
        """Run the ``localnode.reset()`` function.

        Description:
            - This function resets the local node instrument.

        TSP Syntax:
            ```
            - localnode.reset()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.reset()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.reset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
