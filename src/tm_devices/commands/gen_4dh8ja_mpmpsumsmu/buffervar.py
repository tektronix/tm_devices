# pyright: reportConstantRedefinition=none
"""The buffervar commands module.

These commands are used in the following models:
MP5103, MPSU50_2ST, MSMU60_2

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - bufferVar.appendmode
    - bufferVar.cachemode
    - bufferVar.capacity
    - bufferVar.clear()
    - bufferVar.clearcache()
    - bufferVar.columnname.enable
    - bufferVar.fillcount
    - bufferVar.fillmode
    - bufferVar.fractionalseconds[N]
    - bufferVar.measurefunctions[N]
    - bufferVar.measureranges[N]
    - bufferVar.n
    - bufferVar.readings[N]
    - bufferVar.seconds[N]
    - bufferVar.sourcefunctions[N]
    - bufferVar.sourceoutputstates[N]
    - bufferVar.sourceranges[N]
    - bufferVar.sourcevalues[N]
    - bufferVar.statuses[N]
    - bufferVar.timestampresolution
    - bufferVar.timestamps[N]
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from ..helpers import BaseTSPCmd, DefaultDictDeviceCommunication, NoDeviceProvidedError

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class BuffervarColumnname(BaseTSPCmd):
    """The ``bufferVar.columnname`` command tree.

    Info:
        - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer or a
          dedicated reading buffer.
        - ``columnname``, the reading buffer column to enable or disable.

    Properties and methods:
        - ``.enable``: The ``bufferVar.columnname.enable`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``bufferVar.columnname.enable`` attribute.

        Description:
            - This attribute sets which buffer columns will be stored with the readings in the
              buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.columnname.enable)`` query.
            - Setting this property to a value will send the ``bufferVar.columnname.enable = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.columnname.enable = value
            - print(bufferVar.columnname.enable)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``columnname``, the reading buffer column to enable or disable.

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
        """Access the ``bufferVar.columnname.enable`` attribute.

        Description:
            - This attribute sets which buffer columns will be stored with the readings in the
              buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.columnname.enable)`` query.
            - Setting this property to a value will send the ``bufferVar.columnname.enable = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.columnname.enable = value
            - print(bufferVar.columnname.enable)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``columnname``, the reading buffer column to enable or disable.

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


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class Buffervar(BaseTSPCmd):
    """The ``bufferVar`` command tree.

    Info:
        - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer or a
          dedicated reading buffer.

    Properties and methods:
        - ``.appendmode``: The ``bufferVar.appendmode`` attribute.
        - ``.cachemode``: The ``bufferVar.cachemode`` attribute.
        - ``.capacity``: The ``bufferVar.capacity`` attribute.
        - ``.clear()``: The ``bufferVar.clear()`` function.
        - ``.clearcache()``: The ``bufferVar.clearcache()`` function.
        - ``.columnname``: The ``bufferVar.columnname`` command tree.
        - ``.fillcount``: The ``bufferVar.fillcount`` attribute.
        - ``.fillmode``: The ``bufferVar.fillmode`` attribute.
        - ``.fractionalseconds``: The ``bufferVar.fractionalseconds[N]`` attribute.
        - ``.measurefunctions``: The ``bufferVar.measurefunctions[N]`` attribute.
        - ``.measureranges``: The ``bufferVar.measureranges[N]`` attribute.
        - ``.n``: The ``bufferVar.n`` attribute.
        - ``.readings``: The ``bufferVar.readings[N]`` attribute.
        - ``.seconds``: The ``bufferVar.seconds[N]`` attribute.
        - ``.sourcefunctions``: The ``bufferVar.sourcefunctions[N]`` attribute.
        - ``.sourceoutputstates``: The ``bufferVar.sourceoutputstates[N]`` attribute.
        - ``.sourceranges``: The ``bufferVar.sourceranges[N]`` attribute.
        - ``.sourcevalues``: The ``bufferVar.sourcevalues[N]`` attribute.
        - ``.statuses``: The ``bufferVar.statuses[N]`` attribute.
        - ``.timestampresolution``: The ``bufferVar.timestampresolution`` attribute.
        - ``.timestamps``: The ``bufferVar.timestamps[N]`` attribute.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "bufferVar"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._columnname = BuffervarColumnname(device, f"{self._cmd_syntax}.columnname")
        self._fractionalseconds: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.fractionalseconds[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.fractionalseconds[{{key}}])",
            device=self._device,
        )
        self._measurefunctions: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.measurefunctions[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.measurefunctions[{{key}}])",
            device=self._device,
        )
        self._measureranges: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.measureranges[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.measureranges[{{key}}])",
            device=self._device,
        )
        self._readings: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.readings[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.readings[{{key}}])",
            device=self._device,
        )
        self._seconds: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.seconds[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.seconds[{{key}}])",
            device=self._device,
        )
        self._sourcefunctions: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.sourcefunctions[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.sourcefunctions[{{key}}])",
            device=self._device,
        )
        self._sourceoutputstates: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.sourceoutputstates[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.sourceoutputstates[{{key}}])",
            device=self._device,
        )
        self._sourceranges: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.sourceranges[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.sourceranges[{{key}}])",
            device=self._device,
        )
        self._sourcevalues: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.sourcevalues[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.sourcevalues[{{key}}])",
            device=self._device,
        )
        self._statuses: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.statuses[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.statuses[{{key}}])",
            device=self._device,
        )
        self._timestamps: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.timestamps[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.timestamps[{{key}}])",
            device=self._device,
        )

    @property
    def appendmode(self) -> str:
        """Access the ``bufferVar.appendmode`` attribute.

        Description:
            - This attribute sets the state of the append mode of the reading buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.appendmode)`` query.
            - Setting this property to a value will send the ``bufferVar.appendmode = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.appendmode = value
            - print(bufferVar.appendmode)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".appendmode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.appendmode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.appendmode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @appendmode.setter
    def appendmode(self, value: Union[str, float]) -> None:
        """Access the ``bufferVar.appendmode`` attribute.

        Description:
            - This attribute sets the state of the append mode of the reading buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.appendmode)`` query.
            - Setting this property to a value will send the ``bufferVar.appendmode = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.appendmode = value
            - print(bufferVar.appendmode)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".appendmode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.appendmode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.appendmode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def cachemode(self) -> str:
        """Access the ``bufferVar.cachemode`` attribute.

        Description:
            - This attribute enables or disables the reading buffer cache.

        Usage:
            - Accessing this property will send the ``print(bufferVar.cachemode)`` query.
            - Setting this property to a value will send the ``bufferVar.cachemode = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.cachemode = value
            - print(bufferVar.cachemode)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".cachemode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.cachemode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.cachemode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @cachemode.setter
    def cachemode(self, value: Union[str, float]) -> None:
        """Access the ``bufferVar.cachemode`` attribute.

        Description:
            - This attribute enables or disables the reading buffer cache.

        Usage:
            - Accessing this property will send the ``print(bufferVar.cachemode)`` query.
            - Setting this property to a value will send the ``bufferVar.cachemode = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.cachemode = value
            - print(bufferVar.cachemode)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".cachemode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.cachemode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.cachemode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def capacity(self) -> str:
        """Access the ``bufferVar.capacity`` attribute.

        Description:
            - This attribute contains the capacity of the buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.capacity)`` query.

        TSP Syntax:
            ```
            - print(bufferVar.capacity)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".capacity"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.capacity)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.capacity`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def columnname(self) -> BuffervarColumnname:
        """Return the ``bufferVar.columnname`` command tree.

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``columnname``, the reading buffer column to enable or disable.

        Sub-properties and sub-methods:
            - ``.enable``: The ``bufferVar.columnname.enable`` attribute.
        """
        return self._columnname

    @property
    def fillcount(self) -> str:
        """Access the ``bufferVar.fillcount`` attribute.

        Description:
            - This attribute sets the number of readings to store before restarting at index 1.

        Usage:
            - Accessing this property will send the ``print(bufferVar.fillcount)`` query.
            - Setting this property to a value will send the ``bufferVar.fillcount = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.fillcount = value
            - print(bufferVar.fillcount)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".fillcount"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.fillcount)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.fillcount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @fillcount.setter
    def fillcount(self, value: Union[str, float]) -> None:
        """Access the ``bufferVar.fillcount`` attribute.

        Description:
            - This attribute sets the number of readings to store before restarting at index 1.

        Usage:
            - Accessing this property will send the ``print(bufferVar.fillcount)`` query.
            - Setting this property to a value will send the ``bufferVar.fillcount = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.fillcount = value
            - print(bufferVar.fillcount)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".fillcount", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.fillcount = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.fillcount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def fillmode(self) -> str:
        """Access the ``bufferVar.fillmode`` attribute.

        Description:
            - This attribute determines if old data is overwritten when the reading buffer is
              filled.

        Usage:
            - Accessing this property will send the ``print(bufferVar.fillmode)`` query.
            - Setting this property to a value will send the ``bufferVar.fillmode = value`` command.

        TSP Syntax:
            ```
            - bufferVar.fillmode = value
            - print(bufferVar.fillmode)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".fillmode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.fillmode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.fillmode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @fillmode.setter
    def fillmode(self, value: Union[str, float]) -> None:
        """Access the ``bufferVar.fillmode`` attribute.

        Description:
            - This attribute determines if old data is overwritten when the reading buffer is
              filled.

        Usage:
            - Accessing this property will send the ``print(bufferVar.fillmode)`` query.
            - Setting this property to a value will send the ``bufferVar.fillmode = value`` command.

        TSP Syntax:
            ```
            - bufferVar.fillmode = value
            - print(bufferVar.fillmode)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".fillmode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.fillmode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.fillmode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def fractionalseconds(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.fractionalseconds[N]`` attribute.

        Description:
            - This attribute contains the fractional second portion of the timestamp of each reading
              in the reading buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.fractionalseconds[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.fractionalseconds[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer or a
              user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._fractionalseconds

    @property
    def measurefunctions(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.measurefunctions[N]`` attribute.

        Description:
            - This attribute contains the measurement function that was used to acquire a reading
              stored in a specified reading buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.measurefunctions[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.measurefunctions[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``N``, the reading number: 1 to bufferVar.n.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._measurefunctions

    @property
    def measureranges(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.measureranges[N]`` attribute.

        Description:
            - This attribute contains the measurement range values that were used for readings
              stored in a specified buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.measureranges[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.measureranges[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``N``, the reading number: 1 to bufferVar.n.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._measureranges

    @property
    def n(self) -> str:
        """Access the ``bufferVar.n`` attribute.

        Description:
            - This attribute contains the number of readings in the buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.n)`` query.

        TSP Syntax:
            ```
            - print(bufferVar.n)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".n"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.n)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.n`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def readings(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.readings[N]`` attribute.

        Description:
            - This attribute contains the readings stored in a specified reading buffer.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.readings[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.readings[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``N``, the reading number: 1 to bufferVar.n.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._readings

    @property
    def seconds(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.seconds[N]`` attribute.

        Description:
            - This contains the timestamp of a reading in seconds, in UTC format.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.seconds[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.seconds[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer or a
              user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._seconds

    @property
    def sourcefunctions(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourcefunctions[N]`` attribute.

        Description:
            - This function contains the source function that was used for readings stored in a
              specified reading buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.sourcefunctions[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.sourcefunctions[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``N``, the reading number: 1 to bufferVar.n.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._sourcefunctions

    @property
    def sourceoutputstates(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourceoutputstates[N]`` attribute.

        Description:
            - This attribute indicates the state of the source output for readings stored in a
              specified buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.sourceoutputstates[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.sourceoutputstates[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``N``, the reading number: 1 to bufferVar.n.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._sourceoutputstates

    @property
    def sourceranges(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourceranges[N]`` attribute.

        Description:
            - This attribute indicates the state of the source range for readings stored in a
              specified buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.sourceranges[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.sourceranges[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``N``, the reading number: 1 to bufferVar.n.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._sourceranges

    @property
    def sourcevalues(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourcevalues[N]`` attribute.

        Description:
            - When enabled, this attribute contains the source levels being output when readings in
              the reading buffer were acquired.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.sourcevalues[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.sourcevalues[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``N``, the reading number: 1 to bufferVar.n.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._sourcevalues

    @property
    def statuses(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.statuses[N]`` attribute.

        Description:
            - This attribute contains the status values of readings in the reading buffer.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.statuses[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.statuses[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``N``, the reading number: 1 to bufferVar.n.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._statuses

    @property
    def timestampresolution(self) -> str:
        """Access the ``bufferVar.timestampresolution`` attribute.

        Description:
            - This attribute contains the resolution of the timestamp.

        Usage:
            - Accessing this property will send the ``print(bufferVar.timestampresolution)`` query.
            - Setting this property to a value will send the
              ``bufferVar.timestampresolution = value`` command.

        TSP Syntax:
            ```
            - bufferVar.timestampresolution = value
            - print(bufferVar.timestampresolution)
            ```

        Info:
            - ``resolution``, the timestamp resolution in seconds (minimum 1 µs; rounded to an even
              power of 2 µs).
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".timestampresolution"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.timestampresolution)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.timestampresolution`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @timestampresolution.setter
    def timestampresolution(self, value: Union[str, float]) -> None:
        """Access the ``bufferVar.timestampresolution`` attribute.

        Description:
            - This attribute contains the resolution of the timestamp.

        Usage:
            - Accessing this property will send the ``print(bufferVar.timestampresolution)`` query.
            - Setting this property to a value will send the
              ``bufferVar.timestampresolution = value`` command.

        TSP Syntax:
            ```
            - bufferVar.timestampresolution = value
            - print(bufferVar.timestampresolution)
            ```

        Info:
            - ``resolution``, the timestamp resolution in seconds (minimum 1 µs; rounded to an even
              power of 2 µs).
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".timestampresolution", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.timestampresolution = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.timestampresolution`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def timestamps(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.timestamps[N]`` attribute.

        Description:
            - This attribute contains the timestamp for each reading in the specified buffer.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.timestamps[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.timestamps[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``N``, the reading number: 1 to bufferVar.n.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._timestamps

    def clear(self) -> None:
        """Run the ``bufferVar.clear()`` function.

        Description:
            - This function empties the reading buffer.

        TSP Syntax:
            ```
            - bufferVar.clear()
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

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

    def clearcache(self) -> None:
        """Run the ``bufferVar.clearcache()`` function.

        Description:
            - This function clears all readings from the specified cache.

        TSP Syntax:
            ```
            - bufferVar.clearcache()
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.clearcache()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.clearcache()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
