# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The dmm commands module.

These commands are used in the following models:
DMM6500

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - dmm.digitize.analogtrigger.edge.level
    - dmm.digitize.analogtrigger.edge.slope
    - dmm.digitize.analogtrigger.mode
    - dmm.digitize.analogtrigger.window.direction
    - dmm.digitize.analogtrigger.window.levelhigh
    - dmm.digitize.analogtrigger.window.levellow
    - dmm.digitize.dbmreference
    - dmm.digitize.dbreference
    - dmm.digitize.inputimpedance
    - dmm.measure.analogtrigger.edge.level
    - dmm.measure.analogtrigger.edge.slope
    - dmm.measure.analogtrigger.mode
    - dmm.measure.analogtrigger.window.direction
    - dmm.measure.analogtrigger.window.levelhigh
    - dmm.measure.analogtrigger.window.levellow
    - dmm.measure.aperture
    - dmm.measure.autodelay
    - dmm.measure.autorange
    - dmm.measure.autozero.enable
    - dmm.measure.bias.level
    - dmm.measure.count
    - dmm.measure.dbmreference
    - dmm.measure.detectorbandwidth
    - dmm.measure.displaydigits
    - dmm.measure.filter.count
    - dmm.measure.filter.enable
    - dmm.measure.filter.type
    - dmm.measure.filter.window
    - dmm.measure.fourrtd
    - dmm.measure.func
    - dmm.measure.inputimpedance
    - dmm.measure.limit[Y].autoclear
    - dmm.measure.limit[Y].enable
    - dmm.measure.limit[Y].fail
    - dmm.measure.limit[Y].high.value
    - dmm.measure.limit[Y].low.value
    - dmm.measure.linesync
    - dmm.measure.math.enable
    - dmm.measure.math.format
    - dmm.measure.math.mxb.bfactor
    - dmm.measure.math.mxb.mfactor
    - dmm.measure.math.percent
    - dmm.measure.nplc
    - dmm.measure.offsetcompensation.enable
    - dmm.measure.opendetector
    - dmm.measure.range
    - dmm.measure.read()
    - dmm.measure.refjunction
    - dmm.measure.rel.enable
    - dmm.measure.rel.level
    - dmm.measure.rel.method
    - dmm.measure.rtdalpha
    - dmm.measure.rtdbeta
    - dmm.measure.rtddelta
    - dmm.measure.rtdzero
    - dmm.measure.sense.autorange
    - dmm.measure.sense.range
    - dmm.measure.setattribute()
    - dmm.measure.thermistor
    - dmm.measure.thermocouple
    - dmm.measure.threertd
    - dmm.measure.threshold.autorange
    - dmm.measure.threshold.range
    - dmm.measure.transducer
    - dmm.measure.twortd
    - dmm.measure.unit
    - dmm.reset()
    - dmm.terminals
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


class DmmMeasureThreshold(BaseTSPCmd):
    """The ``dmm.measure.threshold`` command tree.

    Properties and methods:
        - ``.autorange``: The ``dmm.measure.threshold.autorange`` attribute.
        - ``.range``: The ``dmm.measure.threshold.range`` attribute.
    """

    @property
    def autorange(self) -> str:
        """Access the ``dmm.measure.threshold.autorange`` attribute.

        Description:
            - This attribute determines if the threshold range is set manually or automatically.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.threshold.autorange)``
              query.
            - Setting this property to a value will send the
              ``dmm.measure.threshold.autorange = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.threshold.autorange = value
            - print(dmm.measure.threshold.autorange)
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
        """Access the ``dmm.measure.threshold.autorange`` attribute.

        Description:
            - This attribute determines if the threshold range is set manually or automatically.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.threshold.autorange)``
              query.
            - Setting this property to a value will send the
              ``dmm.measure.threshold.autorange = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.threshold.autorange = value
            - print(dmm.measure.threshold.autorange)
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
    def range(self) -> str:
        """Access the ``dmm.measure.threshold.range`` attribute.

        Description:
            - This attribute indicates the expected input level of the voltage signal.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.threshold.range)`` query.
            - Setting this property to a value will send the ``dmm.measure.threshold.range = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.threshold.range = value
            - print(dmm.measure.threshold.range)
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
        """Access the ``dmm.measure.threshold.range`` attribute.

        Description:
            - This attribute indicates the expected input level of the voltage signal.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.threshold.range)`` query.
            - Setting this property to a value will send the ``dmm.measure.threshold.range = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.threshold.range = value
            - print(dmm.measure.threshold.range)
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


class DmmMeasureSense(BaseTSPCmd):
    """The ``dmm.measure.sense`` command tree.

    Properties and methods:
        - ``.autorange``: The ``dmm.measure.sense.autorange`` attribute.
        - ``.range``: The ``dmm.measure.sense.range`` attribute.
    """

    @property
    def autorange(self) -> str:
        """Access the ``dmm.measure.sense.autorange`` attribute.

        Description:
            - This attribute returns the setting of sense autorange.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.sense.autorange)`` query.

        TSP Syntax:
            ```
            - print(dmm.measure.sense.autorange)
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

    @property
    def range(self) -> str:
        """Access the ``dmm.measure.sense.range`` attribute.

        Description:
            - This attribute displays the positive full-scale range that is being used for the sense
              measurement.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.sense.range)`` query.

        TSP Syntax:
            ```
            - print(dmm.measure.sense.range)
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


class DmmMeasureRel(BaseTSPCmd):
    """The ``dmm.measure.rel`` command tree.

    Properties and methods:
        - ``.enable``: The ``dmm.measure.rel.enable`` attribute.
        - ``.level``: The ``dmm.measure.rel.level`` attribute.
        - ``.method``: The ``dmm.measure.rel.method`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``dmm.measure.rel.enable`` attribute.

        Description:
            - This attribute enables or disables the application of a relative offset value to the
              measurement.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rel.enable)`` query.
            - Setting this property to a value will send the ``dmm.measure.rel.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rel.enable = value
            - print(dmm.measure.rel.enable)
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
        """Access the ``dmm.measure.rel.enable`` attribute.

        Description:
            - This attribute enables or disables the application of a relative offset value to the
              measurement.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rel.enable)`` query.
            - Setting this property to a value will send the ``dmm.measure.rel.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rel.enable = value
            - print(dmm.measure.rel.enable)
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
        """Access the ``dmm.measure.rel.level`` attribute.

        Description:
            - This attribute contains the relative offset value.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rel.level)`` query.
            - Setting this property to a value will send the ``dmm.measure.rel.level = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rel.level = value
            - print(dmm.measure.rel.level)
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
        """Access the ``dmm.measure.rel.level`` attribute.

        Description:
            - This attribute contains the relative offset value.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rel.level)`` query.
            - Setting this property to a value will send the ``dmm.measure.rel.level = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rel.level = value
            - print(dmm.measure.rel.level)
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
    def method(self) -> str:
        """Access the ``dmm.measure.rel.method`` attribute.

        Description:
            - This attribute determines if relative offset is applied to the measurements before
              calculating the DC voltage ratio value.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rel.method)`` query.
            - Setting this property to a value will send the ``dmm.measure.rel.method = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rel.method = value
            - print(dmm.measure.rel.method)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".method"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.method)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.method`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @method.setter
    def method(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.rel.method`` attribute.

        Description:
            - This attribute determines if relative offset is applied to the measurements before
              calculating the DC voltage ratio value.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rel.method)`` query.
            - Setting this property to a value will send the ``dmm.measure.rel.method = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rel.method = value
            - print(dmm.measure.rel.method)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".method", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.method = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.method`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DmmMeasureOffsetcompensation(BaseTSPCmd):
    """The ``dmm.measure.offsetcompensation`` command tree.

    Properties and methods:
        - ``.enable``: The ``dmm.measure.offsetcompensation.enable`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``dmm.measure.offsetcompensation.enable`` attribute.

        Description:
            - This attribute determines if offset compensation is used.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.offsetcompensation.enable)``
              query.
            - Setting this property to a value will send the
              ``dmm.measure.offsetcompensation.enable = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.offsetcompensation.enable = value
            - print(dmm.measure.offsetcompensation.enable)
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
        """Access the ``dmm.measure.offsetcompensation.enable`` attribute.

        Description:
            - This attribute determines if offset compensation is used.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.offsetcompensation.enable)``
              query.
            - Setting this property to a value will send the
              ``dmm.measure.offsetcompensation.enable = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.offsetcompensation.enable = value
            - print(dmm.measure.offsetcompensation.enable)
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


