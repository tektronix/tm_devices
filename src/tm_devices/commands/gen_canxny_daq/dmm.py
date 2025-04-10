# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The dmm commands module.

These commands are used in the following models:
DAQ6510

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
    - dmm.digitize.aperture
    - dmm.digitize.count
    - dmm.digitize.dbmreference
    - dmm.digitize.dbreference
    - dmm.digitize.displaydigits
    - dmm.digitize.func
    - dmm.digitize.inputimpedance
    - dmm.digitize.limit[Y].audible
    - dmm.digitize.limit[Y].autoclear
    - dmm.digitize.limit[Y].enable
    - dmm.digitize.limit[Y].fail
    - dmm.digitize.limit[Y].high.value
    - dmm.digitize.limit[Y].low.value
    - dmm.digitize.math.enable
    - dmm.digitize.math.format
    - dmm.digitize.math.mxb.bfactor
    - dmm.digitize.math.mxb.mfactor
    - dmm.digitize.math.percent
    - dmm.digitize.range
    - dmm.digitize.read()
    - dmm.digitize.readwithtime()
    - dmm.digitize.rel.acquire()
    - dmm.digitize.rel.enable
    - dmm.digitize.rel.level
    - dmm.digitize.samplerate
    - dmm.digitize.unit
    - dmm.digitize.userdelay[N]
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
    - dmm.measure.configlist.catalog()
    - dmm.measure.configlist.create()
    - dmm.measure.configlist.delete()
    - dmm.measure.configlist.query()
    - dmm.measure.configlist.recall()
    - dmm.measure.configlist.size()
    - dmm.measure.configlist.store()
    - dmm.measure.configlist.storefunc()
    - dmm.measure.count
    - dmm.measure.dbmreference
    - dmm.measure.dbreference
    - dmm.measure.detectorbandwidth
    - dmm.measure.displaydigits
    - dmm.measure.filter.count
    - dmm.measure.filter.enable
    - dmm.measure.filter.type
    - dmm.measure.filter.window
    - dmm.measure.fourrtd
    - dmm.measure.func
    - dmm.measure.getattribute()
    - dmm.measure.inputimpedance
    - dmm.measure.limit[Y].audible
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
    - dmm.measure.readwithtime()
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
    - dmm.measure.simreftemperature
    - dmm.measure.thermistor
    - dmm.measure.thermocouple
    - dmm.measure.threertd
    - dmm.measure.threshold.autorange
    - dmm.measure.threshold.range
    - dmm.measure.transducer
    - dmm.measure.twortd
    - dmm.measure.unit
    - dmm.measure.userdelay[N]
    - dmm.reset()
    - dmm.terminals
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
        - ``.audible``: The ``dmm.measure.limit[Y].audible`` attribute.
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
    def audible(self) -> str:
        """Access the ``dmm.measure.limit[Y].audible`` attribute.

        Description:
            - This attribute determines if the instrument beeper sounds when a limit test passes or
              fails.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.limit[Y].audible)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.limit[Y].audible = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.limit[Y].audible = value
            - print(dmm.measure.limit[Y].audible)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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
        """Access the ``dmm.measure.limit[Y].audible`` attribute.

        Description:
            - This attribute determines if the instrument beeper sounds when a limit test passes or
              fails.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.limit[Y].audible)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.limit[Y].audible = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.limit[Y].audible = value
            - print(dmm.measure.limit[Y].audible)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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


