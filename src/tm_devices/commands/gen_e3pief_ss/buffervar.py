# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The buffervar commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - bufferVar.appendmode
    - bufferVar.basetimefractional
    - bufferVar.basetimeseconds
    - bufferVar.cachemode
    - bufferVar.capacity
    - bufferVar.channels[N]
    - bufferVar.clear()
    - bufferVar.clearcache()
    - bufferVar.collectchannels
    - bufferVar.collecttimestamps
    - bufferVar.dates[N]
    - bufferVar.formattedreadings[N]
    - bufferVar.fractionalseconds[N]
    - bufferVar.n
    - bufferVar.ptpseconds[N]
    - bufferVar.readings[N]
    - bufferVar.relativetimestamps[N]
    - bufferVar.seconds[N]
    - bufferVar.statuses[N]
    - bufferVar.times[N]
    - bufferVar.timestampresolution
    - bufferVar.timestamps[N]
    - bufferVar.units[N]
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
        - ``bufferVar``, the reading buffer.

    Properties and methods:
        - ``.appendmode``: The ``bufferVar.appendmode`` attribute.
        - ``.basetimefractional``: The ``bufferVar.basetimefractional`` attribute.
        - ``.basetimeseconds``: The ``bufferVar.basetimeseconds`` attribute.
        - ``.cachemode``: The ``bufferVar.cachemode`` attribute.
        - ``.capacity``: The ``bufferVar.capacity`` attribute.
        - ``.channels``: The ``bufferVar.channels[N]`` attribute.
        - ``.clear()``: The ``bufferVar.clear()`` function.
        - ``.clearcache()``: The ``bufferVar.clearcache()`` function.
        - ``.collectchannels``: The ``bufferVar.collectchannels`` attribute.
        - ``.collecttimestamps``: The ``bufferVar.collecttimestamps`` attribute.
        - ``.dates``: The ``bufferVar.dates[N]`` attribute.
        - ``.formattedreadings``: The ``bufferVar.formattedreadings[N]`` attribute.
        - ``.fractionalseconds``: The ``bufferVar.fractionalseconds[N]`` attribute.
        - ``.n``: The ``bufferVar.n`` attribute.
        - ``.ptpseconds``: The ``bufferVar.ptpseconds[N]`` attribute.
        - ``.readings``: The ``bufferVar.readings[N]`` attribute.
        - ``.relativetimestamps``: The ``bufferVar.relativetimestamps[N]`` attribute.
        - ``.seconds``: The ``bufferVar.seconds[N]`` attribute.
        - ``.statuses``: The ``bufferVar.statuses[N]`` attribute.
        - ``.times``: The ``bufferVar.times[N]`` attribute.
        - ``.timestampresolution``: The ``bufferVar.timestampresolution`` attribute.
        - ``.timestamps``: The ``bufferVar.timestamps[N]`` attribute.
        - ``.units``: The ``bufferVar.units[N]`` attribute.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "bufferVar"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._channels: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.channels[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.channels[{{key}}])",
            device=self._device,
        )
        self._dates: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.dates[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.dates[{{key}}])",
            device=self._device,
        )
        self._formattedreadings: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.formattedreadings[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.formattedreadings[{{key}}])",
            device=self._device,
        )
        self._fractionalseconds: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.fractionalseconds[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.fractionalseconds[{{key}}])",
            device=self._device,
        )
        self._ptpseconds: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.ptpseconds[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.ptpseconds[{{key}}])",
            device=self._device,
        )
        self._readings: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.readings[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.readings[{{key}}])",
            device=self._device,
        )
        self._relativetimestamps: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.relativetimestamps[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.relativetimestamps[{{key}}])",
            device=self._device,
        )
        self._seconds: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.seconds[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.seconds[{{key}}])",
            device=self._device,
        )
        self._statuses: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.statuses[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.statuses[{{key}}])",
            device=self._device,
        )
        self._times: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.times[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.times[{{key}}])",
            device=self._device,
        )
        self._timestamps: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.timestamps[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.timestamps[{{key}}])",
            device=self._device,
        )
        self._units: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.units[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.units[{{key}}])",
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
            - ``bufferVar``, the reading buffer.

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
            - ``bufferVar``, the reading buffer.

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
    def basetimefractional(self) -> str:
        """Access the ``bufferVar.basetimefractional`` attribute.

        Description:
            - When enabled by the bufferVar.collecttimestamps attribute, this attribute contains the
              fractional portion of the timestamp (in seconds) for the first reading stored in the
              reading buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.basetimefractional)`` query.

        TSP Syntax:
            ```
            - print(bufferVar.basetimefractional)
            ```

        Info:
            - ``bufferVar``, the reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".basetimefractional"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.basetimefractional)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.basetimefractional`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def basetimeseconds(self) -> str:
        """Access the ``bufferVar.basetimeseconds`` attribute.

        Description:
            - When enabled by the bufferVar.collecttimestamps attribute, this attribute represents
              the nonfractional seconds of the timestamp for the first reading stored in the reading
              buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.basetimeseconds)`` query.

        TSP Syntax:
            ```
            - print(bufferVar.basetimeseconds)
            ```

        Info:
            - ``bufferVar``, the reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".basetimeseconds"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.basetimeseconds)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.basetimeseconds`` attribute."  # noqa: E501
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
            - ``bufferVar``, the reading buffer.

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
            - ``bufferVar``, the reading buffer.

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
            - ``bufferVar``, the reading buffer.

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
    def channels(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.channels[N]`` attribute.

        Description:
            - When enabled by the bufferVar.collectchannels attribute, this buffer recall attribute
              gets the channel, backplane relay, or channel pattern information stored with readings
              in the buffer.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.channels[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.channels[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number (1 to bufferVar.n).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._channels

    @property
    def collectchannels(self) -> str:
        """Access the ``bufferVar.collectchannels`` attribute.

        Description:
            - This attribute sets the storage state of channel information with the readings in the
              buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.collectchannels)`` query.
            - Setting this property to a value will send the ``bufferVar.collectchannels = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.collectchannels = value
            - print(bufferVar.collectchannels)
            ```

        Info:
            - ``bufferVar``, the reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".collectchannels"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.collectchannels)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.collectchannels`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @collectchannels.setter
    def collectchannels(self, value: Union[str, float]) -> None:
        """Access the ``bufferVar.collectchannels`` attribute.

        Description:
            - This attribute sets the storage state of channel information with the readings in the
              buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.collectchannels)`` query.
            - Setting this property to a value will send the ``bufferVar.collectchannels = value``
              command.

        TSP Syntax:
            ```
            - bufferVar.collectchannels = value
            - print(bufferVar.collectchannels)
            ```

        Info:
            - ``bufferVar``, the reading buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".collectchannels", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.collectchannels = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.collectchannels`` attribute."  # noqa: E501
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
            - ``bufferVar``, the reading buffer.

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
            - ``bufferVar``, the reading buffer.

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
    def dates(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.dates[N]`` attribute.

        Description:
            - When enabled by the bufferVar.collecttimestamps attribute, this attribute contains the
              dates (month, day, and year) of readings stored in the reading buffer.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.dates[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.dates[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number (1 to bufferVar.n).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._dates

    @property
    def formattedreadings(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.formattedreadings[N]`` attribute.

        Description:
            - This attribute contains the stored readings shown as numbers with units and prefixes.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.formattedreadings[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.formattedreadings[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number (1 to bufferVar.n).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._formattedreadings

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
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._fractionalseconds

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
            - ``bufferVar``, the reading buffer.

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
    def ptpseconds(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.ptpseconds[N]`` attribute.

        Description:
            - When enabled by the bufferVar.collecttimestamps attribute, this attribute contains the
              absolute seconds portion of the timestamp of when the reading was stored, in PTP
              format.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.ptpseconds[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.ptpseconds[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number (1 to bufferVar.n).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._ptpseconds

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
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._readings

    @property
    def relativetimestamps(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.relativetimestamps[N]`` attribute.

        Description:
            - This attribute contains the timestamps, in seconds, when each reading occurred,
              relative to the timestamp of the first entry in the reading buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.relativetimestamps[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.relativetimestamps[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number (1 to bufferVar.n).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._relativetimestamps

    @property
    def seconds(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.seconds[N]`` attribute.

        Description:
            - This attribute contains the timestamp of a reading in seconds, in UTC format.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.seconds[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.seconds[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._seconds

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
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._statuses

    @property
    def times(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.times[N]`` attribute.

        Description:
            - When enabled by the bufferVar.collecttimestamps attribute, this attribute contains the
              time of the readings (in hours, minutes, and seconds format) in the reading buffer.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.times[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.times[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._times

    @property
    def timestampresolution(self) -> str:
        """Access the ``bufferVar.timestampresolution`` attribute.

        Description:
            - This attribute contains the resolution of the timestamp.

        Usage:
            - Accessing this property will send the ``print(bufferVar.timestampresolution)`` query.

        TSP Syntax:
            ```
            - print(bufferVar.timestampresolution)
            ```

        Info:
            - ``resolution``, the timestamp resolution in seconds (minimum 1 µs; rounded to an even
              power of 2 µs).
            - ``bufferVar``, the reading buffer.

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
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number (1 to bufferVar.n).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._timestamps

    @property
    def units(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.units[N]`` attribute.

        Description:
            - This attribute contains the unit of measure that is stored with readings in the
              reading buffer.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.units[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.units[N])
            ```

        Info:
            - ``bufferVar``, the reading buffer.
            - ``N``, the reading number (1 to bufferVar.n).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._units

    def clear(self) -> None:
        """Run the ``bufferVar.clear()`` function.

        Description:
            - This function empties the buffer.

        TSP Syntax:
            ```
            - bufferVar.clear()
            ```

        Info:
            - ``bufferVar``, the reading buffer.

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
            - ``bufferVar``, the reading buffer.

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
