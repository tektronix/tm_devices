# ruff: noqa: D402,PLR0913
# pyright: reportConstantRedefinition=none
"""The dmm commands module.

These commands are used in the following models:
SS3706A

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - dmm.adjustment.count
    - dmm.aperture
    - dmm.appendbuffer()
    - dmm.autorange
    - dmm.autozero
    - dmm.buffer.info()
    - dmm.buffer.maxcapacity
    - dmm.buffer.usedcapacity
    - dmm.calibration.ac()
    - dmm.calibration.dc()
    - dmm.calibration.lock()
    - dmm.calibration.password
    - dmm.calibration.save()
    - dmm.calibration.unlock()
    - dmm.close()
    - dmm.configure.delete()
    - dmm.configure.query()
    - dmm.configure.recall()
    - dmm.configure.set()
    - dmm.connect
    - dmm.dbreference
    - dmm.detectorbandwidth
    - dmm.displaydigits
    - dmm.drycircuit
    - dmm.filter.count
    - dmm.filter.enable
    - dmm.filter.type
    - dmm.filter.window
    - dmm.fourrtd
    - dmm.func
    - dmm.getconfig()
    - dmm.inputdivider
    - dmm.limit[Y].clear()
    - dmm.limit[r].autoclear
    - dmm.limit[r].enable
    - dmm.limit[r].high.fail
    - dmm.limit[r].high.value
    - dmm.linesync
    - dmm.makebuffer()
    - dmm.math.enable
    - dmm.math.format
    - dmm.math.mxb.bfactor
    - dmm.math.mxb.mfactor
    - dmm.math.mxb.units
    - dmm.math.percent
    - dmm.measure()
    - dmm.measurecount
    - dmm.measurewithptp()
    - dmm.measurewithtime()
    - dmm.nplc
    - dmm.offsetcompensation
    - dmm.open()
    - dmm.opendetector
    - dmm.range
    - dmm.refjunction
    - dmm.rel.acquire()
    - dmm.rel.enable
    - dmm.rel.level
    - dmm.reset()
    - dmm.rtdalpha
    - dmm.rtdbeta
    - dmm.rtddelta
    - dmm.rtdzero
    - dmm.savebuffer()
    - dmm.setconfig()
    - dmm.simreftemperature
    - dmm.thermocouple
    - dmm.threertd
    - dmm.threshold
    - dmm.transducer
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


class DmmRel(BaseTSPCmd):
    """The ``dmm.rel`` command tree.

    Properties and methods:
        - ``.acquire()``: The ``dmm.rel.acquire()`` function.
        - ``.enable``: The ``dmm.rel.enable`` attribute.
        - ``.level``: The ``dmm.rel.level`` attribute.
    """

    @property
    def enable(self) -> str:
        """Access the ``dmm.rel.enable`` attribute.

        Description:
            - Enables or disables relative measurement control for the function selected by
              dmm.func.

        Usage:
            - Accessing this property will send the ``print(dmm.rel.enable)`` query.
            - Setting this property to a value will send the ``dmm.rel.enable = value`` command.

        TSP Syntax:
            ```
            - dmm.rel.enable = value
            - print(dmm.rel.enable)
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
        """Access the ``dmm.rel.enable`` attribute.

        Description:
            - Enables or disables relative measurement control for the function selected by
              dmm.func.

        Usage:
            - Accessing this property will send the ``print(dmm.rel.enable)`` query.
            - Setting this property to a value will send the ``dmm.rel.enable = value`` command.

        TSP Syntax:
            ```
            - dmm.rel.enable = value
            - print(dmm.rel.enable)
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
        """Access the ``dmm.rel.level`` attribute.

        Description:
            - The offset value for relative measurements for the function selected by dmm.func.

        Usage:
            - Accessing this property will send the ``print(dmm.rel.level)`` query.
            - Setting this property to a value will send the ``dmm.rel.level = value`` command.

        TSP Syntax:
            ```
            - dmm.rel.level = value
            - print(dmm.rel.level)
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
        """Access the ``dmm.rel.level`` attribute.

        Description:
            - The offset value for relative measurements for the function selected by dmm.func.

        Usage:
            - Accessing this property will send the ``print(dmm.rel.level)`` query.
            - Setting this property to a value will send the ``dmm.rel.level = value`` command.

        TSP Syntax:
            ```
            - dmm.rel.level = value
            - print(dmm.rel.level)
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
        """Run the ``dmm.rel.acquire()`` function.

        Description:
            - This function acquires a measurement and stores it as the relative offset value.

        TSP Syntax:
            ```
            - dmm.rel.acquire()
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


