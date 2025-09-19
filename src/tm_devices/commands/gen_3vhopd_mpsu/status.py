# pyright: reportConstantRedefinition=none
"""The status commands module.

These commands are used in the following models:
MPSU50_2ST

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - status.measurement.condition
    - status.measurement.current_limit.condition
    - status.measurement.current_limit.enable
    - status.measurement.current_limit.event
    - status.measurement.current_limit.ntr
    - status.measurement.current_limit.ptr
    - status.measurement.enable
    - status.measurement.event
    - status.measurement.instrument.condition
    - status.measurement.instrument.enable
    - status.measurement.instrument.event
    - status.measurement.instrument.ntr
    - status.measurement.instrument.psu[X].condition
    - status.measurement.instrument.psu[X].enable
    - status.measurement.instrument.psu[X].event
    - status.measurement.instrument.psu[X].ntr
    - status.measurement.instrument.psu[X].ptr
    - status.measurement.instrument.ptr
    - status.measurement.ntr
    - status.measurement.protection.condition
    - status.measurement.protection.enable
    - status.measurement.protection.event
    - status.measurement.protection.ntr
    - status.measurement.protection.ptr
    - status.measurement.ptr
    - status.measurement.reading_overflow.condition
    - status.measurement.reading_overflow.enable
    - status.measurement.reading_overflow.event
    - status.measurement.reading_overflow.ntr
    - status.measurement.reading_overflow.ptr
    - status.operation.calibrating.condition
    - status.operation.calibrating.enable
    - status.operation.calibrating.event
    - status.operation.calibrating.ntr
    - status.operation.calibrating.ptr
    - status.operation.condition
    - status.operation.enable
    - status.operation.event
    - status.operation.instrument.condition
    - status.operation.instrument.enable
    - status.operation.instrument.event
    - status.operation.instrument.ntr
    - status.operation.instrument.psu[X].condition
    - status.operation.instrument.psu[X].enable
    - status.operation.instrument.psu[X].event
    - status.operation.instrument.psu[X].ntr
    - status.operation.instrument.psu[X].ptr
    - status.operation.instrument.ptr
    - status.operation.measuring.condition
    - status.operation.measuring.enable
    - status.operation.measuring.event
    - status.operation.measuring.ntr
    - status.operation.measuring.ptr
    - status.operation.ntr
    - status.operation.ptr
    - status.operation.sweeping.condition
    - status.operation.sweeping.enable
    - status.operation.sweeping.event
    - status.operation.sweeping.ntr
    - status.operation.sweeping.ptr
    - status.questionable.calibration.condition
    - status.questionable.calibration.enable
    - status.questionable.calibration.event
    - status.questionable.calibration.ntr
    - status.questionable.calibration.ptr
    - status.questionable.condition
    - status.questionable.enable
    - status.questionable.event
    - status.questionable.instrument.condition
    - status.questionable.instrument.enable
    - status.questionable.instrument.event
    - status.questionable.instrument.ntr
    - status.questionable.instrument.psu[X].condition
    - status.questionable.instrument.psu[X].enable
    - status.questionable.instrument.psu[X].event
    - status.questionable.instrument.psu[X].ntr
    - status.questionable.instrument.psu[X].ptr
    - status.questionable.instrument.ptr
    - status.questionable.ntr
    - status.questionable.over_temperature.condition
    - status.questionable.over_temperature.enable
    - status.questionable.over_temperature.event
    - status.questionable.over_temperature.ntr
    - status.questionable.over_temperature.ptr
    - status.questionable.ptr
    - status.reset()
    ```
"""

from typing import Dict, Optional, TYPE_CHECKING, Union

