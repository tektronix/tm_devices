# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The scriptvar commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2604B, SMU2606B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B,
SMU2651A, SMU2657A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - scriptVar.autorun
    - scriptVar.list()
    - scriptVar.name
    - scriptVar.run()
    - scriptVar.save()
    - scriptVar.source
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Scriptvar(BaseTSPCmd):
    """The ``scriptVar`` command tree.

    Info:
        - ``scriptVar``, the name of the variable that references the script.

    Properties and methods:
        - ``.autorun``: The ``scriptVar.autorun`` attribute.
        - ``.list()``: The ``scriptVar.list()`` function.
        - ``.name``: The ``scriptVar.name`` attribute.
        - ``.run()``: The ``scriptVar.run()`` function.
        - ``.save()``: The ``scriptVar.save()`` function.
        - ``.source``: The ``scriptVar.source`` attribute.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "scriptVar"
    ) -> None:
        super().__init__(device, cmd_syntax)

    @property
    def autorun(self) -> str:
        """Access the ``scriptVar.autorun`` attribute.

        Description:
            - This attribute controls the autorun state of a script.

        Usage:
            - Accessing this property will send the ``print(scriptVar.autorun)`` query.
            - Setting this property to a value will send the ``scriptVar.autorun = value`` command.

        TSP Syntax:
            ```
            - scriptVar.autorun = value
            - print(scriptVar.autorun)
            ```

        Info:
            - ``scriptVar``, the name of the variable that references the script.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autorun"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autorun)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorun`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autorun.setter
    def autorun(self, value: Union[str, float]) -> None:
        """Access the ``scriptVar.autorun`` attribute.

        Description:
            - This attribute controls the autorun state of a script.

        Usage:
            - Accessing this property will send the ``print(scriptVar.autorun)`` query.
            - Setting this property to a value will send the ``scriptVar.autorun = value`` command.

        TSP Syntax:
            ```
            - scriptVar.autorun = value
            - print(scriptVar.autorun)
            ```

        Info:
            - ``scriptVar``, the name of the variable that references the script.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autorun", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autorun = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorun`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def name(self) -> str:
        """Access the ``scriptVar.name`` attribute.

        Description:
            - This attribute contains the name of a script in the runtime environment.

        Usage:
            - Accessing this property will send the ``print(scriptVar.name)`` query.
            - Setting this property to a value will send the ``scriptVar.name = value`` command.

        TSP Syntax:
            ```
            - scriptVar.name = value
            - print(scriptVar.name)
            ```

        Info:
            - ``scriptVar``, the name of the variable that references the script.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".name"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.name)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.name`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @name.setter
    def name(self, value: Union[str, float]) -> None:
        """Access the ``scriptVar.name`` attribute.

        Description:
            - This attribute contains the name of a script in the runtime environment.

        Usage:
            - Accessing this property will send the ``print(scriptVar.name)`` query.
            - Setting this property to a value will send the ``scriptVar.name = value`` command.

        TSP Syntax:
            ```
            - scriptVar.name = value
            - print(scriptVar.name)
            ```

        Info:
            - ``scriptVar``, the name of the variable that references the script.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".name", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.name = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.name`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def source(self) -> str:
        """Access the ``scriptVar.source`` attribute.

        Description:
            - This attribute contains the source code of a script.

        Usage:
            - Accessing this property will send the ``print(scriptVar.source)`` query.
            - Setting this property to a value will send the ``scriptVar.source = value`` command.

        TSP Syntax:
            ```
            - scriptVar.source = value
            - print(scriptVar.source)
            ```

        Info:
            - ``scriptVar``, the name of the variable that references the script that contains the
              source code.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".source"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.source)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.source`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @source.setter
    def source(self, value: Union[str, float]) -> None:
        """Access the ``scriptVar.source`` attribute.

        Description:
            - This attribute contains the source code of a script.

        Usage:
            - Accessing this property will send the ``print(scriptVar.source)`` query.
            - Setting this property to a value will send the ``scriptVar.source = value`` command.

        TSP Syntax:
            ```
            - scriptVar.source = value
            - print(scriptVar.source)
            ```

        Info:
            - ``scriptVar``, the name of the variable that references the script that contains the
              source code.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".source", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.source = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.source`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def list(self) -> None:
        """Run the ``scriptVar.list()`` function.

        Description:
            - This function generates a script listing.

        TSP Syntax:
            ```
            - scriptVar.list()
            ```

        Info:
            - ``scriptVar``, the name of the variable that references the script.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.list()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.list()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def run(self) -> None:
        """Run the ``scriptVar.run()`` function.

        Description:
            - This function runs a script.

        TSP Syntax:
            ```
            - scriptVar.run()
            ```

        Info:
            - ``scriptVar``, the name of the variable that references the script.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.run()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.run()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def save(self, filename: Optional[str] = None) -> None:
        """Run the ``scriptVar.save()`` function.

        Description:
            - This function saves the script to nonvolatile memory or to a USB flash drive.

        TSP Syntax:
            ```
            - scriptVar.save()
            ```

        Args:
            filename (optional): A string that contains the file name to use when saving the script
                to a USB flash drive.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (f'"{filename}"' if filename is not None else None,)
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.save({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.save()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