class DmmMathMxb(BaseTSPCmd):
    """The ``dmm.math.mxb`` command tree.

    Properties and methods:
        - ``.bfactor``: The ``dmm.math.mxb.bfactor`` attribute.
        - ``.mfactor``: The ``dmm.math.mxb.mfactor`` attribute.
        - ``.units``: The ``dmm.math.mxb.units`` attribute.
    """

    @property
    def bfactor(self) -> str:
        """Access the ``dmm.math.mxb.bfactor`` attribute.

        Description:
            - This attribute specifies the offset, b, for the y = mx + b operation.

        Usage:
            - Accessing this property will send the ``print(dmm.math.mxb.bfactor)`` query.
            - Setting this property to a value will send the ``dmm.math.mxb.bfactor = value``
              command.

        TSP Syntax:
            ```
            - dmm.math.mxb.bfactor = value
            - print(dmm.math.mxb.bfactor)
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
        """Access the ``dmm.math.mxb.bfactor`` attribute.

        Description:
            - This attribute specifies the offset, b, for the y = mx + b operation.

        Usage:
            - Accessing this property will send the ``print(dmm.math.mxb.bfactor)`` query.
            - Setting this property to a value will send the ``dmm.math.mxb.bfactor = value``
              command.

        TSP Syntax:
            ```
            - dmm.math.mxb.bfactor = value
            - print(dmm.math.mxb.bfactor)
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
        """Access the ``dmm.math.mxb.mfactor`` attribute.

        Description:
            - This attribute specifies the scale factor, m, for the y = mx + b math operation.

        Usage:
            - Accessing this property will send the ``print(dmm.math.mxb.mfactor)`` query.
            - Setting this property to a value will send the ``dmm.math.mxb.mfactor = value``
              command.

        TSP Syntax:
            ```
            - dmm.math.mxb.mfactor = value
            - print(dmm.math.mxb.mfactor)
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
        """Access the ``dmm.math.mxb.mfactor`` attribute.

        Description:
            - This attribute specifies the scale factor, m, for the y = mx + b math operation.

        Usage:
            - Accessing this property will send the ``print(dmm.math.mxb.mfactor)`` query.
            - Setting this property to a value will send the ``dmm.math.mxb.mfactor = value``
              command.

        TSP Syntax:
            ```
            - dmm.math.mxb.mfactor = value
            - print(dmm.math.mxb.mfactor)
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

    @property
    def units(self) -> str:
        """Access the ``dmm.math.mxb.units`` attribute.

        Description:
            - This attribute specifies the unit character for the y = mX + b operation.

        Usage:
            - Accessing this property will send the ``print(dmm.math.mxb.units)`` query.
            - Setting this property to a value will send the ``dmm.math.mxb.units = value`` command.

        TSP Syntax:
            ```
            - dmm.math.mxb.units = value
            - print(dmm.math.mxb.units)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".units"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.units)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.units`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @units.setter
    def units(self, value: Union[str, float]) -> None:
        """Access the ``dmm.math.mxb.units`` attribute.

        Description:
            - This attribute specifies the unit character for the y = mX + b operation.

        Usage:
            - Accessing this property will send the ``print(dmm.math.mxb.units)`` query.
            - Setting this property to a value will send the ``dmm.math.mxb.units = value`` command.

        TSP Syntax:
            ```
            - dmm.math.mxb.units = value
            - print(dmm.math.mxb.units)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".units", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.units = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.units`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DmmMath(BaseTSPCmd):
    """The ``dmm.math`` command tree.

    Properties and methods:
        - ``.enable``: The ``dmm.math.enable`` attribute.
        - ``.format``: The ``dmm.math.format`` attribute.
        - ``.mxb``: The ``dmm.math.mxb`` command tree.
        - ``.percent``: The ``dmm.math.percent`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._mxb = DmmMathMxb(device, f"{self._cmd_syntax}.mxb")

    @property
    def enable(self) -> str:
        """Access the ``dmm.math.enable`` attribute.

        Description:
            - This attribute enables or disables math operations on measurements for the selected
              measurement function.

        Usage:
            - Accessing this property will send the ``print(dmm.math.enable)`` query.
            - Setting this property to a value will send the ``dmm.math.enable = value`` command.

        TSP Syntax:
            ```
            - dmm.math.enable = value
            - print(dmm.math.enable)
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
        """Access the ``dmm.math.enable`` attribute.

        Description:
            - This attribute enables or disables math operations on measurements for the selected
              measurement function.

        Usage:
            - Accessing this property will send the ``print(dmm.math.enable)`` query.
            - Setting this property to a value will send the ``dmm.math.enable = value`` command.

        TSP Syntax:
            ```
            - dmm.math.enable = value
            - print(dmm.math.enable)
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
        """Access the ``dmm.math.format`` attribute.

        Description:
            - This attribute specifies which math operation is performed on measurements when math
              operations are enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.math.format)`` query.
            - Setting this property to a value will send the ``dmm.math.format = value`` command.

        TSP Syntax:
            ```
            - dmm.math.format = value
            - print(dmm.math.format)
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
        """Access the ``dmm.math.format`` attribute.

        Description:
            - This attribute specifies which math operation is performed on measurements when math
              operations are enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.math.format)`` query.
            - Setting this property to a value will send the ``dmm.math.format = value`` command.

        TSP Syntax:
            ```
            - dmm.math.format = value
            - print(dmm.math.format)
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
    def mxb(self) -> DmmMathMxb:
        """Return the ``dmm.math.mxb`` command tree.

        Sub-properties and sub-methods:
            - ``.bfactor``: The ``dmm.math.mxb.bfactor`` attribute.
            - ``.mfactor``: The ``dmm.math.mxb.mfactor`` attribute.
            - ``.units``: The ``dmm.math.mxb.units`` attribute.
        """
        return self._mxb

    @property
    def percent(self) -> str:
        """Access the ``dmm.math.percent`` attribute.

        Description:
            - This attribute specifies the reference constant that is used when math operations are
              set to percent.

        Usage:
            - Accessing this property will send the ``print(dmm.math.percent)`` query.
            - Setting this property to a value will send the ``dmm.math.percent = value`` command.

        TSP Syntax:
            ```
            - dmm.math.percent = value
            - print(dmm.math.percent)
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
        """Access the ``dmm.math.percent`` attribute.

        Description:
            - This attribute specifies the reference constant that is used when math operations are
              set to percent.

        Usage:
            - Accessing this property will send the ``print(dmm.math.percent)`` query.
            - Setting this property to a value will send the ``dmm.math.percent = value`` command.

        TSP Syntax:
            ```
            - dmm.math.percent = value
            - print(dmm.math.percent)
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


class DmmLimitItemHigh(BaseTSPCmd):
    """The ``dmm.limit[r].high`` command tree.

    Properties and methods:
        - ``.fail``: The ``dmm.limit[r].high.fail`` attribute.
        - ``.value``: The ``dmm.limit[r].high.value`` attribute.
    """

    @property
    def fail(self) -> str:
        """Access the ``dmm.limit[r].high.fail`` attribute.

        Description:
            - This attribute queries for the high test results of limit Y. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(dmm.limit[r].high.fail)`` query.

        TSP Syntax:
            ```
            - print(dmm.limit[r].high.fail)
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
    def value(self) -> str:
        """Access the ``dmm.limit[r].high.value`` attribute.

        Description:
            - This attribute specifies the upper limit for a limit test. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(dmm.limit[r].high.value)`` query.
            - Setting this property to a value will send the ``dmm.limit[r].high.value = value``
              command.

        TSP Syntax:
            ```
            - dmm.limit[r].high.value = value
            - print(dmm.limit[r].high.value)
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
        """Access the ``dmm.limit[r].high.value`` attribute.

        Description:
            - This attribute specifies the upper limit for a limit test. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(dmm.limit[r].high.value)`` query.
            - Setting this property to a value will send the ``dmm.limit[r].high.value = value``
              command.

        TSP Syntax:
            ```
            - dmm.limit[r].high.value = value
            - print(dmm.limit[r].high.value)
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


class DmmLimitItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``dmm.limit[r]`` command tree.

    Properties and methods:
        - ``.autoclear``: The ``dmm.limit[r].autoclear`` attribute.
        - ``.clear()``: The ``dmm.limit[r].clear()`` function.
        - ``.enable``: The ``dmm.limit[r].enable`` attribute.
        - ``.high``: The ``dmm.limit[r].high`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._high = DmmLimitItemHigh(device, f"{self._cmd_syntax}.high")

    @property
    def autoclear(self) -> str:
        """Access the ``dmm.limit[r].autoclear`` attribute.

        Description:
            - This attribute indicates if the test result for limit Y should be cleared
              automatically or not. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(dmm.limit[r].autoclear)`` query.
            - Setting this property to a value will send the ``dmm.limit[r].autoclear = value``
              command.

        TSP Syntax:
            ```
            - dmm.limit[r].autoclear = value
            - print(dmm.limit[r].autoclear)
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
        """Access the ``dmm.limit[r].autoclear`` attribute.

        Description:
            - This attribute indicates if the test result for limit Y should be cleared
              automatically or not. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(dmm.limit[r].autoclear)`` query.
            - Setting this property to a value will send the ``dmm.limit[r].autoclear = value``
              command.

        TSP Syntax:
            ```
            - dmm.limit[r].autoclear = value
            - print(dmm.limit[r].autoclear)
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
        """Access the ``dmm.limit[r].enable`` attribute.

        Description:
            - This attribute enables or disables a limit test on the measurement from the selected
              measure function. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(dmm.limit[r].enable)`` query.
            - Setting this property to a value will send the ``dmm.limit[r].enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.limit[r].enable = value
            - print(dmm.limit[r].enable)
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
        """Access the ``dmm.limit[r].enable`` attribute.

        Description:
            - This attribute enables or disables a limit test on the measurement from the selected
              measure function. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(dmm.limit[r].enable)`` query.
            - Setting this property to a value will send the ``dmm.limit[r].enable = value``
              command.

        TSP Syntax:
            ```
            - dmm.limit[r].enable = value
            - print(dmm.limit[r].enable)
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
    def high(self) -> DmmLimitItemHigh:
        """Return the ``dmm.limit[r].high`` command tree.

        Sub-properties and sub-methods:
            - ``.fail``: The ``dmm.limit[r].high.fail`` attribute.
            - ``.value``: The ``dmm.limit[r].high.value`` attribute.
        """
        return self._high

    def clear(self) -> None:
        """Run the ``dmm.limit[r].clear()`` function.

        Description:
            - This function clears the results of the limit test defined by Y. (r = resistance in
              ohms)

        TSP Syntax:
            ```
            - dmm.limit[r].clear()
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


class DmmFilter(BaseTSPCmd):
    """The ``dmm.filter`` command tree.

    Properties and methods:
        - ``.count``: The ``dmm.filter.count`` attribute.
        - ``.enable``: The ``dmm.filter.enable`` attribute.
        - ``.type``: The ``dmm.filter.type`` attribute.
        - ``.window``: The ``dmm.filter.window`` attribute.
    """

    @property
    def count(self) -> str:
        """Access the ``dmm.filter.count`` attribute.

        Description:
            - This attribute sets the filter count setting for the selected DMM function.

        Usage:
            - Accessing this property will send the ``print(dmm.filter.count)`` query.
            - Setting this property to a value will send the ``dmm.filter.count = value`` command.

        TSP Syntax:
            ```
            - dmm.filter.count = value
            - print(dmm.filter.count)
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
        """Access the ``dmm.filter.count`` attribute.

        Description:
            - This attribute sets the filter count setting for the selected DMM function.

        Usage:
            - Accessing this property will send the ``print(dmm.filter.count)`` query.
            - Setting this property to a value will send the ``dmm.filter.count = value`` command.

        TSP Syntax:
            ```
            - dmm.filter.count = value
            - print(dmm.filter.count)
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
        """Access the ``dmm.filter.enable`` attribute.

        Description:
            - This attribute enables or disables the averaging filter for measurements of the
              selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.filter.enable)`` query.
            - Setting this property to a value will send the ``dmm.filter.enable = value`` command.

        TSP Syntax:
            ```
            - dmm.filter.enable = value
            - print(dmm.filter.enable)
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
        """Access the ``dmm.filter.enable`` attribute.

        Description:
            - This attribute enables or disables the averaging filter for measurements of the
              selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.filter.enable)`` query.
            - Setting this property to a value will send the ``dmm.filter.enable = value`` command.

        TSP Syntax:
            ```
            - dmm.filter.enable = value
            - print(dmm.filter.enable)
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
        """Access the ``dmm.filter.type`` attribute.

        Description:
            - This attribute defines the type of averaging filter that is used for the selected
              measure function when the measurement filter is enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.filter.type)`` query.
            - Setting this property to a value will send the ``dmm.filter.type = value`` command.

        TSP Syntax:
            ```
            - dmm.filter.type = value
            - print(dmm.filter.type)
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
        """Access the ``dmm.filter.type`` attribute.

        Description:
            - This attribute defines the type of averaging filter that is used for the selected
              measure function when the measurement filter is enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.filter.type)`` query.
            - Setting this property to a value will send the ``dmm.filter.type = value`` command.

        TSP Syntax:
            ```
            - dmm.filter.type = value
            - print(dmm.filter.type)
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
        """Access the ``dmm.filter.window`` attribute.

        Description:
            - This attribute sets the window for the averaging filter that is used for measurements
              for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.filter.window)`` query.
            - Setting this property to a value will send the ``dmm.filter.window = value`` command.

        TSP Syntax:
            ```
            - dmm.filter.window = value
            - print(dmm.filter.window)
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
        """Access the ``dmm.filter.window`` attribute.

        Description:
            - This attribute sets the window for the averaging filter that is used for measurements
              for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.filter.window)`` query.
            - Setting this property to a value will send the ``dmm.filter.window = value`` command.

        TSP Syntax:
            ```
            - dmm.filter.window = value
            - print(dmm.filter.window)
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