class DmmMeasureMathMxb(BaseTSPCmd):
    """The ``dmm.measure.math.mxb`` command tree.

    Properties and methods:
        - ``.bfactor``: The ``dmm.measure.math.mxb.bfactor`` attribute.
        - ``.mfactor``: The ``dmm.measure.math.mxb.mfactor`` attribute.
    """

    @property
    def bfactor(self) -> str:
        """Access the ``dmm.measure.math.mxb.bfactor`` attribute.

        Description:
            - This attribute specifies the offset, b, for the y = mx + b operation.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.math.mxb.bfactor)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.math.mxb.bfactor = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.math.mxb.bfactor = value
            - print(dmm.measure.math.mxb.bfactor)
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
        """Access the ``dmm.measure.math.mxb.bfactor`` attribute.

        Description:
            - This attribute specifies the offset, b, for the y = mx + b operation.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.math.mxb.bfactor)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.math.mxb.bfactor = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.math.mxb.bfactor = value
            - print(dmm.measure.math.mxb.bfactor)
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
        """Access the ``dmm.measure.math.mxb.mfactor`` attribute.

        Description:
            - This attribute specifies the scale factor, m, for the y = mx + b math operation.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.math.mxb.mfactor)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.math.mxb.mfactor = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.math.mxb.mfactor = value
            - print(dmm.measure.math.mxb.mfactor)
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
        """Access the ``dmm.measure.math.mxb.mfactor`` attribute.

        Description:
            - This attribute specifies the scale factor, m, for the y = mx + b math operation.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.math.mxb.mfactor)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.math.mxb.mfactor = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.math.mxb.mfactor = value
            - print(dmm.measure.math.mxb.mfactor)
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