class DmmMeasureConfiglist(BaseTSPCmd):
    """The ``dmm.measure.configlist`` command tree.

    Properties and methods:
        - ``.catalog()``: The ``dmm.measure.configlist.catalog()`` function.
        - ``.create()``: The ``dmm.measure.configlist.create()`` function.
        - ``.delete()``: The ``dmm.measure.configlist.delete()`` function.
        - ``.query()``: The ``dmm.measure.configlist.query()`` function.
        - ``.recall()``: The ``dmm.measure.configlist.recall()`` function.
        - ``.size()``: The ``dmm.measure.configlist.size()`` function.
        - ``.store()``: The ``dmm.measure.configlist.store()`` function.
        - ``.storefunc()``: The ``dmm.measure.configlist.storefunc()`` function.
    """

    def catalog(self) -> str:
        """Run the ``dmm.measure.configlist.catalog()`` function.

        Description:
            - This function returns the name of one measure configuration list that is stored on the
              instrument.

        TSP Syntax:
            ```
            - dmm.measure.configlist.catalog()
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
        """Run the ``dmm.measure.configlist.create()`` function.

        Description:
            - This function creates an empty measure configuration list.

        TSP Syntax:
            ```
            - dmm.measure.configlist.create()
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
        """Run the ``dmm.measure.configlist.delete()`` function.

        Description:
            - This function deletes a measure configuration list.

        TSP Syntax:
            ```
            - dmm.measure.configlist.delete()
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
        """Run the ``dmm.measure.configlist.query()`` function.

        Description:
            - This function returns a list of TSP commands and parameter settings that are stored in
              the specified configuration index.

        TSP Syntax:
            ```
            - dmm.measure.configlist.query()
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

    def recall(self, list_name: str, index: Optional[int] = None) -> None:
        """Run the ``dmm.measure.configlist.recall()`` function.

        Description:
            - This function recalls a configuration index in a measure configuration list.

        TSP Syntax:
            ```
            - dmm.measure.configlist.recall()
            ```

        Args:
            list_name: A string that represents the name of a measure configuration list.
            index (optional): A number that defines a specific configuration index in the measure
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
                f"{self._cmd_syntax}.recall({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.recall()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def size(self, list_name: str) -> str:
        """Run the ``dmm.measure.configlist.size()`` function.

        Description:
            - This function returns the size (number of configuration indexes) of a measure
              configuration list.

        TSP Syntax:
            ```
            - dmm.measure.configlist.size()
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
        """Run the ``dmm.measure.configlist.store()`` function.

        Description:
            - This function stores the active measure or digitize settings into the named
              configuration list.

        TSP Syntax:
            ```
            - dmm.measure.configlist.store()
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
        """Run the ``dmm.measure.configlist.storefunc()`` function.

        Description:
            - This function allows you to store the settings for a measure function into a measure
              configuration list whether or not the function is active.

        TSP Syntax:
            ```
            - dmm.measure.configlist.storefunc()
            ```

        Args:
            list_name: Name of the configuration list in which to store the function settings.
            function: The measure function settings to save into the configuration list; see
                Details.
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
        - ``.configlist``: The ``dmm.measure.configlist`` command tree.
        - ``.count``: The ``dmm.measure.count`` attribute.
        - ``.dbmreference``: The ``dmm.measure.dbmreference`` attribute.
        - ``.dbreference``: The ``dmm.measure.dbreference`` attribute.
        - ``.detectorbandwidth``: The ``dmm.measure.detectorbandwidth`` attribute.
        - ``.displaydigits``: The ``dmm.measure.displaydigits`` attribute.
        - ``.filter``: The ``dmm.measure.filter`` command tree.
        - ``.fourrtd``: The ``dmm.measure.fourrtd`` attribute.
        - ``.func``: The ``dmm.measure.func`` attribute.
        - ``.getattribute()``: The ``dmm.measure.getattribute()`` function.
        - ``.inputimpedance``: The ``dmm.measure.inputimpedance`` attribute.
        - ``.limit``: The ``dmm.measure.limit[Y]`` command tree.
        - ``.linesync``: The ``dmm.measure.linesync`` attribute.
        - ``.math``: The ``dmm.measure.math`` command tree.
        - ``.nplc``: The ``dmm.measure.nplc`` attribute.
        - ``.offsetcompensation``: The ``dmm.measure.offsetcompensation`` command tree.
        - ``.opendetector``: The ``dmm.measure.opendetector`` attribute.
        - ``.range``: The ``dmm.measure.range`` attribute.
        - ``.read()``: The ``dmm.measure.read()`` function.
        - ``.readwithtime()``: The ``dmm.measure.readwithtime()`` function.
        - ``.refjunction``: The ``dmm.measure.refjunction`` attribute.
        - ``.rel``: The ``dmm.measure.rel`` command tree.
        - ``.rtdalpha``: The ``dmm.measure.rtdalpha`` attribute.
        - ``.rtdbeta``: The ``dmm.measure.rtdbeta`` attribute.
        - ``.rtddelta``: The ``dmm.measure.rtddelta`` attribute.
        - ``.rtdzero``: The ``dmm.measure.rtdzero`` attribute.
        - ``.sense``: The ``dmm.measure.sense`` command tree.
        - ``.setattribute()``: The ``dmm.measure.setattribute()`` function.
        - ``.simreftemperature``: The ``dmm.measure.simreftemperature`` attribute.
        - ``.thermistor``: The ``dmm.measure.thermistor`` attribute.
        - ``.thermocouple``: The ``dmm.measure.thermocouple`` attribute.
        - ``.threertd``: The ``dmm.measure.threertd`` attribute.
        - ``.threshold``: The ``dmm.measure.threshold`` command tree.
        - ``.transducer``: The ``dmm.measure.transducer`` attribute.
        - ``.twortd``: The ``dmm.measure.twortd`` attribute.
        - ``.unit``: The ``dmm.measure.unit`` attribute.
        - ``.userdelay``: The ``dmm.measure.userdelay[N]`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._analogtrigger = DmmMeasureAnalogtrigger(device, f"{self._cmd_syntax}.analogtrigger")
        self._autozero = DmmMeasureAutozero(device, f"{self._cmd_syntax}.autozero")
        self._bias = DmmMeasureBias(device, f"{self._cmd_syntax}.bias")
        self._configlist = DmmMeasureConfiglist(device, f"{self._cmd_syntax}.configlist")
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
        self._userdelay: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.userdelay[{{key}}]",
            write_syntax=f"{self._cmd_syntax}.userdelay[{{key}}] = ",
            query_syntax=f"print({self._cmd_syntax}.userdelay[{{key}}])",
            device=self._device,
        )

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
    def configlist(self) -> DmmMeasureConfiglist:
        """Return the ``dmm.measure.configlist`` command tree.

        Sub-properties and sub-methods:
            - ``.catalog()``: The ``dmm.measure.configlist.catalog()`` function.
            - ``.create()``: The ``dmm.measure.configlist.create()`` function.
            - ``.delete()``: The ``dmm.measure.configlist.delete()`` function.
            - ``.query()``: The ``dmm.measure.configlist.query()`` function.
            - ``.recall()``: The ``dmm.measure.configlist.recall()`` function.
            - ``.size()``: The ``dmm.measure.configlist.size()`` function.
            - ``.store()``: The ``dmm.measure.configlist.store()`` function.
            - ``.storefunc()``: The ``dmm.measure.configlist.storefunc()`` function.
        """
        return self._configlist

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
    def dbreference(self) -> str:
        """Access the ``dmm.measure.dbreference`` attribute.

        Description:
            - This attribute defines the decibel (dB) reference setting for the DMM in volts.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.dbreference)`` query.
            - Setting this property to a value will send the ``dmm.measure.dbreference = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.dbreference = value
            - print(dmm.measure.dbreference)
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
        """Access the ``dmm.measure.dbreference`` attribute.

        Description:
            - This attribute defines the decibel (dB) reference setting for the DMM in volts.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.dbreference)`` query.
            - Setting this property to a value will send the ``dmm.measure.dbreference = value``
              command.

        TSP Syntax:
            ```
            - dmm.measure.dbreference = value
            - print(dmm.measure.dbreference)
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
            - ``.audible``: The ``dmm.measure.limit[Y].audible`` attribute.
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
    def simreftemperature(self) -> str:
        """Access the ``dmm.measure.simreftemperature`` attribute.

        Description:
            - This attribute sets the simulated reference temperature of the thermocouple reference
              junction.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.simreftemperature)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.simreftemperature = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.simreftemperature = value
            - print(dmm.measure.simreftemperature)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".simreftemperature"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.simreftemperature)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.simreftemperature`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @simreftemperature.setter
    def simreftemperature(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measure.simreftemperature`` attribute.

        Description:
            - This attribute sets the simulated reference temperature of the thermocouple reference
              junction.

        Usage:
            - Accessing this property will send the ``print(dmm.measure.simreftemperature)`` query.
            - Setting this property to a value will send the
              ``dmm.measure.simreftemperature = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.simreftemperature = value
            - print(dmm.measure.simreftemperature)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".simreftemperature", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.simreftemperature = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.simreftemperature`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

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

    @property
    def userdelay(self) -> Dict[int, Union[str, float]]:
        """Access the ``dmm.measure.userdelay[N]`` attribute.

        Description:
            - This attribute sets a user-defined delay that you can use in the trigger model.

        Usage:
            - Accessing an item from this property will send the ``print(dmm.measure.userdelay[N])``
              query.
            - Setting an item from this property to a value will send the
              ``dmm.measure.userdelay[N] = value`` command.

        TSP Syntax:
            ```
            - dmm.measure.userdelay[N] = value
            - print(dmm.measure.userdelay[N])
            ```

        Info:
            - ``N``, the user delay to which this time applies (1 to 5).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._userdelay

    def getattribute(self, function: str, setting: str) -> str:
        """Run the ``dmm.measure.getattribute()`` function.

        Description:
            - This function returns the setting for a function attribute.

        TSP Syntax:
            ```
            - dmm.measure.getattribute()
            ```

        Args:
            function: The measurement function; see Details.
            setting: The attribute for the function; refer to dmm.measure.setattribute() for
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

    def readwithtime(self, buffer_name: Optional[str] = None) -> str:
        """Run the ``dmm.measure.readwithtime()`` function.

        Description:
            - This function initiates measurements and returns the last actual measurement and time
              information in UTC format without using the trigger model.

        TSP Syntax:
            ```
            - dmm.measure.readwithtime()
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


class DmmDigitizeRel(BaseTSPCmd):
    """The ``dmm.digitize.rel`` command tree.

    Properties and methods:
        - ``.acquire()``: The ``dmm.digitize.rel.acquire()`` function.
        - ``.enable``: The ``dmm.digitize.rel.enable`` attribute.
        - ``.level``: The ``dmm.digitize.rel.level`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``dmm.digitize.rel.enable`` attribute.

        Description:
            - This attribute enables or disables the application of a relative offset value to the
              measurement.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.rel.enable)`` query.
            - Setting this property to a value will send the ``dmm.digitize.rel.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.rel.enable = value
            - print(dmm.digitize.rel.enable)
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
        """Access the ``dmm.digitize.rel.enable`` attribute.

        Description:
            - This attribute enables or disables the application of a relative offset value to the
              measurement.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.rel.enable)`` query.
            - Setting this property to a value will send the ``dmm.digitize.rel.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.rel.enable = value
            - print(dmm.digitize.rel.enable)
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
        """Access the ``dmm.digitize.rel.level`` attribute.

        Description:
            - This attribute contains the relative offset value.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.rel.level)`` query.
            - Setting this property to a value will send the ``dmm.digitize.rel.level = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.rel.level = value
            - print(dmm.digitize.rel.level)
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
        """Access the ``dmm.digitize.rel.level`` attribute.

        Description:
            - This attribute contains the relative offset value.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.rel.level)`` query.
            - Setting this property to a value will send the ``dmm.digitize.rel.level = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.rel.level = value
            - print(dmm.digitize.rel.level)
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
        """Run the ``dmm.digitize.rel.acquire()`` function.

        Description:
            - This function acquires a measurement and stores it as the relative offset value for
              the selected digitize function.

        TSP Syntax:
            ```
            - dmm.digitize.rel.acquire()
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


class DmmDigitizeMathMxb(BaseTSPCmd):
    """The ``dmm.digitize.math.mxb`` command tree.

    Properties and methods:
        - ``.bfactor``: The ``dmm.digitize.math.mxb.bfactor`` attribute.
        - ``.mfactor``: The ``dmm.digitize.math.mxb.mfactor`` attribute.
    """

    @property
    def bfactor(self) -> str:
        """Access the ``dmm.digitize.math.mxb.bfactor`` attribute.

        Description:
            - This attribute specifies the offset, b, for the y = mx + b operation.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.math.mxb.bfactor)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.math.mxb.bfactor = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.math.mxb.bfactor = value
            - print(dmm.digitize.math.mxb.bfactor)
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
        """Access the ``dmm.digitize.math.mxb.bfactor`` attribute.

        Description:
            - This attribute specifies the offset, b, for the y = mx + b operation.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.math.mxb.bfactor)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.math.mxb.bfactor = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.math.mxb.bfactor = value
            - print(dmm.digitize.math.mxb.bfactor)
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
        """Access the ``dmm.digitize.math.mxb.mfactor`` attribute.

        Description:
            - This attribute specifies the scale factor, m, for the y = mx + b math operation.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.math.mxb.mfactor)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.math.mxb.mfactor = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.math.mxb.mfactor = value
            - print(dmm.digitize.math.mxb.mfactor)
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
        """Access the ``dmm.digitize.math.mxb.mfactor`` attribute.

        Description:
            - This attribute specifies the scale factor, m, for the y = mx + b math operation.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.math.mxb.mfactor)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.math.mxb.mfactor = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.math.mxb.mfactor = value
            - print(dmm.digitize.math.mxb.mfactor)
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


class DmmDigitizeMath(BaseTSPCmd):
    """The ``dmm.digitize.math`` command tree.

    Properties and methods:
        - ``.enable``: The ``dmm.digitize.math.enable`` attribute.
        - ``.format``: The ``dmm.digitize.math.format`` attribute.
        - ``.mxb``: The ``dmm.digitize.math.mxb`` command tree.
        - ``.percent``: The ``dmm.digitize.math.percent`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mxb = DmmDigitizeMathMxb(device, f"{self._cmd_syntax}.mxb")

    @property
    def enable(self) -> str:
        """Access the ``dmm.digitize.math.enable`` attribute.

        Description:
            - This attribute enables or disables math operations on measurements for the selected
              digitize function.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.math.enable)`` query.
            - Setting this property to a value will send the ``dmm.digitize.math.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.math.enable = value
            - print(dmm.digitize.math.enable)
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
        """Access the ``dmm.digitize.math.enable`` attribute.

        Description:
            - This attribute enables or disables math operations on measurements for the selected
              digitize function.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.math.enable)`` query.
            - Setting this property to a value will send the ``dmm.digitize.math.enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.math.enable = value
            - print(dmm.digitize.math.enable)
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
        """Access the ``dmm.digitize.math.format`` attribute.

        Description:
            - This attribute specifies which math operation is performed on measurements when math
              operations are enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.math.format)`` query.
            - Setting this property to a value will send the ``dmm.digitize.math.format = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.math.format = value
            - print(dmm.digitize.math.format)
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
        """Access the ``dmm.digitize.math.format`` attribute.

        Description:
            - This attribute specifies which math operation is performed on measurements when math
              operations are enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.math.format)`` query.
            - Setting this property to a value will send the ``dmm.digitize.math.format = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.math.format = value
            - print(dmm.digitize.math.format)
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
    def mxb(self) -> DmmDigitizeMathMxb:
        """Return the ``dmm.digitize.math.mxb`` command tree.

        Sub-properties and sub-methods:
            - ``.bfactor``: The ``dmm.digitize.math.mxb.bfactor`` attribute.
            - ``.mfactor``: The ``dmm.digitize.math.mxb.mfactor`` attribute.
        """
        return self._mxb

    @property
    def percent(self) -> str:
        """Access the ``dmm.digitize.math.percent`` attribute.

        Description:
            - This attribute specifies the reference constant that is used when math operations are
              set to percent.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.math.percent)`` query.
            - Setting this property to a value will send the ``dmm.digitize.math.percent = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.math.percent = value
            - print(dmm.digitize.math.percent)
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
        """Access the ``dmm.digitize.math.percent`` attribute.

        Description:
            - This attribute specifies the reference constant that is used when math operations are
              set to percent.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.math.percent)`` query.
            - Setting this property to a value will send the ``dmm.digitize.math.percent = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.math.percent = value
            - print(dmm.digitize.math.percent)
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


class DmmDigitizeLimitItemLow(BaseTSPCmd):
    """The ``dmm.digitize.limit[Y].low`` command tree.

    Info:
        - ``Y``, the limit number: 1 or 2.

    Properties and methods:
        - ``.value``: The ``dmm.digitize.limit[Y].low.value`` attribute.
    """

    @property
    def value(self) -> str:
        """Access the ``dmm.digitize.limit[Y].low.value`` attribute.

        Description:
            - This attribute specifies the lower limit for a limit test.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.limit[Y].low.value)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.limit[Y].low.value = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.limit[Y].low.value = value
            - print(dmm.digitize.limit[Y].low.value)
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
        """Access the ``dmm.digitize.limit[Y].low.value`` attribute.

        Description:
            - This attribute specifies the lower limit for a limit test.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.limit[Y].low.value)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.limit[Y].low.value = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.limit[Y].low.value = value
            - print(dmm.digitize.limit[Y].low.value)
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


class DmmDigitizeLimitItemHigh(BaseTSPCmd):
    """The ``dmm.digitize.limit[Y].high`` command tree.

    Info:
        - ``Y``, the limit number: 1 or 2.

    Properties and methods:
        - ``.value``: The ``dmm.digitize.limit[Y].high.value`` attribute.
    """

    @property
    def value(self) -> str:
        """Access the ``dmm.digitize.limit[Y].high.value`` attribute.

        Description:
            - This attribute specifies the upper limit for a limit test.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.limit[Y].high.value)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.limit[Y].high.value = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.limit[Y].high.value = value
            - print(dmm.digitize.limit[Y].high.value)
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
        """Access the ``dmm.digitize.limit[Y].high.value`` attribute.

        Description:
            - This attribute specifies the upper limit for a limit test.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.limit[Y].high.value)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.limit[Y].high.value = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.limit[Y].high.value = value
            - print(dmm.digitize.limit[Y].high.value)
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


class DmmDigitizeLimitItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``dmm.digitize.limit[Y]`` command tree.

    Info:
        - ``Y``, the limit number: 1 or 2.

    Properties and methods:
        - ``.audible``: The ``dmm.digitize.limit[Y].audible`` attribute.
        - ``.autoclear``: The ``dmm.digitize.limit[Y].autoclear`` attribute.
        - ``.enable``: The ``dmm.digitize.limit[Y].enable`` attribute.
        - ``.fail``: The ``dmm.digitize.limit[Y].fail`` attribute.
        - ``.high``: The ``dmm.digitize.limit[Y].high`` command tree.
        - ``.low``: The ``dmm.digitize.limit[Y].low`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = DmmDigitizeLimitItemHigh(device, f"{self._cmd_syntax}.high")
        self._low = DmmDigitizeLimitItemLow(device, f"{self._cmd_syntax}.low")

    @property
    def audible(self) -> str:
        """Access the ``dmm.digitize.limit[Y].audible`` attribute.

        Description:
            - This attribute determines if the instrument beeper sounds when a limit test passes or
              fails.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.limit[Y].audible)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.limit[Y].audible = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.limit[Y].audible = value
            - print(dmm.digitize.limit[Y].audible)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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
        """Access the ``dmm.digitize.limit[Y].audible`` attribute.

        Description:
            - This attribute determines if the instrument beeper sounds when a limit test passes or
              fails.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.limit[Y].audible)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.limit[Y].audible = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.limit[Y].audible = value
            - print(dmm.digitize.limit[Y].audible)
            ```

        Info:
            - ``Y``, the limit number: 1 or 2.

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
        """Access the ``dmm.digitize.limit[Y].autoclear`` attribute.

        Description:
            - This attribute indicates if the test result for limit Y should be cleared
              automatically or not.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.limit[Y].autoclear)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.limit[Y].autoclear = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.limit[Y].autoclear = value
            - print(dmm.digitize.limit[Y].autoclear)
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
        """Access the ``dmm.digitize.limit[Y].autoclear`` attribute.

        Description:
            - This attribute indicates if the test result for limit Y should be cleared
              automatically or not.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.limit[Y].autoclear)``
              query.
            - Setting this property to a value will send the
              ``dmm.digitize.limit[Y].autoclear = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.limit[Y].autoclear = value
            - print(dmm.digitize.limit[Y].autoclear)
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
        """Access the ``dmm.digitize.limit[Y].enable`` attribute.

        Description:
            - This attribute enables or disables a limit test on the measurement from the selected
              digitize function.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.limit[Y].enable)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.limit[Y].enable = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.limit[Y].enable = value
            - print(dmm.digitize.limit[Y].enable)
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
        """Access the ``dmm.digitize.limit[Y].enable`` attribute.

        Description:
            - This attribute enables or disables a limit test on the measurement from the selected
              digitize function.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.limit[Y].enable)`` query.
            - Setting this property to a value will send the
              ``dmm.digitize.limit[Y].enable = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.limit[Y].enable = value
            - print(dmm.digitize.limit[Y].enable)
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
        """Access the ``dmm.digitize.limit[Y].fail`` attribute.

        Description:
            - This attribute queries the results of a limit test.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.limit[Y].fail)`` query.

        TSP Syntax:
            ```
            - print(dmm.digitize.limit[Y].fail)
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
    def high(self) -> DmmDigitizeLimitItemHigh:
        """Return the ``dmm.digitize.limit[Y].high`` command tree.

        Info:
            - ``Y``, the limit number: 1 or 2.

        Sub-properties and sub-methods:
            - ``.value``: The ``dmm.digitize.limit[Y].high.value`` attribute.
        """
        return self._high

    @property
    def low(self) -> DmmDigitizeLimitItemLow:
        """Return the ``dmm.digitize.limit[Y].low`` command tree.

        Info:
            - ``Y``, the limit number: 1 or 2.

        Sub-properties and sub-methods:
            - ``.value``: The ``dmm.digitize.limit[Y].low.value`` attribute.
        """
        return self._low


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
        - ``.aperture``: The ``dmm.digitize.aperture`` attribute.
        - ``.count``: The ``dmm.digitize.count`` attribute.
        - ``.dbmreference``: The ``dmm.digitize.dbmreference`` attribute.
        - ``.dbreference``: The ``dmm.digitize.dbreference`` attribute.
        - ``.displaydigits``: The ``dmm.digitize.displaydigits`` attribute.
        - ``.func``: The ``dmm.digitize.func`` attribute.
        - ``.inputimpedance``: The ``dmm.digitize.inputimpedance`` attribute.
        - ``.limit``: The ``dmm.digitize.limit[Y]`` command tree.
        - ``.math``: The ``dmm.digitize.math`` command tree.
        - ``.range``: The ``dmm.digitize.range`` attribute.
        - ``.read()``: The ``dmm.digitize.read()`` function.
        - ``.readwithtime()``: The ``dmm.digitize.readwithtime()`` function.
        - ``.rel``: The ``dmm.digitize.rel`` command tree.
        - ``.samplerate``: The ``dmm.digitize.samplerate`` attribute.
        - ``.unit``: The ``dmm.digitize.unit`` attribute.
        - ``.userdelay``: The ``dmm.digitize.userdelay[N]`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._analogtrigger = DmmDigitizeAnalogtrigger(device, f"{self._cmd_syntax}.analogtrigger")
        self._limit: Dict[int, DmmDigitizeLimitItem] = DefaultDictPassKeyToFactory(
            lambda x: DmmDigitizeLimitItem(device, f"{self._cmd_syntax}.limit[{x}]")
        )
        self._math = DmmDigitizeMath(device, f"{self._cmd_syntax}.math")
        self._rel = DmmDigitizeRel(device, f"{self._cmd_syntax}.rel")
        self._userdelay: Dict[int, Union[str, float]] = DefaultDictDeviceCommunication(
            cmd_syntax=f"{self._cmd_syntax}.userdelay[{{key}}]",
            write_syntax=f"{self._cmd_syntax}.userdelay[{{key}}] = ",
            query_syntax=f"print({self._cmd_syntax}.userdelay[{{key}}])",
            device=self._device,
        )

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
    def aperture(self) -> str:
        """Access the ``dmm.digitize.aperture`` attribute.

        Description:
            - This attribute determines the aperture setting for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.aperture)`` query.
            - Setting this property to a value will send the ``dmm.digitize.aperture = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.aperture = value
            - print(dmm.digitize.aperture)
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
        """Access the ``dmm.digitize.aperture`` attribute.

        Description:
            - This attribute determines the aperture setting for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.aperture)`` query.
            - Setting this property to a value will send the ``dmm.digitize.aperture = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.aperture = value
            - print(dmm.digitize.aperture)
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
    def count(self) -> str:
        """Access the ``dmm.digitize.count`` attribute.

        Description:
            - This attribute sets the number of measurements to digitize when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.count)`` query.
            - Setting this property to a value will send the ``dmm.digitize.count = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.count = value
            - print(dmm.digitize.count)
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
        """Access the ``dmm.digitize.count`` attribute.

        Description:
            - This attribute sets the number of measurements to digitize when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.count)`` query.
            - Setting this property to a value will send the ``dmm.digitize.count = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.count = value
            - print(dmm.digitize.count)
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
    def displaydigits(self) -> str:
        """Access the ``dmm.digitize.displaydigits`` attribute.

        Description:
            - This attribute describes the number of digits that are displayed on the front panel
              for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.displaydigits)`` query.
            - Setting this property to a value will send the ``dmm.digitize.displaydigits = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.displaydigits = value
            - print(dmm.digitize.displaydigits)
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
        """Access the ``dmm.digitize.displaydigits`` attribute.

        Description:
            - This attribute describes the number of digits that are displayed on the front panel
              for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.displaydigits)`` query.
            - Setting this property to a value will send the ``dmm.digitize.displaydigits = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.displaydigits = value
            - print(dmm.digitize.displaydigits)
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
    def func(self) -> str:
        """Access the ``dmm.digitize.func`` attribute.

        Description:
            - This attribute determines which digitize function is active.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.func)`` query.
            - Setting this property to a value will send the ``dmm.digitize.func = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.func = value
            - print(dmm.digitize.func)
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
        """Access the ``dmm.digitize.func`` attribute.

        Description:
            - This attribute determines which digitize function is active.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.func)`` query.
            - Setting this property to a value will send the ``dmm.digitize.func = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.func = value
            - print(dmm.digitize.func)
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

    @property
    def limit(self) -> Dict[int, DmmDigitizeLimitItem]:
        """Return the ``dmm.digitize.limit[Y]`` command tree.

        Info:
            - ``Y``, the limit number: 1 or 2.

        Sub-properties and sub-methods:
            - ``.audible``: The ``dmm.digitize.limit[Y].audible`` attribute.
            - ``.autoclear``: The ``dmm.digitize.limit[Y].autoclear`` attribute.
            - ``.enable``: The ``dmm.digitize.limit[Y].enable`` attribute.
            - ``.fail``: The ``dmm.digitize.limit[Y].fail`` attribute.
            - ``.high``: The ``dmm.digitize.limit[Y].high`` command tree.
            - ``.low``: The ``dmm.digitize.limit[Y].low`` command tree.
        """
        return self._limit

    @property
    def math(self) -> DmmDigitizeMath:
        """Return the ``dmm.digitize.math`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``dmm.digitize.math.enable`` attribute.
            - ``.format``: The ``dmm.digitize.math.format`` attribute.
            - ``.mxb``: The ``dmm.digitize.math.mxb`` command tree.
            - ``.percent``: The ``dmm.digitize.math.percent`` attribute.
        """
        return self._math

    @property
    def range(self) -> str:
        """Access the ``dmm.digitize.range`` attribute.

        Description:
            - This attribute determines the positive full-scale measure range for the selected
              digitize function.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.range)`` query.
            - Setting this property to a value will send the ``dmm.digitize.range = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.range = value
            - print(dmm.digitize.range)
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
        """Access the ``dmm.digitize.range`` attribute.

        Description:
            - This attribute determines the positive full-scale measure range for the selected
              digitize function.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.range)`` query.
            - Setting this property to a value will send the ``dmm.digitize.range = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.range = value
            - print(dmm.digitize.range)
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
    def rel(self) -> DmmDigitizeRel:
        """Return the ``dmm.digitize.rel`` command tree.

        Sub-properties and sub-methods:
            - ``.acquire()``: The ``dmm.digitize.rel.acquire()`` function.
            - ``.enable``: The ``dmm.digitize.rel.enable`` attribute.
            - ``.level``: The ``dmm.digitize.rel.level`` attribute.
        """
        return self._rel

    @property
    def samplerate(self) -> str:
        """Access the ``dmm.digitize.samplerate`` attribute.

        Description:
            - This attribute defines the precise acquisition rate at which the digitizing
              measurements are made.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.samplerate)`` query.
            - Setting this property to a value will send the ``dmm.digitize.samplerate = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.samplerate = value
            - print(dmm.digitize.samplerate)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".samplerate"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.samplerate)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.samplerate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @samplerate.setter
    def samplerate(self, value: Union[str, float]) -> None:
        """Access the ``dmm.digitize.samplerate`` attribute.

        Description:
            - This attribute defines the precise acquisition rate at which the digitizing
              measurements are made.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.samplerate)`` query.
            - Setting this property to a value will send the ``dmm.digitize.samplerate = value``
              command.

        TSP Syntax:
            ```
            - dmm.digitize.samplerate = value
            - print(dmm.digitize.samplerate)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".samplerate", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.samplerate = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.samplerate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def unit(self) -> str:
        """Access the ``dmm.digitize.unit`` attribute.

        Description:
            - This attribute sets the units of measurement that are displayed on the front panel of
              the instrument and stored in the reading buffer.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.unit)`` query.
            - Setting this property to a value will send the ``dmm.digitize.unit = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.unit = value
            - print(dmm.digitize.unit)
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
        """Access the ``dmm.digitize.unit`` attribute.

        Description:
            - This attribute sets the units of measurement that are displayed on the front panel of
              the instrument and stored in the reading buffer.

        Usage:
            - Accessing this property will send the ``print(dmm.digitize.unit)`` query.
            - Setting this property to a value will send the ``dmm.digitize.unit = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.unit = value
            - print(dmm.digitize.unit)
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
        """Access the ``dmm.digitize.userdelay[N]`` attribute.

        Description:
            - This attribute sets a user-defined delay that you can use in the trigger model.

        Usage:
            - Accessing an item from this property will send the
              ``print(dmm.digitize.userdelay[N])`` query.
            - Setting an item from this property to a value will send the
              ``dmm.digitize.userdelay[N] = value`` command.

        TSP Syntax:
            ```
            - dmm.digitize.userdelay[N] = value
            - print(dmm.digitize.userdelay[N])
            ```

        Info:
            - ``N``, the user delay to which this time applies (1 to 5).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return self._userdelay

    def read(self, buffer_name: Optional[str] = None) -> str:
        """Run the ``dmm.digitize.read()`` function.

        Description:
            - This function makes digitize measurements, places them in a reading buffer, and
              returns the last reading.

        TSP Syntax:
            ```
            - dmm.digitize.read()
            ```

        Args:
            buffer_name (optional): The name of the reading buffer, which may be a default buffer
                (defbuffer1 or defbuffer2) or a user-defined buffer; if nothing is specified, the
                reading is stored in defbuffer1.

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
        """Run the ``dmm.digitize.readwithtime()`` function.

        Description:
            - This function initiates digitize measurements and returns the last actual measurement
              and time information in UTC format without using the trigger mode.

        TSP Syntax:
            ```
            - dmm.digitize.readwithtime()
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


class Dmm(BaseTSPCmd):
    """The ``dmm`` command tree.

    Constants:
        - ``.APERTURE_AUTO``: The aperture setting for the selected function.
        - ``.ATTR_DIGI_APERTURE``: Aperture setting for digitize.
        - ``.ATTR_DIGI_ATRIG_EDGE_LEVEL``: Analog trigger edge level.
        - ``.ATTR_DIGI_ATRIG_EDGE_SLOPE``: Analog trigger edge slope.
        - ``.ATTR_DIGI_ATRIG_MODE``: Analog trigger mode.
        - ``.ATTR_DIGI_ATRIG_WINDOW_DIRECTION``: Analog trigger window direction.
        - ``.ATTR_DIGI_ATRIG_WINDOW_LEVEL_HIGH``: Analog trigger window level high.
        - ``.ATTR_DIGI_ATRIG_WINDOW_LEVEL_LOW``: Analog trigger window level low.
        - ``.ATTR_DIGI_COUNT``: The number of measurements to digitize when a measurement is
          requested.
        - ``.ATTR_DIGI_DBM_REFERENCE``: Decibel-milliwatts (dBm) reference for digitize voltage.
        - ``.ATTR_DIGI_DB_REFERENCE``: Decibel (dB) reference for digitize voltage.
        - ``.ATTR_DIGI_DIGITS``: Display digits setting for digitize.
        - ``.ATTR_DIGI_FUNCTION``: Digitize function.
        - ``.ATTR_DIGI_INPUT_IMPEDANCE``: Input impedance setting.
        - ``.ATTR_DIGI_LIMIT_AUDIBLE_1``: Set limit 1 audible.
        - ``.ATTR_DIGI_LIMIT_AUDIBLE_2``: Set limit 2 audible.
        - ``.ATTR_DIGI_LIMIT_AUTO_CLEAR_1``: Enable or disable limit 1 autoclear.
        - ``.ATTR_DIGI_LIMIT_AUTO_CLEAR_2``: Enable or disable limit 2 autoclear.
        - ``.ATTR_DIGI_LIMIT_ENABLE_1``: Enable or disable limit 1.
        - ``.ATTR_DIGI_LIMIT_ENABLE_2``: Limit 2 enable.
        - ``.ATTR_DIGI_LIMIT_FAIL_1``: Limit 1 fail.
        - ``.ATTR_DIGI_LIMIT_FAIL_2``: Limit 2 fail.
        - ``.ATTR_DIGI_LIMIT_HIGH_1``: Set limit 1 high value.
        - ``.ATTR_DIGI_LIMIT_HIGH_2``: Set limit 2 high value.
        - ``.ATTR_DIGI_LIMIT_LOW_1``: Set limit 1 low value.
        - ``.ATTR_DIGI_LIMIT_LOW_2``: Set limit 2 low value.
        - ``.ATTR_DIGI_MATH_ENABLE``: Enable math operations for the selected measurement function.
        - ``.ATTR_DIGI_MATH_FORMAT``: Math format.
        - ``.ATTR_DIGI_MATH_MXB_BF``: b (offset) value.
        - ``.ATTR_DIGI_MATH_MXB_MF``: m (scalar) value.
        - ``.ATTR_DIGI_MATH_PERCENT``: Percent.
        - ``.ATTR_DIGI_RANGE``: Measure range setting for digitize.
        - ``.ATTR_DIGI_REL_ENABLE``: Relative enable.
        - ``.ATTR_DIGI_REL_LEVEL``: Relative level.
        - ``.ATTR_DIGI_SAMPLE_RATE``: Sample rate for digitize.
        - ``.ATTR_DIGI_UNIT``: Measure unit setting for digitize.
        - ``.ATTR_DIGI_USER_DELAY_1``: User delay 1 setting for digitize.
        - ``.ATTR_DIGI_USER_DELAY_2``: User delay 2 setting for digitize.
        - ``.ATTR_DIGI_USER_DELAY_3``: User delay 3 setting for digitize.
        - ``.ATTR_DIGI_USER_DELAY_4``: User delay 4 setting for digitize.
        - ``.ATTR_DIGI_USER_DELAY_5``: User delay 5 setting for digitize.
        - ``.ATTR_DIGI_WINDOW_DIRECTION``: Defines if the analog trigger occurs when the signal
          enters or leaves the defined high and low analog signal level boundaries.
        - ``.ATTR_DIGI_WINDOW_LEVEL_HIGH``: The upper boundary of the analog trigger window.
        - ``.ATTR_DIGI_WINDOW_LEVEL_LOW``: The lower boundary of the analog trigger window.
        - ``.ATTR_MEAS_APERTURE``: Aperture setting.
        - ``.ATTR_MEAS_ATRIG_EDGE_LEVEL``: Analog trigger edge level.
        - ``.ATTR_MEAS_ATRIG_EDGE_SLOPE``: Analog trigger edge slope.
        - ``.ATTR_MEAS_ATRIG_MODE``: Analog trigger mode.
        - ``.ATTR_MEAS_ATRIG_WINDOW_DIRECTION``: Analog trigger window direction.
        - ``.ATTR_MEAS_ATRIG_WINDOW_LEVEL_HIGH``: Analog trigger window level high.
        - ``.ATTR_MEAS_ATRIG_WINDOW_LEVEL_LOW``: Analog trigger window level low.
        - ``.ATTR_MEAS_AUTO_DELAY``: Autodelay setting.
        - ``.ATTR_MEAS_AUTO_ZERO``: Autozero setting.
        - ``.ATTR_MEAS_BIAS_LEVEL``: Bias level.
        - ``.ATTR_MEAS_COUNT``: Measure count setting.
        - ``.ATTR_MEAS_DBM_REFERENCE``: dBm reference setting.
        - ``.ATTR_MEAS_DB_REFERENCE``: dB reference setting.
        - ``.ATTR_MEAS_DETECTBW``: Detector bandwidth setting.
        - ``.ATTR_MEAS_DIGITS``: Display digits setting.
        - ``.ATTR_MEAS_FILTER_COUNT``: Set filter count.
        - ``.ATTR_MEAS_FILTER_ENABLE``: Enable or disable filter.
        - ``.ATTR_MEAS_FILTER_TYPE``: Set filter type.
        - ``.ATTR_MEAS_FILTER_WINDOW``: Filter window.
        - ``.ATTR_MEAS_FOUR_RTD``: 4-wire RTD type.
        - ``.ATTR_MEAS_INPUT_IMPEDANCE``: Input impedance setting.
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
        - ``.ATTR_MEAS_LINE_SYNC``: Line sync setting.
        - ``.ATTR_MEAS_MATH_ENABLE``: Enable math operations for the selected measurement function.
        - ``.ATTR_MEAS_MATH_FORMAT``: Math format.
        - ``.ATTR_MEAS_MATH_MXB_BF``: b (offset) value.
        - ``.ATTR_MEAS_MATH_MXB_MF``: m (scalar) value.
        - ``.ATTR_MEAS_MATH_PERCENT``: Percent.
        - ``.ATTR_MEAS_NPLC``: NPLC setting.
        - ``.ATTR_MEAS_OFFCOMP_ENABLE``: Offset compensation.
        - ``.ATTR_MEAS_OPEN_DETECTOR``: Open lead detector.
        - ``.ATTR_MEAS_RANGE``: Measure range setting.
        - ``.ATTR_MEAS_RANGE_AUTO``: Autorange setting.
        - ``.ATTR_MEAS_REF_JUNCTION``: Reference junction.
        - ``.ATTR_MEAS_REL_ENABLE``: Relative offset enable.
        - ``.ATTR_MEAS_REL_LEVEL``: Relative offset level.
        - ``.ATTR_MEAS_REL_METHOD``: Relative offset method for DCV ratio measurements.
        - ``.ATTR_MEAS_RTD_ALPHA``: RTD alpha.
        - ``.ATTR_MEAS_RTD_BETA``: RTD beta.
        - ``.ATTR_MEAS_RTD_DELTA``: RTD delta.
        - ``.ATTR_MEAS_RTD_ZERO``: RTD zero.
        - ``.ATTR_MEAS_SENSE_RANGE``: Sense range (read only).
        - ``.ATTR_MEAS_SIM_REF_TEMP``: Simulated reference temperature.
        - ``.ATTR_MEAS_THERMISTOR``: Thermistor.
        - ``.ATTR_MEAS_THERMOCOUPLE``: Thermocouple.
        - ``.ATTR_MEAS_THREE_RTD``: 3-wire RTD type.
        - ``.ATTR_MEAS_THRESHOLD_RANGE``: Threshold range.
        - ``.ATTR_MEAS_THRESHOLD_RANGE_AUTO``: Threshold autorange.
        - ``.ATTR_MEAS_TRANSDUCER``: Transducer.
        - ``.ATTR_MEAS_TWO_RTD``: 2-wire RTD type.
        - ``.ATTR_MEAS_UNIT``: Measure unit setting.
        - ``.ATTR_MEAS_USER_DELAY_1``: User delay 1 setting.
        - ``.ATTR_MEAS_USER_DELAY_2``: User delay 2 setting.
        - ``.ATTR_MEAS_USER_DELAY_3``: User delay 3 setting.
        - ``.ATTR_MEAS_USER_DELAY_4``: User delay 4 setting.
        - ``.ATTR_MEAS_USER_DELAY_5``: User delay 5 setting.
        - ``.AUDIBLE_FAIL``: Sound a beeper when a limit test passes or fails.
        - ``.AUDIBLE_NONE``: Do not sound a beeper when a limit test passes or fails.
        - ``.AUDIBLE_PASS``: Sound a beeper when a limit test passes or passes.
        - ``.DELAY_OFF``: Disable the delay.
        - ``.DELAY_ON``: Enable the delay.
        - ``.DETECTBW_300HZ``: Sets the detector bandwidth to 300 Hz for AC current and AC voltage
          measurements.
        - ``.DETECTBW_30HZ``: Sets the detector bandwidth to 30 Hz for AC current and AC voltage
          measurements.
        - ``.DETECTBW_3HZ``: Sets the detector bandwidth to 3 Hz for AC current and AC voltage
          measurements.
        - ``.DIGITS_3_5``: 3½ display digits.
        - ``.DIGITS_4_5``: 4½ display digits.
        - ``.DIGITS_5_5``: 5½ display digits.
        - ``.DIGITS_6_5``: 6½ display digits.
        - ``.DIRECTION_ENTER``: The analog trigger occurs when the signal enters the defined signal
          boundaries.
        - ``.DIRECTION_LEAVE``: The analog trigger occurs when the signal leaves the defined signal
          boundaries.
        - ``.FAIL_BOTH``: Test failed; measurement exceeded both limits.
        - ``.FAIL_HIGH``: Test failed; measurement exceeded high limit.
        - ``.FAIL_LOW``: Test failed; measurement exceeded low limit.
        - ``.FAIL_NONE``: Test passed; measurement under or equal to the high limit.
        - ``.FILTER_HYBRID_AVG``: Selects the hybrid filter when measurement filter is enabled.
        - ``.FILTER_MOVING_AVG``: Selects the moving filter when measurement filter is enabled.
        - ``.FILTER_REPEAT_AVG``: Selects the repeating filter when measurement filter is enabled.
        - ``.FUNC_4W_RESISTANCE``: 4W resistance measurement function.
        - ``.FUNC_ACV_FREQUENCY``: ACV frequency function.
        - ``.FUNC_ACV_PERIOD``: ACV period function.
        - ``.FUNC_AC_CURRENT``: AC current.
        - ``.FUNC_AC_VOLTAGE``: AC voltage function.
        - ``.FUNC_CAPACITANCE``: Capacitance function.
        - ``.FUNC_CONTINUITY``: Continuity function.
        - ``.FUNC_DCV_RATIO``: DCV ratio function.
        - ``.FUNC_DC_CURRENT``: Current measurement function.
        - ``.FUNC_DC_VOLTAGE``: DC voltage function.
        - ``.FUNC_DIGITIZE_CURRENT``: Digitize current.
        - ``.FUNC_DIGITIZE_VOLTAGE``: Digitize voltage.
        - ``.FUNC_DIODE``: Diode function.
        - ``.FUNC_NONE``: No digitize function selected (read only).
        - ``.FUNC_RESISTANCE``: 2W resistance measurement function.
        - ``.FUNC_TEMPERATURE``: Temperature.
        - ``.IMPEDANCE_10M``: Enable the 10 MΩ input divider for all ranges.
        - ``.IMPEDANCE_AUTO``: Automatically enable the 10 MΩ input divider.
        - ``.MATH_MXB``: Perform y = mx+b operation on measurement.
        - ``.MATH_PERCENT``: Perform percent operation on measurements.
        - ``.MATH_RECIPROCAL``: Perform reciprocal math operation on measurements.
        - ``.METHOD_PARTS``: Apply relative offset to the measurements before calculating the dc
          voltage ratio value.
        - ``.METHOD_RESULT``: Do not apply relative offset to the measurements before calculating
          the dc voltage ratio value.
        - ``.MODE_EDGE``: Set analog trigger event mode to edge (signal crosses one level).
        - ``.MODE_OFF``: Set analog trigger event mode off.
        - ``.MODE_WINDOW``: Set analog trigger event mode to window (signal enters or exits a window
          defined by two levels).
        - ``.OCOMP_AUTO``: Set offset compensation automatically.
        - ``.OCOMP_OFF``: Disable offset compensation.
        - ``.OCOMP_ON``: Enable offset compensation (for 4-wire resistance, not available for ranges
          more than 10 kΩ).
        - ``.OFF``: Set the threshold range manually.
        - ``.ON``: Set the threshold range automatically.
        - ``.RTD_D100``: D100 three-wire RTD.
        - ``.RTD_F100``: F100 4-wire RTD.
        - ``.RTD_PT100``: PT100 three-wire RTD.
        - ``.RTD_PT385``: PT385 three-wire RTD.
        - ``.RTD_PT3916``: PT3916 three-wire RTD.
        - ``.RTD_USER``: User-specified three-wire RTD.
        - ``.SLOPE_FALLING``: Falling slope for the analog trigger edge.
        - ``.SLOPE_RISING``: Rising slope for the analog trigger edge.
        - ``.TERMINALS_FRONT``: Instrument is using the front-panel input and output terminals.
        - ``.TERMINALS_REAR``: Instrument is using the rear-panel input and output terminals.
        - ``.THERMOCOUPLE_B``: B thermocouple type.
        - ``.THERMOCOUPLE_E``: E thermocouple type.
        - ``.THERMOCOUPLE_J``: J thermocouple type.
        - ``.THERMOCOUPLE_K``: K thermocouple type.
        - ``.THERMOCOUPLE_N``: N thermocouple type.
        - ``.THERMOCOUPLE_R``: R thermocouple type.
        - ``.THERMOCOUPLE_S``: S thermocouple type.
        - ``.THERMOCOUPLE_T``: T thermocouple type.
        - ``.THERM_10000``: 10000 ohm thermistor.
        - ``.THERM_2252``: 2252 ohm thermistor.
        - ``.THERM_5000``: 5000 ohm thermistor.
        - ``.TRANS_FOURRTD``: Set the transducer type to  four-wire RTD.
        - ``.TRANS_THERMISTOR``: Set the transducer type to thermistor.
        - ``.TRANS_THERMOCOUPLE``: Set the transducer type to thermocouple.
        - ``.TRANS_THREERTD``: Set the transducer type to  three-wire RTD.
        - ``.TRANS_TWORTD``: Set the transducer type to two-wire RTD.
        - ``.UNIT_AMP``: Set unit of measure to amps (only available for current measurements).
        - ``.UNIT_CELSIUS``: Display Celsius as units of measurement.
        - ``.UNIT_DB``: Display decibels as units for the measure voltage function.
        - ``.UNIT_DBM``: Display decibel-millwatts as units for the  voltage function.
        - ``.UNIT_FAHRENHEIT``: Display Fahrenheit as units of measurement.
        - ``.UNIT_KELVIN``: Display Kelvin as units of measurement.
        - ``.UNIT_VOLT``: Display voltage as units for the voltage function.

    Properties and methods:
        - ``.digitize``: The ``dmm.digitize`` command tree.
        - ``.measure``: The ``dmm.measure`` command tree.
        - ``.reset()``: The ``dmm.reset()`` function.
        - ``.terminals``: The ``dmm.terminals`` attribute.
    """

    APERTURE_AUTO = "dmm.APERTURE_AUTO"
    """str: The aperture setting for the selected function."""
    ATTR_DIGI_APERTURE = "dmm.ATTR_DIGI_APERTURE"
    """str: Aperture setting for digitize."""
    ATTR_DIGI_ATRIG_EDGE_LEVEL = "dmm.ATTR_DIGI_ATRIG_EDGE_LEVEL"
    """str: Analog trigger edge level."""
    ATTR_DIGI_ATRIG_EDGE_SLOPE = "dmm.ATTR_DIGI_ATRIG_EDGE_SLOPE"
    """str: Analog trigger edge slope."""
    ATTR_DIGI_ATRIG_MODE = "dmm.ATTR_DIGI_ATRIG_MODE"
    """str: Analog trigger mode."""
    ATTR_DIGI_ATRIG_WINDOW_DIRECTION = "dmm.ATTR_DIGI_ATRIG_WINDOW_DIRECTION"
    """str: Analog trigger window direction."""
    ATTR_DIGI_ATRIG_WINDOW_LEVEL_HIGH = "dmm.ATTR_DIGI_ATRIG_WINDOW_LEVEL_HIGH"
    """str: Analog trigger window level high."""
    ATTR_DIGI_ATRIG_WINDOW_LEVEL_LOW = "dmm.ATTR_DIGI_ATRIG_WINDOW_LEVEL_LOW"
    """str: Analog trigger window level low."""
    ATTR_DIGI_COUNT = "dmm.ATTR_DIGI_COUNT"
    """str: The number of measurements to digitize when a measurement is requested."""
    ATTR_DIGI_DBM_REFERENCE = "dmm.ATTR_DIGI_DBM_REFERENCE"
    """str: Decibel-milliwatts (dBm) reference for digitize voltage."""
    ATTR_DIGI_DB_REFERENCE = "dmm.ATTR_DIGI_DB_REFERENCE"
    """str: Decibel (dB) reference for digitize voltage."""
    ATTR_DIGI_DIGITS = "dmm.ATTR_DIGI_DIGITS"
    """str: Display digits setting for digitize."""
    ATTR_DIGI_FUNCTION = "dmm.ATTR_DIGI_FUNCTION"
    """str: Digitize function."""
    ATTR_DIGI_INPUT_IMPEDANCE = "dmm.ATTR_DIGI_INPUT_IMPEDANCE"
    """str: Input impedance setting."""
    ATTR_DIGI_LIMIT_AUDIBLE_1 = "dmm.ATTR_DIGI_LIMIT_AUDIBLE_1"
    """str: Set limit 1 audible."""
    ATTR_DIGI_LIMIT_AUDIBLE_2 = "dmm.ATTR_DIGI_LIMIT_AUDIBLE_2"
    """str: Set limit 2 audible."""
    ATTR_DIGI_LIMIT_AUTO_CLEAR_1 = "dmm.ATTR_DIGI_LIMIT_AUTO_CLEAR_1"
    """str: Enable or disable limit 1 autoclear."""
    ATTR_DIGI_LIMIT_AUTO_CLEAR_2 = "dmm.ATTR_DIGI_LIMIT_AUTO_CLEAR_2"
    """str: Enable or disable limit 2 autoclear."""
    ATTR_DIGI_LIMIT_ENABLE_1 = "dmm.ATTR_DIGI_LIMIT_ENABLE_1"
    """str: Enable or disable limit 1."""
    ATTR_DIGI_LIMIT_ENABLE_2 = "dmm.ATTR_DIGI_LIMIT_ENABLE_2"
    """str: Limit 2 enable."""
    ATTR_DIGI_LIMIT_FAIL_1 = "dmm.ATTR_DIGI_LIMIT_FAIL_1"
    """str: Limit 1 fail."""
    ATTR_DIGI_LIMIT_FAIL_2 = "dmm.ATTR_DIGI_LIMIT_FAIL_2"
    """str: Limit 2 fail."""
    ATTR_DIGI_LIMIT_HIGH_1 = "dmm.ATTR_DIGI_LIMIT_HIGH_1"
    """str: Set limit 1 high value."""
    ATTR_DIGI_LIMIT_HIGH_2 = "dmm.ATTR_DIGI_LIMIT_HIGH_2"
    """str: Set limit 2 high value."""
    ATTR_DIGI_LIMIT_LOW_1 = "dmm.ATTR_DIGI_LIMIT_LOW_1"
    """str: Set limit 1 low value."""
    ATTR_DIGI_LIMIT_LOW_2 = "dmm.ATTR_DIGI_LIMIT_LOW_2"
    """str: Set limit 2 low value."""
    ATTR_DIGI_MATH_ENABLE = "dmm.ATTR_DIGI_MATH_ENABLE"
    """str: Enable math operations for the selected measurement function."""
    ATTR_DIGI_MATH_FORMAT = "dmm.ATTR_DIGI_MATH_FORMAT"
    """str: Math format."""
    ATTR_DIGI_MATH_MXB_BF = "dmm.ATTR_DIGI_MATH_MXB_BF"
    """str: b (offset) value."""
    ATTR_DIGI_MATH_MXB_MF = "dmm.ATTR_DIGI_MATH_MXB_MF"
    """str: m (scalar) value."""
    ATTR_DIGI_MATH_PERCENT = "dmm.ATTR_DIGI_MATH_PERCENT"
    """str: Percent."""
    ATTR_DIGI_RANGE = "dmm.ATTR_DIGI_RANGE"
    """str: Measure range setting for digitize."""
    ATTR_DIGI_REL_ENABLE = "dmm.ATTR_DIGI_REL_ENABLE"
    """str: Relative enable."""
    ATTR_DIGI_REL_LEVEL = "dmm.ATTR_DIGI_REL_LEVEL"
    """str: Relative level."""
    ATTR_DIGI_SAMPLE_RATE = "dmm.ATTR_DIGI_SAMPLE_RATE"
    """str: Sample rate for digitize."""
    ATTR_DIGI_UNIT = "dmm.ATTR_DIGI_UNIT"
    """str: Measure unit setting for digitize."""
    ATTR_DIGI_USER_DELAY_1 = "dmm.ATTR_DIGI_USER_DELAY_1"
    """str: User delay 1 setting for digitize."""
    ATTR_DIGI_USER_DELAY_2 = "dmm.ATTR_DIGI_USER_DELAY_2"
    """str: User delay 2 setting for digitize."""
    ATTR_DIGI_USER_DELAY_3 = "dmm.ATTR_DIGI_USER_DELAY_3"
    """str: User delay 3 setting for digitize."""
    ATTR_DIGI_USER_DELAY_4 = "dmm.ATTR_DIGI_USER_DELAY_4"
    """str: User delay 4 setting for digitize."""
    ATTR_DIGI_USER_DELAY_5 = "dmm.ATTR_DIGI_USER_DELAY_5"
    """str: User delay 5 setting for digitize."""
    ATTR_DIGI_WINDOW_DIRECTION = "dmm.ATTR_DIGI_WINDOW_DIRECTION"
    """str: Defines if the analog trigger occurs when the signal enters or leaves the defined high and low analog signal level boundaries."""  # noqa: E501
    ATTR_DIGI_WINDOW_LEVEL_HIGH = "dmm.ATTR_DIGI_WINDOW_LEVEL_HIGH"
    """str: The upper boundary of the analog trigger window."""
    ATTR_DIGI_WINDOW_LEVEL_LOW = "dmm.ATTR_DIGI_WINDOW_LEVEL_LOW"
    """str: The lower boundary of the analog trigger window."""
    ATTR_MEAS_APERTURE = "dmm.ATTR_MEAS_APERTURE"
    """str: Aperture setting."""
    ATTR_MEAS_ATRIG_EDGE_LEVEL = "dmm.ATTR_MEAS_ATRIG_EDGE_LEVEL"
    """str: Analog trigger edge level."""
    ATTR_MEAS_ATRIG_EDGE_SLOPE = "dmm.ATTR_MEAS_ATRIG_EDGE_SLOPE"
    """str: Analog trigger edge slope."""
    ATTR_MEAS_ATRIG_MODE = "dmm.ATTR_MEAS_ATRIG_MODE"
    """str: Analog trigger mode."""
    ATTR_MEAS_ATRIG_WINDOW_DIRECTION = "dmm.ATTR_MEAS_ATRIG_WINDOW_DIRECTION"
    """str: Analog trigger window direction."""
    ATTR_MEAS_ATRIG_WINDOW_LEVEL_HIGH = "dmm.ATTR_MEAS_ATRIG_WINDOW_LEVEL_HIGH"
    """str: Analog trigger window level high."""
    ATTR_MEAS_ATRIG_WINDOW_LEVEL_LOW = "dmm.ATTR_MEAS_ATRIG_WINDOW_LEVEL_LOW"
    """str: Analog trigger window level low."""
    ATTR_MEAS_AUTO_DELAY = "dmm.ATTR_MEAS_AUTO_DELAY"
    """str: Autodelay setting."""
    ATTR_MEAS_AUTO_ZERO = "dmm.ATTR_MEAS_AUTO_ZERO"
    """str: Autozero setting."""
    ATTR_MEAS_BIAS_LEVEL = "dmm.ATTR_MEAS_BIAS_LEVEL"
    """str: Bias level."""
    ATTR_MEAS_COUNT = "dmm.ATTR_MEAS_COUNT"
    """str: Measure count setting."""
    ATTR_MEAS_DBM_REFERENCE = "dmm.ATTR_MEAS_DBM_REFERENCE"
    """str: dBm reference setting."""
    ATTR_MEAS_DB_REFERENCE = "dmm.ATTR_MEAS_DB_REFERENCE"
    """str: dB reference setting."""
    ATTR_MEAS_DETECTBW = "dmm.ATTR_MEAS_DETECTBW"
    """str: Detector bandwidth setting."""
    ATTR_MEAS_DIGITS = "dmm.ATTR_MEAS_DIGITS"
    """str: Display digits setting."""
    ATTR_MEAS_FILTER_COUNT = "dmm.ATTR_MEAS_FILTER_COUNT"
    """str: Set filter count."""
    ATTR_MEAS_FILTER_ENABLE = "dmm.ATTR_MEAS_FILTER_ENABLE"
    """str: Enable or disable filter."""
    ATTR_MEAS_FILTER_TYPE = "dmm.ATTR_MEAS_FILTER_TYPE"
    """str: Set filter type."""
    ATTR_MEAS_FILTER_WINDOW = "dmm.ATTR_MEAS_FILTER_WINDOW"
    """str: Filter window."""
    ATTR_MEAS_FOUR_RTD = "dmm.ATTR_MEAS_FOUR_RTD"
    """str: 4-wire RTD type."""
    ATTR_MEAS_INPUT_IMPEDANCE = "dmm.ATTR_MEAS_INPUT_IMPEDANCE"
    """str: Input impedance setting."""
    ATTR_MEAS_LIMIT_AUDIBLE_1 = "dmm.ATTR_MEAS_LIMIT_AUDIBLE_1"
    """str: Set limit 1 audible."""
    ATTR_MEAS_LIMIT_AUDIBLE_2 = "dmm.ATTR_MEAS_LIMIT_AUDIBLE_2"
    """str: Set limit 2 audible."""
    ATTR_MEAS_LIMIT_AUTO_CLEAR_1 = "dmm.ATTR_MEAS_LIMIT_AUTO_CLEAR_1"
    """str: Enable or disable limit 1 autoclear."""
    ATTR_MEAS_LIMIT_AUTO_CLEAR_2 = "dmm.ATTR_MEAS_LIMIT_AUTO_CLEAR_2"
    """str: Enable or disable limit 2 autoclear."""
    ATTR_MEAS_LIMIT_ENABLE_1 = "dmm.ATTR_MEAS_LIMIT_ENABLE_1"
    """str: Enable or disable limit 1."""
    ATTR_MEAS_LIMIT_ENABLE_2 = "dmm.ATTR_MEAS_LIMIT_ENABLE_2"
    """str: Limit 2 enable."""
    ATTR_MEAS_LIMIT_FAIL_1 = "dmm.ATTR_MEAS_LIMIT_FAIL_1"
    """str: Limit 1 fail."""
    ATTR_MEAS_LIMIT_FAIL_2 = "dmm.ATTR_MEAS_LIMIT_FAIL_2"
    """str: Limit 2 fail."""
    ATTR_MEAS_LIMIT_HIGH_1 = "dmm.ATTR_MEAS_LIMIT_HIGH_1"
    """str: Set limit 1 high value."""
    ATTR_MEAS_LIMIT_HIGH_2 = "dmm.ATTR_MEAS_LIMIT_HIGH_2"
    """str: Set limit 2 high value."""
    ATTR_MEAS_LIMIT_LOW_1 = "dmm.ATTR_MEAS_LIMIT_LOW_1"
    """str: Set limit 1 low value."""
    ATTR_MEAS_LIMIT_LOW_2 = "dmm.ATTR_MEAS_LIMIT_LOW_2"
    """str: Set limit 2 low value."""
    ATTR_MEAS_LINE_SYNC = "dmm.ATTR_MEAS_LINE_SYNC"
    """str: Line sync setting."""
    ATTR_MEAS_MATH_ENABLE = "dmm.ATTR_MEAS_MATH_ENABLE"
    """str: Enable math operations for the selected measurement function."""
    ATTR_MEAS_MATH_FORMAT = "dmm.ATTR_MEAS_MATH_FORMAT"
    """str: Math format."""
    ATTR_MEAS_MATH_MXB_BF = "dmm.ATTR_MEAS_MATH_MXB_BF"
    """str: b (offset) value."""
    ATTR_MEAS_MATH_MXB_MF = "dmm.ATTR_MEAS_MATH_MXB_MF"
    """str: m (scalar) value."""
    ATTR_MEAS_MATH_PERCENT = "dmm.ATTR_MEAS_MATH_PERCENT"
    """str: Percent."""
    ATTR_MEAS_NPLC = "dmm.ATTR_MEAS_NPLC"
    """str: NPLC setting."""
    ATTR_MEAS_OFFCOMP_ENABLE = "dmm.ATTR_MEAS_OFFCOMP_ENABLE"
    """str: Offset compensation."""
    ATTR_MEAS_OPEN_DETECTOR = "dmm.ATTR_MEAS_OPEN_DETECTOR"
    """str: Open lead detector."""
    ATTR_MEAS_RANGE = "dmm.ATTR_MEAS_RANGE"
    """str: Measure range setting."""
    ATTR_MEAS_RANGE_AUTO = "dmm.ATTR_MEAS_RANGE_AUTO"
    """str: Autorange setting."""
    ATTR_MEAS_REF_JUNCTION = "dmm.ATTR_MEAS_REF_JUNCTION"
    """str: Reference junction."""
    ATTR_MEAS_REL_ENABLE = "dmm.ATTR_MEAS_REL_ENABLE"
    """str: Relative offset enable."""
    ATTR_MEAS_REL_LEVEL = "dmm.ATTR_MEAS_REL_LEVEL"
    """str: Relative offset level."""
    ATTR_MEAS_REL_METHOD = "dmm.ATTR_MEAS_REL_METHOD"
    """str: Relative offset method for DCV ratio measurements."""
    ATTR_MEAS_RTD_ALPHA = "dmm.ATTR_MEAS_RTD_ALPHA"
    """str: RTD alpha."""
    ATTR_MEAS_RTD_BETA = "dmm.ATTR_MEAS_RTD_BETA"
    """str: RTD beta."""
    ATTR_MEAS_RTD_DELTA = "dmm.ATTR_MEAS_RTD_DELTA"
    """str: RTD delta."""
    ATTR_MEAS_RTD_ZERO = "dmm.ATTR_MEAS_RTD_ZERO"
    """str: RTD zero."""
    ATTR_MEAS_SENSE_RANGE = "dmm.ATTR_MEAS_SENSE_RANGE"
    """str: Sense range (read only)."""
    ATTR_MEAS_SIM_REF_TEMP = "dmm.ATTR_MEAS_SIM_REF_TEMP"
    """str: Simulated reference temperature."""
    ATTR_MEAS_THERMISTOR = "dmm.ATTR_MEAS_THERMISTOR"
    """str: Thermistor."""
    ATTR_MEAS_THERMOCOUPLE = "dmm.ATTR_MEAS_THERMOCOUPLE"
    """str: Thermocouple."""
    ATTR_MEAS_THREE_RTD = "dmm.ATTR_MEAS_THREE_RTD"
    """str: 3-wire RTD type."""
    ATTR_MEAS_THRESHOLD_RANGE = "dmm.ATTR_MEAS_THRESHOLD_RANGE"
    """str: Threshold range."""
    ATTR_MEAS_THRESHOLD_RANGE_AUTO = "dmm.ATTR_MEAS_THRESHOLD_RANGE_AUTO"
    """str: Threshold autorange."""
    ATTR_MEAS_TRANSDUCER = "dmm.ATTR_MEAS_TRANSDUCER"
    """str: Transducer."""
    ATTR_MEAS_TWO_RTD = "dmm.ATTR_MEAS_TWO_RTD"
    """str: 2-wire RTD type."""
    ATTR_MEAS_UNIT = "dmm.ATTR_MEAS_UNIT"
    """str: Measure unit setting."""
    ATTR_MEAS_USER_DELAY_1 = "dmm.ATTR_MEAS_USER_DELAY_1"
    """str: User delay 1 setting."""
    ATTR_MEAS_USER_DELAY_2 = "dmm.ATTR_MEAS_USER_DELAY_2"
    """str: User delay 2 setting."""
    ATTR_MEAS_USER_DELAY_3 = "dmm.ATTR_MEAS_USER_DELAY_3"
    """str: User delay 3 setting."""
    ATTR_MEAS_USER_DELAY_4 = "dmm.ATTR_MEAS_USER_DELAY_4"
    """str: User delay 4 setting."""
    ATTR_MEAS_USER_DELAY_5 = "dmm.ATTR_MEAS_USER_DELAY_5"
    """str: User delay 5 setting."""
    AUDIBLE_FAIL = "dmm.AUDIBLE_FAIL"
    """str: Sound a beeper when a limit test passes or fails."""
    AUDIBLE_NONE = "dmm.AUDIBLE_NONE"
    """str: Do not sound a beeper when a limit test passes or fails."""
    AUDIBLE_PASS = "dmm.AUDIBLE_PASS"
    """str: Sound a beeper when a limit test passes or passes."""
    DELAY_OFF = "dmm.DELAY_OFF"
    """str: Disable the delay."""
    DELAY_ON = "dmm.DELAY_ON"
    """str: Enable the delay."""
    DETECTBW_300HZ = "dmm.DETECTBW_300HZ"
    """str: Sets the detector bandwidth to 300 Hz for AC current and AC voltage measurements."""
    DETECTBW_30HZ = "dmm.DETECTBW_30HZ"
    """str: Sets the detector bandwidth to 30 Hz for AC current and AC voltage measurements."""
    DETECTBW_3HZ = "dmm.DETECTBW_3HZ"
    """str: Sets the detector bandwidth to 3 Hz for AC current and AC voltage measurements."""
    DIGITS_3_5 = "dmm.DIGITS_3_5"
    """str: 3½ display digits."""
    DIGITS_4_5 = "dmm.DIGITS_4_5"
    """str: 4½ display digits."""
    DIGITS_5_5 = "dmm.DIGITS_5_5"
    """str: 5½ display digits."""
    DIGITS_6_5 = "dmm.DIGITS_6_5"
    """str: 6½ display digits."""
    DIRECTION_ENTER = "dmm.DIRECTION_ENTER"
    """str: The analog trigger occurs when the signal enters the defined signal boundaries."""
    DIRECTION_LEAVE = "dmm.DIRECTION_LEAVE"
    """str: The analog trigger occurs when the signal leaves the defined signal boundaries."""
    FAIL_BOTH = "dmm.FAIL_BOTH"
    """str: Test failed; measurement exceeded both limits."""
    FAIL_HIGH = "dmm.FAIL_HIGH"
    """str: Test failed; measurement exceeded high limit."""
    FAIL_LOW = "dmm.FAIL_LOW"
    """str: Test failed; measurement exceeded low limit."""
    FAIL_NONE = "dmm.FAIL_NONE"
    """str: Test passed; measurement under or equal to the high limit."""
    FILTER_HYBRID_AVG = "dmm.FILTER_HYBRID_AVG"
    """str: Selects the hybrid filter when measurement filter is enabled."""
    FILTER_MOVING_AVG = "dmm.FILTER_MOVING_AVG"
    """str: Selects the moving filter when measurement filter is enabled."""
    FILTER_REPEAT_AVG = "dmm.FILTER_REPEAT_AVG"
    """str: Selects the repeating filter when measurement filter is enabled."""
    FUNC_4W_RESISTANCE = "dmm.FUNC_4W_RESISTANCE"
    """str: 4W resistance measurement function."""
    FUNC_ACV_FREQUENCY = "dmm.FUNC_ACV_FREQUENCY"
    """str: ACV frequency function."""
    FUNC_ACV_PERIOD = "dmm.FUNC_ACV_PERIOD"
    """str: ACV period function."""
    FUNC_AC_CURRENT = "dmm.FUNC_AC_CURRENT"
    """str: AC current."""
    FUNC_AC_VOLTAGE = "dmm.FUNC_AC_VOLTAGE"
    """str: AC voltage function."""
    FUNC_CAPACITANCE = "dmm.FUNC_CAPACITANCE"
    """str: Capacitance function."""
    FUNC_CONTINUITY = "dmm.FUNC_CONTINUITY"
    """str: Continuity function."""
    FUNC_DCV_RATIO = "dmm.FUNC_DCV_RATIO"
    """str: DCV ratio function."""
    FUNC_DC_CURRENT = "dmm.FUNC_DC_CURRENT"
    """str: Current measurement function."""
    FUNC_DC_VOLTAGE = "dmm.FUNC_DC_VOLTAGE"
    """str: DC voltage function."""
    FUNC_DIGITIZE_CURRENT = "dmm.FUNC_DIGITIZE_CURRENT"
    """str: Digitize current."""
    FUNC_DIGITIZE_VOLTAGE = "dmm.FUNC_DIGITIZE_VOLTAGE"
    """str: Digitize voltage."""
    FUNC_DIODE = "dmm.FUNC_DIODE"
    """str: Diode function."""
    FUNC_NONE = "dmm.FUNC_NONE"
    """str: No digitize function selected (read only)."""
    FUNC_RESISTANCE = "dmm.FUNC_RESISTANCE"
    """str: 2W resistance measurement function."""
    FUNC_TEMPERATURE = "dmm.FUNC_TEMPERATURE"
    """str: Temperature."""
    IMPEDANCE_10M = "dmm.IMPEDANCE_10M"
    """str: Enable the 10 MΩ input divider for all ranges."""
    IMPEDANCE_AUTO = "dmm.IMPEDANCE_AUTO"
    """str: Automatically enable the 10 MΩ input divider."""
    MATH_MXB = "dmm.MATH_MXB"
    """str: Perform y = mx+b operation on measurement."""
    MATH_PERCENT = "dmm.MATH_PERCENT"
    """str: Perform percent operation on measurements."""
    MATH_RECIPROCAL = "dmm.MATH_RECIPROCAL"
    """str: Perform reciprocal math operation on measurements."""
    METHOD_PARTS = "dmm.METHOD_PARTS"
    """str: Apply relative offset to the measurements before calculating the dc voltage ratio value."""  # noqa: E501
    METHOD_RESULT = "dmm.METHOD_RESULT"
    """str: Do not apply relative offset to the measurements before calculating the dc voltage ratio value."""  # noqa: E501
    MODE_EDGE = "dmm.MODE_EDGE"
    """str: Set analog trigger event mode to edge (signal crosses one level)."""
    MODE_OFF = "dmm.MODE_OFF"
    """str: Set analog trigger event mode off."""
    MODE_WINDOW = "dmm.MODE_WINDOW"
    """str: Set analog trigger event mode to window (signal enters or exits a window defined by two levels)."""  # noqa: E501
    OCOMP_AUTO = "dmm.OCOMP_AUTO"
    """str: Set offset compensation automatically."""
    OCOMP_OFF = "dmm.OCOMP_OFF"
    """str: Disable offset compensation."""
    OCOMP_ON = "dmm.OCOMP_ON"
    """str: Enable offset compensation (for 4-wire resistance, not available for ranges more than 10 kΩ)."""  # noqa: E501
    OFF = "dmm.OFF"
    """str: Set the threshold range manually."""
    ON = "dmm.ON"
    """str: Set the threshold range automatically."""
    RTD_D100 = "dmm.RTD_D100"
    """str: D100 three-wire RTD."""
    RTD_F100 = "dmm.RTD_F100"
    """str: F100 4-wire RTD."""
    RTD_PT100 = "dmm.RTD_PT100"
    """str: PT100 three-wire RTD."""
    RTD_PT385 = "dmm.RTD_PT385"
    """str: PT385 three-wire RTD."""
    RTD_PT3916 = "dmm.RTD_PT3916"
    """str: PT3916 three-wire RTD."""
    RTD_USER = "dmm.RTD_USER"
    """str: User-specified three-wire RTD."""
    SLOPE_FALLING = "dmm.SLOPE_FALLING"
    """str: Falling slope for the analog trigger edge."""
    SLOPE_RISING = "dmm.SLOPE_RISING"
    """str: Rising slope for the analog trigger edge."""
    TERMINALS_FRONT = "dmm.TERMINALS_FRONT"
    """str: Instrument is using the front-panel input and output terminals."""
    TERMINALS_REAR = "dmm.TERMINALS_REAR"
    """str: Instrument is using the rear-panel input and output terminals."""
    THERMOCOUPLE_B = "dmm.THERMOCOUPLE_B"
    """str: B thermocouple type."""
    THERMOCOUPLE_E = "dmm.THERMOCOUPLE_E"
    """str: E thermocouple type."""
    THERMOCOUPLE_J = "dmm.THERMOCOUPLE_J"
    """str: J thermocouple type."""
    THERMOCOUPLE_K = "dmm.THERMOCOUPLE_K"
    """str: K thermocouple type."""
    THERMOCOUPLE_N = "dmm.THERMOCOUPLE_N"
    """str: N thermocouple type."""
    THERMOCOUPLE_R = "dmm.THERMOCOUPLE_R"
    """str: R thermocouple type."""
    THERMOCOUPLE_S = "dmm.THERMOCOUPLE_S"
    """str: S thermocouple type."""
    THERMOCOUPLE_T = "dmm.THERMOCOUPLE_T"
    """str: T thermocouple type."""
    THERM_10000 = "dmm.THERM_10000"
    """str: 10000 ohm thermistor."""
    THERM_2252 = "dmm.THERM_2252"
    """str: 2252 ohm thermistor."""
    THERM_5000 = "dmm.THERM_5000"
    """str: 5000 ohm thermistor."""
    TRANS_FOURRTD = "dmm.TRANS_FOURRTD"
    """str: Set the transducer type to  four-wire RTD."""
    TRANS_THERMISTOR = "dmm.TRANS_THERMISTOR"
    """str: Set the transducer type to thermistor."""
    TRANS_THERMOCOUPLE = "dmm.TRANS_THERMOCOUPLE"
    """str: Set the transducer type to thermocouple."""
    TRANS_THREERTD = "dmm.TRANS_THREERTD"
    """str: Set the transducer type to  three-wire RTD."""
    TRANS_TWORTD = "dmm.TRANS_TWORTD"
    """str: Set the transducer type to two-wire RTD."""
    UNIT_AMP = "dmm.UNIT_AMP"
    """str: Set unit of measure to amps (only available for current measurements)."""
    UNIT_CELSIUS = "dmm.UNIT_CELSIUS"
    """str: Display Celsius as units of measurement."""
    UNIT_DB = "dmm.UNIT_DB"
    """str: Display decibels as units for the measure voltage function."""
    UNIT_DBM = "dmm.UNIT_DBM"
    """str: Display decibel-millwatts as units for the  voltage function."""
    UNIT_FAHRENHEIT = "dmm.UNIT_FAHRENHEIT"
    """str: Display Fahrenheit as units of measurement."""
    UNIT_KELVIN = "dmm.UNIT_KELVIN"
    """str: Display Kelvin as units of measurement."""
    UNIT_VOLT = "dmm.UNIT_VOLT"
    """str: Display voltage as units for the voltage function."""

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "dmm") -> None:
        super().__init__(device, cmd_syntax)
        self._digitize = DmmDigitize(device, f"{self._cmd_syntax}.digitize")
        self._measure = DmmMeasure(device, f"{self._cmd_syntax}.measure")

    @property
    def digitize(self) -> DmmDigitize:
        """Return the ``dmm.digitize`` command tree.

        Sub-properties and sub-methods:
            - ``.analogtrigger``: The ``dmm.digitize.analogtrigger`` command tree.
            - ``.aperture``: The ``dmm.digitize.aperture`` attribute.
            - ``.count``: The ``dmm.digitize.count`` attribute.
            - ``.dbmreference``: The ``dmm.digitize.dbmreference`` attribute.
            - ``.dbreference``: The ``dmm.digitize.dbreference`` attribute.
            - ``.displaydigits``: The ``dmm.digitize.displaydigits`` attribute.
            - ``.func``: The ``dmm.digitize.func`` attribute.
            - ``.inputimpedance``: The ``dmm.digitize.inputimpedance`` attribute.
            - ``.limit``: The ``dmm.digitize.limit[Y]`` command tree.
            - ``.math``: The ``dmm.digitize.math`` command tree.
            - ``.range``: The ``dmm.digitize.range`` attribute.
            - ``.read()``: The ``dmm.digitize.read()`` function.
            - ``.readwithtime()``: The ``dmm.digitize.readwithtime()`` function.
            - ``.rel``: The ``dmm.digitize.rel`` command tree.
            - ``.samplerate``: The ``dmm.digitize.samplerate`` attribute.
            - ``.unit``: The ``dmm.digitize.unit`` attribute.
            - ``.userdelay``: The ``dmm.digitize.userdelay[N]`` attribute.
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
            - ``.configlist``: The ``dmm.measure.configlist`` command tree.
            - ``.count``: The ``dmm.measure.count`` attribute.
            - ``.dbmreference``: The ``dmm.measure.dbmreference`` attribute.
            - ``.dbreference``: The ``dmm.measure.dbreference`` attribute.
            - ``.detectorbandwidth``: The ``dmm.measure.detectorbandwidth`` attribute.
            - ``.displaydigits``: The ``dmm.measure.displaydigits`` attribute.
            - ``.filter``: The ``dmm.measure.filter`` command tree.
            - ``.fourrtd``: The ``dmm.measure.fourrtd`` attribute.
            - ``.func``: The ``dmm.measure.func`` attribute.
            - ``.getattribute()``: The ``dmm.measure.getattribute()`` function.
            - ``.inputimpedance``: The ``dmm.measure.inputimpedance`` attribute.
            - ``.limit``: The ``dmm.measure.limit[Y]`` command tree.
            - ``.linesync``: The ``dmm.measure.linesync`` attribute.
            - ``.math``: The ``dmm.measure.math`` command tree.
            - ``.nplc``: The ``dmm.measure.nplc`` attribute.
            - ``.offsetcompensation``: The ``dmm.measure.offsetcompensation`` command tree.
            - ``.opendetector``: The ``dmm.measure.opendetector`` attribute.
            - ``.range``: The ``dmm.measure.range`` attribute.
            - ``.read()``: The ``dmm.measure.read()`` function.
            - ``.readwithtime()``: The ``dmm.measure.readwithtime()`` function.
            - ``.refjunction``: The ``dmm.measure.refjunction`` attribute.
            - ``.rel``: The ``dmm.measure.rel`` command tree.
            - ``.rtdalpha``: The ``dmm.measure.rtdalpha`` attribute.
            - ``.rtdbeta``: The ``dmm.measure.rtdbeta`` attribute.
            - ``.rtddelta``: The ``dmm.measure.rtddelta`` attribute.
            - ``.rtdzero``: The ``dmm.measure.rtdzero`` attribute.
            - ``.sense``: The ``dmm.measure.sense`` command tree.
            - ``.setattribute()``: The ``dmm.measure.setattribute()`` function.
            - ``.simreftemperature``: The ``dmm.measure.simreftemperature`` attribute.
            - ``.thermistor``: The ``dmm.measure.thermistor`` attribute.
            - ``.thermocouple``: The ``dmm.measure.thermocouple`` attribute.
            - ``.threertd``: The ``dmm.measure.threertd`` attribute.
            - ``.threshold``: The ``dmm.measure.threshold`` command tree.
            - ``.transducer``: The ``dmm.measure.transducer`` attribute.
            - ``.twortd``: The ``dmm.measure.twortd`` attribute.
            - ``.unit``: The ``dmm.measure.unit`` attribute.
            - ``.userdelay``: The ``dmm.measure.userdelay[N]`` attribute.
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

    def reset(self) -> None:
        """Run the ``dmm.reset()`` function.

        Description:
            - This function resets commands that begin with dmm. to their default settings.

        TSP Syntax:
            ```
            - dmm.reset()
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
