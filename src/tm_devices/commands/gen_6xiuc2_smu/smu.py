# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The smu commands module.

These commands are used in the following models:
SMU2470

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - smu.breakdownprotection
    - smu.interlock.enable
    - smu.interlock.tripped
    - smu.measure.autorange
    - smu.measure.autorangehigh
    - smu.measure.autorangelow
    - smu.measure.autorangerebound
    - smu.measure.autozero.enable
    - smu.measure.autozero.once()
    - smu.measure.configlist.catalog()
    - smu.measure.configlist.create()
    - smu.measure.configlist.delete()
    - smu.measure.configlist.query()
    - smu.measure.configlist.recall()
    - smu.measure.configlist.size()
    - smu.measure.configlist.store()
    - smu.measure.configlist.storefunc()
    - smu.measure.count
    - smu.measure.displaydigits
    - smu.measure.filter.count
    - smu.measure.filter.enable
    - smu.measure.filter.type
    - smu.measure.func
    - smu.measure.getattribute()
    - smu.measure.limit[Y].clear()
    - smu.measure.limit[r].audible
    - smu.measure.limit[r].autoclear
    - smu.measure.limit[r].enable
    - smu.measure.limit[r].fail
    - smu.measure.limit[r].high.value
    - smu.measure.limit[r].low.value
    - smu.measure.math.enable
    - smu.measure.math.format
    - smu.measure.math.mxb.bfactor
    - smu.measure.math.mxb.mfactor
    - smu.measure.math.percent
    - smu.measure.nplc
    - smu.measure.offsetcompensation
    - smu.measure.range
    - smu.measure.read()
    - smu.measure.readwithtime()
    - smu.measure.rel.acquire()
    - smu.measure.rel.enable
    - smu.measure.rel.level
    - smu.measure.sense
    - smu.measure.setattribute()
    - smu.measure.unit
    - smu.measure.userdelay[N]
    - smu.reset()
    - smu.source.autodelay
    - smu.source.autorange
    - smu.source.configlist.catalog()
    - smu.source.configlist.create()
    - smu.source.configlist.delete()
    - smu.source.configlist.query()
    - smu.source.configlist.recall()
    - smu.source.configlist.size()
    - smu.source.configlist.store()
    - smu.source.configlist.storefunc()
    - smu.source.delay
    - smu.source.func
    - smu.source.getattribute()
    - smu.source.highc
    - smu.source.ilimit.level
    - smu.source.ilimit.tripped
    - smu.source.level
    - smu.source.offmode
    - smu.source.output
    - smu.source.protect.level
    - smu.source.protect.tripped
    - smu.source.range
    - smu.source.readback
    - smu.source.setattribute()
    - smu.source.sweeplinear()
    - smu.source.sweeplinearstep()
    - smu.source.sweeplist()
    - smu.source.sweeplog()
    - smu.source.userdelay[N]
    - smu.source.vlimit.level
    - smu.source.vlimit.tripped
    - smu.terminals
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from ..helpers import (
    BaseTSPCmd,
    DefaultDictDeviceCommunication,
    DefaultDictPassKeyToFactory,
    NoDeviceProvidedError,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class SmuSourceVlimit(BaseTSPCmd):
    """The ``smu.source.vlimit`` command tree.

    Properties and methods:
        - ``.level``: The ``smu.source.vlimit.level`` attribute.
        - ``.tripped``: The ``smu.source.vlimit.tripped`` attribute.
    """

    @property
    def level(self) -> str:
        """Access the ``smu.source.vlimit.level`` attribute.

        Description:
            - This attribute selects the source limit for measurements. (voltage)

        Usage:
            - Accessing this property will send the ``print(smu.source.vlimit.level)`` query.
            - Setting this property to a value will send the ``smu.source.vlimit.level = value``
              command.

        TSP Syntax:
            ```
            - smu.source.vlimit.level = value
            - print(smu.source.vlimit.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".level"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.level)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @level.setter
    def level(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.vlimit.level`` attribute.

        Description:
            - This attribute selects the source limit for measurements. (voltage)

        Usage:
            - Accessing this property will send the ``print(smu.source.vlimit.level)`` query.
            - Setting this property to a value will send the ``smu.source.vlimit.level = value``
              command.

        TSP Syntax:
            ```
            - smu.source.vlimit.level = value
            - print(smu.source.vlimit.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".level", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.level = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def tripped(self) -> str:
        """Access the ``smu.source.vlimit.tripped`` attribute.

        Description:
            - This attribute indicates if the source exceeded the limits that were set for the
              selected measurements. (voltage)

        Usage:
            - Accessing this property will send the ``print(smu.source.vlimit.tripped)`` query.

        TSP Syntax:
            ```
            - print(smu.source.vlimit.tripped)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".tripped"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.tripped)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tripped`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuSourceProtect(BaseTSPCmd):
    """The ``smu.source.protect`` command tree.

    Properties and methods:
        - ``.level``: The ``smu.source.protect.level`` attribute.
        - ``.tripped``: The ``smu.source.protect.tripped`` attribute.
    """

    @property
    def level(self) -> str:
        """Access the ``smu.source.protect.level`` attribute.

        Description:
            - This attribute sets the overvoltage protection setting of the source output.

        Usage:
            - Accessing this property will send the ``print(smu.source.protect.level)`` query.
            - Setting this property to a value will send the ``smu.source.protect.level = value``
              command.

        TSP Syntax:
            ```
            - smu.source.protect.level = value
            - print(smu.source.protect.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".level"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.level)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @level.setter
    def level(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.protect.level`` attribute.

        Description:
            - This attribute sets the overvoltage protection setting of the source output.

        Usage:
            - Accessing this property will send the ``print(smu.source.protect.level)`` query.
            - Setting this property to a value will send the ``smu.source.protect.level = value``
              command.

        TSP Syntax:
            ```
            - smu.source.protect.level = value
            - print(smu.source.protect.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".level", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.level = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def tripped(self) -> str:
        """Access the ``smu.source.protect.tripped`` attribute.

        Description:
            - This attribute indicates if the overvoltage source protection feature is active.

        Usage:
            - Accessing this property will send the ``print(smu.source.protect.tripped)`` query.

        TSP Syntax:
            ```
            - print(smu.source.protect.tripped)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".tripped"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.tripped)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tripped`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuSourceIlimit(BaseTSPCmd):
    """The ``smu.source.ilimit`` command tree.

    Properties and methods:
        - ``.level``: The ``smu.source.ilimit.level`` attribute.
        - ``.tripped``: The ``smu.source.ilimit.tripped`` attribute.
    """

    @property
    def level(self) -> str:
        """Access the ``smu.source.ilimit.level`` attribute.

        Description:
            - This attribute selects the source limit for measurements. (current)

        Usage:
            - Accessing this property will send the ``print(smu.source.ilimit.level)`` query.
            - Setting this property to a value will send the ``smu.source.ilimit.level = value``
              command.

        TSP Syntax:
            ```
            - smu.source.ilimit.level = value
            - print(smu.source.ilimit.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".level"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.level)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @level.setter
    def level(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.ilimit.level`` attribute.

        Description:
            - This attribute selects the source limit for measurements. (current)

        Usage:
            - Accessing this property will send the ``print(smu.source.ilimit.level)`` query.
            - Setting this property to a value will send the ``smu.source.ilimit.level = value``
              command.

        TSP Syntax:
            ```
            - smu.source.ilimit.level = value
            - print(smu.source.ilimit.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".level", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.level = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def tripped(self) -> str:
        """Access the ``smu.source.ilimit.tripped`` attribute.

        Description:
            - This attribute indicates if the source exceeded the limits that were set for the
              selected measurements. (current)

        Usage:
            - Accessing this property will send the ``print(smu.source.ilimit.tripped)`` query.

        TSP Syntax:
            ```
            - print(smu.source.ilimit.tripped)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".tripped"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.tripped)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tripped`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuSourceConfiglist(BaseTSPCmd):
    """The ``smu.source.configlist`` command tree.

    Properties and methods:
        - ``.catalog()``: The ``smu.source.configlist.catalog()`` function.
        - ``.create()``: The ``smu.source.configlist.create()`` function.
        - ``.delete()``: The ``smu.source.configlist.delete()`` function.
        - ``.query()``: The ``smu.source.configlist.query()`` function.
        - ``.recall()``: The ``smu.source.configlist.recall()`` function.
        - ``.size()``: The ``smu.source.configlist.size()`` function.
        - ``.store()``: The ``smu.source.configlist.store()`` function.
        - ``.storefunc()``: The ``smu.source.configlist.storefunc()`` function.
    """

    def catalog(self) -> str:
        """Run the ``smu.source.configlist.catalog()`` function.

        Description:
            - This function returns the name of one source configuration list.

        TSP Syntax:
            ```
            - smu.source.configlist.catalog()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.catalog())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.catalog()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def create(self, list_name: str) -> None:
        """Run the ``smu.source.configlist.create()`` function.

        Description:
            - This function creates an empty source configuration list.

        TSP Syntax:
            ```
            - smu.source.configlist.create()
            ```

        Args:
            list_name: A string that represents the name of a source configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.create("{list_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.create()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def delete(self, list_name: str, index: Optional[int] = None) -> None:
        """Run the ``smu.source.configlist.delete()`` function.

        Description:
            - This function deletes a source configuration list.

        TSP Syntax:
            ```
            - smu.source.configlist.delete()
            ```

        Args:
            list_name: A string that represents the name of a source configuration list.
            index (optional): A number that defines a specific configuration index in the
                configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{list_name}"',
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.delete({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.delete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def query(self, list_name: str, index: int, field_separator: Optional[str] = None) -> str:
        """Run the ``smu.source.configlist.query()`` function.

        Description:
            - This function returns a list of TSP commands and parameter settings that are stored in
              the specified configuration index.

        TSP Syntax:
            ```
            - smu.source.configlist.query()
            ```

        Args:
            list_name: A string that represents the name of a source configuration list.
            index: A number that defines a specific configuration index in the configuration list;
                the default is the first index in the configuration list.
            field_separator (optional): String that represents the separator for the data; use one
                of the following.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{list_name}"',
                    index,
                    f'"{field_separator}"' if field_separator is not None else None,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.query({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.query()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def recall(
        self,
        list_name: str,
        index: int,
        measure_list_name: Optional[str] = None,
        measure_index: Optional[float] = None,
    ) -> None:
        """Run the ``smu.source.configlist.recall()`` function.

        Description:
            - This function recalls a specific configuration index in a specific source
              configuration list and an optional measure configuration list.

        TSP Syntax:
            ```
            - smu.source.configlist.recall()
            ```

        Args:
            list_name: A string that represents the name of a source configuration list.
            index: A number that defines a specific configuration index in the source configuration
                list.
            measure_list_name (optional): A string that represents the name of a measure
                configuration list.
            measure_index (optional): A number that defines a specific configuration index in the
                measure configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{list_name}"',
                    index,
                    f'"{measure_list_name}"' if measure_list_name is not None else None,
                    measure_index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.recall({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.recall()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def size(self, list_name: str) -> str:
        """Run the ``smu.source.configlist.size()`` function.

        Description:
            - This function returns the number of configuration indexes in a source configuration
              list.

        TSP Syntax:
            ```
            - smu.source.configlist.size()
            ```

        Args:
            list_name: A string that represents the name of a source configuration list.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.size("{list_name}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.size()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def store(self, list_name: str, index: Optional[int] = None) -> None:
        """Run the ``smu.source.configlist.store()`` function.

        Description:
            - This function stores the active source settings into the named configuration list.

        TSP Syntax:
            ```
            - smu.source.configlist.store()
            ```

        Args:
            list_name: A string that represents the name of a source configuration list.
            index (optional): A number that defines a specific configuration index in the
                configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{list_name}"',
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.store({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.store()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def storefunc(self, config_list_name: str, function: str, index: Optional[int] = None) -> None:
        """Run the ``smu.source.configlist.storefunc()`` function.

        Description:
            - This function allows you to store the settings for a source function into a source
              configuration list whether or not the function is active.

        TSP Syntax:
            ```
            - smu.source.configlist.storefunc()
            ```

        Args:
            config_list_name: Name of the configuration list in which to store the function
                settings.
            function: The function to save into the configuration list.
            index (optional): The number of the configuration list index in which to store the
                settings.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
                    function,
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.storefunc({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.storefunc()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


#  pylint: disable=too-many-public-methods
class SmuSource(BaseTSPCmd):
    """The ``smu.source`` command tree.

    Properties and methods:
        - ``.autodelay``: The ``smu.source.autodelay`` attribute.
        - ``.autorange``: The ``smu.source.autorange`` attribute.
        - ``.configlist``: The ``smu.source.configlist`` command tree.
        - ``.delay``: The ``smu.source.delay`` attribute.
        - ``.func``: The ``smu.source.func`` attribute.
        - ``.getattribute()``: The ``smu.source.getattribute()`` function.
        - ``.highc``: The ``smu.source.highc`` attribute.
        - ``.level``: The ``smu.source.level`` attribute.
        - ``.offmode``: The ``smu.source.offmode`` attribute.
        - ``.output``: The ``smu.source.output`` attribute.
        - ``.protect``: The ``smu.source.protect`` command tree.
        - ``.range``: The ``smu.source.range`` attribute.
        - ``.readback``: The ``smu.source.readback`` attribute.
        - ``.setattribute()``: The ``smu.source.setattribute()`` function.
        - ``.sweeplinear()``: The ``smu.source.sweeplinear()`` function.
        - ``.sweeplinearstep()``: The ``smu.source.sweeplinearstep()`` function.
        - ``.sweeplist()``: The ``smu.source.sweeplist()`` function.
        - ``.sweeplog()``: The ``smu.source.sweeplog()`` function.
        - ``.userdelay``: The ``smu.source.userdelay[N]`` attribute.
        - ``.ilimit``: The ``smu.source.ilimit`` command tree.
        - ``.vlimit``: The ``smu.source.vlimit`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._configlist = SmuSourceConfiglist(device, f"{self._cmd_syntax}.configlist")
        self._protect = SmuSourceProtect(device, f"{self._cmd_syntax}.protect")
        self._userdelay: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.userdelay[{{key}}]",
            write_syntax=f"{self._cmd_syntax}.userdelay[{{key}}] = ",
            query_syntax=f"print({self._cmd_syntax}.userdelay[{{key}}])",
            device=self._device,
        )
        self._ilimit = SmuSourceIlimit(device, f"{self._cmd_syntax}.ilimit")
        self._vlimit = SmuSourceVlimit(device, f"{self._cmd_syntax}.vlimit")

    @property
    def autodelay(self) -> str:
        """Access the ``smu.source.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic delay that occurs when the source is
              turned on.

        Usage:
            - Accessing this property will send the ``print(smu.source.autodelay)`` query.
            - Setting this property to a value will send the ``smu.source.autodelay = value``
              command.

        TSP Syntax:
            ```
            - smu.source.autodelay = value
            - print(smu.source.autodelay)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autodelay"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autodelay)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autodelay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autodelay.setter
    def autodelay(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic delay that occurs when the source is
              turned on.

        Usage:
            - Accessing this property will send the ``print(smu.source.autodelay)`` query.
            - Setting this property to a value will send the ``smu.source.autodelay = value``
              command.

        TSP Syntax:
            ```
            - smu.source.autodelay = value
            - print(smu.source.autodelay)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autodelay", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autodelay = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autodelay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autorange(self) -> str:
        """Access the ``smu.source.autorange`` attribute.

        Description:
            - This attribute determines if the range is selected manually or automatically for the
              selected source function or voltage source.

        Usage:
            - Accessing this property will send the ``print(smu.source.autorange)`` query.
            - Setting this property to a value will send the ``smu.source.autorange = value``
              command.

        TSP Syntax:
            ```
            - smu.source.autorange = value
            - print(smu.source.autorange)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autorange"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autorange)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorange`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autorange.setter
    def autorange(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.autorange`` attribute.

        Description:
            - This attribute determines if the range is selected manually or automatically for the
              selected source function or voltage source.

        Usage:
            - Accessing this property will send the ``print(smu.source.autorange)`` query.
            - Setting this property to a value will send the ``smu.source.autorange = value``
              command.

        TSP Syntax:
            ```
            - smu.source.autorange = value
            - print(smu.source.autorange)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autorange", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autorange = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorange`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def configlist(self) -> SmuSourceConfiglist:
        """Return the ``smu.source.configlist`` command tree.

        Sub-properties and sub-methods:
            - ``.catalog()``: The ``smu.source.configlist.catalog()`` function.
            - ``.create()``: The ``smu.source.configlist.create()`` function.
            - ``.delete()``: The ``smu.source.configlist.delete()`` function.
            - ``.query()``: The ``smu.source.configlist.query()`` function.
            - ``.recall()``: The ``smu.source.configlist.recall()`` function.
            - ``.size()``: The ``smu.source.configlist.size()`` function.
            - ``.store()``: The ``smu.source.configlist.store()`` function.
            - ``.storefunc()``: The ``smu.source.configlist.storefunc()`` function.
        """
        return self._configlist

    @property
    def delay(self) -> str:
        """Access the ``smu.source.delay`` attribute.

        Description:
            - This attribute contains the source delay.

        Usage:
            - Accessing this property will send the ``print(smu.source.delay)`` query.
            - Setting this property to a value will send the ``smu.source.delay = value`` command.

        TSP Syntax:
            ```
            - smu.source.delay = value
            - print(smu.source.delay)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".delay"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.delay)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @delay.setter
    def delay(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.delay`` attribute.

        Description:
            - This attribute contains the source delay.

        Usage:
            - Accessing this property will send the ``print(smu.source.delay)`` query.
            - Setting this property to a value will send the ``smu.source.delay = value`` command.

        TSP Syntax:
            ```
            - smu.source.delay = value
            - print(smu.source.delay)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".delay", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.delay = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.delay`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def func(self) -> str:
        """Access the ``smu.source.func`` attribute.

        Description:
            - This attribute contains the source function, which can be voltage or current.

        Usage:
            - Accessing this property will send the ``print(smu.source.func)`` query.
            - Setting this property to a value will send the ``smu.source.func = value`` command.

        TSP Syntax:
            ```
            - smu.source.func = value
            - print(smu.source.func)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".func"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.func)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.func`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @func.setter
    def func(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.func`` attribute.

        Description:
            - This attribute contains the source function, which can be voltage or current.

        Usage:
            - Accessing this property will send the ``print(smu.source.func)`` query.
            - Setting this property to a value will send the ``smu.source.func = value`` command.

        TSP Syntax:
            ```
            - smu.source.func = value
            - print(smu.source.func)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".func", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.func = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.func`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def highc(self) -> str:
        """Access the ``smu.source.highc`` attribute.

        Description:
            - This attribute enables or disables high-capacitance mode.

        Usage:
            - Accessing this property will send the ``print(smu.source.highc)`` query.
            - Setting this property to a value will send the ``smu.source.highc = value`` command.

        TSP Syntax:
            ```
            - smu.source.highc = value
            - print(smu.source.highc)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".highc"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.highc)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.highc`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @highc.setter
    def highc(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.highc`` attribute.

        Description:
            - This attribute enables or disables high-capacitance mode.

        Usage:
            - Accessing this property will send the ``print(smu.source.highc)`` query.
            - Setting this property to a value will send the ``smu.source.highc = value`` command.

        TSP Syntax:
            ```
            - smu.source.highc = value
            - print(smu.source.highc)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".highc", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.highc = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.highc`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def level(self) -> str:
        """Access the ``smu.source.level`` attribute.

        Description:
            - This attribute immediately selects a fixed amplitude for the selected source function.

        Usage:
            - Accessing this property will send the ``print(smu.source.level)`` query.
            - Setting this property to a value will send the ``smu.source.level = value`` command.

        TSP Syntax:
            ```
            - smu.source.level = value
            - print(smu.source.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".level"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.level)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @level.setter
    def level(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.level`` attribute.

        Description:
            - This attribute immediately selects a fixed amplitude for the selected source function.

        Usage:
            - Accessing this property will send the ``print(smu.source.level)`` query.
            - Setting this property to a value will send the ``smu.source.level = value`` command.

        TSP Syntax:
            ```
            - smu.source.level = value
            - print(smu.source.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".level", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.level = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offmode(self) -> str:
        """Access the ``smu.source.offmode`` attribute.

        Description:
            - This attribute defines the state of the source when the output is turned off.

        Usage:
            - Accessing this property will send the ``print(smu.source.offmode)`` query.
            - Setting this property to a value will send the ``smu.source.offmode = value`` command.

        TSP Syntax:
            ```
            - smu.source.offmode = value
            - print(smu.source.offmode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".offmode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.offmode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offmode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @offmode.setter
    def offmode(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.offmode`` attribute.

        Description:
            - This attribute defines the state of the source when the output is turned off.

        Usage:
            - Accessing this property will send the ``print(smu.source.offmode)`` query.
            - Setting this property to a value will send the ``smu.source.offmode = value`` command.

        TSP Syntax:
            ```
            - smu.source.offmode = value
            - print(smu.source.offmode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".offmode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.offmode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offmode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def output(self) -> str:
        """Access the ``smu.source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(smu.source.output)`` query.
            - Setting this property to a value will send the ``smu.source.output = value`` command.

        TSP Syntax:
            ```
            - smu.source.output = value
            - print(smu.source.output)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".output"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.output)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.output`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @output.setter
    def output(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(smu.source.output)`` query.
            - Setting this property to a value will send the ``smu.source.output = value`` command.

        TSP Syntax:
            ```
            - smu.source.output = value
            - print(smu.source.output)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".output", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.output = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.output`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def protect(self) -> SmuSourceProtect:
        """Return the ``smu.source.protect`` command tree.

        Sub-properties and sub-methods:
            - ``.level``: The ``smu.source.protect.level`` attribute.
            - ``.tripped``: The ``smu.source.protect.tripped`` attribute.
        """
        return self._protect

    @property
    def range(self) -> str:
        """Access the ``smu.source.range`` attribute.

        Description:
            - This attribute selects the range for the source for the selected source function.

        Usage:
            - Accessing this property will send the ``print(smu.source.range)`` query.
            - Setting this property to a value will send the ``smu.source.range = value`` command.

        TSP Syntax:
            ```
            - smu.source.range = value
            - print(smu.source.range)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".range"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.range)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.range`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @range.setter
    def range(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.range`` attribute.

        Description:
            - This attribute selects the range for the source for the selected source function.

        Usage:
            - Accessing this property will send the ``print(smu.source.range)`` query.
            - Setting this property to a value will send the ``smu.source.range = value`` command.

        TSP Syntax:
            ```
            - smu.source.range = value
            - print(smu.source.range)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".range", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.range = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.range`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def readback(self) -> str:
        """Access the ``smu.source.readback`` attribute.

        Description:
            - This attribute determines if the instrument records the measured source value or the
              configured source value when making a measurement.

        Usage:
            - Accessing this property will send the ``print(smu.source.readback)`` query.
            - Setting this property to a value will send the ``smu.source.readback = value``
              command.

        TSP Syntax:
            ```
            - smu.source.readback = value
            - print(smu.source.readback)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".readback"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.readback)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.readback`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @readback.setter
    def readback(self, value: Union[str, float]) -> None:
        """Access the ``smu.source.readback`` attribute.

        Description:
            - This attribute determines if the instrument records the measured source value or the
              configured source value when making a measurement.

        Usage:
            - Accessing this property will send the ``print(smu.source.readback)`` query.
            - Setting this property to a value will send the ``smu.source.readback = value``
              command.

        TSP Syntax:
            ```
            - smu.source.readback = value
            - print(smu.source.readback)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".readback", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.readback = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.readback`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def userdelay(self) -> Dict[int, Union[str, float]]:
        """Access the ``smu.source.userdelay[N]`` attribute.

        Description:
            - This attribute sets a user-defined delay that you can use in the trigger model.

        Usage:
            - Accessing an item from this property will send the ``print(smu.source.userdelay[N])``
              query.
            - Setting an item from this property to a value will send the
              ``smu.source.userdelay[N] = value`` command.

        TSP Syntax:
            ```
            - smu.source.userdelay[N] = value
            - print(smu.source.userdelay[N])
            ```

        Info:
            - ``N``, the number that identifies this user delay (1 to 5).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._userdelay

    @property
    def ilimit(self) -> SmuSourceIlimit:
        """Return the ``smu.source.ilimit`` command tree.

        Sub-properties and sub-methods:
            - ``.level``: The ``smu.source.ilimit.level`` attribute.
            - ``.tripped``: The ``smu.source.ilimit.tripped`` attribute.
        """
        return self._ilimit

    @property
    def vlimit(self) -> SmuSourceVlimit:
        """Return the ``smu.source.vlimit`` command tree.

        Sub-properties and sub-methods:
            - ``.level``: The ``smu.source.vlimit.level`` attribute.
            - ``.tripped``: The ``smu.source.vlimit.tripped`` attribute.
        """
        return self._vlimit

    def getattribute(self, function: str, setting: str) -> str:
        """Run the ``smu.source.getattribute()`` function.

        Description:
            - This function returns the setting for a function attribute.

        TSP Syntax:
            ```
            - smu.source.getattribute()
            ```

        Args:
            function: The source function.
            setting: The setting of the attribute; refer to smu.source.setattribute() for the list
                of attributes.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getattribute({function}, {setting}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getattribute()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setattribute(self, function: str, setting: str, value: str) -> None:
        """Run the ``smu.source.setattribute()`` function.

        Description:
            - This function allows you to set up a source function whether or not the function is
              active.

        TSP Syntax:
            ```
            - smu.source.setattribute()
            ```

        Args:
            function: The source function; set to one of the following values.
            setting: The parameter to be set; see Details.
            value: The function or setting value.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setattribute({function}, {setting}, {value})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setattribute()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    # pylint: disable=too-many-arguments
    def sweeplinear(
        self,
        config_list_name: str,
        start: float,
        stop: float,
        points: int,
        s_delay: Optional[float] = None,
        count: Optional[int] = None,
        range_type: Optional[str] = None,
        fail_abort: Optional[str] = None,
        dual: Optional[str] = None,
        buffer_name: Optional[str] = None,
    ) -> None:
        """Run the ``smu.source.sweeplinear()`` function.

        Description:
            - This function sets up a linear sweep for a fixed number of measurement points.

        TSP Syntax:
            ```
            - smu.source.sweeplinear()
            ```

        Args:
            config_list_name: A string that contains the name of the configuration list that the
                instrument will create for this sweep.
            start: The voltage or current source level at which the sweep starts.
            stop: The voltage or current at which the sweep stops.
            points: The number of source-measure points between the start and stop values of the
                sweep (2 to 1e6); to calculate the number of source-measure points in a sweep, use
                the following formula.
            s_delay (optional): The delay between measurement points; default is smu.DELAY_AUTO,
                which enables autodelay, or a specific delay value from 50 µs to 10 ks, or 0 for no
                delay.
            count (optional): The number of times to run the sweep; default is 1.
            range_type (optional): The source range that is used for the sweep.
            fail_abort (optional): Complete the sweep if the source limit is exceeded.
            dual (optional): Determines if the sweep runs from start to stop and then from stop to
                start.
            buffer_name (optional): The name of a reading buffer; the default buffers (defbuffer1 or
                defbuffer2) or the name of a user-defined buffer; if no buffer is specified, this
                parameter defaults to defbuffer1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
                    start,
                    stop,
                    points,
                    s_delay,
                    count,
                    range_type,
                    fail_abort,
                    dual,
                    buffer_name,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.sweeplinear({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.sweeplinear()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    # pylint: disable=too-many-arguments
    def sweeplinearstep(
        self,
        config_list_name: str,
        start: float,
        stop: float,
        step: str,
        s_delay: Optional[float] = None,
        count: Optional[int] = None,
        range_type: Optional[str] = None,
        fail_abort: Optional[str] = None,
        dual: Optional[str] = None,
        buffer_name: Optional[str] = None,
    ) -> None:
        """Run the ``smu.source.sweeplinearstep()`` function.

        Description:
            - This function sets up a linear source sweep configuration list and trigger model with
              a fixed number of steps.

        TSP Syntax:
            ```
            - smu.source.sweeplinearstep()
            ```

        Args:
            config_list_name: A string that contains the name of the configuration list that the
                instrument will create for this sweep.
            start: The voltage or current source level at which the sweep starts.
            stop: The voltage or current at which the sweep stops.
            step: The step size at which the source level will change; must be more than 0.
            s_delay (optional): The delay between measurement points; default is smu.DELAY_AUTO,
                which enables autodelay, a specific delay value from 50 μs to 10 ks, or 0 for no
                delay.
            count (optional): The number of times to run the sweep; default is 1.
            range_type (optional): The source range that is used for the sweep.
            fail_abort (optional): Complete the sweep if the source limit is exceeded.
            dual (optional): Determines if the sweep runs from start to stop and then from stop to
                start.
            buffer_name (optional): The name of a reading buffer; the default buffers (defbuffer1 or
                defbuffer2) or the name of a user-defined buffer; if no buffer is specified, this
                parameter defaults to defbuffer1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
                    start,
                    stop,
                    step,
                    s_delay,
                    count,
                    range_type,
                    fail_abort,
                    dual,
                    buffer_name,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.sweeplinearstep({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.sweeplinearstep()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def sweeplist(
        self,
        config_list_name: str,
        index: Optional[int] = None,
        s_delay: Optional[float] = None,
        count: Optional[int] = None,
        fail_abort: Optional[str] = None,
        buffer_name: Optional[str] = None,
    ) -> None:
        """Run the ``smu.source.sweeplist()`` function.

        Description:
            - This function sets up a sweep based on a configuration list, which allows you to
              customize the sweep.

        TSP Syntax:
            ```
            - smu.source.sweeplist()
            ```

        Args:
            config_list_name: The name of the source configuration list that the sweep uses; this
                must be defined before sending this command.
            index (optional): The index in the configuration list where the sweep starts; default is
                1.
            s_delay (optional): The delay between measurement points; default is 0 for no delay or
                you can set a specific delay value from 50 ms to 10 ks.
            count (optional): The number of times to run the sweep; default is 1.
            fail_abort (optional): Complete the sweep if the source limit is exceeded.
            buffer_name (optional): The name of a reading buffer; the default buffers (defbuffer1 or
                defbuffer2) or the name of a user-defined buffer; if no buffer is specified, this
                parameter defaults to defbuffer1.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
                    index,
                    s_delay,
                    count,
                    fail_abort,
                    buffer_name,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.sweeplist({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.sweeplist()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    # pylint: disable=too-many-arguments
    def sweeplog(
        self,
        config_list_name: str,
        start: float,
        stop: float,
        points: int,
        s_delay: Optional[float] = None,
        count: Optional[int] = None,
        range_type: Optional[str] = None,
        fail_abort: Optional[str] = None,
        dual: Optional[str] = None,
        buffer_name: Optional[str] = None,
        asymptote: Optional[str] = None,
    ) -> None:
        """Run the ``smu.source.sweeplog()`` function.

        Description:
            - This function sets up a logarithmic sweep for a set number of measurement points.

        TSP Syntax:
            ```
            - smu.source.sweeplog()
            ```

        Args:
            config_list_name: A string that contains the name of the configuration list that the
                instrument will create for this sweep.
            start: The voltage or current source level at which the sweep starts.
            stop: The voltage or current at which the sweep stops.
            points: The number of source-measure points between the start and stop values of the
                sweep (2 to 1e6); to calculate the number of source-measure points in a sweep, use
                the following formula.
            s_delay (optional): The delay between measurement points; default is smu.DELAY_AUTO,
                which enables autodelay, or a specific delay value from 50 μs to 10 ks, or 0 for no
                delay.
            count (optional): The number of times to run the sweep; default is 1.
            range_type (optional): The source range that is used for the sweep.
            fail_abort (optional): Complete the sweep if the source limit is exceeded.
            dual (optional): Determines if the sweep runs from start to stop and then from stop to
                start.
            buffer_name (optional): The name of a reading buffer; the default buffers (defbuffer1 or
                defbuffer2) or the name of a user-defined buffer; if no buffer is specified, this
                parameter defaults to defbuffer1.
            asymptote (optional): Default is 0; see Details.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
                    start,
                    stop,
                    points,
                    s_delay,
                    count,
                    range_type,
                    fail_abort,
                    dual,
                    buffer_name,
                    asymptote,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.sweeplog({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.sweeplog()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuMeasureRel(BaseTSPCmd):
    """The ``smu.measure.rel`` command tree.

    Properties and methods:
        - ``.acquire()``: The ``smu.measure.rel.acquire()`` function.
        - ``.enable``: The ``smu.measure.rel.enable`` attribute.
        - ``.level``: The ``smu.measure.rel.level`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``smu.measure.rel.enable`` attribute.

        Description:
            - This attribute enables or disables the application of a relative offset value to the
              measurement.

        Usage:
            - Accessing this property will send the ``print(smu.measure.rel.enable)`` query.
            - Setting this property to a value will send the ``smu.measure.rel.enable = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.rel.enable = value
            - print(smu.measure.rel.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.rel.enable`` attribute.

        Description:
            - This attribute enables or disables the application of a relative offset value to the
              measurement.

        Usage:
            - Accessing this property will send the ``print(smu.measure.rel.enable)`` query.
            - Setting this property to a value will send the ``smu.measure.rel.enable = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.rel.enable = value
            - print(smu.measure.rel.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def level(self) -> str:
        """Access the ``smu.measure.rel.level`` attribute.

        Description:
            - This attribute contains the relative offset value.

        Usage:
            - Accessing this property will send the ``print(smu.measure.rel.level)`` query.
            - Setting this property to a value will send the ``smu.measure.rel.level = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.rel.level = value
            - print(smu.measure.rel.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".level"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.level)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @level.setter
    def level(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.rel.level`` attribute.

        Description:
            - This attribute contains the relative offset value.

        Usage:
            - Accessing this property will send the ``print(smu.measure.rel.level)`` query.
            - Setting this property to a value will send the ``smu.measure.rel.level = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.rel.level = value
            - print(smu.measure.rel.level)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".level", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.level = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.level`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def acquire(self) -> str:
        """Run the ``smu.measure.rel.acquire()`` function.

        Description:
            - This function acquires a measurement and stores it as the relative offset value.

        TSP Syntax:
            ```
            - smu.measure.rel.acquire()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.acquire())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.acquire()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuMeasureMathMxb(BaseTSPCmd):
    """The ``smu.measure.math.mxb`` command tree.

    Properties and methods:
        - ``.bfactor``: The ``smu.measure.math.mxb.bfactor`` attribute.
        - ``.mfactor``: The ``smu.measure.math.mxb.mfactor`` attribute.
    """

    @property
    def bfactor(self) -> str:
        """Access the ``smu.measure.math.mxb.bfactor`` attribute.

        Description:
            - This attribute specifies the offset, b, for the y = mx + b operation.

        Usage:
            - Accessing this property will send the ``print(smu.measure.math.mxb.bfactor)`` query.
            - Setting this property to a value will send the
              ``smu.measure.math.mxb.bfactor = value`` command.

        TSP Syntax:
            ```
            - smu.measure.math.mxb.bfactor = value
            - print(smu.measure.math.mxb.bfactor)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".bfactor"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.bfactor)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.bfactor`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @bfactor.setter
    def bfactor(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.math.mxb.bfactor`` attribute.

        Description:
            - This attribute specifies the offset, b, for the y = mx + b operation.

        Usage:
            - Accessing this property will send the ``print(smu.measure.math.mxb.bfactor)`` query.
            - Setting this property to a value will send the
              ``smu.measure.math.mxb.bfactor = value`` command.

        TSP Syntax:
            ```
            - smu.measure.math.mxb.bfactor = value
            - print(smu.measure.math.mxb.bfactor)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".bfactor", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.bfactor = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.bfactor`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def mfactor(self) -> str:
        """Access the ``smu.measure.math.mxb.mfactor`` attribute.

        Description:
            - This attribute specifies the scale factor, m, for the y = mx + b math operation.

        Usage:
            - Accessing this property will send the ``print(smu.measure.math.mxb.mfactor)`` query.
            - Setting this property to a value will send the
              ``smu.measure.math.mxb.mfactor = value`` command.

        TSP Syntax:
            ```
            - smu.measure.math.mxb.mfactor = value
            - print(smu.measure.math.mxb.mfactor)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".mfactor"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.mfactor)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mfactor`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @mfactor.setter
    def mfactor(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.math.mxb.mfactor`` attribute.

        Description:
            - This attribute specifies the scale factor, m, for the y = mx + b math operation.

        Usage:
            - Accessing this property will send the ``print(smu.measure.math.mxb.mfactor)`` query.
            - Setting this property to a value will send the
              ``smu.measure.math.mxb.mfactor = value`` command.

        TSP Syntax:
            ```
            - smu.measure.math.mxb.mfactor = value
            - print(smu.measure.math.mxb.mfactor)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".mfactor", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.mfactor = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mfactor`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuMeasureMath(BaseTSPCmd):
    """The ``smu.measure.math`` command tree.

    Properties and methods:
        - ``.enable``: The ``smu.measure.math.enable`` attribute.
        - ``.format``: The ``smu.measure.math.format`` attribute.
        - ``.mxb``: The ``smu.measure.math.mxb`` command tree.
        - ``.percent``: The ``smu.measure.math.percent`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mxb = SmuMeasureMathMxb(device, f"{self._cmd_syntax}.mxb")

    @property
    def enable(self) -> str:
        """Access the ``smu.measure.math.enable`` attribute.

        Description:
            - This attribute enables or disables math operations on measurements for the selected
              measurement function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.math.enable)`` query.
            - Setting this property to a value will send the ``smu.measure.math.enable = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.math.enable = value
            - print(smu.measure.math.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.math.enable`` attribute.

        Description:
            - This attribute enables or disables math operations on measurements for the selected
              measurement function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.math.enable)`` query.
            - Setting this property to a value will send the ``smu.measure.math.enable = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.math.enable = value
            - print(smu.measure.math.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def format(self) -> str:
        """Access the ``smu.measure.math.format`` attribute.

        Description:
            - This attribute specifies which math operation is performed on measurements when math
              operations are enabled.

        Usage:
            - Accessing this property will send the ``print(smu.measure.math.format)`` query.
            - Setting this property to a value will send the ``smu.measure.math.format = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.math.format = value
            - print(smu.measure.math.format)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".format"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.format)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.format`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @format.setter
    def format(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.math.format`` attribute.

        Description:
            - This attribute specifies which math operation is performed on measurements when math
              operations are enabled.

        Usage:
            - Accessing this property will send the ``print(smu.measure.math.format)`` query.
            - Setting this property to a value will send the ``smu.measure.math.format = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.math.format = value
            - print(smu.measure.math.format)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".format", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.format = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.format`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def mxb(self) -> SmuMeasureMathMxb:
        """Return the ``smu.measure.math.mxb`` command tree.

        Sub-properties and sub-methods:
            - ``.bfactor``: The ``smu.measure.math.mxb.bfactor`` attribute.
            - ``.mfactor``: The ``smu.measure.math.mxb.mfactor`` attribute.
        """
        return self._mxb

    @property
    def percent(self) -> str:
        """Access the ``smu.measure.math.percent`` attribute.

        Description:
            - This attribute specifies the reference constant that is used when math operations are
              set to percent.

        Usage:
            - Accessing this property will send the ``print(smu.measure.math.percent)`` query.
            - Setting this property to a value will send the ``smu.measure.math.percent = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.math.percent = value
            - print(smu.measure.math.percent)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".percent"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.percent)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.percent`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @percent.setter
    def percent(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.math.percent`` attribute.

        Description:
            - This attribute specifies the reference constant that is used when math operations are
              set to percent.

        Usage:
            - Accessing this property will send the ``print(smu.measure.math.percent)`` query.
            - Setting this property to a value will send the ``smu.measure.math.percent = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.math.percent = value
            - print(smu.measure.math.percent)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".percent", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.percent = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.percent`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuMeasureLimitItemLow(BaseTSPCmd):
    """The ``smu.measure.limit[r].low`` command tree.

    Properties and methods:
        - ``.value``: The ``smu.measure.limit[r].low.value`` attribute.
    """

    @property
    def value(self) -> str:
        """Access the ``smu.measure.limit[r].low.value`` attribute.

        Description:
            - This attribute specifies the lower limit for a limit test. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu.measure.limit[r].low.value)`` query.
            - Setting this property to a value will send the
              ``smu.measure.limit[r].low.value = value`` command.

        TSP Syntax:
            ```
            - smu.measure.limit[r].low.value = value
            - print(smu.measure.limit[r].low.value)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".value"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.value)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.value`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @value.setter
    def value(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.limit[r].low.value`` attribute.

        Description:
            - This attribute specifies the lower limit for a limit test. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu.measure.limit[r].low.value)`` query.
            - Setting this property to a value will send the
              ``smu.measure.limit[r].low.value = value`` command.

        TSP Syntax:
            ```
            - smu.measure.limit[r].low.value = value
            - print(smu.measure.limit[r].low.value)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".value", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.value = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.value`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuMeasureLimitItemHigh(BaseTSPCmd):
    """The ``smu.measure.limit[r].high`` command tree.

    Properties and methods:
        - ``.value``: The ``smu.measure.limit[r].high.value`` attribute.
    """

    @property
    def value(self) -> str:
        """Access the ``smu.measure.limit[r].high.value`` attribute.

        Description:
            - This attribute specifies the upper limit for a limit test. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu.measure.limit[r].high.value)``
              query.
            - Setting this property to a value will send the
              ``smu.measure.limit[r].high.value = value`` command.

        TSP Syntax:
            ```
            - smu.measure.limit[r].high.value = value
            - print(smu.measure.limit[r].high.value)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".value"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.value)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.value`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @value.setter
    def value(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.limit[r].high.value`` attribute.

        Description:
            - This attribute specifies the upper limit for a limit test. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu.measure.limit[r].high.value)``
              query.
            - Setting this property to a value will send the
              ``smu.measure.limit[r].high.value = value`` command.

        TSP Syntax:
            ```
            - smu.measure.limit[r].high.value = value
            - print(smu.measure.limit[r].high.value)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".value", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.value = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.value`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuMeasureLimitItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``smu.measure.limit[r]`` command tree.

    Properties and methods:
        - ``.audible``: The ``smu.measure.limit[r].audible`` attribute.
        - ``.autoclear``: The ``smu.measure.limit[r].autoclear`` attribute.
        - ``.clear()``: The ``smu.measure.limit[r].clear()`` function.
        - ``.enable``: The ``smu.measure.limit[r].enable`` attribute.
        - ``.fail``: The ``smu.measure.limit[r].fail`` attribute.
        - ``.high``: The ``smu.measure.limit[r].high`` command tree.
        - ``.low``: The ``smu.measure.limit[r].low`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = SmuMeasureLimitItemHigh(device, f"{self._cmd_syntax}.high")
        self._low = SmuMeasureLimitItemLow(device, f"{self._cmd_syntax}.low")

    @property
    def audible(self) -> str:
        """Access the ``smu.measure.limit[r].audible`` attribute.

        Description:
            - This attribute determines if the instrument beeper sounds when a limit test passes or
              fails. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu.measure.limit[r].audible)`` query.
            - Setting this property to a value will send the
              ``smu.measure.limit[r].audible = value`` command.

        TSP Syntax:
            ```
            - smu.measure.limit[r].audible = value
            - print(smu.measure.limit[r].audible)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".audible"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.audible)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.audible`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @audible.setter
    def audible(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.limit[r].audible`` attribute.

        Description:
            - This attribute determines if the instrument beeper sounds when a limit test passes or
              fails. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu.measure.limit[r].audible)`` query.
            - Setting this property to a value will send the
              ``smu.measure.limit[r].audible = value`` command.

        TSP Syntax:
            ```
            - smu.measure.limit[r].audible = value
            - print(smu.measure.limit[r].audible)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".audible", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.audible = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.audible`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autoclear(self) -> str:
        """Access the ``smu.measure.limit[r].autoclear`` attribute.

        Description:
            - This attribute indicates if the test result for limit Y should be cleared
              automatically or not. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu.measure.limit[r].autoclear)`` query.
            - Setting this property to a value will send the
              ``smu.measure.limit[r].autoclear = value`` command.

        TSP Syntax:
            ```
            - smu.measure.limit[r].autoclear = value
            - print(smu.measure.limit[r].autoclear)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autoclear"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autoclear)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autoclear`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autoclear.setter
    def autoclear(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.limit[r].autoclear`` attribute.

        Description:
            - This attribute indicates if the test result for limit Y should be cleared
              automatically or not. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu.measure.limit[r].autoclear)`` query.
            - Setting this property to a value will send the
              ``smu.measure.limit[r].autoclear = value`` command.

        TSP Syntax:
            ```
            - smu.measure.limit[r].autoclear = value
            - print(smu.measure.limit[r].autoclear)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autoclear", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autoclear = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autoclear`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``smu.measure.limit[r].enable`` attribute.

        Description:
            - This attribute enables or disables a limit test on the measurement from the selected
              measure function. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu.measure.limit[r].enable)`` query.
            - Setting this property to a value will send the ``smu.measure.limit[r].enable = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.limit[r].enable = value
            - print(smu.measure.limit[r].enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.limit[r].enable`` attribute.

        Description:
            - This attribute enables or disables a limit test on the measurement from the selected
              measure function. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu.measure.limit[r].enable)`` query.
            - Setting this property to a value will send the ``smu.measure.limit[r].enable = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.limit[r].enable = value
            - print(smu.measure.limit[r].enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def fail(self) -> str:
        """Access the ``smu.measure.limit[r].fail`` attribute.

        Description:
            - This attribute queries the results of a limit test. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(smu.measure.limit[r].fail)`` query.

        TSP Syntax:
            ```
            - print(smu.measure.limit[r].fail)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".fail"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.fail)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.fail`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def high(self) -> SmuMeasureLimitItemHigh:
        """Return the ``smu.measure.limit[r].high`` command tree.

        Sub-properties and sub-methods:
            - ``.value``: The ``smu.measure.limit[r].high.value`` attribute.
        """
        return self._high

    @property
    def low(self) -> SmuMeasureLimitItemLow:
        """Return the ``smu.measure.limit[r].low`` command tree.

        Sub-properties and sub-methods:
            - ``.value``: The ``smu.measure.limit[r].low.value`` attribute.
        """
        return self._low

    def clear(self) -> None:
        """Run the ``smu.measure.limit[r].clear()`` function.

        Description:
            - This function clears the results of the limit test defined by Y for the selected
              measurement function. (r = resistance in ohms)

        TSP Syntax:
            ```
            - smu.measure.limit[r].clear()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.clear()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.clear()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuMeasureFilter(BaseTSPCmd):
    """The ``smu.measure.filter`` command tree.

    Properties and methods:
        - ``.count``: The ``smu.measure.filter.count`` attribute.
        - ``.enable``: The ``smu.measure.filter.enable`` attribute.
        - ``.type``: The ``smu.measure.filter.type`` attribute.
    """

    @property
    def count(self) -> str:
        """Access the ``smu.measure.filter.count`` attribute.

        Description:
            - This attribute sets the number of measurements that are averaged when filtering is
              enabled.

        Usage:
            - Accessing this property will send the ``print(smu.measure.filter.count)`` query.
            - Setting this property to a value will send the ``smu.measure.filter.count = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.filter.count = value
            - print(smu.measure.filter.count)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".count"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.count)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @count.setter
    def count(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.filter.count`` attribute.

        Description:
            - This attribute sets the number of measurements that are averaged when filtering is
              enabled.

        Usage:
            - Accessing this property will send the ``print(smu.measure.filter.count)`` query.
            - Setting this property to a value will send the ``smu.measure.filter.count = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.filter.count = value
            - print(smu.measure.filter.count)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".count", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.count = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``smu.measure.filter.enable`` attribute.

        Description:
            - This attribute enables or disables the averaging filter for the selected measurement
              function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.filter.enable)`` query.
            - Setting this property to a value will send the ``smu.measure.filter.enable = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.filter.enable = value
            - print(smu.measure.filter.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.filter.enable`` attribute.

        Description:
            - This attribute enables or disables the averaging filter for the selected measurement
              function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.filter.enable)`` query.
            - Setting this property to a value will send the ``smu.measure.filter.enable = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.filter.enable = value
            - print(smu.measure.filter.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def type(self) -> str:
        """Access the ``smu.measure.filter.type`` attribute.

        Description:
            - This attribute sets the type of averaging filter that is used for the selected measure
              function when the measurement filter is enabled.

        Usage:
            - Accessing this property will send the ``print(smu.measure.filter.type)`` query.
            - Setting this property to a value will send the ``smu.measure.filter.type = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.filter.type = value
            - print(smu.measure.filter.type)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".type"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.type)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.type`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @type.setter
    def type(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.filter.type`` attribute.

        Description:
            - This attribute sets the type of averaging filter that is used for the selected measure
              function when the measurement filter is enabled.

        Usage:
            - Accessing this property will send the ``print(smu.measure.filter.type)`` query.
            - Setting this property to a value will send the ``smu.measure.filter.type = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.filter.type = value
            - print(smu.measure.filter.type)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".type", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.type = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.type`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuMeasureConfiglist(BaseTSPCmd):
    """The ``smu.measure.configlist`` command tree.

    Properties and methods:
        - ``.catalog()``: The ``smu.measure.configlist.catalog()`` function.
        - ``.create()``: The ``smu.measure.configlist.create()`` function.
        - ``.delete()``: The ``smu.measure.configlist.delete()`` function.
        - ``.query()``: The ``smu.measure.configlist.query()`` function.
        - ``.recall()``: The ``smu.measure.configlist.recall()`` function.
        - ``.size()``: The ``smu.measure.configlist.size()`` function.
        - ``.store()``: The ``smu.measure.configlist.store()`` function.
        - ``.storefunc()``: The ``smu.measure.configlist.storefunc()`` function.
    """

    def catalog(self) -> str:
        """Run the ``smu.measure.configlist.catalog()`` function.

        Description:
            - This function returns the name of one measure configuration list that is stored on the
              instrument.

        TSP Syntax:
            ```
            - smu.measure.configlist.catalog()
            ```

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.catalog())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.catalog()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def create(self, list_name: str) -> None:
        """Run the ``smu.measure.configlist.create()`` function.

        Description:
            - This function creates an empty measure configuration list.

        TSP Syntax:
            ```
            - smu.measure.configlist.create()
            ```

        Args:
            list_name: A string that represents the name of a measure configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.create("{list_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.create()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def delete(self, list_name: str, index: Optional[int] = None) -> None:
        """Run the ``smu.measure.configlist.delete()`` function.

        Description:
            - This function deletes a measure configuration list.

        TSP Syntax:
            ```
            - smu.measure.configlist.delete()
            ```

        Args:
            list_name: A string that represents the name of a measure configuration list.
            index (optional): A number that defines a specific configuration index in the
                configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{list_name}"',
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.delete({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.delete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def query(self, list_name: str, index: int, field_separator: Optional[str] = None) -> str:
        """Run the ``smu.measure.configlist.query()`` function.

        Description:
            - This function returns a list of TSP commands and parameter settings that are stored in
              the specified configuration index.

        TSP Syntax:
            ```
            - smu.measure.configlist.query()
            ```

        Args:
            list_name: A string that represents the name of a measure configuration list.
            index: A number that defines a specific configuration index in the configuration list.
            field_separator (optional): String that represents the separator for the data; use one
                of the following.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{list_name}"',
                    index,
                    f'"{field_separator}"' if field_separator is not None else None,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.query({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.query()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def recall(
        self,
        list_name: str,
        index: Optional[int] = None,
        source_list_name: Optional[str] = None,
        source_index: Optional[int] = None,
    ) -> None:
        """Run the ``smu.measure.configlist.recall()`` function.

        Description:
            - This function recalls a configuration index in a measure configuration list and an
              optional source configuration list.

        TSP Syntax:
            ```
            - smu.measure.configlist.recall()
            ```

        Args:
            list_name: A string that represents the name of a measure configuration list.
            index (optional): A number that defines a specific configuration index in the measure
                configuration list.
            source_list_name (optional): A string that represents the name of a source configuration
                list.
            source_index (optional): A number that defines a specific configuration index in the
                source configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{list_name}"',
                    index,
                    f'"{source_list_name}"' if source_list_name is not None else None,
                    source_index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.recall({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.recall()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def size(self, list_name: str) -> str:
        """Run the ``smu.measure.configlist.size()`` function.

        Description:
            - This function returns the size (number of configuration indexes) of a measure
              configuration list.

        TSP Syntax:
            ```
            - smu.measure.configlist.size()
            ```

        Args:
            list_name: A string that represents the name of a measure configuration list.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.size("{list_name}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.size()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def store(self, list_name: str, index: Optional[int] = None) -> None:
        """Run the ``smu.measure.configlist.store()`` function.

        Description:
            - This function stores the active measure or digitize settings into the named
              configuration list.

        TSP Syntax:
            ```
            - smu.measure.configlist.store()
            ```

        Args:
            list_name: A string that represents the name of a measure configuration list.
            index (optional): A number that defines a specific configuration index in the
                configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{list_name}"',
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.store({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.store()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def storefunc(self, list_name: str, function: str, index: Optional[int] = None) -> None:
        """Run the ``smu.measure.configlist.storefunc()`` function.

        Description:
            - This function allows you to store the settings for a measure function into a measure
              configuration list whether or not the function is active.

        TSP Syntax:
            ```
            - smu.measure.configlist.storefunc()
            ```

        Args:
            list_name: Name of the configuration list in which to store the function settings.
            function: The measure function settings to save into the configuration list.
            index (optional): The number of the configuration list index in which to store the
                settings.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{list_name}"',
                    function,
                    index,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.storefunc({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.storefunc()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuMeasureAutozero(BaseTSPCmd):
    """The ``smu.measure.autozero`` command tree.

    Properties and methods:
        - ``.enable``: The ``smu.measure.autozero.enable`` attribute.
        - ``.once()``: The ``smu.measure.autozero.once()`` function.
    """

    @property
    def enable(self) -> str:
        """Access the ``smu.measure.autozero.enable`` attribute.

        Description:
            - This attribute enables or disables automatic updates to the internal reference
              measurements (autozero) of the instrument.

        Usage:
            - Accessing this property will send the ``print(smu.measure.autozero.enable)`` query.
            - Setting this property to a value will send the ``smu.measure.autozero.enable = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.autozero.enable = value
            - print(smu.measure.autozero.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.autozero.enable`` attribute.

        Description:
            - This attribute enables or disables automatic updates to the internal reference
              measurements (autozero) of the instrument.

        Usage:
            - Accessing this property will send the ``print(smu.measure.autozero.enable)`` query.
            - Setting this property to a value will send the ``smu.measure.autozero.enable = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.autozero.enable = value
            - print(smu.measure.autozero.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def once(self) -> None:
        """Run the ``smu.measure.autozero.once()`` function.

        Description:
            - This function causes the instrument to refresh the reference and zero measurements
              once.

        TSP Syntax:
            ```
            - smu.measure.autozero.once()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.once()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.once()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


#  pylint: disable=too-many-public-methods
class SmuMeasure(BaseTSPCmd):
    """The ``smu.measure`` command tree.

    Properties and methods:
        - ``.autorange``: The ``smu.measure.autorange`` attribute.
        - ``.autorangehigh``: The ``smu.measure.autorangehigh`` attribute.
        - ``.autorangelow``: The ``smu.measure.autorangelow`` attribute.
        - ``.autorangerebound``: The ``smu.measure.autorangerebound`` attribute.
        - ``.autozero``: The ``smu.measure.autozero`` command tree.
        - ``.configlist``: The ``smu.measure.configlist`` command tree.
        - ``.count``: The ``smu.measure.count`` attribute.
        - ``.displaydigits``: The ``smu.measure.displaydigits`` attribute.
        - ``.filter``: The ``smu.measure.filter`` command tree.
        - ``.func``: The ``smu.measure.func`` attribute.
        - ``.getattribute()``: The ``smu.measure.getattribute()`` function.
        - ``.limit``: The ``smu.measure.limit[r]`` command tree.
        - ``.math``: The ``smu.measure.math`` command tree.
        - ``.nplc``: The ``smu.measure.nplc`` attribute.
        - ``.offsetcompensation``: The ``smu.measure.offsetcompensation`` attribute.
        - ``.range``: The ``smu.measure.range`` attribute.
        - ``.read()``: The ``smu.measure.read()`` function.
        - ``.readwithtime()``: The ``smu.measure.readwithtime()`` function.
        - ``.rel``: The ``smu.measure.rel`` command tree.
        - ``.sense``: The ``smu.measure.sense`` attribute.
        - ``.setattribute()``: The ``smu.measure.setattribute()`` function.
        - ``.unit``: The ``smu.measure.unit`` attribute.
        - ``.userdelay``: The ``smu.measure.userdelay[N]`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._autozero = SmuMeasureAutozero(device, f"{self._cmd_syntax}.autozero")
        self._configlist = SmuMeasureConfiglist(device, f"{self._cmd_syntax}.configlist")
        self._filter = SmuMeasureFilter(device, f"{self._cmd_syntax}.filter")
        self._limit: Dict[int, SmuMeasureLimitItem] = DefaultDictPassKeyToFactory(
            lambda x: SmuMeasureLimitItem(device, f"{self._cmd_syntax}.limit[{x}]")
        )
        self._math = SmuMeasureMath(device, f"{self._cmd_syntax}.math")
        self._rel = SmuMeasureRel(device, f"{self._cmd_syntax}.rel")
        self._userdelay: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.userdelay[{{key}}]",
            write_syntax=f"{self._cmd_syntax}.userdelay[{{key}}] = ",
            query_syntax=f"print({self._cmd_syntax}.userdelay[{{key}}])",
            device=self._device,
        )

    @property
    def autorange(self) -> str:
        """Access the ``smu.measure.autorange`` attribute.

        Description:
            - This attribute determines if the measurement range is set manually or automatically
              for the selected measure function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.autorange)`` query.
            - Setting this property to a value will send the ``smu.measure.autorange = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.autorange = value
            - print(smu.measure.autorange)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autorange"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autorange)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorange`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autorange.setter
    def autorange(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.autorange`` attribute.

        Description:
            - This attribute determines if the measurement range is set manually or automatically
              for the selected measure function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.autorange)`` query.
            - Setting this property to a value will send the ``smu.measure.autorange = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.autorange = value
            - print(smu.measure.autorange)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autorange", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autorange = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorange`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autorangehigh(self) -> str:
        """Access the ``smu.measure.autorangehigh`` attribute.

        Description:
            - When autorange is selected, this attribute represents the highest measurement range
              that is used when the instrument selects the measurement range automatically.

        Usage:
            - Accessing this property will send the ``print(smu.measure.autorangehigh)`` query.
            - Setting this property to a value will send the ``smu.measure.autorangehigh = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.autorangehigh = value
            - print(smu.measure.autorangehigh)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autorangehigh"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autorangehigh)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangehigh`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autorangehigh.setter
    def autorangehigh(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.autorangehigh`` attribute.

        Description:
            - When autorange is selected, this attribute represents the highest measurement range
              that is used when the instrument selects the measurement range automatically.

        Usage:
            - Accessing this property will send the ``print(smu.measure.autorangehigh)`` query.
            - Setting this property to a value will send the ``smu.measure.autorangehigh = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.autorangehigh = value
            - print(smu.measure.autorangehigh)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autorangehigh", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autorangehigh = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangehigh`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autorangelow(self) -> str:
        """Access the ``smu.measure.autorangelow`` attribute.

        Description:
            - This attribute selects the lower limit for measurements of the selected function when
              the range is selected automatically.

        Usage:
            - Accessing this property will send the ``print(smu.measure.autorangelow)`` query.
            - Setting this property to a value will send the ``smu.measure.autorangelow = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.autorangelow = value
            - print(smu.measure.autorangelow)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autorangelow"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autorangelow)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangelow`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autorangelow.setter
    def autorangelow(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.autorangelow`` attribute.

        Description:
            - This attribute selects the lower limit for measurements of the selected function when
              the range is selected automatically.

        Usage:
            - Accessing this property will send the ``print(smu.measure.autorangelow)`` query.
            - Setting this property to a value will send the ``smu.measure.autorangelow = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.autorangelow = value
            - print(smu.measure.autorangelow)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autorangelow", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autorangelow = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangelow`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autorangerebound(self) -> str:
        """Access the ``smu.measure.autorangerebound`` attribute.

        Description:
            - This attribute determines if the instrument restores the measure range to match the
              limit range after making a measurement.

        Usage:
            - Accessing this property will send the ``print(smu.measure.autorangerebound)`` query.
            - Setting this property to a value will send the
              ``smu.measure.autorangerebound = value`` command.

        TSP Syntax:
            ```
            - smu.measure.autorangerebound = value
            - print(smu.measure.autorangerebound)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autorangerebound"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autorangerebound)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangerebound`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autorangerebound.setter
    def autorangerebound(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.autorangerebound`` attribute.

        Description:
            - This attribute determines if the instrument restores the measure range to match the
              limit range after making a measurement.

        Usage:
            - Accessing this property will send the ``print(smu.measure.autorangerebound)`` query.
            - Setting this property to a value will send the
              ``smu.measure.autorangerebound = value`` command.

        TSP Syntax:
            ```
            - smu.measure.autorangerebound = value
            - print(smu.measure.autorangerebound)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autorangerebound", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autorangerebound = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autorangerebound`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autozero(self) -> SmuMeasureAutozero:
        """Return the ``smu.measure.autozero`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``smu.measure.autozero.enable`` attribute.
            - ``.once()``: The ``smu.measure.autozero.once()`` function.
        """
        return self._autozero

    @property
    def configlist(self) -> SmuMeasureConfiglist:
        """Return the ``smu.measure.configlist`` command tree.

        Sub-properties and sub-methods:
            - ``.catalog()``: The ``smu.measure.configlist.catalog()`` function.
            - ``.create()``: The ``smu.measure.configlist.create()`` function.
            - ``.delete()``: The ``smu.measure.configlist.delete()`` function.
            - ``.query()``: The ``smu.measure.configlist.query()`` function.
            - ``.recall()``: The ``smu.measure.configlist.recall()`` function.
            - ``.size()``: The ``smu.measure.configlist.size()`` function.
            - ``.store()``: The ``smu.measure.configlist.store()`` function.
            - ``.storefunc()``: The ``smu.measure.configlist.storefunc()`` function.
        """
        return self._configlist

    @property
    def count(self) -> str:
        """Access the ``smu.measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements to make when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(smu.measure.count)`` query.
            - Setting this property to a value will send the ``smu.measure.count = value`` command.

        TSP Syntax:
            ```
            - smu.measure.count = value
            - print(smu.measure.count)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".count"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.count)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @count.setter
    def count(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements to make when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(smu.measure.count)`` query.
            - Setting this property to a value will send the ``smu.measure.count = value`` command.

        TSP Syntax:
            ```
            - smu.measure.count = value
            - print(smu.measure.count)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".count", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.count = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.count`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def displaydigits(self) -> str:
        """Access the ``smu.measure.displaydigits`` attribute.

        Description:
            - This attribute determines the number of digits that are displayed for measurements on
              the front panel for the selected function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.displaydigits)`` query.
            - Setting this property to a value will send the ``smu.measure.displaydigits = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.displaydigits = value
            - print(smu.measure.displaydigits)
            ```

        Info:
            - ``digits``, the 6½ display digits: smu.DIGITS_6_5
              5½ display digits: smu.DIGITS_5_5
              4½ display digits: smu.DIGITS_4_5
              3½ display digits: smu.DIGITS_3_5.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".displaydigits"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.displaydigits)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.displaydigits`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @displaydigits.setter
    def displaydigits(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.displaydigits`` attribute.

        Description:
            - This attribute determines the number of digits that are displayed for measurements on
              the front panel for the selected function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.displaydigits)`` query.
            - Setting this property to a value will send the ``smu.measure.displaydigits = value``
              command.

        TSP Syntax:
            ```
            - smu.measure.displaydigits = value
            - print(smu.measure.displaydigits)
            ```

        Info:
            - ``digits``, the 6½ display digits: smu.DIGITS_6_5
              5½ display digits: smu.DIGITS_5_5
              4½ display digits: smu.DIGITS_4_5
              3½ display digits: smu.DIGITS_3_5.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".displaydigits", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.displaydigits = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.displaydigits`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def filter(self) -> SmuMeasureFilter:
        """Return the ``smu.measure.filter`` command tree.

        Sub-properties and sub-methods:
            - ``.count``: The ``smu.measure.filter.count`` attribute.
            - ``.enable``: The ``smu.measure.filter.enable`` attribute.
            - ``.type``: The ``smu.measure.filter.type`` attribute.
        """
        return self._filter

    @property
    def func(self) -> str:
        """Access the ``smu.measure.func`` attribute.

        Description:
            - This attribute selects the active measure function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.func)`` query.
            - Setting this property to a value will send the ``smu.measure.func = value`` command.

        TSP Syntax:
            ```
            - smu.measure.func = value
            - print(smu.measure.func)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".func"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.func)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.func`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @func.setter
    def func(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.func`` attribute.

        Description:
            - This attribute selects the active measure function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.func)`` query.
            - Setting this property to a value will send the ``smu.measure.func = value`` command.

        TSP Syntax:
            ```
            - smu.measure.func = value
            - print(smu.measure.func)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".func", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.func = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.func`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limit(self) -> Dict[int, SmuMeasureLimitItem]:
        """Return the ``smu.measure.limit[r]`` command tree.

        Sub-properties and sub-methods:
            - ``.audible``: The ``smu.measure.limit[r].audible`` attribute.
            - ``.autoclear``: The ``smu.measure.limit[r].autoclear`` attribute.
            - ``.clear()``: The ``smu.measure.limit[r].clear()`` function.
            - ``.enable``: The ``smu.measure.limit[r].enable`` attribute.
            - ``.fail``: The ``smu.measure.limit[r].fail`` attribute.
            - ``.high``: The ``smu.measure.limit[r].high`` command tree.
            - ``.low``: The ``smu.measure.limit[r].low`` command tree.
        """
        return self._limit

    @property
    def math(self) -> SmuMeasureMath:
        """Return the ``smu.measure.math`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``smu.measure.math.enable`` attribute.
            - ``.format``: The ``smu.measure.math.format`` attribute.
            - ``.mxb``: The ``smu.measure.math.mxb`` command tree.
            - ``.percent``: The ``smu.measure.math.percent`` attribute.
        """
        return self._math

    @property
    def nplc(self) -> str:
        """Access the ``smu.measure.nplc`` attribute.

        Description:
            - This command sets the time that the input signal is measured for the selected
              function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.nplc)`` query.
            - Setting this property to a value will send the ``smu.measure.nplc = value`` command.

        TSP Syntax:
            ```
            - smu.measure.nplc = value
            - print(smu.measure.nplc)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".nplc"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.nplc)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.nplc`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @nplc.setter
    def nplc(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.nplc`` attribute.

        Description:
            - This command sets the time that the input signal is measured for the selected
              function.

        Usage:
            - Accessing this property will send the ``print(smu.measure.nplc)`` query.
            - Setting this property to a value will send the ``smu.measure.nplc = value`` command.

        TSP Syntax:
            ```
            - smu.measure.nplc = value
            - print(smu.measure.nplc)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".nplc", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.nplc = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.nplc`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offsetcompensation(self) -> str:
        """Access the ``smu.measure.offsetcompensation`` attribute.

        Description:
            - This attribute determines if offset compensation is used.

        Usage:
            - Accessing this property will send the ``print(smu.measure.offsetcompensation)`` query.
            - Setting this property to a value will send the
              ``smu.measure.offsetcompensation = value`` command.

        TSP Syntax:
            ```
            - smu.measure.offsetcompensation = value
            - print(smu.measure.offsetcompensation)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".offsetcompensation"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.offsetcompensation)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offsetcompensation`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @offsetcompensation.setter
    def offsetcompensation(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.offsetcompensation`` attribute.

        Description:
            - This attribute determines if offset compensation is used.

        Usage:
            - Accessing this property will send the ``print(smu.measure.offsetcompensation)`` query.
            - Setting this property to a value will send the
              ``smu.measure.offsetcompensation = value`` command.

        TSP Syntax:
            ```
            - smu.measure.offsetcompensation = value
            - print(smu.measure.offsetcompensation)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".offsetcompensation", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.offsetcompensation = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.offsetcompensation`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def range(self) -> str:
        """Access the ``smu.measure.range`` attribute.

        Description:
            - This attribute determines the positive full-scale measure range.

        Usage:
            - Accessing this property will send the ``print(smu.measure.range)`` query.
            - Setting this property to a value will send the ``smu.measure.range = value`` command.

        TSP Syntax:
            ```
            - smu.measure.range = value
            - print(smu.measure.range)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".range"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.range)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.range`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @range.setter
    def range(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.range`` attribute.

        Description:
            - This attribute determines the positive full-scale measure range.

        Usage:
            - Accessing this property will send the ``print(smu.measure.range)`` query.
            - Setting this property to a value will send the ``smu.measure.range = value`` command.

        TSP Syntax:
            ```
            - smu.measure.range = value
            - print(smu.measure.range)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".range", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.range = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.range`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rel(self) -> SmuMeasureRel:
        """Return the ``smu.measure.rel`` command tree.

        Sub-properties and sub-methods:
            - ``.acquire()``: The ``smu.measure.rel.acquire()`` function.
            - ``.enable``: The ``smu.measure.rel.enable`` attribute.
            - ``.level``: The ``smu.measure.rel.level`` attribute.
        """
        return self._rel

    @property
    def sense(self) -> str:
        """Access the ``smu.measure.sense`` attribute.

        Description:
            - This attribute selects local (2-wire) or remote (4-wire) sensing.

        Usage:
            - Accessing this property will send the ``print(smu.measure.sense)`` query.
            - Setting this property to a value will send the ``smu.measure.sense = value`` command.

        TSP Syntax:
            ```
            - smu.measure.sense = value
            - print(smu.measure.sense)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".sense"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.sense)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.sense`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @sense.setter
    def sense(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.sense`` attribute.

        Description:
            - This attribute selects local (2-wire) or remote (4-wire) sensing.

        Usage:
            - Accessing this property will send the ``print(smu.measure.sense)`` query.
            - Setting this property to a value will send the ``smu.measure.sense = value`` command.

        TSP Syntax:
            ```
            - smu.measure.sense = value
            - print(smu.measure.sense)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".sense", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.sense = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.sense`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def unit(self) -> str:
        """Access the ``smu.measure.unit`` attribute.

        Description:
            - This attribute sets the units of measurement that are displayed on the front panel of
              the instrument and stored in the reading buffer.

        Usage:
            - Accessing this property will send the ``print(smu.measure.unit)`` query.
            - Setting this property to a value will send the ``smu.measure.unit = value`` command.

        TSP Syntax:
            ```
            - smu.measure.unit = value
            - print(smu.measure.unit)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".unit"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.unit)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.unit`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @unit.setter
    def unit(self, value: Union[str, float]) -> None:
        """Access the ``smu.measure.unit`` attribute.

        Description:
            - This attribute sets the units of measurement that are displayed on the front panel of
              the instrument and stored in the reading buffer.

        Usage:
            - Accessing this property will send the ``print(smu.measure.unit)`` query.
            - Setting this property to a value will send the ``smu.measure.unit = value`` command.

        TSP Syntax:
            ```
            - smu.measure.unit = value
            - print(smu.measure.unit)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".unit", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.unit = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.unit`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def userdelay(self) -> Dict[int, Union[str, float]]:
        """Access the ``smu.measure.userdelay[N]`` attribute.

        Description:
            - This attribute sets a user-defined delay that you can use in the trigger model.

        Usage:
            - Accessing an item from this property will send the ``print(smu.measure.userdelay[N])``
              query.
            - Setting an item from this property to a value will send the
              ``smu.measure.userdelay[N] = value`` command.

        TSP Syntax:
            ```
            - smu.measure.userdelay[N] = value
            - print(smu.measure.userdelay[N])
            ```

        Info:
            - ``N``, the user delay to which this time applies (1 to 5).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._userdelay

    def getattribute(self, function: str, setting: str) -> str:
        """Run the ``smu.measure.getattribute()`` function.

        Description:
            - This function returns the setting for a function attribute.

        TSP Syntax:
            ```
            - smu.measure.getattribute()
            ```

        Args:
            function: The measurement function.
            setting: The attribute for the function; refer to smu.measure.setattribute() for
                available settings.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.getattribute({function}, {setting}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getattribute()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def read(self, buffer_name: Optional[str] = None) -> str:
        """Run the ``smu.measure.read()`` function.

        Description:
            - This function makes measurements, places them in a reading buffer, and returns the
              last reading.

        TSP Syntax:
            ```
            - smu.measure.read()
            ```

        Args:
            buffer_name (optional): The name of the reading buffer, which may be a default buffer
                (defbuffer1 or defbuffer2) or a user-defined buffer; if no buffer is defined, it
                defaults to defbuffer1.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (buffer_name,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.read({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.read()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def readwithtime(self, buffer_name: Optional[str] = None) -> str:
        """Run the ``smu.measure.readwithtime()`` function.

        Description:
            - This function initiates measurements and returns the last actual measurement and time
              information in UTC format without using the trigger model.

        TSP Syntax:
            ```
            - smu.measure.readwithtime()
            ```

        Args:
            buffer_name (optional): The name of the reading buffer, which may be a default buffer
                (defbuffer1 or defbuffer2) or a user-defined buffer; if no buffer is specified, this
                parameter defaults to defbuffer1.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (buffer_name,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.readwithtime({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.readwithtime()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setattribute(self, function: str, setting: str, value: str) -> None:
        """Run the ``smu.measure.setattribute()`` function.

        Description:
            - This function allows you to set up a measure function whether or not the function is
              active.

        TSP Syntax:
            ```
            - smu.measure.setattribute()
            ```

        Args:
            function: The measurement function.
            setting: The attribute for the function; refer to Details and the tables following the
                examples.
            value: The attribute value.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.setattribute({function}, {setting}, {value})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setattribute()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class SmuInterlock(BaseTSPCmd):
    """The ``smu.interlock`` command tree.

    Properties and methods:
        - ``.enable``: The ``smu.interlock.enable`` attribute.
        - ``.tripped``: The ``smu.interlock.tripped`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``smu.interlock.enable`` attribute.

        Description:
            - This attribute determines if the output can be turned on when the interlock is not
              engaged.

        Usage:
            - Accessing this property will send the ``print(smu.interlock.enable)`` query.
            - Setting this property to a value will send the ``smu.interlock.enable = value``
              command.

        TSP Syntax:
            ```
            - smu.interlock.enable = value
            - print(smu.interlock.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enable"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enable)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enable.setter
    def enable(self, value: Union[str, float]) -> None:
        """Access the ``smu.interlock.enable`` attribute.

        Description:
            - This attribute determines if the output can be turned on when the interlock is not
              engaged.

        Usage:
            - Accessing this property will send the ``print(smu.interlock.enable)`` query.
            - Setting this property to a value will send the ``smu.interlock.enable = value``
              command.

        TSP Syntax:
            ```
            - smu.interlock.enable = value
            - print(smu.interlock.enable)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enable", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enable = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enable`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def tripped(self) -> str:
        """Access the ``smu.interlock.tripped`` attribute.

        Description:
            - This attribute indicates that the interlock has been tripped.

        Usage:
            - Accessing this property will send the ``print(smu.interlock.tripped)`` query.

        TSP Syntax:
            ```
            - print(smu.interlock.tripped)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".tripped"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.tripped)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tripped`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Smu(BaseTSPCmd):
    """The ``smu`` command tree.

    Constants:
        - ``.ATTR_MEAS_AUTO_ZERO``: Autozero enable.
        - ``.ATTR_MEAS_COUNT``: Set the measure count.
        - ``.ATTR_MEAS_DIGITS``: Display digits.
        - ``.ATTR_MEAS_FILTER_COUNT``: Set filter count.
        - ``.ATTR_MEAS_FILTER_ENABLE``: Enable or disable filter.
        - ``.ATTR_MEAS_FILTER_TYPE``: Set filter type.
        - ``.ATTR_MEAS_LIMIT_AUDIBLE_1``: Set limit 1 audible.
        - ``.ATTR_MEAS_LIMIT_AUDIBLE_2``: Set limit 2 audible.
        - ``.ATTR_MEAS_LIMIT_AUTO_CLEAR_1``: Enable or disable limit 1 autoclear.
        - ``.ATTR_MEAS_LIMIT_AUTO_CLEAR_2``: Enable or disable limit 2 autoclear.
        - ``.ATTR_MEAS_LIMIT_ENABLE_1``: Enable or disable limit 1.
        - ``.ATTR_MEAS_LIMIT_ENABLE_2``: Limit 2 enable.
        - ``.ATTR_MEAS_LIMIT_FAIL_1``: Limit 1 fail.
        - ``.ATTR_MEAS_LIMIT_FAIL_2``: Limit 2 fail.
        - ``.ATTR_MEAS_LIMIT_HIGH_1``: Set limit 1 high value.
        - ``.ATTR_MEAS_LIMIT_HIGH_2``: Set limit 2 high value.
        - ``.ATTR_MEAS_LIMIT_LOW_1``: Set limit 1 low value.
        - ``.ATTR_MEAS_LIMIT_LOW_2``: Set limit 2 low value.
        - ``.ATTR_MEAS_MATH_ENABLE``: Enable or disable math.
        - ``.ATTR_MEAS_MATH_FORMAT``: Select the math format.
        - ``.ATTR_MEAS_MATH_MXB_BF``: Set the mxb b (offset) value.
        - ``.ATTR_MEAS_MATH_MXB_MF``: Set the mxb m (scalar) value.
        - ``.ATTR_MEAS_MATH_PERCENT``: Set the percent match function.
        - ``.ATTR_MEAS_NPLC``: NPLC.
        - ``.ATTR_MEAS_OFFSET_COMP``: Offset compensation.
        - ``.ATTR_MEAS_RANGE``: Range.
        - ``.ATTR_MEAS_RANGE_AUTO``: Set up autorange.
        - ``.ATTR_MEAS_RANGE_HIGH``: Set up autorange high limit.
        - ``.ATTR_MEAS_RANGE_LOW``: Set up autorange low limit.
        - ``.ATTR_MEAS_RANGE_REBOUND``: Set autorange rebound.
        - ``.ATTR_MEAS_REL_ENABLE``: Relative offset enable.
        - ``.ATTR_MEAS_REL_LEVEL``: Relative offset level.
        - ``.ATTR_MEAS_SENSE``: Sense (2-wire or 4-wire).
        - ``.ATTR_MEAS_UNIT``: Measurement unit.
        - ``.ATTR_MEAS_USER_DELAY_N``: Set user delay, where N is 1 to 5.
        - ``.ATTR_SRC_DELAY``: Delay in addition to normal settling times after turning on the
          source.
        - ``.ATTR_SRC_DELAY_AUTO``: Set autodelay.
        - ``.ATTR_SRC_FUNCTION``: Set the function.
        - ``.ATTR_SRC_HIGHC``: Set high capacitance.
        - ``.ATTR_SRC_LEVEL``: Set level.
        - ``.ATTR_SRC_LIMIT_LEVEL``: Set limit level.
        - ``.ATTR_SRC_LIMIT_TRIPPED``: Source limit exceeded.
        - ``.ATTR_SRC_OFFMODE``: Set output off mode.
        - ``.ATTR_SRC_PROTECT_LEVEL``: Set overvoltage protection limit.
        - ``.ATTR_SRC_PROTECT_TRIPPED``: The overvoltage protection limit is active.
        - ``.ATTR_SRC_RANGE``: Set range.
        - ``.ATTR_SRC_RANGE_AUTO``: Set autorange.
        - ``.ATTR_SRC_READBACK``: Set source readback.
        - ``.ATTR_SRC_USER_DELAY_N``: User delay N, where N is the user delay, 1 to 5.
        - ``.AUDIBLE_FAIL``: Beeper sound on test failure.
        - ``.AUDIBLE_NONE``: Beeper never sounds.
        - ``.AUDIBLE_PASS``: Beeper sound on test pass.
        - ``.DELAY_AUTO``: Delay between measurement points set to autodelay.
        - ``.DIGITS_3_5``: Set display to 3.5 digits.
        - ``.DIGITS_4_5``: Set display to 4.5 digits.
        - ``.DIGITS_5_5``: Set display to 5.5 digits.
        - ``.DIGITS_6_5``: Set display to 6.5 digits.
        - ``.FAIL_BOTH``: Test failed; measurement exceeded both limits.
        - ``.FAIL_HIGH``: Test failed; measurement exceeded high limit.
        - ``.FAIL_LOW``: Test failed; measurement exceeded low limit.
        - ``.FAIL_NONE``: Test passed; measurement under or equal to the high limit.
        - ``.FILTER_MOVING_AVG``: Use the moving average filter for the selected measure function
          when the measurement filter is enabled.
        - ``.FILTER_REPEAT_AVG``: Use the repeatinter average filter for the selected measure
          function when the measurement filter is enabled.
        - ``.FUNC_DC_CURRENT``: Current measurement function.
        - ``.FUNC_DC_VOLTAGE``: Voltage measurement function.
        - ``.FUNC_RESISTANCE``: Resistance measurement function.
        - ``.INFINITE``: Set count to infinite.
        - ``.MATH_MXB``: Perform y = mx+b operation on measurement.
        - ``.MATH_PERCENT``: Perform percent operation on measurements.
        - ``.MATH_RECIPROCAL``: Perform reciprocal math operation on measurements.
        - ``.OFF``: Allow the output to be turned on when the interlock is not engaged.
        - ``.OFFMODE_GUARD``: Set the state when the output is turned off to guard.
        - ``.OFFMODE_HIGHZ``: Set the state when the output is turned off to  high impedance.
        - ``.OFFMODE_NORMAL``: Set the state when the output is turned off to normal.
        - ``.OFFMODE_ZERO``: Set the state when the output is turned off to zero.
        - ``.ON``: Only allow the output to be turned on if the interlock is engaged.
        - ``.PROTECT_100V``: The overvoltage protection value.
        - ``.PROTECT_10V``: The overvoltage protection value.
        - ``.PROTECT_120V``: The overvoltage protection value.
        - ``.PROTECT_140V``: The overvoltage protection value.
        - ``.PROTECT_160V``: The overvoltage protection value.
        - ``.PROTECT_180V``: The overvoltage protection value.
        - ``.PROTECT_20V``: The overvoltage protection value.
        - ``.PROTECT_2V``: The overvoltage protection value.
        - ``.PROTECT_40V``: The overvoltage protection value.
        - ``.PROTECT_5V``: The overvoltage protection value.
        - ``.PROTECT_60V``: The overvoltage protection value.
        - ``.PROTECT_80V``: The overvoltage protection value.
        - ``.PROTECT_NONE``: The overvoltage protection value.
        - ``.RANGE_AUTO``: Most sensitive source range for each source level in the sweep.
        - ``.RANGE_BEST``: Best fixed range.
        - ``.RANGE_FIXED``: Present source range for the entire sweep.
        - ``.SENSE_2WIRE``: Use two-wire sensing.
        - ``.SENSE_4WIRE``: Use four-wire sensing.
        - ``.TERMINALS_FRONT``: Use the front-panel input and output terminals.
        - ``.TERMINALS_REAR``: Use the rear-panel input and output terminals.
        - ``.UNIT_AMP``: Set unit of measure to amps (only available for current measurements).
        - ``.UNIT_OHM``: Set unit of measure to ohms (available for voltage, current, or resistance
          measurements).
        - ``.UNIT_VOLT``: Set unit of measure to volts (only available for voltage measurements).
        - ``.UNIT_WATT``: Set unit of measure to power (only available for voltage or current
          measurements).

    Properties and methods:
        - ``.breakdownprotection``: The ``smu.breakdownprotection`` attribute.
        - ``.interlock``: The ``smu.interlock`` command tree.
        - ``.measure``: The ``smu.measure`` command tree.
        - ``.reset()``: The ``smu.reset()`` function.
        - ``.source``: The ``smu.source`` command tree.
        - ``.terminals``: The ``smu.terminals`` attribute.
    """

    ATTR_MEAS_AUTO_ZERO = "smu.ATTR_MEAS_AUTO_ZERO"
    """str: Autozero enable."""
    ATTR_MEAS_COUNT = "smu.ATTR_MEAS_COUNT"
    """str: Set the measure count."""
    ATTR_MEAS_DIGITS = "smu.ATTR_MEAS_DIGITS"
    """str: Display digits."""
    ATTR_MEAS_FILTER_COUNT = "smu.ATTR_MEAS_FILTER_COUNT"
    """str: Set filter count."""
    ATTR_MEAS_FILTER_ENABLE = "smu.ATTR_MEAS_FILTER_ENABLE"
    """str: Enable or disable filter."""
    ATTR_MEAS_FILTER_TYPE = "smu.ATTR_MEAS_FILTER_TYPE"
    """str: Set filter type."""
    ATTR_MEAS_LIMIT_AUDIBLE_1 = "smu.ATTR_MEAS_LIMIT_AUDIBLE_1"
    """str: Set limit 1 audible."""
    ATTR_MEAS_LIMIT_AUDIBLE_2 = "smu.ATTR_MEAS_LIMIT_AUDIBLE_2"
    """str: Set limit 2 audible."""
    ATTR_MEAS_LIMIT_AUTO_CLEAR_1 = "smu.ATTR_MEAS_LIMIT_AUTO_CLEAR_1"
    """str: Enable or disable limit 1 autoclear."""
    ATTR_MEAS_LIMIT_AUTO_CLEAR_2 = "smu.ATTR_MEAS_LIMIT_AUTO_CLEAR_2"
    """str: Enable or disable limit 2 autoclear."""
    ATTR_MEAS_LIMIT_ENABLE_1 = "smu.ATTR_MEAS_LIMIT_ENABLE_1"
    """str: Enable or disable limit 1."""
    ATTR_MEAS_LIMIT_ENABLE_2 = "smu.ATTR_MEAS_LIMIT_ENABLE_2"
    """str: Limit 2 enable."""
    ATTR_MEAS_LIMIT_FAIL_1 = "smu.ATTR_MEAS_LIMIT_FAIL_1"
    """str: Limit 1 fail."""
    ATTR_MEAS_LIMIT_FAIL_2 = "smu.ATTR_MEAS_LIMIT_FAIL_2"
    """str: Limit 2 fail."""
    ATTR_MEAS_LIMIT_HIGH_1 = "smu.ATTR_MEAS_LIMIT_HIGH_1"
    """str: Set limit 1 high value."""
    ATTR_MEAS_LIMIT_HIGH_2 = "smu.ATTR_MEAS_LIMIT_HIGH_2"
    """str: Set limit 2 high value."""
    ATTR_MEAS_LIMIT_LOW_1 = "smu.ATTR_MEAS_LIMIT_LOW_1"
    """str: Set limit 1 low value."""
    ATTR_MEAS_LIMIT_LOW_2 = "smu.ATTR_MEAS_LIMIT_LOW_2"
    """str: Set limit 2 low value."""
    ATTR_MEAS_MATH_ENABLE = "smu.ATTR_MEAS_MATH_ENABLE"
    """str: Enable or disable math."""
    ATTR_MEAS_MATH_FORMAT = "smu.ATTR_MEAS_MATH_FORMAT"
    """str: Select the math format."""
    ATTR_MEAS_MATH_MXB_BF = "smu.ATTR_MEAS_MATH_MXB_BF"
    """str: Set the mxb b (offset) value."""
    ATTR_MEAS_MATH_MXB_MF = "smu.ATTR_MEAS_MATH_MXB_MF"
    """str: Set the mxb m (scalar) value."""
    ATTR_MEAS_MATH_PERCENT = "smu.ATTR_MEAS_MATH_PERCENT"
    """str: Set the percent match function."""
    ATTR_MEAS_NPLC = "smu.ATTR_MEAS_NPLC"
    """str: NPLC."""
    ATTR_MEAS_OFFSET_COMP = "smu.ATTR_MEAS_OFFSET_COMP"
    """str: Offset compensation."""
    ATTR_MEAS_RANGE = "smu.ATTR_MEAS_RANGE"
    """str: Range."""
    ATTR_MEAS_RANGE_AUTO = "smu.ATTR_MEAS_RANGE_AUTO"
    """str: Set up autorange."""
    ATTR_MEAS_RANGE_HIGH = "smu.ATTR_MEAS_RANGE_HIGH"
    """str: Set up autorange high limit."""
    ATTR_MEAS_RANGE_LOW = "smu.ATTR_MEAS_RANGE_LOW"
    """str: Set up autorange low limit."""
    ATTR_MEAS_RANGE_REBOUND = "smu.ATTR_MEAS_RANGE_REBOUND"
    """str: Set autorange rebound."""
    ATTR_MEAS_REL_ENABLE = "smu.ATTR_MEAS_REL_ENABLE"
    """str: Relative offset enable."""
    ATTR_MEAS_REL_LEVEL = "smu.ATTR_MEAS_REL_LEVEL"
    """str: Relative offset level."""
    ATTR_MEAS_SENSE = "smu.ATTR_MEAS_SENSE"
    """str: Sense (2-wire or 4-wire)."""
    ATTR_MEAS_UNIT = "smu.ATTR_MEAS_UNIT"
    """str: Measurement unit."""
    ATTR_MEAS_USER_DELAY_N = "smu.ATTR_MEAS_USER_DELAY_N"
    """str: Set user delay, where N is 1 to 5."""
    ATTR_SRC_DELAY = "smu.ATTR_SRC_DELAY"
    """str: Delay in addition to normal settling times after turning on the source."""
    ATTR_SRC_DELAY_AUTO = "smu.ATTR_SRC_DELAY_AUTO"
    """str: Set autodelay."""
    ATTR_SRC_FUNCTION = "smu.ATTR_SRC_FUNCTION"
    """str: Set the function."""
    ATTR_SRC_HIGHC = "smu.ATTR_SRC_HIGHC"
    """str: Set high capacitance."""
    ATTR_SRC_LEVEL = "smu.ATTR_SRC_LEVEL"
    """str: Set level."""
    ATTR_SRC_LIMIT_LEVEL = "smu.ATTR_SRC_LIMIT_LEVEL"
    """str: Set limit level."""
    ATTR_SRC_LIMIT_TRIPPED = "smu.ATTR_SRC_LIMIT_TRIPPED"
    """str: Source limit exceeded."""
    ATTR_SRC_OFFMODE = "smu.ATTR_SRC_OFFMODE"
    """str: Set output off mode."""
    ATTR_SRC_PROTECT_LEVEL = "smu.ATTR_SRC_PROTECT_LEVEL"
    """str: Set overvoltage protection limit."""
    ATTR_SRC_PROTECT_TRIPPED = "smu.ATTR_SRC_PROTECT_TRIPPED"
    """str: The overvoltage protection limit is active."""
    ATTR_SRC_RANGE = "smu.ATTR_SRC_RANGE"
    """str: Set range."""
    ATTR_SRC_RANGE_AUTO = "smu.ATTR_SRC_RANGE_AUTO"
    """str: Set autorange."""
    ATTR_SRC_READBACK = "smu.ATTR_SRC_READBACK"
    """str: Set source readback."""
    ATTR_SRC_USER_DELAY_N = "smu.ATTR_SRC_USER_DELAY_N"
    """str: User delay N, where N is the user delay, 1 to 5."""
    AUDIBLE_FAIL = "smu.AUDIBLE_FAIL"
    """str: Beeper sound on test failure."""
    AUDIBLE_NONE = "smu.AUDIBLE_NONE"
    """str: Beeper never sounds."""
    AUDIBLE_PASS = "smu.AUDIBLE_PASS"
    """str: Beeper sound on test pass."""
    DELAY_AUTO = "smu.DELAY_AUTO"
    """str: Delay between measurement points set to autodelay."""
    DIGITS_3_5 = "smu.DIGITS_3_5"
    """str: Set display to 3.5 digits."""
    DIGITS_4_5 = "smu.DIGITS_4_5"
    """str: Set display to 4.5 digits."""
    DIGITS_5_5 = "smu.DIGITS_5_5"
    """str: Set display to 5.5 digits."""
    DIGITS_6_5 = "smu.DIGITS_6_5"
    """str: Set display to 6.5 digits."""
    FAIL_BOTH = "smu.FAIL_BOTH"
    """str: Test failed; measurement exceeded both limits."""
    FAIL_HIGH = "smu.FAIL_HIGH"
    """str: Test failed; measurement exceeded high limit."""
    FAIL_LOW = "smu.FAIL_LOW"
    """str: Test failed; measurement exceeded low limit."""
    FAIL_NONE = "smu.FAIL_NONE"
    """str: Test passed; measurement under or equal to the high limit."""
    FILTER_MOVING_AVG = "smu.FILTER_MOVING_AVG"
    """str: Use the moving average filter for the selected measure function when the measurement filter is enabled."""  # noqa: E501
    FILTER_REPEAT_AVG = "smu.FILTER_REPEAT_AVG"
    """str: Use the repeatinter average filter for the selected measure function when the measurement filter is enabled."""  # noqa: E501
    FUNC_DC_CURRENT = "smu.FUNC_DC_CURRENT"
    """str: Current measurement function."""
    FUNC_DC_VOLTAGE = "smu.FUNC_DC_VOLTAGE"
    """str: Voltage measurement function."""
    FUNC_RESISTANCE = "smu.FUNC_RESISTANCE"
    """str: Resistance measurement function."""
    INFINITE = "smu.INFINITE"
    """str: Set count to infinite."""
    MATH_MXB = "smu.MATH_MXB"
    """str: Perform y = mx+b operation on measurement."""
    MATH_PERCENT = "smu.MATH_PERCENT"
    """str: Perform percent operation on measurements."""
    MATH_RECIPROCAL = "smu.MATH_RECIPROCAL"
    """str: Perform reciprocal math operation on measurements."""
    OFF = "smu.OFF"
    """str: Allow the output to be turned on when the interlock is not engaged."""
    OFFMODE_GUARD = "smu.OFFMODE_GUARD"
    """str: Set the state when the output is turned off to guard."""
    OFFMODE_HIGHZ = "smu.OFFMODE_HIGHZ"
    """str: Set the state when the output is turned off to  high impedance."""
    OFFMODE_NORMAL = "smu.OFFMODE_NORMAL"
    """str: Set the state when the output is turned off to normal."""
    OFFMODE_ZERO = "smu.OFFMODE_ZERO"
    """str: Set the state when the output is turned off to zero."""
    ON = "smu.ON"
    """str: Only allow the output to be turned on if the interlock is engaged."""
    PROTECT_100V = "smu.PROTECT_100V"
    """str: The overvoltage protection value."""
    PROTECT_10V = "smu.PROTECT_10V"
    """str: The overvoltage protection value."""
    PROTECT_120V = "smu.PROTECT_120V"
    """str: The overvoltage protection value."""
    PROTECT_140V = "smu.PROTECT_140V"
    """str: The overvoltage protection value."""
    PROTECT_160V = "smu.PROTECT_160V"
    """str: The overvoltage protection value."""
    PROTECT_180V = "smu.PROTECT_180V"
    """str: The overvoltage protection value."""
    PROTECT_20V = "smu.PROTECT_20V"
    """str: The overvoltage protection value."""
    PROTECT_2V = "smu.PROTECT_2V"
    """str: The overvoltage protection value."""
    PROTECT_40V = "smu.PROTECT_40V"
    """str: The overvoltage protection value."""
    PROTECT_5V = "smu.PROTECT_5V"
    """str: The overvoltage protection value."""
    PROTECT_60V = "smu.PROTECT_60V"
    """str: The overvoltage protection value."""
    PROTECT_80V = "smu.PROTECT_80V"
    """str: The overvoltage protection value."""
    PROTECT_NONE = "smu.PROTECT_NONE"
    """str: The overvoltage protection value."""
    RANGE_AUTO = "smu.RANGE_AUTO"
    """str: Most sensitive source range for each source level in the sweep."""
    RANGE_BEST = "smu.RANGE_BEST"
    """str: Best fixed range."""
    RANGE_FIXED = "smu.RANGE_FIXED"
    """str: Present source range for the entire sweep."""
    SENSE_2WIRE = "smu.SENSE_2WIRE"
    """str: Use two-wire sensing."""
    SENSE_4WIRE = "smu.SENSE_4WIRE"
    """str: Use four-wire sensing."""
    TERMINALS_FRONT = "smu.TERMINALS_FRONT"
    """str: Use the front-panel input and output terminals."""
    TERMINALS_REAR = "smu.TERMINALS_REAR"
    """str: Use the rear-panel input and output terminals."""
    UNIT_AMP = "smu.UNIT_AMP"
    """str: Set unit of measure to amps (only available for current measurements)."""
    UNIT_OHM = "smu.UNIT_OHM"
    """str: Set unit of measure to ohms (available for voltage, current, or resistance measurements)."""  # noqa: E501
    UNIT_VOLT = "smu.UNIT_VOLT"
    """str: Set unit of measure to volts (only available for voltage measurements)."""
    UNIT_WATT = "smu.UNIT_WATT"
    """str: Set unit of measure to power (only available for voltage or current measurements)."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "smu") -> None:
        super().__init__(device, cmd_syntax)
        self._interlock = SmuInterlock(device, f"{self._cmd_syntax}.interlock")
        self._measure = SmuMeasure(device, f"{self._cmd_syntax}.measure")
        self._source = SmuSource(device, f"{self._cmd_syntax}.source")

    @property
    def breakdownprotection(self) -> str:
        """Access the ``smu.breakdownprotection`` attribute.

        Description:
            - This attribute allows you to enable the breakdown protection in situations where the
              current may exceed the programmed current or the limit current value due to a
              breakdown condition.

        Usage:
            - Accessing this property will send the ``print(smu.breakdownprotection)`` query.
            - Setting this property to a value will send the ``smu.breakdownprotection = value``
              command.

        TSP Syntax:
            ```
            - smu.breakdownprotection = value
            - print(smu.breakdownprotection)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".breakdownprotection"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.breakdownprotection)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.breakdownprotection`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @breakdownprotection.setter
    def breakdownprotection(self, value: Union[str, float]) -> None:
        """Access the ``smu.breakdownprotection`` attribute.

        Description:
            - This attribute allows you to enable the breakdown protection in situations where the
              current may exceed the programmed current or the limit current value due to a
              breakdown condition.

        Usage:
            - Accessing this property will send the ``print(smu.breakdownprotection)`` query.
            - Setting this property to a value will send the ``smu.breakdownprotection = value``
              command.

        TSP Syntax:
            ```
            - smu.breakdownprotection = value
            - print(smu.breakdownprotection)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".breakdownprotection", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.breakdownprotection = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.breakdownprotection`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def interlock(self) -> SmuInterlock:
        """Return the ``smu.interlock`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``smu.interlock.enable`` attribute.
            - ``.tripped``: The ``smu.interlock.tripped`` attribute.
        """
        return self._interlock

    @property
    def measure(self) -> SmuMeasure:
        """Return the ``smu.measure`` command tree.

        Sub-properties and sub-methods:
            - ``.autorange``: The ``smu.measure.autorange`` attribute.
            - ``.autorangehigh``: The ``smu.measure.autorangehigh`` attribute.
            - ``.autorangelow``: The ``smu.measure.autorangelow`` attribute.
            - ``.autorangerebound``: The ``smu.measure.autorangerebound`` attribute.
            - ``.autozero``: The ``smu.measure.autozero`` command tree.
            - ``.configlist``: The ``smu.measure.configlist`` command tree.
            - ``.count``: The ``smu.measure.count`` attribute.
            - ``.displaydigits``: The ``smu.measure.displaydigits`` attribute.
            - ``.filter``: The ``smu.measure.filter`` command tree.
            - ``.func``: The ``smu.measure.func`` attribute.
            - ``.getattribute()``: The ``smu.measure.getattribute()`` function.
            - ``.limit``: The ``smu.measure.limit[r]`` command tree.
            - ``.math``: The ``smu.measure.math`` command tree.
            - ``.nplc``: The ``smu.measure.nplc`` attribute.
            - ``.offsetcompensation``: The ``smu.measure.offsetcompensation`` attribute.
            - ``.range``: The ``smu.measure.range`` attribute.
            - ``.read()``: The ``smu.measure.read()`` function.
            - ``.readwithtime()``: The ``smu.measure.readwithtime()`` function.
            - ``.rel``: The ``smu.measure.rel`` command tree.
            - ``.sense``: The ``smu.measure.sense`` attribute.
            - ``.setattribute()``: The ``smu.measure.setattribute()`` function.
            - ``.unit``: The ``smu.measure.unit`` attribute.
            - ``.userdelay``: The ``smu.measure.userdelay[N]`` attribute.
        """
        return self._measure

    @property
    def source(self) -> SmuSource:
        """Return the ``smu.source`` command tree.

        Sub-properties and sub-methods:
            - ``.autodelay``: The ``smu.source.autodelay`` attribute.
            - ``.autorange``: The ``smu.source.autorange`` attribute.
            - ``.configlist``: The ``smu.source.configlist`` command tree.
            - ``.delay``: The ``smu.source.delay`` attribute.
            - ``.func``: The ``smu.source.func`` attribute.
            - ``.getattribute()``: The ``smu.source.getattribute()`` function.
            - ``.highc``: The ``smu.source.highc`` attribute.
            - ``.level``: The ``smu.source.level`` attribute.
            - ``.offmode``: The ``smu.source.offmode`` attribute.
            - ``.output``: The ``smu.source.output`` attribute.
            - ``.protect``: The ``smu.source.protect`` command tree.
            - ``.range``: The ``smu.source.range`` attribute.
            - ``.readback``: The ``smu.source.readback`` attribute.
            - ``.setattribute()``: The ``smu.source.setattribute()`` function.
            - ``.sweeplinear()``: The ``smu.source.sweeplinear()`` function.
            - ``.sweeplinearstep()``: The ``smu.source.sweeplinearstep()`` function.
            - ``.sweeplist()``: The ``smu.source.sweeplist()`` function.
            - ``.sweeplog()``: The ``smu.source.sweeplog()`` function.
            - ``.userdelay``: The ``smu.source.userdelay[N]`` attribute.
            - ``.ilimit``: The ``smu.source.ilimit`` command tree.
            - ``.vlimit``: The ``smu.source.vlimit`` command tree.
        """
        return self._source

    @property
    def terminals(self) -> str:
        """Access the ``smu.terminals`` attribute.

        Description:
            - This attribute describes which set of input and output terminals the instrument is
              using.

        Usage:
            - Accessing this property will send the ``print(smu.terminals)`` query.
            - Setting this property to a value will send the ``smu.terminals = value`` command.

        TSP Syntax:
            ```
            - smu.terminals = value
            - print(smu.terminals)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".terminals"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.terminals)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.terminals`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @terminals.setter
    def terminals(self, value: Union[str, float]) -> None:
        """Access the ``smu.terminals`` attribute.

        Description:
            - This attribute describes which set of input and output terminals the instrument is
              using.

        Usage:
            - Accessing this property will send the ``print(smu.terminals)`` query.
            - Setting this property to a value will send the ``smu.terminals = value`` command.

        TSP Syntax:
            ```
            - smu.terminals = value
            - print(smu.terminals)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".terminals", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.terminals = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.terminals`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def reset(self) -> None:
        """Run the ``smu.reset()`` function.

        Description:
            - This function turns off the output and resets the commands that begin with smu. to
              their default settings.

        TSP Syntax:
            ```
            - smu.reset()
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
