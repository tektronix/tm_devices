# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The scriptvar commands module.

These commands are used in the following models:
DAQ6510, DMM6500, DMM7510, SMU2450, SMU2460, SMU2461, SMU2470

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - scriptVar.run()
    - scriptVar.save()
    - scriptVar.source
    ```
"""

from typing import Optional, TYPE_CHECKING

from ..helpers import BaseTSPCmd, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class Scriptvar(BaseTSPCmd):
    """The ``scriptVar`` command tree.

    Info:
        - ``scriptVar``, the name of the variable that references the script.

    Properties and methods:
        - ``.run()``: The ``scriptVar.run()`` function.
        - ``.save()``: The ``scriptVar.save()`` function.
        - ``.source``: The ``scriptVar.source`` attribute.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "scriptVar"
    ) -> None:
        super().__init__(device, cmd_syntax)

    @property
    def source(self) -> str:
        """Access the ``scriptVar.source`` attribute.

        Description:
            - This attribute contains the source code of a script.

        Usage:
            - Accessing this property will send the ``print(scriptVar.source)`` query.

        TSP Syntax:
            ```
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
