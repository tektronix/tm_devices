# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The buffervar commands module.

These commands are used in the following models:
SMU2601B, SMU2602B, SMU2604B, SMU2606B, SMU2611B, SMU2612B, SMU2614B, SMU2634B, SMU2635B, SMU2636B,
SMU2651A, SMU2657A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - bufferVar.appendmode
    - bufferVar.basetimestamp
    - bufferVar.cachemode
    - bufferVar.capacity
    - bufferVar.clear()
    - bufferVar.clearcache()
    - bufferVar.collectsourcevalues
    - bufferVar.collecttimestamps
    - bufferVar.fillcount
    - bufferVar.fillmode
    - bufferVar.measurefunctions[N]
    - bufferVar.measureranges[N]
    - bufferVar.n
    - bufferVar.readings[N]
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


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class Buffervar(BaseTSPCmd):
    """The ``bufferVar`` command tree.

    Info:
        - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer or a
          dedicated reading buffer.

    Properties and methods:
        - ``.appendmode``: The ``bufferVar.appendmode`` attribute.
        - ``.basetimestamp``: The ``bufferVar.basetimestamp`` attribute.
        - ``.cachemode``: The ``bufferVar.cachemode`` attribute.
        - ``.capacity``: The ``bufferVar.capacity`` attribute.
        - ``.clear()``: The ``bufferVar.clear()`` function.
        - ``.clearcache()``: The ``bufferVar.clearcache()`` function.
        - ``.collectsourcevalues``: The ``bufferVar.collectsourcevalues`` attribute.
        - ``.collecttimestamps``: The ``bufferVar.collecttimestamps`` attribute.
        - ``.fillcount``: The ``bufferVar.fillcount`` attribute.
        - ``.fillmode``: The ``bufferVar.fillmode`` attribute.
        - ``.measurefunctions``: The ``bufferVar.measurefunctions[N]`` attribute.
        - ``.measureranges``: The ``bufferVar.measureranges[N]`` attribute.
        - ``.n``: The ``bufferVar.n`` attribute.
        - ``.readings``: The ``bufferVar.readings[N]`` attribute.
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
    def basetimestamp(self) -> str:
        """Access the ``bufferVar.basetimestamp`` attribute.

        Description:
            - This attribute contains the timestamp that indicates when the first reading was stored
              in the buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.basetimestamp)`` query.

        TSP Syntax:
            ```
            - print(bufferVar.basetimestamp)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".basetimestamp"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.basetimestamp)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.basetimestamp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def cachemode(self) -> str:
        """Access the ``bufferVar.cachemode`` attribute.

        Description:
            - This attribute enables or disables the reading buffer cache (on or off).

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
            - This attribute enables or disables the reading buffer cache (on or off).

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
            - This attribute sets the number of readings a buffer can store.

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
    def collectsourcevalues(self) -> str:
        """Access the ``bufferVar.collectsourcevalues`` attribute.

        Description:
            - This attribute sets whether or not source values are stored with the readings in the
              buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.collectsourcevalues)`` query.
            - Setting this property to a value will send the
              ``bufferVar.collectsourcevalues = value`` command.

        TSP Syntax:
            ```
            - bufferVar.collectsourcevalues = value
            - print(bufferVar.collectsourcevalues)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".collectsourcevalues"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.collectsourcevalues)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.collectsourcevalues`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @collectsourcevalues.setter
    def collectsourcevalues(self, value: Union[str, float]) -> None:
        """Access the ``bufferVar.collectsourcevalues`` attribute.

        Description:
            - This attribute sets whether or not source values are stored with the readings in the
              buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.collectsourcevalues)`` query.
            - Setting this property to a value will send the
              ``bufferVar.collectsourcevalues = value`` command.

        TSP Syntax:
            ```
            - bufferVar.collectsourcevalues = value
            - print(bufferVar.collectsourcevalues)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".collectsourcevalues", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.collectsourcevalues = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.collectsourcevalues`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def collecttimestamps(self) -> str:
        """Access the ``bufferVar.collecttimestamps`` attribute.

        Description:
            - This attribute sets whether or not timestamp values are stored with the readings in
              the buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.collecttimestamps)`` query.
            - Setting this property to a value will send the ``bufferVar.collecttimestamps = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.collecttimestamps = value
            - print(bufferVar.collecttimestamps)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".collecttimestamps"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.collecttimestamps)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.collecttimestamps`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @collecttimestamps.setter
    def collecttimestamps(self, value: Union[str, float]) -> None:
        """Access the ``bufferVar.collecttimestamps`` attribute.

        Description:
            - This attribute sets whether or not timestamp values are stored with the readings in
              the buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.collecttimestamps)`` query.
            - Setting this property to a value will send the ``bufferVar.collecttimestamps = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.collecttimestamps = value
            - print(bufferVar.collecttimestamps)
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
                    self._cmd_syntax + ".collecttimestamps", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.collecttimestamps = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.collecttimestamps`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def fillcount(self) -> str:
        """Access the ``bufferVar.fillcount`` attribute.

        Description:
            - This attribute sets the reading buffer fill count.

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
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).

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
            - This attribute sets the reading buffer fill count.

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
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).

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
            - This attribute sets the reading buffer fill mode.

        Usage:
            - Accessing this property will send the ``print(bufferVar.fillmode)`` query.
            - Setting this property to a value will send the ``bufferVar.fillmode = value`` command.

        TSP Syntax:
            ```
            - bufferVar.fillmode = value
            - print(bufferVar.fillmode)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).

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
            - This attribute sets the reading buffer fill mode.

        Usage:
            - Accessing this property will send the ``print(bufferVar.fillmode)`` query.
            - Setting this property to a value will send the ``bufferVar.fillmode = value`` command.

        TSP Syntax:
            ```
            - bufferVar.fillmode = value
            - print(bufferVar.fillmode)
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).

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
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).
            - ``N``, the reading number (1 to bufferVar.n).

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
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).
            - ``N``, the reading number (1 to bufferVar.n).

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
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._readings

    @property
    def sourcefunctions(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourcefunctions[N]`` attribute.

        Description:
            - This attribute contains the source function that was being used when the readings were
              stored in a specified reading buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.sourcefunctions[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.sourcefunctions[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).
            - ``N``, the reading number (1 to bufferVar.n).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._sourcefunctions

    @property
    def sourceoutputstates(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourceoutputstates[N]`` attribute.

        Description:
            - This attribute indicates the state of the source output for readings that are stored
              in a specified buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.sourceoutputstates[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.sourceoutputstates[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).
            - ``N``, the reading number (1 to bufferVar.n).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._sourceoutputstates

    @property
    def sourceranges(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourceranges[N]`` attribute.

        Description:
            - This attribute contains the source range that was used for readings stored in a
              specified reading buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.sourceranges[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.sourceranges[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined), or a dedicated reading buffer (such as smua.nvbuffer1).
            - ``N``, the reading number (1 to bufferVar.n).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._sourceranges

    @property
    def sourcevalues(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourcevalues[N]`` attribute.

        Description:
            - When enabled by the bufferVar.collectsourcevalues attribute, this attribute contains
              the source levels being output when readings in the reading buffer were acquired.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.sourcevalues[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.sourcevalues[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated buffer
              (user-defined) or a dedicated reading buffer (such as smua.nvbuffer1).
            - ``N``, the reading number (1 to bufferVar.n).

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
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

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
            - When enabled by the bufferVar.collecttimestamps attribute, this attribute contains the
              timestamp when each reading saved in the specified reading buffer occurred.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.timestamps[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.timestamps[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer; can be a dynamically allocated user-defined buffer
              or a dedicated reading buffer.
            - ``N``, the reading number (1 to bufferVar.n).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._timestamps

    def clear(self) -> None:
        """Run the ``bufferVar.clear()`` function.

        Description:
            - This function empties the buffer.

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
            - This function clears the cache.

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