from ..helpers import (
    BaseTSPCmd,
    DefaultDictPassKeyToFactory,
    NoDeviceProvidedError,
    ValidatedDynamicNumberCmd,
)

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class StatusQuestionableOverTemperature(BaseTSPCmd):
    """The ``status.questionable.over_temperature`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.questionable.over_temperature.condition`` attribute.
        - ``.enable``: The ``status.questionable.over_temperature.enable`` attribute.
        - ``.event``: The ``status.questionable.over_temperature.event`` attribute.
        - ``.ntr``: The ``status.questionable.over_temperature.ntr`` attribute.
        - ``.ptr``: The ``status.questionable.over_temperature.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.over_temperature.condition`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.condition)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.over_temperature.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.questionable.over_temperature.enable`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.enable = value
            - print(status.questionable.over_temperature.enable)
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
        """Access the ``status.questionable.over_temperature.enable`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.enable = value
            - print(status.questionable.over_temperature.enable)
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
    def event(self) -> str:
        """Access the ``status.questionable.over_temperature.event`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.event)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.over_temperature.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.questionable.over_temperature.ntr`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.ntr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.ntr = value
            - print(status.questionable.over_temperature.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.questionable.over_temperature.ntr`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.ntr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.ntr = value
            - print(status.questionable.over_temperature.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.questionable.over_temperature.ptr`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.ptr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.ptr = value
            - print(status.questionable.over_temperature.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.questionable.over_temperature.ptr`` attribute.

        Description:
            - This attribute contains the Questionable Status Overtemperature Summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.over_temperature.ptr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.over_temperature.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.over_temperature.ptr = value
            - print(status.questionable.over_temperature.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusQuestionableInstrumentPsuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``status.questionable.instrument.psu[X]`` command tree.

    Info:
        - ``X``, the channel of the PSU: 1 or 2.

    Properties and methods:
        - ``.condition``: The ``status.questionable.instrument.psu[X].condition`` attribute.
        - ``.enable``: The ``status.questionable.instrument.psu[X].enable`` attribute.
        - ``.event``: The ``status.questionable.instrument.psu[X].event`` attribute.
        - ``.ntr``: The ``status.questionable.instrument.psu[X].ntr`` attribute.
        - ``.ptr``: The ``status.questionable.instrument.psu[X].ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.instrument.psu[X].condition`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.psu[X].condition)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.instrument.psu[X].condition)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.questionable.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.psu[X].enable = value
            - print(status.questionable.instrument.psu[X].enable)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

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
        """Access the ``status.questionable.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.psu[X].enable = value
            - print(status.questionable.instrument.psu[X].enable)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

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
    def event(self) -> str:
        """Access the ``status.questionable.instrument.psu[X].event`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.psu[X].event)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.instrument.psu[X].event)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.questionable.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.psu[X].ntr = value
            - print(status.questionable.instrument.psu[X].ntr)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.questionable.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.psu[X].ntr = value
            - print(status.questionable.instrument.psu[X].ntr)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.questionable.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.psu[X].ptr = value
            - print(status.questionable.instrument.psu[X].ptr)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.questionable.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the questionable status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.psu[X].ptr = value
            - print(status.questionable.instrument.psu[X].ptr)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusQuestionableInstrument(BaseTSPCmd):
    """The ``status.questionable.instrument`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.questionable.instrument.condition`` attribute.
        - ``.enable``: The ``status.questionable.instrument.enable`` attribute.
        - ``.event``: The ``status.questionable.instrument.event`` attribute.
        - ``.ntr``: The ``status.questionable.instrument.ntr`` attribute.
        - ``.psu``: The ``status.questionable.instrument.psu[X]`` command tree.
        - ``.ptr``: The ``status.questionable.instrument.ptr`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._psu: Dict[int, StatusQuestionableInstrumentPsuItem] = DefaultDictPassKeyToFactory(
            lambda x: StatusQuestionableInstrumentPsuItem(device, f"{self._cmd_syntax}.psu[{x}]")
        )

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.instrument.condition`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.instrument.condition)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.instrument.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.questionable.instrument.enable`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.enable = value
            - print(status.questionable.instrument.enable)
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
        """Access the ``status.questionable.instrument.enable`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.enable = value
            - print(status.questionable.instrument.enable)
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
    def event(self) -> str:
        """Access the ``status.questionable.instrument.event`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.event)``
              query.

        TSP Syntax:
            ```
            - print(status.questionable.instrument.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.questionable.instrument.ntr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.ntr = value
            - print(status.questionable.instrument.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.questionable.instrument.ntr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.ntr = value
            - print(status.questionable.instrument.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def psu(self) -> Dict[int, StatusQuestionableInstrumentPsuItem]:
        """Return the ``status.questionable.instrument.psu[X]`` command tree.

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.questionable.instrument.psu[X].condition`` attribute.
            - ``.enable``: The ``status.questionable.instrument.psu[X].enable`` attribute.
            - ``.event``: The ``status.questionable.instrument.psu[X].event`` attribute.
            - ``.ntr``: The ``status.questionable.instrument.psu[X].ntr`` attribute.
            - ``.ptr``: The ``status.questionable.instrument.psu[X].ptr`` attribute.
        """
        return self._psu

    @property
    def ptr(self) -> str:
        """Access the ``status.questionable.instrument.ptr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.ptr = value
            - print(status.questionable.instrument.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.questionable.instrument.ptr`` attribute.

        Description:
            - This attribute contains the questionable status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.instrument.ptr = value
            - print(status.questionable.instrument.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusQuestionableCalibration(BaseTSPCmd):
    """The ``status.questionable.calibration`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.questionable.calibration.condition`` attribute.
        - ``.enable``: The ``status.questionable.calibration.enable`` attribute.
        - ``.event``: The ``status.questionable.calibration.event`` attribute.
        - ``.ntr``: The ``status.questionable.calibration.ntr`` attribute.
        - ``.ptr``: The ``status.questionable.calibration.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.calibration.condition`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.calibration.condition)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.calibration.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.questionable.calibration.enable`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.calibration.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.enable = value
            - print(status.questionable.calibration.enable)
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
        """Access the ``status.questionable.calibration.enable`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.questionable.calibration.enable)`` query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.enable = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.enable = value
            - print(status.questionable.calibration.enable)
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
    def event(self) -> str:
        """Access the ``status.questionable.calibration.event`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.calibration.event)``
              query.

        TSP Syntax:
            ```
            - print(status.questionable.calibration.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.questionable.calibration.ntr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.calibration.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.ntr = value
            - print(status.questionable.calibration.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.questionable.calibration.ntr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.calibration.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.ntr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.ntr = value
            - print(status.questionable.calibration.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.questionable.calibration.ptr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.calibration.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.ptr = value
            - print(status.questionable.calibration.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.questionable.calibration.ptr`` attribute.

        Description:
            - This attribute contains the questionable status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.questionable.calibration.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.questionable.calibration.ptr = value`` command.

        TSP Syntax:
            ```
            - status.questionable.calibration.ptr = value
            - print(status.questionable.calibration.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusQuestionable(BaseTSPCmd):
    """The ``status.questionable`` command tree.

    Properties and methods:
        - ``.calibration``: The ``status.questionable.calibration`` command tree.
        - ``.condition``: The ``status.questionable.condition`` attribute.
        - ``.enable``: The ``status.questionable.enable`` attribute.
        - ``.event``: The ``status.questionable.event`` attribute.
        - ``.instrument``: The ``status.questionable.instrument`` command tree.
        - ``.ntr``: The ``status.questionable.ntr`` attribute.
        - ``.over_temperature``: The ``status.questionable.over_temperature`` command tree.
        - ``.ptr``: The ``status.questionable.ptr`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._calibration = StatusQuestionableCalibration(device, f"{self._cmd_syntax}.calibration")
        self._instrument = StatusQuestionableInstrument(device, f"{self._cmd_syntax}.instrument")
        self._over_temperature = StatusQuestionableOverTemperature(
            device, f"{self._cmd_syntax}.over_temperature"
        )

    @property
    def calibration(self) -> StatusQuestionableCalibration:
        """Return the ``status.questionable.calibration`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.questionable.calibration.condition`` attribute.
            - ``.enable``: The ``status.questionable.calibration.enable`` attribute.
            - ``.event``: The ``status.questionable.calibration.event`` attribute.
            - ``.ntr``: The ``status.questionable.calibration.ntr`` attribute.
            - ``.ptr``: The ``status.questionable.calibration.ptr`` attribute.
        """
        return self._calibration

    @property
    def condition(self) -> str:
        """Access the ``status.questionable.condition`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.condition)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.questionable.enable`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.enable)`` query.
            - Setting this property to a value will send the ``status.questionable.enable = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.enable = value
            - print(status.questionable.enable)
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
        """Access the ``status.questionable.enable`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.enable)`` query.
            - Setting this property to a value will send the ``status.questionable.enable = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.enable = value
            - print(status.questionable.enable)
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
    def event(self) -> str:
        """Access the ``status.questionable.event`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.event)`` query.

        TSP Syntax:
            ```
            - print(status.questionable.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def instrument(self) -> StatusQuestionableInstrument:
        """Return the ``status.questionable.instrument`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.questionable.instrument.condition`` attribute.
            - ``.enable``: The ``status.questionable.instrument.enable`` attribute.
            - ``.event``: The ``status.questionable.instrument.event`` attribute.
            - ``.ntr``: The ``status.questionable.instrument.ntr`` attribute.
            - ``.psu``: The ``status.questionable.instrument.psu[X]`` command tree.
            - ``.ptr``: The ``status.questionable.instrument.ptr`` attribute.
        """
        return self._instrument

    @property
    def ntr(self) -> str:
        """Access the ``status.questionable.ntr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.ntr)`` query.
            - Setting this property to a value will send the ``status.questionable.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.ntr = value
            - print(status.questionable.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.questionable.ntr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.ntr)`` query.
            - Setting this property to a value will send the ``status.questionable.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.ntr = value
            - print(status.questionable.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def over_temperature(self) -> StatusQuestionableOverTemperature:
        """Return the ``status.questionable.over_temperature`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.questionable.over_temperature.condition`` attribute.
            - ``.enable``: The ``status.questionable.over_temperature.enable`` attribute.
            - ``.event``: The ``status.questionable.over_temperature.event`` attribute.
            - ``.ntr``: The ``status.questionable.over_temperature.ntr`` attribute.
            - ``.ptr``: The ``status.questionable.over_temperature.ptr`` attribute.
        """
        return self._over_temperature

    @property
    def ptr(self) -> str:
        """Access the ``status.questionable.ptr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.ptr)`` query.
            - Setting this property to a value will send the ``status.questionable.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.ptr = value
            - print(status.questionable.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.questionable.ptr`` attribute.

        Description:
            - These attributes manage the questionable status register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.questionable.ptr)`` query.
            - Setting this property to a value will send the ``status.questionable.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.questionable.ptr = value
            - print(status.questionable.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusOperationSweeping(BaseTSPCmd):
    """The ``status.operation.sweeping`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.sweeping.condition`` attribute.
        - ``.enable``: The ``status.operation.sweeping.enable`` attribute.
        - ``.event``: The ``status.operation.sweeping.event`` attribute.
        - ``.ntr``: The ``status.operation.sweeping.ntr`` attribute.
        - ``.ptr``: The ``status.operation.sweeping.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.operation.sweeping.condition`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.condition)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.sweeping.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.operation.sweeping.enable`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.enable = value
            - print(status.operation.sweeping.enable)
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
        """Access the ``status.operation.sweeping.enable`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.enable = value
            - print(status.operation.sweeping.enable)
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
    def event(self) -> str:
        """Access the ``status.operation.sweeping.event`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.sweeping.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.operation.sweeping.ntr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.ntr = value
            - print(status.operation.sweeping.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.sweeping.ntr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.ntr = value
            - print(status.operation.sweeping.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.operation.sweeping.ptr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.ptr = value
            - print(status.operation.sweeping.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.sweeping.ptr`` attribute.

        Description:
            - This attribute contains the operation status sweeping summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.sweeping.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.sweeping.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.sweeping.ptr = value
            - print(status.operation.sweeping.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusOperationMeasuring(BaseTSPCmd):
    """The ``status.operation.measuring`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.measuring.condition`` attribute.
        - ``.enable``: The ``status.operation.measuring.enable`` attribute.
        - ``.event``: The ``status.operation.measuring.event`` attribute.
        - ``.ntr``: The ``status.operation.measuring.ntr`` attribute.
        - ``.ptr``: The ``status.operation.measuring.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.operation.measuring.condition`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.condition)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.measuring.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.operation.measuring.enable`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.measuring.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.enable = value
            - print(status.operation.measuring.enable)
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
        """Access the ``status.operation.measuring.enable`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.measuring.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.enable = value
            - print(status.operation.measuring.enable)
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
    def event(self) -> str:
        """Access the ``status.operation.measuring.event`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.measuring.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.operation.measuring.ntr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.measuring.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.ntr = value
            - print(status.operation.measuring.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.measuring.ntr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.measuring.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.ntr = value
            - print(status.operation.measuring.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.operation.measuring.ptr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.measuring.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.ptr = value
            - print(status.operation.measuring.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.measuring.ptr`` attribute.

        Description:
            - This attribute contains the operation status measuring summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.measuring.ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.measuring.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.measuring.ptr = value
            - print(status.operation.measuring.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusOperationInstrumentPsuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``status.operation.instrument.psu[X]`` command tree.

    Info:
        - ``X``, the power supply unit (PSU) channel (for example
          slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.psu[X].condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.psu[X].enable`` attribute.
        - ``.event``: The ``status.operation.instrument.psu[X].event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.psu[X].ntr`` attribute.
        - ``.ptr``: The ``status.operation.instrument.psu[X].ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.psu[X].condition`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.psu[X].condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.psu[X].condition)
            ```

        Info:
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.operation.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.psu[X].enable = value
            - print(status.operation.instrument.psu[X].enable)
            ```

        Info:
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

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
        """Access the ``status.operation.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.psu[X].enable = value
            - print(status.operation.instrument.psu[X].enable)
            ```

        Info:
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

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
    def event(self) -> str:
        """Access the ``status.operation.instrument.psu[X].event`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.psu[X].event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.psu[X].event)
            ```

        Info:
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.operation.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.psu[X].ntr = value
            - print(status.operation.instrument.psu[X].ntr)
            ```

        Info:
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.psu[X].ntr = value
            - print(status.operation.instrument.psu[X].ntr)
            ```

        Info:
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.operation.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.psu[X].ptr = value
            - print(status.operation.instrument.psu[X].ptr)
            ```

        Info:
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the operation status PSU summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``status.operation.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.psu[X].ptr = value
            - print(status.operation.instrument.psu[X].ptr)
            ```

        Info:
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusOperationInstrument(BaseTSPCmd):
    """The ``status.operation.instrument`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.instrument.condition`` attribute.
        - ``.enable``: The ``status.operation.instrument.enable`` attribute.
        - ``.event``: The ``status.operation.instrument.event`` attribute.
        - ``.ntr``: The ``status.operation.instrument.ntr`` attribute.
        - ``.psu``: The ``status.operation.instrument.psu[X]`` command tree.
        - ``.ptr``: The ``status.operation.instrument.ptr`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._psu: Dict[int, StatusOperationInstrumentPsuItem] = DefaultDictPassKeyToFactory(
            lambda x: StatusOperationInstrumentPsuItem(device, f"{self._cmd_syntax}.psu[{x}]")
        )

    @property
    def condition(self) -> str:
        """Access the ``status.operation.instrument.condition`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.condition)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.operation.instrument.enable`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.enable = value
            - print(status.operation.instrument.enable)
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
        """Access the ``status.operation.instrument.enable`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.enable = value
            - print(status.operation.instrument.enable)
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
    def event(self) -> str:
        """Access the ``status.operation.instrument.event`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.instrument.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.operation.instrument.ntr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.ntr = value
            - print(status.operation.instrument.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.instrument.ntr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.ntr = value
            - print(status.operation.instrument.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def psu(self) -> Dict[int, StatusOperationInstrumentPsuItem]:
        """Return the ``status.operation.instrument.psu[X]`` command tree.

        Info:
            - ``X``, the power supply unit (PSU) channel (for example
              slot[1].status.operation.instrument.psu[1].enable applies to PSU channel 1 in slot 1).

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.psu[X].condition`` attribute.
            - ``.enable``: The ``status.operation.instrument.psu[X].enable`` attribute.
            - ``.event``: The ``status.operation.instrument.psu[X].event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.psu[X].ntr`` attribute.
            - ``.ptr``: The ``status.operation.instrument.psu[X].ptr`` attribute.
        """
        return self._psu

    @property
    def ptr(self) -> str:
        """Access the ``status.operation.instrument.ptr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.ptr = value
            - print(status.operation.instrument.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.instrument.ptr`` attribute.

        Description:
            - This attribute contains the operation status instrument summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.instrument.ptr = value
            - print(status.operation.instrument.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusOperationCalibrating(BaseTSPCmd):
    """The ``status.operation.calibrating`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.operation.calibrating.condition`` attribute.
        - ``.enable``: The ``status.operation.calibrating.enable`` attribute.
        - ``.event``: The ``status.operation.calibrating.event`` attribute.
        - ``.ntr``: The ``status.operation.calibrating.ntr`` attribute.
        - ``.ptr``: The ``status.operation.calibrating.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.operation.calibrating.condition`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.operation.calibrating.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.calibrating.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.operation.calibrating.enable`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.enable = value
            - print(status.operation.calibrating.enable)
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
        """Access the ``status.operation.calibrating.enable`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.enable)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.enable = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.enable = value
            - print(status.operation.calibrating.enable)
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
    def event(self) -> str:
        """Access the ``status.operation.calibrating.event`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.event)``
              query.

        TSP Syntax:
            ```
            - print(status.operation.calibrating.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.operation.calibrating.ntr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.ntr = value
            - print(status.operation.calibrating.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.calibrating.ntr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.ntr = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.ntr = value
            - print(status.operation.calibrating.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.operation.calibrating.ptr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.ptr = value
            - print(status.operation.calibrating.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.calibrating.ptr`` attribute.

        Description:
            - This attribute contains the operation status calibration summary register set.

        Usage:
            - Accessing this property will send the ``print(status.operation.calibrating.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.operation.calibrating.ptr = value`` command.

        TSP Syntax:
            ```
            - status.operation.calibrating.ptr = value
            - print(status.operation.calibrating.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusOperation(BaseTSPCmd):
    """The ``status.operation`` command tree.

    Properties and methods:
        - ``.calibrating``: The ``status.operation.calibrating`` command tree.
        - ``.condition``: The ``status.operation.condition`` attribute.
        - ``.enable``: The ``status.operation.enable`` attribute.
        - ``.event``: The ``status.operation.event`` attribute.
        - ``.instrument``: The ``status.operation.instrument`` command tree.
        - ``.measuring``: The ``status.operation.measuring`` command tree.
        - ``.ntr``: The ``status.operation.ntr`` attribute.
        - ``.ptr``: The ``status.operation.ptr`` attribute.
        - ``.sweeping``: The ``status.operation.sweeping`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._calibrating = StatusOperationCalibrating(device, f"{self._cmd_syntax}.calibrating")
        self._instrument = StatusOperationInstrument(device, f"{self._cmd_syntax}.instrument")
        self._measuring = StatusOperationMeasuring(device, f"{self._cmd_syntax}.measuring")
        self._sweeping = StatusOperationSweeping(device, f"{self._cmd_syntax}.sweeping")

    @property
    def calibrating(self) -> StatusOperationCalibrating:
        """Return the ``status.operation.calibrating`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.calibrating.condition`` attribute.
            - ``.enable``: The ``status.operation.calibrating.enable`` attribute.
            - ``.event``: The ``status.operation.calibrating.event`` attribute.
            - ``.ntr``: The ``status.operation.calibrating.ntr`` attribute.
            - ``.ptr``: The ``status.operation.calibrating.ptr`` attribute.
        """
        return self._calibrating

    @property
    def condition(self) -> str:
        """Access the ``status.operation.condition`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.condition)`` query.

        TSP Syntax:
            ```
            - print(status.operation.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.operation.enable`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.enable)`` query.
            - Setting this property to a value will send the ``status.operation.enable = value``
              command.

        TSP Syntax:
            ```
            - status.operation.enable = value
            - print(status.operation.enable)
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
        """Access the ``status.operation.enable`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.enable)`` query.
            - Setting this property to a value will send the ``status.operation.enable = value``
              command.

        TSP Syntax:
            ```
            - status.operation.enable = value
            - print(status.operation.enable)
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
    def event(self) -> str:
        """Access the ``status.operation.event`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.event)`` query.

        TSP Syntax:
            ```
            - print(status.operation.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def instrument(self) -> StatusOperationInstrument:
        """Return the ``status.operation.instrument`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.instrument.condition`` attribute.
            - ``.enable``: The ``status.operation.instrument.enable`` attribute.
            - ``.event``: The ``status.operation.instrument.event`` attribute.
            - ``.ntr``: The ``status.operation.instrument.ntr`` attribute.
            - ``.psu``: The ``status.operation.instrument.psu[X]`` command tree.
            - ``.ptr``: The ``status.operation.instrument.ptr`` attribute.
        """
        return self._instrument

    @property
    def measuring(self) -> StatusOperationMeasuring:
        """Return the ``status.operation.measuring`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.measuring.condition`` attribute.
            - ``.enable``: The ``status.operation.measuring.enable`` attribute.
            - ``.event``: The ``status.operation.measuring.event`` attribute.
            - ``.ntr``: The ``status.operation.measuring.ntr`` attribute.
            - ``.ptr``: The ``status.operation.measuring.ptr`` attribute.
        """
        return self._measuring

    @property
    def ntr(self) -> str:
        """Access the ``status.operation.ntr`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.ntr)`` query.
            - Setting this property to a value will send the ``status.operation.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.ntr = value
            - print(status.operation.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.ntr`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.ntr)`` query.
            - Setting this property to a value will send the ``status.operation.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.ntr = value
            - print(status.operation.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.operation.ptr`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.ptr)`` query.
            - Setting this property to a value will send the ``status.operation.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.ptr = value
            - print(status.operation.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.operation.ptr`` attribute.

        Description:
            - These attributes manage the Operation Status Register set of the status model.

        Usage:
            - Accessing this property will send the ``print(status.operation.ptr)`` query.
            - Setting this property to a value will send the ``status.operation.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.operation.ptr = value
            - print(status.operation.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def sweeping(self) -> StatusOperationSweeping:
        """Return the ``status.operation.sweeping`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.operation.sweeping.condition`` attribute.
            - ``.enable``: The ``status.operation.sweeping.enable`` attribute.
            - ``.event``: The ``status.operation.sweeping.event`` attribute.
            - ``.ntr``: The ``status.operation.sweeping.ntr`` attribute.
            - ``.ptr``: The ``status.operation.sweeping.ptr`` attribute.
        """
        return self._sweeping


class StatusMeasurementReadingOverflow(BaseTSPCmd):
    """The ``status.measurement.reading_overflow`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.measurement.reading_overflow.condition`` attribute.
        - ``.enable``: The ``status.measurement.reading_overflow.enable`` attribute.
        - ``.event``: The ``status.measurement.reading_overflow.event`` attribute.
        - ``.ntr``: The ``status.measurement.reading_overflow.ntr`` attribute.
        - ``.ptr``: The ``status.measurement.reading_overflow.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.reading_overflow.condition`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.reading_overflow.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.measurement.reading_overflow.enable`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.enable = value
            - print(status.measurement.reading_overflow.enable)
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
        """Access the ``status.measurement.reading_overflow.enable`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.enable = value
            - print(status.measurement.reading_overflow.enable)
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
    def event(self) -> str:
        """Access the ``status.measurement.reading_overflow.event`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.event)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.reading_overflow.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.measurement.reading_overflow.ntr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.ntr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.ntr = value
            - print(status.measurement.reading_overflow.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.reading_overflow.ntr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.ntr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.ntr = value
            - print(status.measurement.reading_overflow.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.measurement.reading_overflow.ptr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.ptr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.ptr = value
            - print(status.measurement.reading_overflow.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.reading_overflow.ptr`` attribute.

        Description:
            - This attribute contains the measurement event reading overflow summary register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.reading_overflow.ptr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.reading_overflow.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.reading_overflow.ptr = value
            - print(status.measurement.reading_overflow.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusMeasurementProtection(BaseTSPCmd):
    """The ``status.measurement.protection`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.measurement.protection.condition`` attribute.
        - ``.enable``: The ``status.measurement.protection.enable`` attribute.
        - ``.event``: The ``status.measurement.protection.event`` attribute.
        - ``.ntr``: The ``status.measurement.protection.ntr`` attribute.
        - ``.ptr``: The ``status.measurement.protection.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.protection.condition`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.protection.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.protection.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.measurement.protection.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.protection.enable)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.protection.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.protection.enable = value
            - print(status.measurement.protection.enable)
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
        """Access the ``status.measurement.protection.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.protection.enable)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.protection.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.protection.enable = value
            - print(status.measurement.protection.enable)
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
    def event(self) -> str:
        """Access the ``status.measurement.protection.event`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.protection.event)``
              query.

        TSP Syntax:
            ```
            - print(status.measurement.protection.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.measurement.protection.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.protection.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.protection.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.protection.ntr = value
            - print(status.measurement.protection.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.protection.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.protection.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.protection.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.protection.ntr = value
            - print(status.measurement.protection.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.measurement.protection.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.protection.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.protection.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.protection.ptr = value
            - print(status.measurement.protection.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.protection.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event protection summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.protection.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.protection.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.protection.ptr = value
            - print(status.measurement.protection.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusMeasurementInstrumentPsuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``status.measurement.instrument.psu[X]`` command tree.

    Info:
        - ``X``, the channel of the PSU: 1 or 2.

    Properties and methods:
        - ``.condition``: The ``status.measurement.instrument.psu[X].condition`` attribute.
        - ``.enable``: The ``status.measurement.instrument.psu[X].enable`` attribute.
        - ``.event``: The ``status.measurement.instrument.psu[X].event`` attribute.
        - ``.ntr``: The ``status.measurement.instrument.psu[X].ntr`` attribute.
        - ``.ptr``: The ``status.measurement.instrument.psu[X].ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.instrument.psu[X].condition`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.psu[X].condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.instrument.psu[X].condition)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.measurement.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.psu[X].enable = value
            - print(status.measurement.instrument.psu[X].enable)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

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
        """Access the ``status.measurement.instrument.psu[X].enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.psu[X].enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.psu[X].enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.psu[X].enable = value
            - print(status.measurement.instrument.psu[X].enable)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

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
    def event(self) -> str:
        """Access the ``status.measurement.instrument.psu[X].event`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.psu[X].event)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.instrument.psu[X].event)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.measurement.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.psu[X].ntr = value
            - print(status.measurement.instrument.psu[X].ntr)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.instrument.psu[X].ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.psu[X].ntr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.psu[X].ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.psu[X].ntr = value
            - print(status.measurement.instrument.psu[X].ntr)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.measurement.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.psu[X].ptr = value
            - print(status.measurement.instrument.psu[X].ptr)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.instrument.psu[X].ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event PSU 1 summary register
              set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.psu[X].ptr)`` query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.psu[X].ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.psu[X].ptr = value
            - print(status.measurement.instrument.psu[X].ptr)
            ```

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusMeasurementInstrument(BaseTSPCmd):
    """The ``status.measurement.instrument`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.measurement.instrument.condition`` attribute.
        - ``.enable``: The ``status.measurement.instrument.enable`` attribute.
        - ``.event``: The ``status.measurement.instrument.event`` attribute.
        - ``.ntr``: The ``status.measurement.instrument.ntr`` attribute.
        - ``.psu``: The ``status.measurement.instrument.psu[X]`` command tree.
        - ``.ptr``: The ``status.measurement.instrument.ptr`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._psu: Dict[int, StatusMeasurementInstrumentPsuItem] = DefaultDictPassKeyToFactory(
            lambda x: StatusMeasurementInstrumentPsuItem(device, f"{self._cmd_syntax}.psu[{x}]")
        )

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.instrument.condition`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.instrument.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.instrument.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.measurement.instrument.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.enable = value
            - print(status.measurement.instrument.enable)
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
        """Access the ``status.measurement.instrument.enable`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.enable)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.enable = value
            - print(status.measurement.instrument.enable)
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
    def event(self) -> str:
        """Access the ``status.measurement.instrument.event`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.event)``
              query.

        TSP Syntax:
            ```
            - print(status.measurement.instrument.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.measurement.instrument.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.ntr = value
            - print(status.measurement.instrument.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.instrument.ntr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.ntr = value
            - print(status.measurement.instrument.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def psu(self) -> Dict[int, StatusMeasurementInstrumentPsuItem]:
        """Return the ``status.measurement.instrument.psu[X]`` command tree.

        Info:
            - ``X``, the channel of the PSU: 1 or 2.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.instrument.psu[X].condition`` attribute.
            - ``.enable``: The ``status.measurement.instrument.psu[X].enable`` attribute.
            - ``.event``: The ``status.measurement.instrument.psu[X].event`` attribute.
            - ``.ntr``: The ``status.measurement.instrument.psu[X].ntr`` attribute.
            - ``.ptr``: The ``status.measurement.instrument.psu[X].ptr`` attribute.
        """
        return self._psu

    @property
    def ptr(self) -> str:
        """Access the ``status.measurement.instrument.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.ptr = value
            - print(status.measurement.instrument.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.instrument.ptr`` attribute.

        Description:
            - This attribute contains the registers of the measurement event instrument summary
              register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.instrument.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.instrument.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.instrument.ptr = value
            - print(status.measurement.instrument.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusMeasurementCurrentLimit(BaseTSPCmd):
    """The ``status.measurement.current_limit`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.measurement.current_limit.condition`` attribute.
        - ``.enable``: The ``status.measurement.current_limit.enable`` attribute.
        - ``.event``: The ``status.measurement.current_limit.event`` attribute.
        - ``.ntr``: The ``status.measurement.current_limit.ntr`` attribute.
        - ``.ptr``: The ``status.measurement.current_limit.ptr`` attribute.
    """

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.current_limit.condition`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.current_limit.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.current_limit.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enable(self) -> str:
        """Access the ``status.measurement.current_limit.enable`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.current_limit.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.enable = value
            - print(status.measurement.current_limit.enable)
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
        """Access the ``status.measurement.current_limit.enable`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.current_limit.enable)`` query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.enable = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.enable = value
            - print(status.measurement.current_limit.enable)
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
    def event(self) -> str:
        """Access the ``status.measurement.current_limit.event`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the
              ``print(status.measurement.current_limit.event)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.current_limit.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ntr(self) -> str:
        """Access the ``status.measurement.current_limit.ntr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the ``print(status.measurement.current_limit.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.ntr = value
            - print(status.measurement.current_limit.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.current_limit.ntr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the ``print(status.measurement.current_limit.ntr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.ntr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.ntr = value
            - print(status.measurement.current_limit.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def ptr(self) -> str:
        """Access the ``status.measurement.current_limit.ptr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the ``print(status.measurement.current_limit.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.ptr = value
            - print(status.measurement.current_limit.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.current_limit.ptr`` attribute.

        Description:
            - This attribute contains the measurement event current limit summary registers.

        Usage:
            - Accessing this property will send the ``print(status.measurement.current_limit.ptr)``
              query.
            - Setting this property to a value will send the
              ``status.measurement.current_limit.ptr = value`` command.

        TSP Syntax:
            ```
            - status.measurement.current_limit.ptr = value
            - print(status.measurement.current_limit.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class StatusMeasurement(BaseTSPCmd):
    """The ``status.measurement`` command tree.

    Properties and methods:
        - ``.condition``: The ``status.measurement.condition`` attribute.
        - ``.current_limit``: The ``status.measurement.current_limit`` command tree.
        - ``.enable``: The ``status.measurement.enable`` attribute.
        - ``.event``: The ``status.measurement.event`` attribute.
        - ``.instrument``: The ``status.measurement.instrument`` command tree.
        - ``.ntr``: The ``status.measurement.ntr`` attribute.
        - ``.protection``: The ``status.measurement.protection`` command tree.
        - ``.ptr``: The ``status.measurement.ptr`` attribute.
        - ``.reading_overflow``: The ``status.measurement.reading_overflow`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._current_limit = StatusMeasurementCurrentLimit(
            device, f"{self._cmd_syntax}.current_limit"
        )
        self._instrument = StatusMeasurementInstrument(device, f"{self._cmd_syntax}.instrument")
        self._protection = StatusMeasurementProtection(device, f"{self._cmd_syntax}.protection")
        self._reading_overflow = StatusMeasurementReadingOverflow(
            device, f"{self._cmd_syntax}.reading_overflow"
        )

    @property
    def condition(self) -> str:
        """Access the ``status.measurement.condition`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.condition)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.condition)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".condition"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.condition)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.condition`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def current_limit(self) -> StatusMeasurementCurrentLimit:
        """Return the ``status.measurement.current_limit`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.current_limit.condition`` attribute.
            - ``.enable``: The ``status.measurement.current_limit.enable`` attribute.
            - ``.event``: The ``status.measurement.current_limit.event`` attribute.
            - ``.ntr``: The ``status.measurement.current_limit.ntr`` attribute.
            - ``.ptr``: The ``status.measurement.current_limit.ptr`` attribute.
        """
        return self._current_limit

    @property
    def enable(self) -> str:
        """Access the ``status.measurement.enable`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.enable)`` query.
            - Setting this property to a value will send the ``status.measurement.enable = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.enable = value
            - print(status.measurement.enable)
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
        """Access the ``status.measurement.enable`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.enable)`` query.
            - Setting this property to a value will send the ``status.measurement.enable = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.enable = value
            - print(status.measurement.enable)
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
    def event(self) -> str:
        """Access the ``status.measurement.event`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.event)`` query.

        TSP Syntax:
            ```
            - print(status.measurement.event)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".event"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.event)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.event`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def instrument(self) -> StatusMeasurementInstrument:
        """Return the ``status.measurement.instrument`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.instrument.condition`` attribute.
            - ``.enable``: The ``status.measurement.instrument.enable`` attribute.
            - ``.event``: The ``status.measurement.instrument.event`` attribute.
            - ``.ntr``: The ``status.measurement.instrument.ntr`` attribute.
            - ``.psu``: The ``status.measurement.instrument.psu[X]`` command tree.
            - ``.ptr``: The ``status.measurement.instrument.ptr`` attribute.
        """
        return self._instrument

    @property
    def ntr(self) -> str:
        """Access the ``status.measurement.ntr`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.ntr)`` query.
            - Setting this property to a value will send the ``status.measurement.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.ntr = value
            - print(status.measurement.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ntr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ntr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ntr.setter
    def ntr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.ntr`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.ntr)`` query.
            - Setting this property to a value will send the ``status.measurement.ntr = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.ntr = value
            - print(status.measurement.ntr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ntr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ntr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ntr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def protection(self) -> StatusMeasurementProtection:
        """Return the ``status.measurement.protection`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.protection.condition`` attribute.
            - ``.enable``: The ``status.measurement.protection.enable`` attribute.
            - ``.event``: The ``status.measurement.protection.event`` attribute.
            - ``.ntr``: The ``status.measurement.protection.ntr`` attribute.
            - ``.ptr``: The ``status.measurement.protection.ptr`` attribute.
        """
        return self._protection

    @property
    def ptr(self) -> str:
        """Access the ``status.measurement.ptr`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.ptr)`` query.
            - Setting this property to a value will send the ``status.measurement.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.ptr = value
            - print(status.measurement.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".ptr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.ptr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @ptr.setter
    def ptr(self, value: Union[str, float]) -> None:
        """Access the ``status.measurement.ptr`` attribute.

        Description:
            - This attribute contains the Measurement Event register set.

        Usage:
            - Accessing this property will send the ``print(status.measurement.ptr)`` query.
            - Setting this property to a value will send the ``status.measurement.ptr = value``
              command.

        TSP Syntax:
            ```
            - status.measurement.ptr = value
            - print(status.measurement.ptr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".ptr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.ptr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.ptr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def reading_overflow(self) -> StatusMeasurementReadingOverflow:
        """Return the ``status.measurement.reading_overflow`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.reading_overflow.condition`` attribute.
            - ``.enable``: The ``status.measurement.reading_overflow.enable`` attribute.
            - ``.event``: The ``status.measurement.reading_overflow.event`` attribute.
            - ``.ntr``: The ``status.measurement.reading_overflow.ntr`` attribute.
            - ``.ptr``: The ``status.measurement.reading_overflow.ptr`` attribute.
        """
        return self._reading_overflow


class Status(BaseTSPCmd):
    """The ``status`` command tree.

    Properties and methods:
        - ``.measurement``: The ``status.measurement`` command tree.
        - ``.operation``: The ``status.operation`` command tree.
        - ``.questionable``: The ``status.questionable`` command tree.
        - ``.reset()``: The ``status.reset()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "status") -> None:
        super().__init__(device, cmd_syntax)
        self._measurement = StatusMeasurement(device, f"{self._cmd_syntax}.measurement")
        self._operation = StatusOperation(device, f"{self._cmd_syntax}.operation")
        self._questionable = StatusQuestionable(device, f"{self._cmd_syntax}.questionable")

    @property
    def measurement(self) -> StatusMeasurement:
        """Return the ``status.measurement`` command tree.

        Sub-properties and sub-methods:
            - ``.condition``: The ``status.measurement.condition`` attribute.
            - ``.current_limit``: The ``status.measurement.current_limit`` command tree.
            - ``.enable``: The ``status.measurement.enable`` attribute.
            - ``.event``: The ``status.measurement.event`` attribute.
            - ``.instrument``: The ``status.measurement.instrument`` command tree.
            - ``.ntr``: The ``status.measurement.ntr`` attribute.
            - ``.protection``: The ``status.measurement.protection`` command tree.
            - ``.ptr``: The ``status.measurement.ptr`` attribute.
            - ``.reading_overflow``: The ``status.measurement.reading_overflow`` command tree.
        """
        return self._measurement

    @property
    def operation(self) -> StatusOperation:
        """Return the ``status.operation`` command tree.

        Sub-properties and sub-methods:
            - ``.calibrating``: The ``status.operation.calibrating`` command tree.
            - ``.condition``: The ``status.operation.condition`` attribute.
            - ``.enable``: The ``status.operation.enable`` attribute.
            - ``.event``: The ``status.operation.event`` attribute.
            - ``.instrument``: The ``status.operation.instrument`` command tree.
            - ``.measuring``: The ``status.operation.measuring`` command tree.
            - ``.ntr``: The ``status.operation.ntr`` attribute.
            - ``.ptr``: The ``status.operation.ptr`` attribute.
            - ``.sweeping``: The ``status.operation.sweeping`` command tree.
        """
        return self._operation

    @property
    def questionable(self) -> StatusQuestionable:
        """Return the ``status.questionable`` command tree.

        Sub-properties and sub-methods:
            - ``.calibration``: The ``status.questionable.calibration`` command tree.
            - ``.condition``: The ``status.questionable.condition`` attribute.
            - ``.enable``: The ``status.questionable.enable`` attribute.
            - ``.event``: The ``status.questionable.event`` attribute.
            - ``.instrument``: The ``status.questionable.instrument`` command tree.
            - ``.ntr``: The ``status.questionable.ntr`` attribute.
            - ``.over_temperature``: The ``status.questionable.over_temperature`` command tree.
            - ``.ptr``: The ``status.questionable.ptr`` attribute.
        """
        return self._questionable

    def reset(self) -> None:
        """Run the ``status.reset()`` function.

        Description:
            - This function resets all bits in the status model for the defined slot to default
              values.

        TSP Syntax:
            ```
            - status.reset()
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