class DmmMeasureMath(BaseTSPCmd):
    """The ``dmm.measure.math`` command tree.

    Properties and methods:
        - ``.enable``: The ``dmm.measure.math.enable`` attribute.
        - ``.format``: The ``dmm.measure.math.format`` attribute.
        - ``.mxb``: The ``dmm.measure.math.mxb`` command tree.
        - ``.percent``: The ``dmm.measure.math.percent`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mxb = DmmMeasureMathMxb(device, f"{self._cmd_syntax}.mxb")

    @property
    def enable(self) -> str:
        """Access the ``dmm.measure.math.enable`` attribute.

        Description:
            - This attribute enables or disables math operations on measurements for the selected
              measurement function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.math.enable)`` query.
            - Setting this property to a value will send the ``dmm.measure.math.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.math.enable = value
            - print(dmm.measure.math.enable)
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
        """Access the ``dmm.measure.math.enable`` attribute.

        Description:
            - This attribute enables or disables math operations on measurements for the selected
              measurement function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.math.enable)`` query.
            - Setting this property to a value will send the ``dmm.measure.math.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.math.enable = value
            - print(dmm.measure.math.enable)
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
        """Access the ``dmm.measure.math.format`` attribute.

        Description:
            - This attribute specifies which math operation is performed on measurements when math
              operations are enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.math.format)`` query.
            - Setting this property to a value will send the ``dmm.measure.math.format = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.math.format = value
            - print(dmm.measure.math.format)
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
        """Access the ``dmm.measure.math.format`` attribute.

        Description:
            - This attribute specifies which math operation is performed on measurements when math
              operations are enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.math.format)`` query.
            - Setting this property to a value will send the ``dmm.measure.math.format = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.math.format = value
            - print(dmm.measure.math.format)
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
    def mxb(self) -> DmmMeasureMathMxb:
        """Return the ``dmm.measure.math.mxb`` command tree.

        Sub-properties and sub-methods:
            - ``.bfactor``: The ``dmm.measure.math.mxb.bfactor`` attribute.
            - ``.mfactor``: The ``dmm.measure.math.mxb.mfactor`` attribute.
        """
        return self._mxb

    @property
    def percent(self) -> str:
        """Access the ``dmm.measure.math.percent`` attribute.

        Description:
            - This attribute specifies the reference constant that is used when math operations are
              set to percent.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.math.percent)`` query.
            - Setting this property to a value will send the ``dmm.measure.math.percent = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.math.percent = value
            - print(dmm.measure.math.percent)
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
        """Access the ``dmm.measure.math.percent`` attribute.

        Description:
            - This attribute specifies the reference constant that is used when math operations are
              set to percent.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.math.percent)`` query.
            - Setting this property to a value will send the ``dmm.measure.math.percent = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.math.percent = value
            - print(dmm.measure.math.percent)
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


class DmmMeasureLimitItemLow(BaseTSPCmd):
    """The ``dmm.measure.limit[Y].low`` command tree.

    Info:
        - ``Y``, the limit number: 1 or 2.

    Properties and methods:
        - ``.value``: The ``dmm.measure.limit[Y].low.value`` attribute.
    """

    @property
    def value(self) -> str:
        """Access the ``dmm.measure.limit[Y].low.value`` attribute.

        Description:
            - This attribute specifies the lower limit for a limit test.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.limit[Y].low.value)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.limit[Y].low.value = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.limit[Y].low.value = value
            - print(dmm.measure.limit[Y].low.value)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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
        """Access the ``dmm.measure.limit[Y].low.value`` attribute.

        Description:
            - This attribute specifies the lower limit for a limit test.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.limit[Y].low.value)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.limit[Y].low.value = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.limit[Y].low.value = value
            - print(dmm.measure.limit[Y].low.value)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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


class DmmMeasureLimitItemHigh(BaseTSPCmd):
    """The ``dmm.measure.limit[Y].high`` command tree.

    Info:
        - ``Y``, the limit number: 1 or 2.

    Properties and methods:
        - ``.value``: The ``dmm.measure.limit[Y].high.value`` attribute.
    """

    @property
    def value(self) -> str:
        """Access the ``dmm.measure.limit[Y].high.value`` attribute.

        Description:
            - This attribute specifies the upper limit for a limit test.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.limit[Y].high.value)``
              query.
            - Setting this property to a value will send the
              ``dmm.measure.limit[Y].high.value = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.limit[Y].high.value = value
            - print(dmm.measure.limit[Y].high.value)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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
        """Access the ``dmm.measure.limit[Y].high.value`` attribute.

        Description:
            - This attribute specifies the upper limit for a limit test.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.limit[Y].high.value)``
              query.
            - Setting this property to a value will send the
              ``dmm.measure.limit[Y].high.value = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.limit[Y].high.value = value
            - print(dmm.measure.limit[Y].high.value)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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


class DmmMeasureLimitItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``dmm.measure.limit[Y]`` command tree.

    Info:
        - ``Y``, the limit number: 1 or 2.

    Properties and methods:
        - ``.autoclear``: The ``dmm.measure.limit[Y].autoclear`` attribute.
        - ``.enable``: The ``dmm.measure.limit[Y].enable`` attribute.
        - ``.fail``: The ``dmm.measure.limit[Y].fail`` attribute.
        - ``.high``: The ``dmm.measure.limit[Y].high`` command tree.
        - ``.low``: The ``dmm.measure.limit[Y].low`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = DmmMeasureLimitItemHigh(device, f"{self._cmd_syntax}.high")
        self._low = DmmMeasureLimitItemLow(device, f"{self._cmd_syntax}.low")

    @property
    def autoclear(self) -> str:
        """Access the ``dmm.measure.limit[Y].autoclear`` attribute.

        Description:
            - This attribute indicates if the test result for limit Y should be cleared
              automatically or not.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.limit[Y].autoclear)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.limit[Y].autoclear = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.limit[Y].autoclear = value
            - print(dmm.measure.limit[Y].autoclear)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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
        """Access the ``dmm.measure.limit[Y].autoclear`` attribute.

        Description:
            - This attribute indicates if the test result for limit Y should be cleared
              automatically or not.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.limit[Y].autoclear)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.limit[Y].autoclear = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.limit[Y].autoclear = value
            - print(dmm.measure.limit[Y].autoclear)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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
        """Access the ``dmm.measure.limit[Y].enable`` attribute.

        Description:
            - This attribute enables or disables a limit test on the measurement from the selected
              measure function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.limit[Y].enable)`` query.
            - Setting this property to a value will send the ``dmm.measure.limit[Y].enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.limit[Y].enable = value
            - print(dmm.measure.limit[Y].enable)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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
        """Access the ``dmm.measure.limit[Y].enable`` attribute.

        Description:
            - This attribute enables or disables a limit test on the measurement from the selected
              measure function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.limit[Y].enable)`` query.
            - Setting this property to a value will send the ``dmm.measure.limit[Y].enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.limit[Y].enable = value
            - print(dmm.measure.limit[Y].enable)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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
        """Access the ``dmm.measure.limit[Y].fail`` attribute.

        Description:
            - This attribute queries the results of a limit test.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.limit[Y].fail)`` query.

        TSP Syntax:
            ```
            - print(dmm.measure.limit[Y].fail)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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
    def high(self) -> DmmMeasureLimitItemHigh:
        """Return the ``dmm.measure.limit[Y].high`` command tree.

        Info:
            - ``Y``, the limit number: 1 or 2.

        Sub-properties and sub-methods:
            - ``.value``: The ``dmm.measure.limit[Y].high.value`` attribute.
        """
        return self._high

    @property
    def low(self) -> DmmMeasureLimitItemLow:
        """Return the ``dmm.measure.limit[Y].low`` command tree.

        Info:
            - ``Y``, the limit number: 1 or 2.

        Sub-properties and sub-methods:
            - ``.value``: The ``dmm.measure.limit[Y].low.value`` attribute.
        """
        return self._low


class DmmMeasureFilter(BaseTSPCmd):
    """The ``dmm.measure.filter`` command tree.

    Properties and methods:
        - ``.count``: The ``dmm.measure.filter.count`` attribute.
        - ``.enable``: The ``dmm.measure.filter.enable`` attribute.
        - ``.type``: The ``dmm.measure.filter.type`` attribute.
        - ``.window``: The ``dmm.measure.filter.window`` attribute.
    """

    @property
    def count(self) -> str:
        """Access the ``dmm.measure.filter.count`` attribute.

        Description:
            - This attribute sets the number of measurements that are averaged when filtering is
              enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.filter.count)`` query.
            - Setting this property to a value will send the ``dmm.measure.filter.count = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.filter.count = value
            - print(dmm.measure.filter.count)
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
        """Access the ``dmm.measure.filter.count`` attribute.

        Description:
            - This attribute sets the number of measurements that are averaged when filtering is
              enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.filter.count)`` query.
            - Setting this property to a value will send the ``dmm.measure.filter.count = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.filter.count = value
            - print(dmm.measure.filter.count)
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
        """Access the ``dmm.measure.filter.enable`` attribute.

        Description:
            - This attribute enables or disables the averaging filter for measurements of the
              selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.filter.enable)`` query.
            - Setting this property to a value will send the ``dmm.measure.filter.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.filter.enable = value
            - print(dmm.measure.filter.enable)
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
        """Access the ``dmm.measure.filter.enable`` attribute.

        Description:
            - This attribute enables or disables the averaging filter for measurements of the
              selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.filter.enable)`` query.
            - Setting this property to a value will send the ``dmm.measure.filter.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.filter.enable = value
            - print(dmm.measure.filter.enable)
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
        """Access the ``dmm.measure.filter.type`` attribute.

        Description:
            - This attribute defines the type of averaging filter that is used for the selected
              measure function when the measurement filter is enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.filter.type)`` query.
            - Setting this property to a value will send the ``dmm.measure.filter.type = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.filter.type = value
            - print(dmm.measure.filter.type)
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
        """Access the ``dmm.measure.filter.type`` attribute.

        Description:
            - This attribute defines the type of averaging filter that is used for the selected
              measure function when the measurement filter is enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.filter.type)`` query.
            - Setting this property to a value will send the ``dmm.measure.filter.type = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.filter.type = value
            - print(dmm.measure.filter.type)
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

    @property
    def window(self) -> str:
        """Access the ``dmm.measure.filter.window`` attribute.

        Description:
            - This attribute sets the window for the averaging filter that is used for measurements
              for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.filter.window)`` query.
            - Setting this property to a value will send the ``dmm.measure.filter.window = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.filter.window = value
            - print(dmm.measure.filter.window)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".window"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.window)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.window`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @window.setter
    def window(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.filter.window`` attribute.

        Description:
            - This attribute sets the window for the averaging filter that is used for measurements
              for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.filter.window)`` query.
            - Setting this property to a value will send the ``dmm.measure.filter.window = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.filter.window = value
            - print(dmm.measure.filter.window)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".window", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.window = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.window`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DmmMeasureBias(BaseTSPCmd):
    """The ``dmm.measure.bias`` command tree.

    Properties and methods:
        - ``.level``: The ``dmm.measure.bias.level`` attribute.
    """

    @property
    def level(self) -> str:
        """Access the ``dmm.measure.bias.level`` attribute.

        Description:
            - This attribute selects the amount of current the instrument sources when it makes
              measurements.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.bias.level)`` query.
            - Setting this property to a value will send the ``dmm.measure.bias.level = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.bias.level = value
            - print(dmm.measure.bias.level)
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
        """Access the ``dmm.measure.bias.level`` attribute.

        Description:
            - This attribute selects the amount of current the instrument sources when it makes
              measurements.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.bias.level)`` query.
            - Setting this property to a value will send the ``dmm.measure.bias.level = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.bias.level = value
            - print(dmm.measure.bias.level)
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


class DmmMeasureAutozero(BaseTSPCmd):
    """The ``dmm.measure.autozero`` command tree.

    Properties and methods:
        - ``.enable``: The ``dmm.measure.autozero.enable`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``dmm.measure.autozero.enable`` attribute.

        Description:
            - This attribute enables or disables automatic updates to the internal reference
              measurements (autozero) of the instrument.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.autozero.enable)`` query.
            - Setting this property to a value will send the ``dmm.measure.autozero.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.autozero.enable = value
            - print(dmm.measure.autozero.enable)
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
        """Access the ``dmm.measure.autozero.enable`` attribute.

        Description:
            - This attribute enables or disables automatic updates to the internal reference
              measurements (autozero) of the instrument.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.autozero.enable)`` query.
            - Setting this property to a value will send the ``dmm.measure.autozero.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.autozero.enable = value
            - print(dmm.measure.autozero.enable)
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


class DmmMeasureAnalogtriggerWindow(BaseTSPCmd):
    """The ``dmm.measure.analogtrigger.window`` command tree.

    Properties and methods:
        - ``.direction``: The ``dmm.measure.analogtrigger.window.direction`` attribute.
        - ``.levelhigh``: The ``dmm.measure.analogtrigger.window.levelhigh`` attribute.
        - ``.levellow``: The ``dmm.measure.analogtrigger.window.levellow`` attribute.
    """

    @property
    def direction(self) -> str:
        """Access the ``dmm.measure.analogtrigger.window.direction`` attribute.

        Description:
            - This attribute defines if the analog trigger occurs when the signal enters or leaves
              the defined high and low analog signal level boundaries.

        Usage:
            - Accessing this property will send the
              ``print(dmm.measure.analogtrigger.window.direction)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.window.direction = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.window.direction = value
            - print(dmm.measure.analogtrigger.window.direction)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".direction"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.direction)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.direction`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @direction.setter
    def direction(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.analogtrigger.window.direction`` attribute.

        Description:
            - This attribute defines if the analog trigger occurs when the signal enters or leaves
              the defined high and low analog signal level boundaries.

        Usage:
            - Accessing this property will send the
              ``print(dmm.measure.analogtrigger.window.direction)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.window.direction = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.window.direction = value
            - print(dmm.measure.analogtrigger.window.direction)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".direction", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.direction = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.direction`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelhigh(self) -> str:
        """Access the ``dmm.measure.analogtrigger.window.levelhigh`` attribute.

        Description:
            - This attribute defines the upper boundary of the analog trigger window.

        Usage:
            - Accessing this property will send the
              ``print(dmm.measure.analogtrigger.window.levelhigh)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.window.levelhigh = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.window.levelhigh = value
            - print(dmm.measure.analogtrigger.window.levelhigh)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelhigh"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelhigh)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelhigh`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelhigh.setter
    def levelhigh(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.analogtrigger.window.levelhigh`` attribute.

        Description:
            - This attribute defines the upper boundary of the analog trigger window.

        Usage:
            - Accessing this property will send the
              ``print(dmm.measure.analogtrigger.window.levelhigh)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.window.levelhigh = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.window.levelhigh = value
            - print(dmm.measure.analogtrigger.window.levelhigh)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelhigh", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelhigh = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelhigh`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levellow(self) -> str:
        """Access the ``dmm.measure.analogtrigger.window.levellow`` attribute.

        Description:
            - This attribute defines the lower boundary of the analog trigger window.

        Usage:
            - Accessing this property will send the
              ``print(dmm.measure.analogtrigger.window.levellow)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.window.levellow = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.window.levellow = value
            - print(dmm.measure.analogtrigger.window.levellow)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levellow"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levellow)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levellow`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levellow.setter
    def levellow(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.analogtrigger.window.levellow`` attribute.

        Description:
            - This attribute defines the lower boundary of the analog trigger window.

        Usage:
            - Accessing this property will send the
              ``print(dmm.measure.analogtrigger.window.levellow)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.window.levellow = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.window.levellow = value
            - print(dmm.measure.analogtrigger.window.levellow)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levellow", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levellow = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levellow`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DmmMeasureAnalogtriggerEdge(BaseTSPCmd):
    """The ``dmm.measure.analogtrigger.edge`` command tree.

    Properties and methods:
        - ``.level``: The ``dmm.measure.analogtrigger.edge.level`` attribute.
        - ``.slope``: The ``dmm.measure.analogtrigger.edge.slope`` attribute.
    """

    @property
    def level(self) -> str:
        """Access the ``dmm.measure.analogtrigger.edge.level`` attribute.

        Description:
            - This attribute defines the signal level that generates the analog trigger event for
              the edge trigger mode.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.analogtrigger.edge.level)``
              query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.edge.level = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.edge.level = value
            - print(dmm.measure.analogtrigger.edge.level)
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
        """Access the ``dmm.measure.analogtrigger.edge.level`` attribute.

        Description:
            - This attribute defines the signal level that generates the analog trigger event for
              the edge trigger mode.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.analogtrigger.edge.level)``
              query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.edge.level = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.edge.level = value
            - print(dmm.measure.analogtrigger.edge.level)
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
    def slope(self) -> str:
        """Access the ``dmm.measure.analogtrigger.edge.slope`` attribute.

        Description:
            - This attribute defines the slope of the analog trigger edge.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.analogtrigger.edge.slope)``
              query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.edge.slope = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.edge.slope = value
            - print(dmm.measure.analogtrigger.edge.slope)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".slope"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.slope)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.slope`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @slope.setter
    def slope(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.analogtrigger.edge.slope`` attribute.

        Description:
            - This attribute defines the slope of the analog trigger edge.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.analogtrigger.edge.slope)``
              query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.edge.slope = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.edge.slope = value
            - print(dmm.measure.analogtrigger.edge.slope)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".slope", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.slope = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.slope`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DmmMeasureAnalogtrigger(BaseTSPCmd):
    """The ``dmm.measure.analogtrigger`` command tree.

    Properties and methods:
        - ``.edge``: The ``dmm.measure.analogtrigger.edge`` command tree.
        - ``.mode``: The ``dmm.measure.analogtrigger.mode`` attribute.
        - ``.window``: The ``dmm.measure.analogtrigger.window`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = DmmMeasureAnalogtriggerEdge(device, f"{self._cmd_syntax}.edge")
        self._window = DmmMeasureAnalogtriggerWindow(device, f"{self._cmd_syntax}.window")

    @property
    def edge(self) -> DmmMeasureAnalogtriggerEdge:
        """Return the ``dmm.measure.analogtrigger.edge`` command tree.

        Sub-properties and sub-methods:
            - ``.level``: The ``dmm.measure.analogtrigger.edge.level`` attribute.
            - ``.slope``: The ``dmm.measure.analogtrigger.edge.slope`` attribute.
        """
        return self._edge

    @property
    def mode(self) -> str:
        """Access the ``dmm.measure.analogtrigger.mode`` attribute.

        Description:
            - This attribute configures the type of signal behavior that can generate an analog
              trigger event.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.analogtrigger.mode)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.mode = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.mode = value
            - print(dmm.measure.analogtrigger.mode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".mode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.mode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @mode.setter
    def mode(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.analogtrigger.mode`` attribute.

        Description:
            - This attribute configures the type of signal behavior that can generate an analog
              trigger event.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.analogtrigger.mode)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.analogtrigger.mode = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.analogtrigger.mode = value
            - print(dmm.measure.analogtrigger.mode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".mode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.mode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def window(self) -> DmmMeasureAnalogtriggerWindow:
        """Return the ``dmm.measure.analogtrigger.window`` command tree.

        Sub-properties and sub-methods:
            - ``.direction``: The ``dmm.measure.analogtrigger.window.direction`` attribute.
            - ``.levelhigh``: The ``dmm.measure.analogtrigger.window.levelhigh`` attribute.
            - ``.levellow``: The ``dmm.measure.analogtrigger.window.levellow`` attribute.
        """
        return self._window


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class DmmMeasure(BaseTSPCmd):
    """The ``dmm.measure`` command tree.

    Properties and methods:
        - ``.analogtrigger``: The ``dmm.measure.analogtrigger`` command tree.
        - ``.aperture``: The ``dmm.measure.aperture`` attribute.
        - ``.autodelay``: The ``dmm.measure.autodelay`` attribute.
        - ``.autorange``: The ``dmm.measure.autorange`` attribute.
        - ``.autozero``: The ``dmm.measure.autozero`` command tree.
        - ``.bias``: The ``dmm.measure.bias`` command tree.
        - ``.count``: The ``dmm.measure.count`` attribute.
        - ``.dbmreference``: The ``dmm.measure.dbmreference`` attribute.
        - ``.detectorbandwidth``: The ``dmm.measure.detectorbandwidth`` attribute.
        - ``.displaydigits``: The ``dmm.measure.displaydigits`` attribute.
        - ``.filter``: The ``dmm.measure.filter`` command tree.
        - ``.fourrtd``: The ``dmm.measure.fourrtd`` attribute.
        - ``.func``: The ``dmm.measure.func`` attribute.
        - ``.inputimpedance``: The ``dmm.measure.inputimpedance`` attribute.
        - ``.limit``: The ``dmm.measure.limit[Y]`` command tree.
        - ``.linesync``: The ``dmm.measure.linesync`` attribute.
        - ``.math``: The ``dmm.measure.math`` command tree.
        - ``.nplc``: The ``dmm.measure.nplc`` attribute.
        - ``.offsetcompensation``: The ``dmm.measure.offsetcompensation`` command tree.
        - ``.opendetector``: The ``dmm.measure.opendetector`` attribute.
        - ``.range``: The ``dmm.measure.range`` attribute.
        - ``.read()``: The ``dmm.measure.read()`` function.
        - ``.refjunction``: The ``dmm.measure.refjunction`` attribute.
        - ``.rel``: The ``dmm.measure.rel`` command tree.
        - ``.rtdalpha``: The ``dmm.measure.rtdalpha`` attribute.
        - ``.rtdbeta``: The ``dmm.measure.rtdbeta`` attribute.
        - ``.rtddelta``: The ``dmm.measure.rtddelta`` attribute.
        - ``.rtdzero``: The ``dmm.measure.rtdzero`` attribute.
        - ``.sense``: The ``dmm.measure.sense`` command tree.
        - ``.setattribute()``: The ``dmm.measure.setattribute()`` function.
        - ``.thermistor``: The ``dmm.measure.thermistor`` attribute.
        - ``.thermocouple``: The ``dmm.measure.thermocouple`` attribute.
        - ``.threertd``: The ``dmm.measure.threertd`` attribute.
        - ``.threshold``: The ``dmm.measure.threshold`` command tree.
        - ``.transducer``: The ``dmm.measure.transducer`` attribute.
        - ``.twortd``: The ``dmm.measure.twortd`` attribute.
        - ``.unit``: The ``dmm.measure.unit`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._analogtrigger = DmmMeasureAnalogtrigger(device, f"{self._cmd_syntax}.analogtrigger")
        self._autozero = DmmMeasureAutozero(device, f"{self._cmd_syntax}.autozero")
        self._bias = DmmMeasureBias(device, f"{self._cmd_syntax}.bias")
        self._filter = DmmMeasureFilter(device, f"{self._cmd_syntax}.filter")
        self._limit: Dict[int, DmmMeasureLimitItem] = DefaultDictPassKeyToFactory(
            lambda x: DmmMeasureLimitItem(device, f"{self._cmd_syntax}.limit[{x}]")
        )
        self._math = DmmMeasureMath(device, f"{self._cmd_syntax}.math")
        self._offsetcompensation = DmmMeasureOffsetcompensation(
            device, f"{self._cmd_syntax}.offsetcompensation"
        )
        self._rel = DmmMeasureRel(device, f"{self._cmd_syntax}.rel")
        self._sense = DmmMeasureSense(device, f"{self._cmd_syntax}.sense")
        self._threshold = DmmMeasureThreshold(device, f"{self._cmd_syntax}.threshold")

    @property
    def analogtrigger(self) -> DmmMeasureAnalogtrigger:
        """Return the ``dmm.measure.analogtrigger`` command tree.

        Sub-properties and sub-methods:
            - ``.edge``: The ``dmm.measure.analogtrigger.edge`` command tree.
            - ``.mode``: The ``dmm.measure.analogtrigger.mode`` attribute.
            - ``.window``: The ``dmm.measure.analogtrigger.window`` command tree.
        """
        return self._analogtrigger

    @property
    def aperture(self) -> str:
        """Access the ``dmm.measure.aperture`` attribute.

        Description:
            - This function determines the aperture setting for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.aperture)`` query.
            - Setting this property to a value will send the ``dmm.measure.aperture = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.aperture = value
            - print(dmm.measure.aperture)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".aperture"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.aperture)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.aperture`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @aperture.setter
    def aperture(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.aperture`` attribute.

        Description:
            - This function determines the aperture setting for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.aperture)`` query.
            - Setting this property to a value will send the ``dmm.measure.aperture = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.aperture = value
            - print(dmm.measure.aperture)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".aperture", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.aperture = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.aperture`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def autodelay(self) -> str:
        """Access the ``dmm.measure.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic delay that occurs before each
              measurement.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.autodelay)`` query.
            - Setting this property to a value will send the ``dmm.measure.autodelay = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.autodelay = value
            - print(dmm.measure.autodelay)
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
        """Access the ``dmm.measure.autodelay`` attribute.

        Description:
            - This attribute enables or disables the automatic delay that occurs before each
              measurement.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.autodelay)`` query.
            - Setting this property to a value will send the ``dmm.measure.autodelay = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.autodelay = value
            - print(dmm.measure.autodelay)
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
        """Access the ``dmm.measure.autorange`` attribute.

        Description:
            - This attribute determines if the measurement range is set manually or automatically
              for the selected measure function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.autorange)`` query.
            - Setting this property to a value will send the ``dmm.measure.autorange = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.autorange = value
            - print(dmm.measure.autorange)
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
        """Access the ``dmm.measure.autorange`` attribute.

        Description:
            - This attribute determines if the measurement range is set manually or automatically
              for the selected measure function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.autorange)`` query.
            - Setting this property to a value will send the ``dmm.measure.autorange = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.autorange = value
            - print(dmm.measure.autorange)
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
    def autozero(self) -> DmmMeasureAutozero:
        """Return the ``dmm.measure.autozero`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``dmm.measure.autozero.enable`` attribute.
        """
        return self._autozero

    @property
    def bias(self) -> DmmMeasureBias:
        """Return the ``dmm.measure.bias`` command tree.

        Sub-properties and sub-methods:
            - ``.level``: The ``dmm.measure.bias.level`` attribute.
        """
        return self._bias

    @property
    def count(self) -> str:
        """Access the ``dmm.measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements to make when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.count)`` query.
            - Setting this property to a value will send the ``dmm.measure.count = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.count = value
            - print(dmm.measure.count)
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
        """Access the ``dmm.measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements to make when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.count)`` query.
            - Setting this property to a value will send the ``dmm.measure.count = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.count = value
            - print(dmm.measure.count)
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
    def dbmreference(self) -> str:
        """Access the ``dmm.measure.dbmreference`` attribute.

        Description:
            - This attribute defines the decibel-milliwatts (dBm) reference.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.dbmreference)`` query.
            - Setting this property to a value will send the ``dmm.measure.dbmreference = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.dbmreference = value
            - print(dmm.measure.dbmreference)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".dbmreference"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.dbmreference)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.dbmreference`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @dbmreference.setter
    def dbmreference(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.dbmreference`` attribute.

        Description:
            - This attribute defines the decibel-milliwatts (dBm) reference.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.dbmreference)`` query.
            - Setting this property to a value will send the ``dmm.measure.dbmreference = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.dbmreference = value
            - print(dmm.measure.dbmreference)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".dbmreference", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.dbmreference = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.dbmreference`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def detectorbandwidth(self) -> str:
        """Access the ``dmm.measure.detectorbandwidth`` attribute.

        Description:
            - This attribute selects the detector bandwidth for AC current and AC voltage
              measurements.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.detectorbandwidth)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.detectorbandwidth = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.detectorbandwidth = value
            - print(dmm.measure.detectorbandwidth)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".detectorbandwidth"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.detectorbandwidth)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.detectorbandwidth`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @detectorbandwidth.setter
    def detectorbandwidth(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.detectorbandwidth`` attribute.

        Description:
            - This attribute selects the detector bandwidth for AC current and AC voltage
              measurements.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.detectorbandwidth)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.detectorbandwidth = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.detectorbandwidth = value
            - print(dmm.measure.detectorbandwidth)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".detectorbandwidth", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.detectorbandwidth = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.detectorbandwidth`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def displaydigits(self) -> str:
        """Access the ``dmm.measure.displaydigits`` attribute.

        Description:
            - This attribute determines the number of digits that are displayed for measurements on
              the front panel.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.displaydigits)`` query.
            - Setting this property to a value will send the ``dmm.measure.displaydigits = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.displaydigits = value
            - print(dmm.measure.displaydigits)
            ```

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
        """Access the ``dmm.measure.displaydigits`` attribute.

        Description:
            - This attribute determines the number of digits that are displayed for measurements on
              the front panel.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.displaydigits)`` query.
            - Setting this property to a value will send the ``dmm.measure.displaydigits = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.displaydigits = value
            - print(dmm.measure.displaydigits)
            ```

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
    def filter(self) -> DmmMeasureFilter:
        """Return the ``dmm.measure.filter`` command tree.

        Sub-properties and sub-methods:
            - ``.count``: The ``dmm.measure.filter.count`` attribute.
            - ``.enable``: The ``dmm.measure.filter.enable`` attribute.
            - ``.type``: The ``dmm.measure.filter.type`` attribute.
            - ``.window``: The ``dmm.measure.filter.window`` attribute.
        """
        return self._filter

    @property
    def fourrtd(self) -> str:
        """Access the ``dmm.measure.fourrtd`` attribute.

        Description:
            - This attribute defines the type of 4-wire RTD that is being used

        Usage:
            - Accessing this property will send the ``print(dmm.measure.fourrtd)`` query.
            - Setting this property to a value will send the ``dmm.measure.fourrtd = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.fourrtd = value
            - print(dmm.measure.fourrtd)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".fourrtd"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.fourrtd)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.fourrtd`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @fourrtd.setter
    def fourrtd(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.fourrtd`` attribute.

        Description:
            - This attribute defines the type of 4-wire RTD that is being used

        Usage:
            - Accessing this property will send the ``print(dmm.measure.fourrtd)`` query.
            - Setting this property to a value will send the ``dmm.measure.fourrtd = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.fourrtd = value
            - print(dmm.measure.fourrtd)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".fourrtd", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.fourrtd = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.fourrtd`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def func(self) -> str:
        """Access the ``dmm.measure.func`` attribute.

        Description:
            - This attribute selects the active measure function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.func)`` query.
            - Setting this property to a value will send the ``dmm.measure.func = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.func = value
            - print(dmm.measure.func)
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
        """Access the ``dmm.measure.func`` attribute.

        Description:
            - This attribute selects the active measure function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.func)`` query.
            - Setting this property to a value will send the ``dmm.measure.func = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.func = value
            - print(dmm.measure.func)
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
    def inputimpedance(self) -> str:
        """Access the ``dmm.measure.inputimpedance`` attribute.

        Description:
            - This attribute determines when the 10 MΩ input divider is enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.inputimpedance)`` query.
            - Setting this property to a value will send the ``dmm.measure.inputimpedance = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.inputimpedance = value
            - print(dmm.measure.inputimpedance)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".inputimpedance"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.inputimpedance)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.inputimpedance`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @inputimpedance.setter
    def inputimpedance(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.inputimpedance`` attribute.

        Description:
            - This attribute determines when the 10 MΩ input divider is enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.inputimpedance)`` query.
            - Setting this property to a value will send the ``dmm.measure.inputimpedance = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.inputimpedance = value
            - print(dmm.measure.inputimpedance)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".inputimpedance", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.inputimpedance = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.inputimpedance`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limit(self) -> Dict[int, DmmMeasureLimitItem]:
        """Return the ``dmm.measure.limit[Y]`` command tree.

        Info:
            - ``Y``, the limit number: 1 or 2.

        Sub-properties and sub-methods:
            - ``.autoclear``: The ``dmm.measure.limit[Y].autoclear`` attribute.
            - ``.enable``: The ``dmm.measure.limit[Y].enable`` attribute.
            - ``.fail``: The ``dmm.measure.limit[Y].fail`` attribute.
            - ``.high``: The ``dmm.measure.limit[Y].high`` command tree.
            - ``.low``: The ``dmm.measure.limit[Y].low`` command tree.
        """
        return self._limit

    @property
    def linesync(self) -> str:
        """Access the ``dmm.measure.linesync`` attribute.

        Description:
            - This attribute determines if line synchronization is used during the measurement.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.linesync)`` query.
            - Setting this property to a value will send the ``dmm.measure.linesync = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.linesync = value
            - print(dmm.measure.linesync)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".linesync"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.linesync)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.linesync`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @linesync.setter
    def linesync(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.linesync`` attribute.

        Description:
            - This attribute determines if line synchronization is used during the measurement.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.linesync)`` query.
            - Setting this property to a value will send the ``dmm.measure.linesync = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.linesync = value
            - print(dmm.measure.linesync)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".linesync", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.linesync = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.linesync`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def math(self) -> DmmMeasureMath:
        """Return the ``dmm.measure.math`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``dmm.measure.math.enable`` attribute.
            - ``.format``: The ``dmm.measure.math.format`` attribute.
            - ``.mxb``: The ``dmm.measure.math.mxb`` command tree.
            - ``.percent``: The ``dmm.measure.math.percent`` attribute.
        """
        return self._math

    @property
    def nplc(self) -> str:
        """Access the ``dmm.measure.nplc`` attribute.

        Description:
            - This command sets the time that the input signal is measured for the selected
              function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.nplc)`` query.
            - Setting this property to a value will send the ``dmm.measure.nplc = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.nplc = value
            - print(dmm.measure.nplc)
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
        """Access the ``dmm.measure.nplc`` attribute.

        Description:
            - This command sets the time that the input signal is measured for the selected
              function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.nplc)`` query.
            - Setting this property to a value will send the ``dmm.measure.nplc = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.nplc = value
            - print(dmm.measure.nplc)
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
    def offsetcompensation(self) -> DmmMeasureOffsetcompensation:
        """Return the ``dmm.measure.offsetcompensation`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``dmm.measure.offsetcompensation.enable`` attribute.
        """
        return self._offsetcompensation

    @property
    def opendetector(self) -> str:
        """Access the ``dmm.measure.opendetector`` attribute.

        Description:
            - This attribute determines if the detection of open leads is enabled or disabled.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.opendetector)`` query.
            - Setting this property to a value will send the ``dmm.measure.opendetector = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.opendetector = value
            - print(dmm.measure.opendetector)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".opendetector"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.opendetector)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.opendetector`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @opendetector.setter
    def opendetector(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.opendetector`` attribute.

        Description:
            - This attribute determines if the detection of open leads is enabled or disabled.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.opendetector)`` query.
            - Setting this property to a value will send the ``dmm.measure.opendetector = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.opendetector = value
            - print(dmm.measure.opendetector)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".opendetector", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.opendetector = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.opendetector`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def range(self) -> str:
        """Access the ``dmm.measure.range`` attribute.

        Description:
            - This attribute determines the positive full-scale measure range.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.range)`` query.
            - Setting this property to a value will send the ``dmm.measure.range = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.range = value
            - print(dmm.measure.range)
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
        """Access the ``dmm.measure.range`` attribute.

        Description:
            - This attribute determines the positive full-scale measure range.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.range)`` query.
            - Setting this property to a value will send the ``dmm.measure.range = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.range = value
            - print(dmm.measure.range)
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
    def refjunction(self) -> str:
        """Access the ``dmm.measure.refjunction`` attribute.

        Description:
            - This attribute defines the type of the thermocouple reference junction.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.refjunction)`` query.
            - Setting this property to a value will send the ``dmm.measure.refjunction = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.refjunction = value
            - print(dmm.measure.refjunction)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".refjunction"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.refjunction)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.refjunction`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @refjunction.setter
    def refjunction(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.refjunction`` attribute.

        Description:
            - This attribute defines the type of the thermocouple reference junction.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.refjunction)`` query.
            - Setting this property to a value will send the ``dmm.measure.refjunction = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.refjunction = value
            - print(dmm.measure.refjunction)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".refjunction", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.refjunction = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.refjunction`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rel(self) -> DmmMeasureRel:
        """Return the ``dmm.measure.rel`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``dmm.measure.rel.enable`` attribute.
            - ``.level``: The ``dmm.measure.rel.level`` attribute.
            - ``.method``: The ``dmm.measure.rel.method`` attribute.
        """
        return self._rel

    @property
    def rtdalpha(self) -> str:
        """Access the ``dmm.measure.rtdalpha`` attribute.

        Description:
            - This attribute contains the alpha value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rtdalpha)`` query.
            - Setting this property to a value will send the ``dmm.measure.rtdalpha = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rtdalpha = value
            - print(dmm.measure.rtdalpha)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rtdalpha"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rtdalpha)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rtdalpha`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @rtdalpha.setter
    def rtdalpha(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.rtdalpha`` attribute.

        Description:
            - This attribute contains the alpha value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rtdalpha)`` query.
            - Setting this property to a value will send the ``dmm.measure.rtdalpha = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rtdalpha = value
            - print(dmm.measure.rtdalpha)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".rtdalpha", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.rtdalpha = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rtdalpha`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rtdbeta(self) -> str:
        """Access the ``dmm.measure.rtdbeta`` attribute.

        Description:
            - This attribute contains the beta value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rtdbeta)`` query.
            - Setting this property to a value will send the ``dmm.measure.rtdbeta = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rtdbeta = value
            - print(dmm.measure.rtdbeta)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rtdbeta"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rtdbeta)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rtdbeta`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @rtdbeta.setter
    def rtdbeta(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.rtdbeta`` attribute.

        Description:
            - This attribute contains the beta value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rtdbeta)`` query.
            - Setting this property to a value will send the ``dmm.measure.rtdbeta = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rtdbeta = value
            - print(dmm.measure.rtdbeta)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".rtdbeta", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.rtdbeta = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rtdbeta`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rtddelta(self) -> str:
        """Access the ``dmm.measure.rtddelta`` attribute.

        Description:
            - This attribute contains the delta value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rtddelta)`` query.
            - Setting this property to a value will send the ``dmm.measure.rtddelta = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rtddelta = value
            - print(dmm.measure.rtddelta)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rtddelta"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rtddelta)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rtddelta`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @rtddelta.setter
    def rtddelta(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.rtddelta`` attribute.

        Description:
            - This attribute contains the delta value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rtddelta)`` query.
            - Setting this property to a value will send the ``dmm.measure.rtddelta = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rtddelta = value
            - print(dmm.measure.rtddelta)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".rtddelta", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.rtddelta = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rtddelta`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rtdzero(self) -> str:
        """Access the ``dmm.measure.rtdzero`` attribute.

        Description:
            - This attribute contains the zero value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rtdzero)`` query.
            - Setting this property to a value will send the ``dmm.measure.rtdzero = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rtdzero = value
            - print(dmm.measure.rtdzero)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rtdzero"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rtdzero)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rtdzero`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @rtdzero.setter
    def rtdzero(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.rtdzero`` attribute.

        Description:
            - This attribute contains the zero value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.rtdzero)`` query.
            - Setting this property to a value will send the ``dmm.measure.rtdzero = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.rtdzero = value
            - print(dmm.measure.rtdzero)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".rtdzero", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.rtdzero = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rtdzero`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def sense(self) -> DmmMeasureSense:
        """Return the ``dmm.measure.sense`` command tree.

        Sub-properties and sub-methods:
            - ``.autorange``: The ``dmm.measure.sense.autorange`` attribute.
            - ``.range``: The ``dmm.measure.sense.range`` attribute.
        """
        return self._sense

    @property
    def thermistor(self) -> str:
        """Access the ``dmm.measure.thermistor`` attribute.

        Description:
            - This attribute describes the type of thermistor.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.thermistor)`` query.
            - Setting this property to a value will send the ``dmm.measure.thermistor = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.thermistor = value
            - print(dmm.measure.thermistor)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".thermistor"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.thermistor)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.thermistor`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @thermistor.setter
    def thermistor(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.thermistor`` attribute.

        Description:
            - This attribute describes the type of thermistor.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.thermistor)`` query.
            - Setting this property to a value will send the ``dmm.measure.thermistor = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.thermistor = value
            - print(dmm.measure.thermistor)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".thermistor", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.thermistor = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.thermistor`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def thermocouple(self) -> str:
        """Access the ``dmm.measure.thermocouple`` attribute.

        Description:
            - This attribute indicates the thermocouple type.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.thermocouple)`` query.
            - Setting this property to a value will send the ``dmm.measure.thermocouple = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.thermocouple = value
            - print(dmm.measure.thermocouple)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".thermocouple"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.thermocouple)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.thermocouple`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @thermocouple.setter
    def thermocouple(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.thermocouple`` attribute.

        Description:
            - This attribute indicates the thermocouple type.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.thermocouple)`` query.
            - Setting this property to a value will send the ``dmm.measure.thermocouple = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.thermocouple = value
            - print(dmm.measure.thermocouple)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".thermocouple", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.thermocouple = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.thermocouple`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def threertd(self) -> str:
        """Access the ``dmm.measure.threertd`` attribute.

        Description:
            - This attribute defines the type of three-wire RTD that is being used.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.threertd)`` query.
            - Setting this property to a value will send the ``dmm.measure.threertd = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.threertd = value
            - print(dmm.measure.threertd)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".threertd"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.threertd)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.threertd`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @threertd.setter
    def threertd(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.threertd`` attribute.

        Description:
            - This attribute defines the type of three-wire RTD that is being used.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.threertd)`` query.
            - Setting this property to a value will send the ``dmm.measure.threertd = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.threertd = value
            - print(dmm.measure.threertd)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".threertd", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.threertd = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.threertd`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def threshold(self) -> DmmMeasureThreshold:
        """Return the ``dmm.measure.threshold`` command tree.

        Sub-properties and sub-methods:
            - ``.autorange``: The ``dmm.measure.threshold.autorange`` attribute.
            - ``.range``: The ``dmm.measure.threshold.range`` attribute.
        """
        return self._threshold

    @property
    def transducer(self) -> str:
        """Access the ``dmm.measure.transducer`` attribute.

        Description:
            - This attribute sets the transducer type for the temperature measurement function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.transducer)`` query.
            - Setting this property to a value will send the ``dmm.measure.transducer = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.transducer = value
            - print(dmm.measure.transducer)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".transducer"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.transducer)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.transducer`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @transducer.setter
    def transducer(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.transducer`` attribute.

        Description:
            - This attribute sets the transducer type for the temperature measurement function.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.transducer)`` query.
            - Setting this property to a value will send the ``dmm.measure.transducer = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.transducer = value
            - print(dmm.measure.transducer)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".transducer", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.transducer = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.transducer`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def twortd(self) -> str:
        """Access the ``dmm.measure.twortd`` attribute.

        Description:
            - This attribute defines the type of 2-wire RTD that is being used.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.twortd)`` query.
            - Setting this property to a value will send the ``dmm.measure.twortd = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.twortd = value
            - print(dmm.measure.twortd)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".twortd"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.twortd)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.twortd`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @twortd.setter
    def twortd(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.twortd`` attribute.

        Description:
            - This attribute defines the type of 2-wire RTD that is being used.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.twortd)`` query.
            - Setting this property to a value will send the ``dmm.measure.twortd = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.twortd = value
            - print(dmm.measure.twortd)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".twortd", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.twortd = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.twortd`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def unit(self) -> str:
        """Access the ``dmm.measure.unit`` attribute.

        Description:
            - This attribute sets the units of measurement that are displayed on the front panel of
              the instrument and stored in the reading buffer.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.unit)`` query.
            - Setting this property to a value will send the ``dmm.measure.unit = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.unit = value
            - print(dmm.measure.unit)
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
        """Access the ``dmm.measure.unit`` attribute.

        Description:
            - This attribute sets the units of measurement that are displayed on the front panel of
              the instrument and stored in the reading buffer.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.unit)`` query.
            - Setting this property to a value will send the ``dmm.measure.unit = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.unit = value
            - print(dmm.measure.unit)
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

    def read(self, buffer_name: Optional[str] = None) -> str:
        """Run the ``dmm.measure.read()`` function.

        Description:
            - This function makes measurements, places them in a reading buffer, and returns the
              last reading.

        TSP Syntax:
            ```
            - dmm.measure.read()
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

    def setattribute(self, function: str, setting: str, value: str) -> None:
        """Run the ``dmm.measure.setattribute()`` function.

        Description:
            - This function allows you to set up a measure function whether or not the function is
              active.

        TSP Syntax:
            ```
            - dmm.measure.setattribute()
            ```

        Args:
            function: The function for which you are setting parameters; see Functions.
            setting: The parameter for the function; refer to Details and the tables following the
                examples.
            value: The parameter value.

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


class DmmDigitizeAnalogtriggerWindow(BaseTSPCmd):
    """The ``dmm.digitize.analogtrigger.window`` command tree.

    Properties and methods:
        - ``.direction``: The ``dmm.digitize.analogtrigger.window.direction`` attribute.
        - ``.levelhigh``: The ``dmm.digitize.analogtrigger.window.levelhigh`` attribute.
        - ``.levellow``: The ``dmm.digitize.analogtrigger.window.levellow`` attribute.
    """

    @property
    def direction(self) -> str:
        """Access the ``dmm.digitize.analogtrigger.window.direction`` attribute.

        Description:
            - This attribute defines if the analog trigger occurs when the signal enters or leaves
              the defined high and low analog signal level boundaries.

        Usage:
            - Accessing this property will send the
              ``print(dmm.digitize.analogtrigger.window.direction)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.window.direction = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.window.direction = value
            - print(dmm.digitize.analogtrigger.window.direction)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".direction"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.direction)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.direction`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @direction.setter
    def direction(self, value: Union[str, float]) -> None:
        """Access the ``dmm.digitize.analogtrigger.window.direction`` attribute.

        Description:
            - This attribute defines if the analog trigger occurs when the signal enters or leaves
              the defined high and low analog signal level boundaries.

        Usage:
            - Accessing this property will send the
              ``print(dmm.digitize.analogtrigger.window.direction)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.window.direction = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.window.direction = value
            - print(dmm.digitize.analogtrigger.window.direction)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".direction", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.direction = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.direction`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelhigh(self) -> str:
        """Access the ``dmm.digitize.analogtrigger.window.levelhigh`` attribute.

        Description:
            - This attribute defines the upper boundary of the analog trigger window.

        Usage:
            - Accessing this property will send the
              ``print(dmm.digitize.analogtrigger.window.levelhigh)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.window.levelhigh = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.window.levelhigh = value
            - print(dmm.digitize.analogtrigger.window.levelhigh)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelhigh"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelhigh)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelhigh`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelhigh.setter
    def levelhigh(self, value: Union[str, float]) -> None:
        """Access the ``dmm.digitize.analogtrigger.window.levelhigh`` attribute.

        Description:
            - This attribute defines the upper boundary of the analog trigger window.

        Usage:
            - Accessing this property will send the
              ``print(dmm.digitize.analogtrigger.window.levelhigh)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.window.levelhigh = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.window.levelhigh = value
            - print(dmm.digitize.analogtrigger.window.levelhigh)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelhigh", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelhigh = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelhigh`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levellow(self) -> str:
        """Access the ``dmm.digitize.analogtrigger.window.levellow`` attribute.

        Description:
            - This attribute defines the lower boundary of the analog trigger window.

        Usage:
            - Accessing this property will send the
              ``print(dmm.digitize.analogtrigger.window.levellow)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.window.levellow = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.window.levellow = value
            - print(dmm.digitize.analogtrigger.window.levellow)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levellow"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levellow)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levellow`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levellow.setter
    def levellow(self, value: Union[str, float]) -> None:
        """Access the ``dmm.digitize.analogtrigger.window.levellow`` attribute.

        Description:
            - This attribute defines the lower boundary of the analog trigger window.

        Usage:
            - Accessing this property will send the
              ``print(dmm.digitize.analogtrigger.window.levellow)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.window.levellow = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.window.levellow = value
            - print(dmm.digitize.analogtrigger.window.levellow)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levellow", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levellow = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levellow`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DmmDigitizeAnalogtriggerEdge(BaseTSPCmd):
    """The ``dmm.digitize.analogtrigger.edge`` command tree.

    Properties and methods:
        - ``.level``: The ``dmm.digitize.analogtrigger.edge.level`` attribute.
        - ``.slope``: The ``dmm.digitize.analogtrigger.edge.slope`` attribute.
    """

    @property
    def level(self) -> str:
        """Access the ``dmm.digitize.analogtrigger.edge.level`` attribute.

        Description:
            - This attribute defines the signal level that generates the analog trigger event for
              the edge trigger mode.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.analogtrigger.edge.level)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.edge.level = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.edge.level = value
            - print(dmm.digitize.analogtrigger.edge.level)
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
        """Access the ``dmm.digitize.analogtrigger.edge.level`` attribute.

        Description:
            - This attribute defines the signal level that generates the analog trigger event for
              the edge trigger mode.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.analogtrigger.edge.level)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.edge.level = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.edge.level = value
            - print(dmm.digitize.analogtrigger.edge.level)
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
    def slope(self) -> str:
        """Access the ``dmm.digitize.analogtrigger.edge.slope`` attribute.

        Description:
            - This attribute defines the slope of the analog trigger edge.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.analogtrigger.edge.slope)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.edge.slope = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.edge.slope = value
            - print(dmm.digitize.analogtrigger.edge.slope)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".slope"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.slope)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.slope`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @slope.setter
    def slope(self, value: Union[str, float]) -> None:
        """Access the ``dmm.digitize.analogtrigger.edge.slope`` attribute.

        Description:
            - This attribute defines the slope of the analog trigger edge.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.analogtrigger.edge.slope)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.edge.slope = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.edge.slope = value
            - print(dmm.digitize.analogtrigger.edge.slope)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".slope", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.slope = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.slope`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DmmDigitizeAnalogtrigger(BaseTSPCmd):
    """The ``dmm.digitize.analogtrigger`` command tree.

    Properties and methods:
        - ``.edge``: The ``dmm.digitize.analogtrigger.edge`` command tree.
        - ``.mode``: The ``dmm.digitize.analogtrigger.mode`` attribute.
        - ``.window``: The ``dmm.digitize.analogtrigger.window`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._edge = DmmDigitizeAnalogtriggerEdge(device, f"{self._cmd_syntax}.edge")
        self._window = DmmDigitizeAnalogtriggerWindow(device, f"{self._cmd_syntax}.window")

    @property
    def edge(self) -> DmmDigitizeAnalogtriggerEdge:
        """Return the ``dmm.digitize.analogtrigger.edge`` command tree.

        Sub-properties and sub-methods:
            - ``.level``: The ``dmm.digitize.analogtrigger.edge.level`` attribute.
            - ``.slope``: The ``dmm.digitize.analogtrigger.edge.slope`` attribute.
        """
        return self._edge

    @property
    def mode(self) -> str:
        """Access the ``dmm.digitize.analogtrigger.mode`` attribute.

        Description:
            - This attribute configures the type of signal behavior that can generate an analog
              trigger event.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.analogtrigger.mode)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.mode = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.mode = value
            - print(dmm.digitize.analogtrigger.mode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".mode"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.mode)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @mode.setter
    def mode(self, value: Union[str, float]) -> None:
        """Access the ``dmm.digitize.analogtrigger.mode`` attribute.

        Description:
            - This attribute configures the type of signal behavior that can generate an analog
              trigger event.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.analogtrigger.mode)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.analogtrigger.mode = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.analogtrigger.mode = value
            - print(dmm.digitize.analogtrigger.mode)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".mode", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.mode = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.mode`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def window(self) -> DmmDigitizeAnalogtriggerWindow:
        """Return the ``dmm.digitize.analogtrigger.window`` command tree.

        Sub-properties and sub-methods:
            - ``.direction``: The ``dmm.digitize.analogtrigger.window.direction`` attribute.
            - ``.levelhigh``: The ``dmm.digitize.analogtrigger.window.levelhigh`` attribute.
            - ``.levellow``: The ``dmm.digitize.analogtrigger.window.levellow`` attribute.
        """
        return self._window


class DmmDigitize(BaseTSPCmd):
    """The ``dmm.digitize`` command tree.

    Properties and methods:
        - ``.analogtrigger``: The ``dmm.digitize.analogtrigger`` command tree.
        - ``.dbmreference``: The ``dmm.digitize.dbmreference`` attribute.
        - ``.dbreference``: The ``dmm.digitize.dbreference`` attribute.
        - ``.inputimpedance``: The ``dmm.digitize.inputimpedance`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._analogtrigger = DmmDigitizeAnalogtrigger(device, f"{self._cmd_syntax}.analogtrigger")

    @property
    def analogtrigger(self) -> DmmDigitizeAnalogtrigger:
        """Return the ``dmm.digitize.analogtrigger`` command tree.

        Sub-properties and sub-methods:
            - ``.edge``: The ``dmm.digitize.analogtrigger.edge`` command tree.
            - ``.mode``: The ``dmm.digitize.analogtrigger.mode`` attribute.
            - ``.window``: The ``dmm.digitize.analogtrigger.window`` command tree.
        """
        return self._analogtrigger

    @property
    def dbmreference(self) -> str:
        """Access the ``dmm.digitize.dbmreference`` attribute.

        Description:
            - This attribute defines the decibel-milliwatts (dBm) reference.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.dbmreference)`` query.
            - Setting this property to a value will send the ``dmm.digitize.dbmreference = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.dbmreference = value
            - print(dmm.digitize.dbmreference)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".dbmreference"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.dbmreference)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.dbmreference`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @dbmreference.setter
    def dbmreference(self, value: Union[str, float]) -> None:
        """Access the ``dmm.digitize.dbmreference`` attribute.

        Description:
            - This attribute defines the decibel-milliwatts (dBm) reference.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.dbmreference)`` query.
            - Setting this property to a value will send the ``dmm.digitize.dbmreference = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.dbmreference = value
            - print(dmm.digitize.dbmreference)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".dbmreference", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.dbmreference = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.dbmreference`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def dbreference(self) -> str:
        """Access the ``dmm.digitize.dbreference`` attribute.

        Description:
            - This attribute defines the decibel (dB) reference setting for the DMM in volts.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.dbreference)`` query.
            - Setting this property to a value will send the ``dmm.digitize.dbreference = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.dbreference = value
            - print(dmm.digitize.dbreference)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".dbreference"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.dbreference)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.dbreference`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @dbreference.setter
    def dbreference(self, value: Union[str, float]) -> None:
        """Access the ``dmm.digitize.dbreference`` attribute.

        Description:
            - This attribute defines the decibel (dB) reference setting for the DMM in volts.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.dbreference)`` query.
            - Setting this property to a value will send the ``dmm.digitize.dbreference = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.dbreference = value
            - print(dmm.digitize.dbreference)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".dbreference", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.dbreference = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.dbreference`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def inputimpedance(self) -> str:
        """Access the ``dmm.digitize.inputimpedance`` attribute.

        Description:
            - This attribute determines when the 10 MΩ input divider is enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.inputimpedance)`` query.
            - Setting this property to a value will send the ``dmm.digitize.inputimpedance = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.inputimpedance = value
            - print(dmm.digitize.inputimpedance)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".inputimpedance"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.inputimpedance)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.inputimpedance`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @inputimpedance.setter
    def inputimpedance(self, value: Union[str, float]) -> None:
        """Access the ``dmm.digitize.inputimpedance`` attribute.

        Description:
            - This attribute determines when the 10 MΩ input divider is enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.inputimpedance)`` query.
            - Setting this property to a value will send the ``dmm.digitize.inputimpedance = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.inputimpedance = value
            - print(dmm.digitize.inputimpedance)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".inputimpedance", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.inputimpedance = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.inputimpedance`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class Dmm(BaseTSPCmd):
    """The ``dmm`` command tree.

    Properties and methods:
        - ``.digitize``: The ``dmm.digitize`` command tree.
        - ``.measure``: The ``dmm.measure`` command tree.
        - ``.reset()``: The ``dmm.reset()`` function.
        - ``.terminals``: The ``dmm.terminals`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "dmm") -> None:
        super().__init__(device, cmd_syntax)
        self._digitize = DmmDigitize(device, f"{self._cmd_syntax}.digitize")
        self._measure = DmmMeasure(device, f"{self._cmd_syntax}.measure")

    @property
    def digitize(self) -> DmmDigitize:
        """Return the ``dmm.digitize`` command tree.

        Sub-properties and sub-methods:
            - ``.analogtrigger``: The ``dmm.digitize.analogtrigger`` command tree.
            - ``.dbmreference``: The ``dmm.digitize.dbmreference`` attribute.
            - ``.dbreference``: The ``dmm.digitize.dbreference`` attribute.
            - ``.inputimpedance``: The ``dmm.digitize.inputimpedance`` attribute.
        """
        return self._digitize

    @property
    def measure(self) -> DmmMeasure:
        """Return the ``dmm.measure`` command tree.

        Sub-properties and sub-methods:
            - ``.analogtrigger``: The ``dmm.measure.analogtrigger`` command tree.
            - ``.aperture``: The ``dmm.measure.aperture`` attribute.
            - ``.autodelay``: The ``dmm.measure.autodelay`` attribute.
            - ``.autorange``: The ``dmm.measure.autorange`` attribute.
            - ``.autozero``: The ``dmm.measure.autozero`` command tree.
            - ``.bias``: The ``dmm.measure.bias`` command tree.
            - ``.count``: The ``dmm.measure.count`` attribute.
            - ``.dbmreference``: The ``dmm.measure.dbmreference`` attribute.
            - ``.detectorbandwidth``: The ``dmm.measure.detectorbandwidth`` attribute.
            - ``.displaydigits``: The ``dmm.measure.displaydigits`` attribute.
            - ``.filter``: The ``dmm.measure.filter`` command tree.
            - ``.fourrtd``: The ``dmm.measure.fourrtd`` attribute.
            - ``.func``: The ``dmm.measure.func`` attribute.
            - ``.inputimpedance``: The ``dmm.measure.inputimpedance`` attribute.
            - ``.limit``: The ``dmm.measure.limit[Y]`` command tree.
            - ``.linesync``: The ``dmm.measure.linesync`` attribute.
            - ``.math``: The ``dmm.measure.math`` command tree.
            - ``.nplc``: The ``dmm.measure.nplc`` attribute.
            - ``.offsetcompensation``: The ``dmm.measure.offsetcompensation`` command tree.
            - ``.opendetector``: The ``dmm.measure.opendetector`` attribute.
            - ``.range``: The ``dmm.measure.range`` attribute.
            - ``.read()``: The ``dmm.measure.read()`` function.
            - ``.refjunction``: The ``dmm.measure.refjunction`` attribute.
            - ``.rel``: The ``dmm.measure.rel`` command tree.
            - ``.rtdalpha``: The ``dmm.measure.rtdalpha`` attribute.
            - ``.rtdbeta``: The ``dmm.measure.rtdbeta`` attribute.
            - ``.rtddelta``: The ``dmm.measure.rtddelta`` attribute.
            - ``.rtdzero``: The ``dmm.measure.rtdzero`` attribute.
            - ``.sense``: The ``dmm.measure.sense`` command tree.
            - ``.setattribute()``: The ``dmm.measure.setattribute()`` function.
            - ``.thermistor``: The ``dmm.measure.thermistor`` attribute.
            - ``.thermocouple``: The ``dmm.measure.thermocouple`` attribute.
            - ``.threertd``: The ``dmm.measure.threertd`` attribute.
            - ``.threshold``: The ``dmm.measure.threshold`` command tree.
            - ``.transducer``: The ``dmm.measure.transducer`` attribute.
            - ``.twortd``: The ``dmm.measure.twortd`` attribute.
            - ``.unit``: The ``dmm.measure.unit`` attribute.
        """
        return self._measure

    @property
    def terminals(self) -> str:
        """Access the ``dmm.terminals`` attribute.

        Description:
            - This attribute describes which set of input and output terminals the instrument is
              using.

        Usage:
            - Accessing this property will send the ``print(dmm.terminals)`` query.

        TSP Syntax:
            ```
            - print(dmm.terminals)
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

    def reset(self, scope: str) -> None:
        """Run the ``dmm.reset()`` function.

        Description:
            - Resets the DMM functions and attributes in the instrument, as indicated by the
              parameter.

        TSP Syntax:
            ```
            - dmm.reset()
            ```

        Args:
            scope: A string equaling 'active' to set the active function only to factory default
                settings or 'all' to set all functions back to factory default settings.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.reset({scope})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.reset()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
