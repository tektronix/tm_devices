# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The buffervar commands module.

These commands are used in the following models:
SMU2450, SMU2460, SMU2461, SMU2470

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - bufferVar.capacity
    - bufferVar.clear()
    - bufferVar.dates[N]
    - bufferVar.endindex
    - bufferVar.extraformattedvalues[N]
    - bufferVar.extravalues[N]
    - bufferVar.extravalueunits[N]
    - bufferVar.fillmode
    - bufferVar.formattedreadings[N]
    - bufferVar.fractionalseconds[N]
    - bufferVar.logstate
    - bufferVar.n
    - bufferVar.readings[N]
    - bufferVar.relativetimestamps[N]
    - bufferVar.seconds[N]
    - bufferVar.sourceformattedvalues[N]
    - bufferVar.sourcestatuses[N]
    - bufferVar.sourceunits[N]
    - bufferVar.sourcevalues[N]
    - bufferVar.startindex
    - bufferVar.statuses[N]
    - bufferVar.times[N]
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
        - ``bufferVar``, the name of the reading buffer, which may be a default buffer (defbuffer1
          or defbuffer2) or a user-defined buffer.

    Properties and methods:
        - ``.capacity``: The ``bufferVar.capacity`` attribute.
        - ``.clear()``: The ``bufferVar.clear()`` function.
        - ``.dates``: The ``bufferVar.dates[N]`` attribute.
        - ``.endindex``: The ``bufferVar.endindex`` attribute.
        - ``.extraformattedvalues``: The ``bufferVar.extraformattedvalues[N]`` attribute.
        - ``.extravalues``: The ``bufferVar.extravalues[N]`` attribute.
        - ``.extravalueunits``: The ``bufferVar.extravalueunits[N]`` attribute.
        - ``.fillmode``: The ``bufferVar.fillmode`` attribute.
        - ``.formattedreadings``: The ``bufferVar.formattedreadings[N]`` attribute.
        - ``.fractionalseconds``: The ``bufferVar.fractionalseconds[N]`` attribute.
        - ``.logstate``: The ``bufferVar.logstate`` attribute.
        - ``.n``: The ``bufferVar.n`` attribute.
        - ``.readings``: The ``bufferVar.readings[N]`` attribute.
        - ``.relativetimestamps``: The ``bufferVar.relativetimestamps[N]`` attribute.
        - ``.seconds``: The ``bufferVar.seconds[N]`` attribute.
        - ``.sourceformattedvalues``: The ``bufferVar.sourceformattedvalues[N]`` attribute.
        - ``.sourcestatuses``: The ``bufferVar.sourcestatuses[N]`` attribute.
        - ``.sourceunits``: The ``bufferVar.sourceunits[N]`` attribute.
        - ``.sourcevalues``: The ``bufferVar.sourcevalues[N]`` attribute.
        - ``.startindex``: The ``bufferVar.startindex`` attribute.
        - ``.statuses``: The ``bufferVar.statuses[N]`` attribute.
        - ``.times``: The ``bufferVar.times[N]`` attribute.
        - ``.timestamps``: The ``bufferVar.timestamps[N]`` attribute.
        - ``.units``: The ``bufferVar.units[N]`` attribute.
    """

    def __init__(
        self, device: Optional["TSPControl"] = None, cmd_syntax: str = "bufferVar"
    ) -> None:
        super().__init__(device, cmd_syntax)
        self._dates: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.dates[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.dates[{{key}}])",
            device=self._device,
        )
        self._extraformattedvalues: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.extraformattedvalues[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.extraformattedvalues[{{key}}])",
            device=self._device,
        )
        self._extravalues: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.extravalues[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.extravalues[{{key}}])",
            device=self._device,
        )
        self._extravalueunits: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.extravalueunits[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.extravalueunits[{{key}}])",
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
        self._sourceformattedvalues: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.sourceformattedvalues[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.sourceformattedvalues[{{key}}])",
            device=self._device,
        )
        self._sourcestatuses: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.sourcestatuses[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.sourcestatuses[{{key}}])",
            device=self._device,
        )
        self._sourceunits: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.sourceunits[{{key}}]",
            query_syntax=f"print({self._cmd_syntax}.sourceunits[{{key}}])",
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
    def capacity(self) -> str:
        """Access the ``bufferVar.capacity`` attribute.

        Description:
            - This attribute sets the number of readings a buffer can store.

        Usage:
            - Accessing this property will send the ``print(bufferVar.capacity)`` query.
            - Setting this property to a value will send the ``bufferVar.capacity = value`` command.

        TSP Syntax:
            ```
            - bufferVar.capacity = value
            - print(bufferVar.capacity)
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.

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

    @capacity.setter
    def capacity(self, value: Union[str, float]) -> None:
        """Access the ``bufferVar.capacity`` attribute.

        Description:
            - This attribute sets the number of readings a buffer can store.

        Usage:
            - Accessing this property will send the ``print(bufferVar.capacity)`` query.
            - Setting this property to a value will send the ``bufferVar.capacity = value`` command.

        TSP Syntax:
            ```
            - bufferVar.capacity = value
            - print(bufferVar.capacity)
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".capacity", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.capacity = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.capacity`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def dates(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.dates[N]`` attribute.

        Description:
            - This attribute contains the dates of readings that are stored in the reading buffer.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.dates[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.dates[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._dates

    @property
    def endindex(self) -> str:
        """Access the ``bufferVar.endindex`` attribute.

        Description:
            - This attribute indicates the last index in a reading buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.endindex)`` query.

        TSP Syntax:
            ```
            - print(bufferVar.endindex)
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".endindex"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.endindex)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.endindex`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def extraformattedvalues(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.extraformattedvalues[N]`` attribute.

        Description:
            - This attribute contains the measurement and the unit of measure of the additional
              values in a reading buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.extraformattedvalues[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.extraformattedvalues[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._extraformattedvalues

    @property
    def extravalues(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.extravalues[N]`` attribute.

        Description:
            - This attribute contains the additional values in a reading buffer.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.extravalues[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.extravalues[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._extravalues

    @property
    def extravalueunits(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.extravalueunits[N]`` attribute.

        Description:
            - This attribute contains the units of the additional values in a reading buffer.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.extravalueunits[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.extravalueunits[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._extravalueunits

    @property
    def fillmode(self) -> str:
        """Access the ``bufferVar.fillmode`` attribute.

        Description:
            - This attribute determines if a reading buffer is filled continuously or is filled once
              and stops.

        Usage:
            - Accessing this property will send the ``print(bufferVar.fillmode)`` query.
            - Setting this property to a value will send the ``bufferVar.fillmode = value`` command.

        TSP Syntax:
            ```
            - bufferVar.fillmode = value
            - print(bufferVar.fillmode)
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.

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
            - This attribute determines if a reading buffer is filled continuously or is filled once
              and stops.

        Usage:
            - Accessing this property will send the ``print(bufferVar.fillmode)`` query.
            - Setting this property to a value will send the ``bufferVar.fillmode = value`` command.

        TSP Syntax:
            ```
            - bufferVar.fillmode = value
            - print(bufferVar.fillmode)
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.

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
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

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
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._fractionalseconds

    @property
    def logstate(self) -> str:
        """Access the ``bufferVar.logstate`` attribute.

        Description:
            - This attribute indicates if information events are logged when the specified reading
              buffer is at 0% or 100% filled.

        Usage:
            - Accessing this property will send the ``print(bufferVar.logstate)`` query.
            - Setting this property to a value will send the ``bufferVar.logstate = value`` command.

        TSP Syntax:
            ```
            - bufferVar.logstate = value
            - print(bufferVar.logstate)
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".logstate"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.logstate)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.logstate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @logstate.setter
    def logstate(self, value: Union[str, float]) -> None:
        """Access the ``bufferVar.logstate`` attribute.

        Description:
            - This attribute indicates if information events are logged when the specified reading
              buffer is at 0% or 100% filled.

        Usage:
            - Accessing this property will send the ``print(bufferVar.logstate)`` query.
            - Setting this property to a value will send the ``bufferVar.logstate = value`` command.

        TSP Syntax:
            ```
            - bufferVar.logstate = value
            - print(bufferVar.logstate)
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".logstate", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.logstate = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.logstate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def n(self) -> str:
        """Access the ``bufferVar.n`` attribute.

        Description:
            - This attribute contains the number of readings in the specified reading buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.n)`` query.

        TSP Syntax:
            ```
            - print(bufferVar.n)
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.

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
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
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
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

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
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._seconds

    @property
    def sourceformattedvalues(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourceformattedvalues[N]`` attribute.

        Description:
            - This attribute contains the source levels formatted as they appear on the front-panel
              display when the readings in the reading buffer were acquired.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.sourceformattedvalues[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.sourceformattedvalues[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._sourceformattedvalues

    @property
    def sourcestatuses(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourcestatuses[N]`` attribute.

        Description:
            - This attribute contains the source status conditions of the instrument for the reading
              point.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.sourcestatuses[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.sourcestatuses[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._sourcestatuses

    @property
    def sourceunits(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourceunits[N]`` attribute.

        Description:
            - This attribute contains the units of measure of the source.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.sourceunits[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.sourceunits[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._sourceunits

    @property
    def sourcevalues(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.sourcevalues[N]`` attribute.

        Description:
            - This attribute contains the source levels being output when readings in the reading
              buffer were acquired.

        Usage:
            - Accessing an item from this property will send the
              ``print(bufferVar.sourcevalues[N])`` query.

        TSP Syntax:
            ```
            - print(bufferVar.sourcevalues[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._sourcevalues

    @property
    def startindex(self) -> str:
        """Access the ``bufferVar.startindex`` attribute.

        Description:
            - This attribute indicates the starting index in a reading buffer.

        Usage:
            - Accessing this property will send the ``print(bufferVar.startindex)`` query.

        TSP Syntax:
            ```
            - print(bufferVar.startindex)
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".startindex"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.startindex)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.startindex`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

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
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
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
            - This attribute contains the time when the instrument made the reading.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.times[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.times[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._times

    @property
    def timestamps(self) -> Dict[int, Union[str, float]]:
        """Access the ``bufferVar.timestamps[N]`` attribute.

        Description:
            - This attribute contains the timestamp when each reading saved in the specified reading
              buffer occurred.

        Usage:
            - Accessing an item from this property will send the ``print(bufferVar.timestamps[N])``
              query.

        TSP Syntax:
            ```
            - print(bufferVar.timestamps[N])
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

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
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.
            - ``N``, the reading number N; can be any value from 1 to the number of readings in the
              buffer; use the bufferVar.n command to determine the number of readings in the buffer.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._units

    def clear(self) -> None:
        """Run the ``bufferVar.clear()`` function.

        Description:
            - This function clears all readings and statistics from the specified buffer.

        TSP Syntax:
            ```
            - bufferVar.clear()
            ```

        Info:
            - ``bufferVar``, the name of the reading buffer, which may be a default buffer
              (defbuffer1 or defbuffer2) or a user-defined buffer.

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