class DmmConfigure(BaseTSPCmd):
    """The ``dmm.configure`` command tree.

    Properties and methods:
        - ``.delete()``: The ``dmm.configure.delete()`` function.
        - ``.query()``: The ``dmm.configure.query()`` function.
        - ``.recall()``: The ``dmm.configure.recall()`` function.
        - ``.set()``: The ``dmm.configure.set()`` function.
    """

    def delete(self, name: str) -> None:
        """Run the ``dmm.configure.delete()`` function.

        Description:
            - This function deletes a user-created DMM configuration from memory.

        TSP Syntax:
            ```
            - dmm.configure.delete()
            ```

        Args:
            name: String that contains the name of the DMM configuration to delete.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.delete("{name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.delete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def query(self, user_configuration: str, user_separator: Optional[str] = None) -> str:
        """Run the ``dmm.configure.query()`` function.

        Description:
            - This function lists DMM settings associated with a configuration.

        TSP Syntax:
            ```
            - dmm.configure.query()
            ```

        Args:
            user_configuration: A string that contains the name for the DMM configuration to be
                listed; to query the settings for the active function, set this parameter to
                'active'.
            user_separator (optional): A string that represents the two-character separator that is
                inserted between items; the default value is a comma followed by a space (, ).

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{user_configuration}"',
                    f'"{user_separator}"' if user_separator is not None else None,
                )
                if x is not None
            )
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.query({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.query()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def recall(self, configuration: str) -> None:
        """Run the ``dmm.configure.recall()`` function.

        Description:
            - This function recalls a user or factory DMM configuration and replaces attributes in
              the present configuration with attributes from the recalled version.

        TSP Syntax:
            ```
            - dmm.configure.recall()
            ```

        Args:
            configuration: A string that represents the name of the DMM configuration to recall.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.recall("{configuration}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.recall()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def set_(self, name: str) -> None:
        """Run the ``dmm.configure.set()`` function.

        Description:
            - This function creates a named DMM configuration for the selected function. The
              configuration includes pertinent attributes for that function.

        TSP Syntax:
            ```
            - dmm.configure.set()
            ```

        Args:
            name: A string that contains the name of the DMM configuration that you are creating.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.set("{name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.set()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DmmCalibration(BaseTSPCmd):
    """The ``dmm.calibration`` command tree.

    Properties and methods:
        - ``.ac()``: The ``dmm.calibration.ac()`` function.
        - ``.dc()``: The ``dmm.calibration.dc()`` function.
        - ``.lock()``: The ``dmm.calibration.lock()`` function.
        - ``.password``: The ``dmm.calibration.password`` attribute.
        - ``.save()``: The ``dmm.calibration.save()`` function.
        - ``.unlock()``: The ``dmm.calibration.unlock()`` function.
    """

    @property
    def password(self) -> str:
        """Access the ``dmm.calibration.password`` attribute.

        Description:
            - This attribute sets the password that must be entered before you can unlock
              calibration.

        Usage:
            - Setting this property to a value will send the ``dmm.calibration.password = value``
              command.

        TSP Syntax:
            ```
            - dmm.calibration.password = value
            ```

        Raises:
            AttributeError: Indicates that this attribute is write-only.
        """
        if self._device.command_syntax_enabled:  # type: ignore[union-attr]
            return self._cmd_syntax + ".password"
        msg = f"``{self._cmd_syntax}.password`` is a write-only attribute."
        raise AttributeError(msg)

    @password.setter
    def password(self, value: Union[str, float]) -> None:
        """Access the ``dmm.calibration.password`` attribute.

        Description:
            - This attribute sets the password that must be entered before you can unlock
              calibration.

        Usage:
            - Setting this property to a value will send the ``dmm.calibration.password = value``
              command.

        TSP Syntax:
            ```
            - dmm.calibration.password = value
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.password = {value}"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.password`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def ac(self, step: str, value: Optional[str] = None) -> None:
        """Run the ``dmm.calibration.ac()`` function.

        Description:
            - This function begins the specified AC adjustment step on the DMM.

        TSP Syntax:
            ```
            - dmm.calibration.ac()
            ```

        Args:
            step: The AC adjustment step to perform.
            value (optional): The value for this adjustment step (if the adjustment step has a
                value).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    step,
                    value,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.ac({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.ac()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def dc(self, step: str, value: Optional[str] = None) -> None:
        """Run the ``dmm.calibration.dc()`` function.

        Description:
            - This function begins a DC adjustment step on the DMM.

        TSP Syntax:
            ```
            - dmm.calibration.dc()
            ```

        Args:
            step: The DC adjustment step to perform.
            value (optional): The value for this adjustment step (if the adjustment step has a
                value).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    step,
                    value,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.dc({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.dc()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def lock(self) -> None:
        """Run the ``dmm.calibration.lock()`` function.

        Description:
            - This function locks calibration to prevent unintended changes.

        TSP Syntax:
            ```
            - dmm.calibration.lock()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.lock()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.lock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def save(self) -> None:
        """Run the ``dmm.calibration.save()`` function.

        Description:
            - This function saves calibration data.

        TSP Syntax:
            ```
            - dmm.calibration.save()
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.save()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.save()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def unlock(self, password: str) -> None:
        """Run the ``dmm.calibration.unlock()`` function.

        Description:
            - This function unlocks calibration if calibration was locked.

        TSP Syntax:
            ```
            - dmm.calibration.unlock()
            ```

        Args:
            password: A string representing the password to unlock calibration.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.unlock("{password}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.unlock()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DmmBuffer(BaseTSPCmd):
    """The ``dmm.buffer`` command tree.

    Properties and methods:
        - ``.info()``: The ``dmm.buffer.info()`` function.
        - ``.maxcapacity``: The ``dmm.buffer.maxcapacity`` attribute.
        - ``.usedcapacity``: The ``dmm.buffer.usedcapacity`` attribute.
    """

    @property
    def maxcapacity(self) -> str:
        """Access the ``dmm.buffer.maxcapacity`` attribute.

        Description:
            - This attribute returns the overall maximum capacity for reading buffers in the
              instrument.

        Usage:
            - Accessing this property will send the ``print(dmm.buffer.maxcapacity)`` query.

        TSP Syntax:
            ```
            - print(dmm.buffer.maxcapacity)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".maxcapacity"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.maxcapacity)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.maxcapacity`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def usedcapacity(self) -> str:
        """Access the ``dmm.buffer.usedcapacity`` attribute.

        Description:
            - This attribute indicates how much of the maximum capacity for reading buffers in the
              instrument is used.

        Usage:
            - Accessing this property will send the ``print(dmm.buffer.usedcapacity)`` query.

        TSP Syntax:
            ```
            - print(dmm.buffer.usedcapacity)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".usedcapacity"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.usedcapacity)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.usedcapacity`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def info(self, buffer_var: str) -> str:
        """Run the ``dmm.buffer.info()`` function.

        Description:
            - This function returns the size and capacity of the reading buffer parameter.

        TSP Syntax:
            ```
            - dmm.buffer.info()
            ```

        Args:
            buffer_var: String representing the reading buffer name that you want to query for size
                and capacity.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.info({buffer_var}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.info()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class DmmAdjustment(BaseTSPCmd):
    """The ``dmm.adjustment`` command tree.

    Properties and methods:
        - ``.count``: The ``dmm.adjustment.count`` attribute.
    """

    @property
    def count(self) -> str:
        """Access the ``dmm.adjustment.count`` attribute.

        Description:
            - This attribute indicates the number of times the instrument has been adjusted
              (calibrated).

        Usage:
            - Accessing this property will send the ``print(dmm.adjustment.count)`` query.

        TSP Syntax:
            ```
            - print(dmm.adjustment.count)
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


#  pylint: disable=too-many-instance-attributes,too-many-public-methods
class Dmm(BaseTSPCmd):
    """The ``dmm`` command tree.

    Properties and methods:
        - ``.adjustment``: The ``dmm.adjustment`` command tree.
        - ``.aperture``: The ``dmm.aperture`` attribute.
        - ``.appendbuffer()``: The ``dmm.appendbuffer()`` function.
        - ``.autorange``: The ``dmm.autorange`` attribute.
        - ``.autozero``: The ``dmm.autozero`` attribute.
        - ``.buffer``: The ``dmm.buffer`` command tree.
        - ``.calibration``: The ``dmm.calibration`` command tree.
        - ``.close()``: The ``dmm.close()`` function.
        - ``.configure``: The ``dmm.configure`` command tree.
        - ``.connect``: The ``dmm.connect`` attribute.
        - ``.dbreference``: The ``dmm.dbreference`` attribute.
        - ``.detectorbandwidth``: The ``dmm.detectorbandwidth`` attribute.
        - ``.displaydigits``: The ``dmm.displaydigits`` attribute.
        - ``.drycircuit``: The ``dmm.drycircuit`` attribute.
        - ``.filter``: The ``dmm.filter`` command tree.
        - ``.fourrtd``: The ``dmm.fourrtd`` attribute.
        - ``.func``: The ``dmm.func`` attribute.
        - ``.getconfig()``: The ``dmm.getconfig()`` function.
        - ``.inputdivider``: The ``dmm.inputdivider`` attribute.
        - ``.limit``: The ``dmm.limit[r]`` command tree.
        - ``.linesync``: The ``dmm.linesync`` attribute.
        - ``.makebuffer()``: The ``dmm.makebuffer()`` function.
        - ``.math``: The ``dmm.math`` command tree.
        - ``.measure()``: The ``dmm.measure()`` function.
        - ``.measurecount``: The ``dmm.measurecount`` attribute.
        - ``.measurewithptp()``: The ``dmm.measurewithptp()`` function.
        - ``.measurewithtime()``: The ``dmm.measurewithtime()`` function.
        - ``.nplc``: The ``dmm.nplc`` attribute.
        - ``.offsetcompensation``: The ``dmm.offsetcompensation`` attribute.
        - ``.open()``: The ``dmm.open()`` function.
        - ``.opendetector``: The ``dmm.opendetector`` attribute.
        - ``.range``: The ``dmm.range`` attribute.
        - ``.refjunction``: The ``dmm.refjunction`` attribute.
        - ``.rel``: The ``dmm.rel`` command tree.
        - ``.reset()``: The ``dmm.reset()`` function.
        - ``.rtdalpha``: The ``dmm.rtdalpha`` attribute.
        - ``.rtdbeta``: The ``dmm.rtdbeta`` attribute.
        - ``.rtddelta``: The ``dmm.rtddelta`` attribute.
        - ``.rtdzero``: The ``dmm.rtdzero`` attribute.
        - ``.savebuffer()``: The ``dmm.savebuffer()`` function.
        - ``.setconfig()``: The ``dmm.setconfig()`` function.
        - ``.simreftemperature``: The ``dmm.simreftemperature`` attribute.
        - ``.thermocouple``: The ``dmm.thermocouple`` attribute.
        - ``.threertd``: The ``dmm.threertd`` attribute.
        - ``.threshold``: The ``dmm.threshold`` attribute.
        - ``.transducer``: The ``dmm.transducer`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "dmm") -> None:
        super().__init__(device, cmd_syntax)
        self._adjustment = DmmAdjustment(device, f"{self._cmd_syntax}.adjustment")
        self._buffer = DmmBuffer(device, f"{self._cmd_syntax}.buffer")
        self._calibration = DmmCalibration(device, f"{self._cmd_syntax}.calibration")
        self._configure = DmmConfigure(device, f"{self._cmd_syntax}.configure")
        self._filter = DmmFilter(device, f"{self._cmd_syntax}.filter")
        self._limit: Dict[int, DmmLimitItem] = DefaultDictPassKeyToFactory(
            lambda x: DmmLimitItem(device, f"{self._cmd_syntax}.limit[{x}]")
        )
        self._math = DmmMath(device, f"{self._cmd_syntax}.math")
        self._rel = DmmRel(device, f"{self._cmd_syntax}.rel")

    @property
    def adjustment(self) -> DmmAdjustment:
        """Return the ``dmm.adjustment`` command tree.

        Sub-properties and sub-methods:
            - ``.count``: The ``dmm.adjustment.count`` attribute.
        """
        return self._adjustment

    @property
    def aperture(self) -> str:
        """Access the ``dmm.aperture`` attribute.

        Description:
            - This attribute determines the aperture setting for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.aperture)`` query.
            - Setting this property to a value will send the ``dmm.aperture = value`` command.

        TSP Syntax:
            ```
            - dmm.aperture = value
            - print(dmm.aperture)
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
        """Access the ``dmm.aperture`` attribute.

        Description:
            - This attribute determines the aperture setting for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.aperture)`` query.
            - Setting this property to a value will send the ``dmm.aperture = value`` command.

        TSP Syntax:
            ```
            - dmm.aperture = value
            - print(dmm.aperture)
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
    def autorange(self) -> str:
        """Access the ``dmm.autorange`` attribute.

        Description:
            - This attribute specifies the autorange setting for the active function

        Usage:
            - Accessing this property will send the ``print(dmm.autorange)`` query.
            - Setting this property to a value will send the ``dmm.autorange = value`` command.

        TSP Syntax:
            ```
            - dmm.autorange = value
            - print(dmm.autorange)
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
        """Access the ``dmm.autorange`` attribute.

        Description:
            - This attribute specifies the autorange setting for the active function

        Usage:
            - Accessing this property will send the ``print(dmm.autorange)`` query.
            - Setting this property to a value will send the ``dmm.autorange = value`` command.

        TSP Syntax:
            ```
            - dmm.autorange = value
            - print(dmm.autorange)
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
    def autozero(self) -> str:
        """Access the ``dmm.autozero`` attribute.

        Description:
            - This attribute enables or disables automatic updates to the internal reference
              measurements (autozero) of the instrument

        Usage:
            - Accessing this property will send the ``print(dmm.autozero)`` query.
            - Setting this property to a value will send the ``dmm.autozero = value`` command.

        TSP Syntax:
            ```
            - dmm.autozero = value
            - print(dmm.autozero)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".autozero"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.autozero)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autozero`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @autozero.setter
    def autozero(self, value: Union[str, float]) -> None:
        """Access the ``dmm.autozero`` attribute.

        Description:
            - This attribute enables or disables automatic updates to the internal reference
              measurements (autozero) of the instrument

        Usage:
            - Accessing this property will send the ``print(dmm.autozero)`` query.
            - Setting this property to a value will send the ``dmm.autozero = value`` command.

        TSP Syntax:
            ```
            - dmm.autozero = value
            - print(dmm.autozero)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".autozero", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.autozero = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.autozero`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def buffer(self) -> DmmBuffer:
        """Return the ``dmm.buffer`` command tree.

        Sub-properties and sub-methods:
            - ``.info()``: The ``dmm.buffer.info()`` function.
            - ``.maxcapacity``: The ``dmm.buffer.maxcapacity`` attribute.
            - ``.usedcapacity``: The ``dmm.buffer.usedcapacity`` attribute.
        """
        return self._buffer

    @property
    def calibration(self) -> DmmCalibration:
        """Return the ``dmm.calibration`` command tree.

        Sub-properties and sub-methods:
            - ``.ac()``: The ``dmm.calibration.ac()`` function.
            - ``.dc()``: The ``dmm.calibration.dc()`` function.
            - ``.lock()``: The ``dmm.calibration.lock()`` function.
            - ``.password``: The ``dmm.calibration.password`` attribute.
            - ``.save()``: The ``dmm.calibration.save()`` function.
            - ``.unlock()``: The ``dmm.calibration.unlock()`` function.
        """
        return self._calibration

    @property
    def configure(self) -> DmmConfigure:
        """Return the ``dmm.configure`` command tree.

        Sub-properties and sub-methods:
            - ``.delete()``: The ``dmm.configure.delete()`` function.
            - ``.query()``: The ``dmm.configure.query()`` function.
            - ``.recall()``: The ``dmm.configure.recall()`` function.
            - ``.set()``: The ``dmm.configure.set()`` function.
        """
        return self._configure

    @property
    def connect(self) -> str:
        """Access the ``dmm.connect`` attribute.

        Description:
            - This attribute indicates how the DMM relays should be connected to the analog
              backplane.

        Usage:
            - Accessing this property will send the ``print(dmm.connect)`` query.
            - Setting this property to a value will send the ``dmm.connect = value`` command.

        TSP Syntax:
            ```
            - dmm.connect = value
            - print(dmm.connect)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".connect"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.connect)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.connect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @connect.setter
    def connect(self, value: Union[str, float]) -> None:
        """Access the ``dmm.connect`` attribute.

        Description:
            - This attribute indicates how the DMM relays should be connected to the analog
              backplane.

        Usage:
            - Accessing this property will send the ``print(dmm.connect)`` query.
            - Setting this property to a value will send the ``dmm.connect = value`` command.

        TSP Syntax:
            ```
            - dmm.connect = value
            - print(dmm.connect)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".connect", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.connect = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.connect`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def dbreference(self) -> str:
        """Access the ``dmm.dbreference`` attribute.

        Description:
            - This attribute defines the decibel (dB) reference setting for the DMM in volts.

        Usage:
            - Accessing this property will send the ``print(dmm.dbreference)`` query.
            - Setting this property to a value will send the ``dmm.dbreference = value`` command.

        TSP Syntax:
            ```
            - dmm.dbreference = value
            - print(dmm.dbreference)
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
        """Access the ``dmm.dbreference`` attribute.

        Description:
            - This attribute defines the decibel (dB) reference setting for the DMM in volts.

        Usage:
            - Accessing this property will send the ``print(dmm.dbreference)`` query.
            - Setting this property to a value will send the ``dmm.dbreference = value`` command.

        TSP Syntax:
            ```
            - dmm.dbreference = value
            - print(dmm.dbreference)
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
        """Access the ``dmm.detectorbandwidth`` attribute.

        Description:
            - This attribute sets the AC detector bandwidth setting for the DMM in Hertz.

        Usage:
            - Accessing this property will send the ``print(dmm.detectorbandwidth)`` query.
            - Setting this property to a value will send the ``dmm.detectorbandwidth = value``
              command.

        TSP Syntax:
            ```
            - dmm.detectorbandwidth = value
            - print(dmm.detectorbandwidth)
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
        """Access the ``dmm.detectorbandwidth`` attribute.

        Description:
            - This attribute sets the AC detector bandwidth setting for the DMM in Hertz.

        Usage:
            - Accessing this property will send the ``print(dmm.detectorbandwidth)`` query.
            - Setting this property to a value will send the ``dmm.detectorbandwidth = value``
              command.

        TSP Syntax:
            ```
            - dmm.detectorbandwidth = value
            - print(dmm.detectorbandwidth)
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
        """Access the ``dmm.displaydigits`` attribute.

        Description:
            - This attribute determines the number of digits that are displayed for measurements on
              the front panel.

        Usage:
            - Accessing this property will send the ``print(dmm.displaydigits)`` query.
            - Setting this property to a value will send the ``dmm.displaydigits = value`` command.

        TSP Syntax:
            ```
            - dmm.displaydigits = value
            - print(dmm.displaydigits)
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
        """Access the ``dmm.displaydigits`` attribute.

        Description:
            - This attribute determines the number of digits that are displayed for measurements on
              the front panel.

        Usage:
            - Accessing this property will send the ``print(dmm.displaydigits)`` query.
            - Setting this property to a value will send the ``dmm.displaydigits = value`` command.

        TSP Syntax:
            ```
            - dmm.displaydigits = value
            - print(dmm.displaydigits)
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
    def drycircuit(self) -> str:
        """Access the ``dmm.drycircuit`` attribute.

        Description:
            - This attribute enables or disables the dry circuit feature of the 4-wire resistance
              measure function.

        Usage:
            - Accessing this property will send the ``print(dmm.drycircuit)`` query.
            - Setting this property to a value will send the ``dmm.drycircuit = value`` command.

        TSP Syntax:
            ```
            - dmm.drycircuit = value
            - print(dmm.drycircuit)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".drycircuit"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.drycircuit)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.drycircuit`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @drycircuit.setter
    def drycircuit(self, value: Union[str, float]) -> None:
        """Access the ``dmm.drycircuit`` attribute.

        Description:
            - This attribute enables or disables the dry circuit feature of the 4-wire resistance
              measure function.

        Usage:
            - Accessing this property will send the ``print(dmm.drycircuit)`` query.
            - Setting this property to a value will send the ``dmm.drycircuit = value`` command.

        TSP Syntax:
            ```
            - dmm.drycircuit = value
            - print(dmm.drycircuit)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".drycircuit", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.drycircuit = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.drycircuit`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def filter(self) -> DmmFilter:
        """Return the ``dmm.filter`` command tree.

        Sub-properties and sub-methods:
            - ``.count``: The ``dmm.filter.count`` attribute.
            - ``.enable``: The ``dmm.filter.enable`` attribute.
            - ``.type``: The ``dmm.filter.type`` attribute.
            - ``.window``: The ``dmm.filter.window`` attribute.
        """
        return self._filter

    @property
    def fourrtd(self) -> str:
        """Access the ``dmm.fourrtd`` attribute.

        Description:
            - This attribute sets the type of 4-wire RTD that is being used.

        Usage:
            - Accessing this property will send the ``print(dmm.fourrtd)`` query.
            - Setting this property to a value will send the ``dmm.fourrtd = value`` command.

        TSP Syntax:
            ```
            - dmm.fourrtd = value
            - print(dmm.fourrtd)
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
        """Access the ``dmm.fourrtd`` attribute.

        Description:
            - This attribute sets the type of 4-wire RTD that is being used.

        Usage:
            - Accessing this property will send the ``print(dmm.fourrtd)`` query.
            - Setting this property to a value will send the ``dmm.fourrtd = value`` command.

        TSP Syntax:
            ```
            - dmm.fourrtd = value
            - print(dmm.fourrtd)
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
        """Access the ``dmm.func`` attribute.

        Description:
            - This attribute selects the active measure function.

        Usage:
            - Accessing this property will send the ``print(dmm.func)`` query.
            - Setting this property to a value will send the ``dmm.func = value`` command.

        TSP Syntax:
            ```
            - dmm.func = value
            - print(dmm.func)
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
        """Access the ``dmm.func`` attribute.

        Description:
            - This attribute selects the active measure function.

        Usage:
            - Accessing this property will send the ``print(dmm.func)`` query.
            - Setting this property to a value will send the ``dmm.func = value`` command.

        TSP Syntax:
            ```
            - dmm.func = value
            - print(dmm.func)
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
    def inputdivider(self) -> str:
        """Access the ``dmm.inputdivider`` attribute.

        Description:
            - This attribute determines when the 10 MΩ input divider is enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.inputdivider)`` query.
            - Setting this property to a value will send the ``dmm.inputdivider = value`` command.

        TSP Syntax:
            ```
            - dmm.inputdivider = value
            - print(dmm.inputdivider)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".inputdivider"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.inputdivider)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.inputdivider`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @inputdivider.setter
    def inputdivider(self, value: Union[str, float]) -> None:
        """Access the ``dmm.inputdivider`` attribute.

        Description:
            - This attribute determines when the 10 MΩ input divider is enabled.

        Usage:
            - Accessing this property will send the ``print(dmm.inputdivider)`` query.
            - Setting this property to a value will send the ``dmm.inputdivider = value`` command.

        TSP Syntax:
            ```
            - dmm.inputdivider = value
            - print(dmm.inputdivider)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".inputdivider", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.inputdivider = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.inputdivider`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limit(self) -> Dict[int, DmmLimitItem]:
        """Return the ``dmm.limit[r]`` command tree.

        Sub-properties and sub-methods:
            - ``.autoclear``: The ``dmm.limit[r].autoclear`` attribute.
            - ``.clear()``: The ``dmm.limit[r].clear()`` function.
            - ``.enable``: The ``dmm.limit[r].enable`` attribute.
            - ``.high``: The ``dmm.limit[r].high`` command tree.
        """
        return self._limit

    @property
    def linesync(self) -> str:
        """Access the ``dmm.linesync`` attribute.

        Description:
            - This attribute determines if line synchronization is used during the measurement.

        Usage:
            - Accessing this property will send the ``print(dmm.linesync)`` query.
            - Setting this property to a value will send the ``dmm.linesync = value`` command.

        TSP Syntax:
            ```
            - dmm.linesync = value
            - print(dmm.linesync)
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
        """Access the ``dmm.linesync`` attribute.

        Description:
            - This attribute determines if line synchronization is used during the measurement.

        Usage:
            - Accessing this property will send the ``print(dmm.linesync)`` query.
            - Setting this property to a value will send the ``dmm.linesync = value`` command.

        TSP Syntax:
            ```
            - dmm.linesync = value
            - print(dmm.linesync)
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
    def math(self) -> DmmMath:
        """Return the ``dmm.math`` command tree.

        Sub-properties and sub-methods:
            - ``.enable``: The ``dmm.math.enable`` attribute.
            - ``.format``: The ``dmm.math.format`` attribute.
            - ``.mxb``: The ``dmm.math.mxb`` command tree.
            - ``.percent``: The ``dmm.math.percent`` attribute.
        """
        return self._math

    @property
    def measurecount(self) -> str:
        """Access the ``dmm.measurecount`` attribute.

        Description:
            - This attribute sets the number of measurements to take when a measurement is requested
              by a DMM measure command.

        Usage:
            - Accessing this property will send the ``print(dmm.measurecount)`` query.
            - Setting this property to a value will send the ``dmm.measurecount = value`` command.

        TSP Syntax:
            ```
            - dmm.measurecount = value
            - print(dmm.measurecount)
            ```

        Info:
            - ``count``, the number of measurements to take when a DMM measure function is used
              (maximum 450,000).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".measurecount"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.measurecount)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.measurecount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @measurecount.setter
    def measurecount(self, value: Union[str, float]) -> None:
        """Access the ``dmm.measurecount`` attribute.

        Description:
            - This attribute sets the number of measurements to take when a measurement is requested
              by a DMM measure command.

        Usage:
            - Accessing this property will send the ``print(dmm.measurecount)`` query.
            - Setting this property to a value will send the ``dmm.measurecount = value`` command.

        TSP Syntax:
            ```
            - dmm.measurecount = value
            - print(dmm.measurecount)
            ```

        Info:
            - ``count``, the number of measurements to take when a DMM measure function is used
              (maximum 450,000).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".measurecount", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.measurecount = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.measurecount`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def nplc(self) -> str:
        """Access the ``dmm.nplc`` attribute.

        Description:
            - This attribute sets the integration rate in line cycles for the DMM for the function
              selected by dmm.func.

        Usage:
            - Accessing this property will send the ``print(dmm.nplc)`` query.
            - Setting this property to a value will send the ``dmm.nplc = value`` command.

        TSP Syntax:
            ```
            - dmm.nplc = value
            - print(dmm.nplc)
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
        """Access the ``dmm.nplc`` attribute.

        Description:
            - This attribute sets the integration rate in line cycles for the DMM for the function
              selected by dmm.func.

        Usage:
            - Accessing this property will send the ``print(dmm.nplc)`` query.
            - Setting this property to a value will send the ``dmm.nplc = value`` command.

        TSP Syntax:
            ```
            - dmm.nplc = value
            - print(dmm.nplc)
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
        """Access the ``dmm.offsetcompensation`` attribute.

        Description:
            - This attribute specifies the offset compensation setting for the DMM for the function
              selected by dmm.func.

        Usage:
            - Accessing this property will send the ``print(dmm.offsetcompensation)`` query.
            - Setting this property to a value will send the ``dmm.offsetcompensation = value``
              command.

        TSP Syntax:
            ```
            - dmm.offsetcompensation = value
            - print(dmm.offsetcompensation)
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
        """Access the ``dmm.offsetcompensation`` attribute.

        Description:
            - This attribute specifies the offset compensation setting for the DMM for the function
              selected by dmm.func.

        Usage:
            - Accessing this property will send the ``print(dmm.offsetcompensation)`` query.
            - Setting this property to a value will send the ``dmm.offsetcompensation = value``
              command.

        TSP Syntax:
            ```
            - dmm.offsetcompensation = value
            - print(dmm.offsetcompensation)
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
    def opendetector(self) -> str:
        """Access the ``dmm.opendetector`` attribute.

        Description:
            - This attributes determines if the detection of open leads is enabled or disabled.

        Usage:
            - Accessing this property will send the ``print(dmm.opendetector)`` query.
            - Setting this property to a value will send the ``dmm.opendetector = value`` command.

        TSP Syntax:
            ```
            - dmm.opendetector = value
            - print(dmm.opendetector)
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
        """Access the ``dmm.opendetector`` attribute.

        Description:
            - This attributes determines if the detection of open leads is enabled or disabled.

        Usage:
            - Accessing this property will send the ``print(dmm.opendetector)`` query.
            - Setting this property to a value will send the ``dmm.opendetector = value`` command.

        TSP Syntax:
            ```
            - dmm.opendetector = value
            - print(dmm.opendetector)
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
        """Access the ``dmm.range`` attribute.

        Description:
            - Indicates the range of DMM for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.range)`` query.
            - Setting this property to a value will send the ``dmm.range = value`` command.

        TSP Syntax:
            ```
            - dmm.range = value
            - print(dmm.range)
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
        """Access the ``dmm.range`` attribute.

        Description:
            - Indicates the range of DMM for the selected function.

        Usage:
            - Accessing this property will send the ``print(dmm.range)`` query.
            - Setting this property to a value will send the ``dmm.range = value`` command.

        TSP Syntax:
            ```
            - dmm.range = value
            - print(dmm.range)
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
        """Access the ``dmm.refjunction`` attribute.

        Description:
            - This attribute defines the type of the thermocouple reference junction.

        Usage:
            - Accessing this property will send the ``print(dmm.refjunction)`` query.
            - Setting this property to a value will send the ``dmm.refjunction = value`` command.

        TSP Syntax:
            ```
            - dmm.refjunction = value
            - print(dmm.refjunction)
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
        """Access the ``dmm.refjunction`` attribute.

        Description:
            - This attribute defines the type of the thermocouple reference junction.

        Usage:
            - Accessing this property will send the ``print(dmm.refjunction)`` query.
            - Setting this property to a value will send the ``dmm.refjunction = value`` command.

        TSP Syntax:
            ```
            - dmm.refjunction = value
            - print(dmm.refjunction)
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
    def rel(self) -> DmmRel:
        """Return the ``dmm.rel`` command tree.

        Sub-properties and sub-methods:
            - ``.acquire()``: The ``dmm.rel.acquire()`` function.
            - ``.enable``: The ``dmm.rel.enable`` attribute.
            - ``.level``: The ``dmm.rel.level`` attribute.
        """
        return self._rel

    @property
    def rtdalpha(self) -> str:
        """Access the ``dmm.rtdalpha`` attribute.

        Description:
            - This attribute contains the alpha value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.rtdalpha)`` query.
            - Setting this property to a value will send the ``dmm.rtdalpha = value`` command.

        TSP Syntax:
            ```
            - dmm.rtdalpha = value
            - print(dmm.rtdalpha)
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
        """Access the ``dmm.rtdalpha`` attribute.

        Description:
            - This attribute contains the alpha value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.rtdalpha)`` query.
            - Setting this property to a value will send the ``dmm.rtdalpha = value`` command.

        TSP Syntax:
            ```
            - dmm.rtdalpha = value
            - print(dmm.rtdalpha)
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
        """Access the ``dmm.rtdbeta`` attribute.

        Description:
            - This attribute contains the beta value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.rtdbeta)`` query.
            - Setting this property to a value will send the ``dmm.rtdbeta = value`` command.

        TSP Syntax:
            ```
            - dmm.rtdbeta = value
            - print(dmm.rtdbeta)
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
        """Access the ``dmm.rtdbeta`` attribute.

        Description:
            - This attribute contains the beta value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.rtdbeta)`` query.
            - Setting this property to a value will send the ``dmm.rtdbeta = value`` command.

        TSP Syntax:
            ```
            - dmm.rtdbeta = value
            - print(dmm.rtdbeta)
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
        """Access the ``dmm.rtddelta`` attribute.

        Description:
            - This attribute contains the delta value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.rtddelta)`` query.
            - Setting this property to a value will send the ``dmm.rtddelta = value`` command.

        TSP Syntax:
            ```
            - dmm.rtddelta = value
            - print(dmm.rtddelta)
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
        """Access the ``dmm.rtddelta`` attribute.

        Description:
            - This attribute contains the delta value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.rtddelta)`` query.
            - Setting this property to a value will send the ``dmm.rtddelta = value`` command.

        TSP Syntax:
            ```
            - dmm.rtddelta = value
            - print(dmm.rtddelta)
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
        """Access the ``dmm.rtdzero`` attribute.

        Description:
            - This attribute contains the zero value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.rtdzero)`` query.
            - Setting this property to a value will send the ``dmm.rtdzero = value`` command.

        TSP Syntax:
            ```
            - dmm.rtdzero = value
            - print(dmm.rtdzero)
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
        """Access the ``dmm.rtdzero`` attribute.

        Description:
            - This attribute contains the zero value of a user-defined RTD.

        Usage:
            - Accessing this property will send the ``print(dmm.rtdzero)`` query.
            - Setting this property to a value will send the ``dmm.rtdzero = value`` command.

        TSP Syntax:
            ```
            - dmm.rtdzero = value
            - print(dmm.rtdzero)
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
    def simreftemperature(self) -> str:
        """Access the ``dmm.simreftemperature`` attribute.

        Description:
            - This attribute sets the simulated reference temperature of the thermocouple reference
              junction.

        Usage:
            - Accessing this property will send the ``print(dmm.simreftemperature)`` query.
            - Setting this property to a value will send the ``dmm.simreftemperature = value``
              command.

        TSP Syntax:
            ```
            - dmm.simreftemperature = value
            - print(dmm.simreftemperature)
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
        """Access the ``dmm.simreftemperature`` attribute.

        Description:
            - This attribute sets the simulated reference temperature of the thermocouple reference
              junction.

        Usage:
            - Accessing this property will send the ``print(dmm.simreftemperature)`` query.
            - Setting this property to a value will send the ``dmm.simreftemperature = value``
              command.

        TSP Syntax:
            ```
            - dmm.simreftemperature = value
            - print(dmm.simreftemperature)
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
    def thermocouple(self) -> str:
        """Access the ``dmm.thermocouple`` attribute.

        Description:
            - This attribute indicates the thermocouple type.

        Usage:
            - Accessing this property will send the ``print(dmm.thermocouple)`` query.
            - Setting this property to a value will send the ``dmm.thermocouple = value`` command.

        TSP Syntax:
            ```
            - dmm.thermocouple = value
            - print(dmm.thermocouple)
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
        """Access the ``dmm.thermocouple`` attribute.

        Description:
            - This attribute indicates the thermocouple type.

        Usage:
            - Accessing this property will send the ``print(dmm.thermocouple)`` query.
            - Setting this property to a value will send the ``dmm.thermocouple = value`` command.

        TSP Syntax:
            ```
            - dmm.thermocouple = value
            - print(dmm.thermocouple)
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
        """Access the ``dmm.threertd`` attribute.

        Description:
            - This attribute defines the type of three-wire RTD that is being used.

        Usage:
            - Accessing this property will send the ``print(dmm.threertd)`` query.
            - Setting this property to a value will send the ``dmm.threertd = value`` command.

        TSP Syntax:
            ```
            - dmm.threertd = value
            - print(dmm.threertd)
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
        """Access the ``dmm.threertd`` attribute.

        Description:
            - This attribute defines the type of three-wire RTD that is being used.

        Usage:
            - Accessing this property will send the ``print(dmm.threertd)`` query.
            - Setting this property to a value will send the ``dmm.threertd = value`` command.

        TSP Syntax:
            ```
            - dmm.threertd = value
            - print(dmm.threertd)
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
    def threshold(self) -> str:
        """Access the ``dmm.threshold`` attribute.

        Description:
            - This attribute determines the signal level where the instrument makes frequency or
              period measurements.

        Usage:
            - Accessing this property will send the ``print(dmm.threshold)`` query.
            - Setting this property to a value will send the ``dmm.threshold = value`` command.

        TSP Syntax:
            ```
            - dmm.threshold = value
            - print(dmm.threshold)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".threshold"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.threshold)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.threshold`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @threshold.setter
    def threshold(self, value: Union[str, float]) -> None:
        """Access the ``dmm.threshold`` attribute.

        Description:
            - This attribute determines the signal level where the instrument makes frequency or
              period measurements.

        Usage:
            - Accessing this property will send the ``print(dmm.threshold)`` query.
            - Setting this property to a value will send the ``dmm.threshold = value`` command.

        TSP Syntax:
            ```
            - dmm.threshold = value
            - print(dmm.threshold)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".threshold", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.threshold = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.threshold`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def transducer(self) -> str:
        """Access the ``dmm.transducer`` attribute.

        Description:
            - This attribute contains the transducer type.

        Usage:
            - Accessing this property will send the ``print(dmm.transducer)`` query.
            - Setting this property to a value will send the ``dmm.transducer = value`` command.

        TSP Syntax:
            ```
            - dmm.transducer = value
            - print(dmm.transducer)
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
        """Access the ``dmm.transducer`` attribute.

        Description:
            - This attribute contains the transducer type.

        Usage:
            - Accessing this property will send the ``print(dmm.transducer)`` query.
            - Setting this property to a value will send the ``dmm.transducer = value`` command.

        TSP Syntax:
            ```
            - dmm.transducer = value
            - print(dmm.transducer)
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

    def appendbuffer(
        self, buffer_var: str, file_name: str, time_format: Optional[str] = None
    ) -> None:
        """Run the ``dmm.appendbuffer()`` function.

        Description:
            - This function appends data from the reading buffer to a file on the USB flash drive.
              If no file exists, this function creates a file.

        TSP Syntax:
            ```
            - dmm.appendbuffer()
            ```

        Args:
            buffer_var: A string with the name of a DMM reading buffer from which you want to append
                data to the specified file.
            file_name: A string with the file name of the file on the USB flash drive to which
                reading buffer data will be appended.
            time_format (optional): How the date and time information should be saved. The values
                for timeFormat are.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{buffer_var}"',
                    f'"{file_name}"',
                    time_format,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.appendbuffer({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.appendbuffer()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def close(self, channel_list: str) -> None:
        """Run the ``dmm.close()`` function.

        Description:
            - This function closes the specified channel or channel pattern to prepare for a
              measurement.

        TSP Syntax:
            ```
            - dmm.close()
            ```

        Args:
            channel_list: A string that lists the channel or channel pattern to close.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.close("{channel_list}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.close()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def getconfig(self, channel_list: str) -> str:
        """Run the ``dmm.getconfig()`` function.

        Description:
            - This function queries for the DMM configurations that are associated with the
              specified channels or channel patterns.

        TSP Syntax:
            ```
            - dmm.getconfig()
            ```

        Args:
            channel_list: The channels or channel patterns to query.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.getconfig("{channel_list}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.getconfig()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def makebuffer(self, buffer_size: str) -> str:
        """Run the ``dmm.makebuffer()`` function.

        Description:
            - This function creates a user buffer for storing readings. Reading buffers are
              allocated dynamically.

        TSP Syntax:
            ```
            - dmm.makebuffer()
            ```

        Args:
            buffer_size: Maximum number of readings that the buffer can store.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.makebuffer({buffer_size}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.makebuffer()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def measure(self, buffer_var: Optional[str] = None) -> str:
        """Run the ``dmm.measure()`` function.

        Description:
            - This function returns the last reading of the measurement process without using the
              trigger model.

        TSP Syntax:
            ```
            - dmm.measure()
            ```

        Args:
            buffer_var (optional): A previously created reading buffer where all readings are
                stored.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (buffer_var,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.measure({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.measure()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def measurewithptp(self, buffer_var: Optional[str] = None) -> str:
        """Run the ``dmm.measurewithptp()`` function.

        Description:
            - This function returns the last actual measurement and time information in PTP format
              without using the trigger model. You can also use a reading buffer to store additional
              information that is acquired while making a measurement.

        TSP Syntax:
            ```
            - dmm.measurewithptp()
            ```

        Args:
            buffer_var (optional): A previously created reading buffer variable in which all
                readings are stored.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (buffer_var,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.measurewithptp({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.measurewithptp()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def measurewithtime(self, buffer_var: Optional[str] = None) -> str:
        """Run the ``dmm.measurewithtime()`` function.

        Description:
            - This function returns the last actual measurement and time information in UTC format
              without using the trigger model. You can also use a reading buffer to store additional
              information that is acquired while making a measurement.

        TSP Syntax:
            ```
            - dmm.measurewithtime()
            ```

        Args:
            buffer_var (optional): A previously created reading buffer variable in which all
                readings are stored.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (buffer_var,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.measurewithtime({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.measurewithtime()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def open(self, channel_list: str) -> None:
        """Run the ``dmm.open()`` function.

        Description:
            - Opens the specified channel or channel pattern.

        TSP Syntax:
            ```
            - dmm.open()
            ```

        Args:
            channel_list: A string that lists the channel or channel pattern to open.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.open("{channel_list}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.open()`` function."  # noqa: E501
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

    def savebuffer(
        self, buffer_var: str, file_name: str, time_format: Optional[str] = None
    ) -> None:
        """Run the ``dmm.savebuffer()`` function.

        Description:
            - Saves data from the specified reading buffer to a USB flash drive using the specified
              filename.

        TSP Syntax:
            ```
            - dmm.savebuffer()
            ```

        Args:
            buffer_var: A string that specifies the name of the DMM reading buffer that was created
                by dmm.makebuffer().
            file_name: A string that indicates the name of the file on the USB flash drive in which
                to save the reading buffer.
            time_format (optional): How date and time information from the buffer is saved in the
                file on the USB flash drive; the values are.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{buffer_var}"',
                    f'"{file_name}"',
                    time_format,
                )
                if x is not None
            )
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.savebuffer({function_args})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.savebuffer()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def setconfig(self, channel_list: str, dmm_configuration: str) -> None:
        """Run the ``dmm.setconfig()`` function.

        Description:
            - Associates a DMM configuration with items specified in parameter channel list.

        TSP Syntax:
            ```
            - dmm.setconfig()
            ```

        Args:
            channel_list: A string that lists the channels and channel patterns to change.
            dmm_configuration: A string with the name of the DMM configuration that will be assigned
                to items in channelList.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.setconfig("{channel_list}", "{dmm_configuration}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.setconfig()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
