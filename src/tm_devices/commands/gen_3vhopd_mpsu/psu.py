# pyright: reportConstantRedefinition=none
"""The psu commands module.

These commands are used in the following models:
MPSU50_2ST

THIS FILE IS AUTO-GENERATED, IT SHOULD NOT BE MANUALLY MODIFIED.

Please report an issue if one is found.

Attributes and Functions:
    ```
    - psu[X].abort()
    - psu[X].configlist.create()
    - psu[X].configlist.delete()
    - psu[X].configlist.query()
    - psu[X].configlist.recall()
    - psu[X].configlist.size()
    - psu[X].configlist.store()
    - psu[X].configlist.table()
    - psu[X].defbuffer1
    - psu[X].defbuffer2
    - psu[X].makebuffer()
    - psu[X].measure.aperture
    - psu[X].measure.count
    - psu[X].measure.i()
    - psu[X].measure.nplc
    - psu[X].measure.overlappedi()
    - psu[X].measure.overlappediv()
    - psu[X].measure.overlappedp()
    - psu[X].measure.overlappedr()
    - psu[X].measure.overlappedv()
    - psu[X].measure.p()
    - psu[X].measure.r()
    - psu[X].measure.rangei
    - psu[X].measure.rangev
    - psu[X].measure.rate
    - psu[X].measure.rel.enablei
    - psu[X].measure.rel.enablep
    - psu[X].measure.rel.enabler
    - psu[X].measure.rel.enablev
    - psu[X].measure.rel.leveli
    - psu[X].measure.rel.levelp
    - psu[X].measure.rel.levelr
    - psu[X].measure.rel.levelv
    - psu[X].measure.tempcomp
    - psu[X].measure.v()
    - psu[X].overlapped
    - psu[X].reset()
    - psu[X].source.constantcurrent
    - psu[X].source.levelv
    - psu[X].source.limiti
    - psu[X].source.offmode
    - psu[X].source.output
    - psu[X].source.protect.enablei
    - psu[X].source.protect.enablev
    - psu[X].source.protect.leveli
    - psu[X].source.protect.levelv
    - psu[X].source.protect.trippedi
    - psu[X].source.protect.trippedv
    - psu[X].source.rangev
    - psu[X].source.slewratev
    - psu[X].trigger.measure.i()
    - psu[X].trigger.measure.iv()
    - psu[X].trigger.measure.p()
    - psu[X].trigger.measure.r()
    - psu[X].trigger.measure.v()
    - psu[X].trigger.source.linearv()
    - psu[X].trigger.source.listv()
    - psu[X].trigger.source.logv()
    - psu[X].waitcomplete()
    ```
"""

from typing import Optional, TYPE_CHECKING, Union

from tm_devices.helpers import ReadOnlyCachedProperty as cached_property  # noqa: N813

from ..gen_4dh8ja_mpmpsumsmu.buffervar import Buffervar
from ..helpers import BaseTSPCmd, NoDeviceProvidedError, ValidatedDynamicNumberCmd

if TYPE_CHECKING:
    from tm_devices.driver_mixins.device_control.tsp_control import TSPControl


class PsuItemTriggerSource(BaseTSPCmd):
    """The ``psu[X].trigger.source`` command tree.

    Properties and methods:
        - ``.linearv()``: The ``psu[X].trigger.source.linearv()`` function.
        - ``.listv()``: The ``psu[X].trigger.source.listv()`` function.
        - ``.logv()``: The ``psu[X].trigger.source.logv()`` function.
    """

    def linearv(self, start: str, end: str, points: str) -> None:
        """Run the ``psu[X].trigger.source.linearv()`` function.

        Description:
            - This function configures the linear sweep for the trigger model. (v = voltage in
              volts)

        TSP Syntax:
            ```
            - psu[X].trigger.source.linearv()
            ```

        Args:
            start: Start source level.
            end: End source level.
            points: Number of points used to calculate the step size.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.linearv({start}, {end}, {points})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.linearv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def listv(self, source_levels: str) -> None:
        """Run the ``psu[X].trigger.source.listv()`` function.

        Description:
            - This function configures the list sweep for the trigger model. (v = voltage in volts)

        TSP Syntax:
            ```
            - psu[X].trigger.source.listv()
            ```

        Args:
            source_levels: List of source levels. Each time a source block is reached, the index
                increases by 1. When it reaches the end, it cycles back to the beginning.

        For example, ({1, 2, 3}).

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.listv({source_levels})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.listv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def logv(self, start: str, end: str, points: str) -> None:
        """Run the ``psu[X].trigger.source.logv()`` function.

        Description:
            - This function configures a logarithmic sweep for the trigger model. (v = voltage in
              volts)

        TSP Syntax:
            ```
            - psu[X].trigger.source.logv()
            ```

        Args:
            start: Start source level.
            end: End source level.
            points: Number of points used to calculate the step size.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.logv({start}, {end}, {points})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.logv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class PsuItemTriggerMeasure(BaseTSPCmd):
    """The ``psu[X].trigger.measure`` command tree.

    Properties and methods:
        - ``.i()``: The ``psu[X].trigger.measure.i()`` function.
        - ``.iv()``: The ``psu[X].trigger.measure.iv()`` function.
        - ``.p()``: The ``psu[X].trigger.measure.p()`` function.
        - ``.r()``: The ``psu[X].trigger.measure.r()`` function.
        - ``.v()``: The ``psu[X].trigger.measure.v()`` function.
    """

    def i(self, reading_buffer: str) -> None:
        """Run the ``psu[X].trigger.measure.i()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (i
              = current in amperes)

        TSP Syntax:
            ```
            - psu[X].trigger.measure.i()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.i({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.i()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def iv(self, ibuffer: str, vbuffer: str) -> None:
        """Run the ``psu[X].trigger.measure.iv()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (i
              = current in amperes, v = voltage in volts)

        TSP Syntax:
            ```
            - psu[X].trigger.measure.iv()
            ```

        Args:
            ibuffer: Buffer to store current readings.
            vbuffer: Buffer to store voltage readings.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.iv({ibuffer}, {vbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.iv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def p(self, reading_buffer: str) -> None:
        """Run the ``psu[X].trigger.measure.p()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (p
              = power in watts)

        TSP Syntax:
            ```
            - psu[X].trigger.measure.p()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.p({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.p()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def r(self, reading_buffer: str) -> None:
        """Run the ``psu[X].trigger.measure.r()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (r
              = resistance in ohms)

        TSP Syntax:
            ```
            - psu[X].trigger.measure.r()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.r({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.r()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def v(self, reading_buffer: str) -> None:
        """Run the ``psu[X].trigger.measure.v()`` function.

        Description:
            - This function configures the reading buffer and measure type for the trigger model. (v
              = voltage in volts)

        TSP Syntax:
            ```
            - psu[X].trigger.measure.v()
            ```

        Args:
            reading_buffer: Buffer to store the measurement result.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.v({reading_buffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.v()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class PsuItemTrigger(BaseTSPCmd):
    """The ``psu[X].trigger`` command tree.

    Properties and methods:
        - ``.measure``: The ``psu[X].trigger.measure`` command tree.
        - ``.source``: The ``psu[X].trigger.source`` command tree.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._measure = PsuItemTriggerMeasure(device, f"{self._cmd_syntax}.measure")
        self._source = PsuItemTriggerSource(device, f"{self._cmd_syntax}.source")

    @property
    def measure(self) -> PsuItemTriggerMeasure:
        """Return the ``psu[X].trigger.measure`` command tree.

        Sub-properties and sub-methods:
            - ``.i()``: The ``psu[X].trigger.measure.i()`` function.
            - ``.iv()``: The ``psu[X].trigger.measure.iv()`` function.
            - ``.p()``: The ``psu[X].trigger.measure.p()`` function.
            - ``.r()``: The ``psu[X].trigger.measure.r()`` function.
            - ``.v()``: The ``psu[X].trigger.measure.v()`` function.
        """
        return self._measure

    @property
    def source(self) -> PsuItemTriggerSource:
        """Return the ``psu[X].trigger.source`` command tree.

        Sub-properties and sub-methods:
            - ``.linearv()``: The ``psu[X].trigger.source.linearv()`` function.
            - ``.listv()``: The ``psu[X].trigger.source.listv()`` function.
            - ``.logv()``: The ``psu[X].trigger.source.logv()`` function.
        """
        return self._source


class PsuItemSourceProtect(BaseTSPCmd):
    """The ``psu[X].source.protect`` command tree.

    Properties and methods:
        - ``.enablei``: The ``psu[X].source.protect.enablei`` attribute.
        - ``.enablev``: The ``psu[X].source.protect.enablev`` attribute.
        - ``.leveli``: The ``psu[X].source.protect.leveli`` attribute.
        - ``.levelv``: The ``psu[X].source.protect.levelv`` attribute.
        - ``.trippedi``: The ``psu[X].source.protect.trippedi`` attribute.
        - ``.trippedv``: The ``psu[X].source.protect.trippedv`` attribute.
    """

    @property
    def enablei(self) -> str:
        """Access the ``psu[X].source.protect.enablei`` attribute.

        Description:
            - This attribute enables or disables the overcurrent protection function.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.protect.enablei)`` query.
            - Setting this property to a value will send the
              ``psu[X].source.protect.enablei = value`` command.

        TSP Syntax:
            ```
            - psu[X].source.protect.enablei = value
            - print(psu[X].source.protect.enablei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablei.setter
    def enablei(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].source.protect.enablei`` attribute.

        Description:
            - This attribute enables or disables the overcurrent protection function.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.protect.enablei)`` query.
            - Setting this property to a value will send the
              ``psu[X].source.protect.enablei = value`` command.

        TSP Syntax:
            ```
            - psu[X].source.protect.enablei = value
            - print(psu[X].source.protect.enablei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablei", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablei = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enablev(self) -> str:
        """Access the ``psu[X].source.protect.enablev`` attribute.

        Description:
            - This attribute enables or disables the overvoltage protection function.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.protect.enablev)`` query.
            - Setting this property to a value will send the
              ``psu[X].source.protect.enablev = value`` command.

        TSP Syntax:
            ```
            - psu[X].source.protect.enablev = value
            - print(psu[X].source.protect.enablev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablev.setter
    def enablev(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].source.protect.enablev`` attribute.

        Description:
            - This attribute enables or disables the overvoltage protection function.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.protect.enablev)`` query.
            - Setting this property to a value will send the
              ``psu[X].source.protect.enablev = value`` command.

        TSP Syntax:
            ```
            - psu[X].source.protect.enablev = value
            - print(psu[X].source.protect.enablev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def leveli(self) -> str:
        """Access the ``psu[X].source.protect.leveli`` attribute.

        Description:
            - This attribute configures the overcurrent protection level.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.protect.leveli)`` query.
            - Setting this property to a value will send the
              ``psu[X].source.protect.leveli = value`` command.

        TSP Syntax:
            ```
            - psu[X].source.protect.leveli = value
            - print(psu[X].source.protect.leveli)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".leveli"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.leveli)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @leveli.setter
    def leveli(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].source.protect.leveli`` attribute.

        Description:
            - This attribute configures the overcurrent protection level.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.protect.leveli)`` query.
            - Setting this property to a value will send the
              ``psu[X].source.protect.leveli = value`` command.

        TSP Syntax:
            ```
            - psu[X].source.protect.leveli = value
            - print(psu[X].source.protect.leveli)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".leveli", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.leveli = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelv(self) -> str:
        """Access the ``psu[X].source.protect.levelv`` attribute.

        Description:
            - This attribute configures the overvoltage protection level.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.protect.levelv)`` query.
            - Setting this property to a value will send the
              ``psu[X].source.protect.levelv = value`` command.

        TSP Syntax:
            ```
            - psu[X].source.protect.levelv = value
            - print(psu[X].source.protect.levelv)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelv.setter
    def levelv(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].source.protect.levelv`` attribute.

        Description:
            - This attribute configures the overvoltage protection level.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.protect.levelv)`` query.
            - Setting this property to a value will send the
              ``psu[X].source.protect.levelv = value`` command.

        TSP Syntax:
            ```
            - psu[X].source.protect.levelv = value
            - print(psu[X].source.protect.levelv)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def trippedi(self) -> str:
        """Access the ``psu[X].source.protect.trippedi`` attribute.

        Description:
            - This attribute indicates if the overcurrent protection circuit was tripped.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.protect.trippedi)`` query.

        TSP Syntax:
            ```
            - print(psu[X].source.protect.trippedi)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".trippedi"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.trippedi)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.trippedi`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def trippedv(self) -> str:
        """Access the ``psu[X].source.protect.trippedv`` attribute.

        Description:
            - This attribute indicates if the overvoltage protection circuit was tripped.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.protect.trippedv)`` query.

        TSP Syntax:
            ```
            - print(psu[X].source.protect.trippedv)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".trippedv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.trippedv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.trippedv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class PsuItemSource(BaseTSPCmd):
    """The ``psu[X].source`` command tree.

    Info:
        - ``X``, the module channel number.

    Properties and methods:
        - ``.constantcurrent``: The ``psu[X].source.constantcurrent`` attribute.
        - ``.levelv``: The ``psu[X].source.levelv`` attribute.
        - ``.limiti``: The ``psu[X].source.limiti`` attribute.
        - ``.offmode``: The ``psu[X].source.offmode`` attribute.
        - ``.output``: The ``psu[X].source.output`` attribute.
        - ``.protect``: The ``psu[X].source.protect`` command tree.
        - ``.rangev``: The ``psu[X].source.rangev`` attribute.
        - ``.slewratev``: The ``psu[X].source.slewratev`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._protect = PsuItemSourceProtect(device, f"{self._cmd_syntax}.protect")

    @property
    def constantcurrent(self) -> str:
        """Access the ``psu[X].source.constantcurrent`` attribute.

        Description:
            - This attribute indicates when the source is within the current limit.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.constantcurrent)`` query.

        TSP Syntax:
            ```
            - print(psu[X].source.constantcurrent)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".constantcurrent"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.constantcurrent)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.constantcurrent`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelv(self) -> str:
        """Access the ``psu[X].source.levelv`` attribute.

        Description:
            - This attribute configures the voltage source level.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.levelv)`` query.
            - Setting this property to a value will send the ``psu[X].source.levelv = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.levelv = value
            - print(psu[X].source.levelv)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelv.setter
    def levelv(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].source.levelv`` attribute.

        Description:
            - This attribute configures the voltage source level.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.levelv)`` query.
            - Setting this property to a value will send the ``psu[X].source.levelv = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.levelv = value
            - print(psu[X].source.levelv)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def limiti(self) -> str:
        """Access the ``psu[X].source.limiti`` attribute.

        Description:
            - This attribute configures the source current limit.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.limiti)`` query.
            - Setting this property to a value will send the ``psu[X].source.limiti = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.limiti = value
            - print(psu[X].source.limiti)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".limiti"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.limiti)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limiti`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @limiti.setter
    def limiti(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].source.limiti`` attribute.

        Description:
            - This attribute configures the source current limit.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.limiti)`` query.
            - Setting this property to a value will send the ``psu[X].source.limiti = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.limiti = value
            - print(psu[X].source.limiti)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".limiti", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.limiti = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.limiti`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def offmode(self) -> str:
        """Access the ``psu[X].source.offmode`` attribute.

        Description:
            - This attribute sets the source output-off mode.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.offmode)`` query.
            - Setting this property to a value will send the ``psu[X].source.offmode = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.offmode = value
            - print(psu[X].source.offmode)
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
        """Access the ``psu[X].source.offmode`` attribute.

        Description:
            - This attribute sets the source output-off mode.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.offmode)`` query.
            - Setting this property to a value will send the ``psu[X].source.offmode = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.offmode = value
            - print(psu[X].source.offmode)
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
        """Access the ``psu[X].source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.output)`` query.
            - Setting this property to a value will send the ``psu[X].source.output = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.output = value
            - print(psu[X].source.output)
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
        """Access the ``psu[X].source.output`` attribute.

        Description:
            - This attribute enables or disables the source output.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.output)`` query.
            - Setting this property to a value will send the ``psu[X].source.output = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.output = value
            - print(psu[X].source.output)
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
    def protect(self) -> PsuItemSourceProtect:
        """Return the ``psu[X].source.protect`` command tree.

        Sub-properties and sub-methods:
            - ``.enablei``: The ``psu[X].source.protect.enablei`` attribute.
            - ``.enablev``: The ``psu[X].source.protect.enablev`` attribute.
            - ``.leveli``: The ``psu[X].source.protect.leveli`` attribute.
            - ``.levelv``: The ``psu[X].source.protect.levelv`` attribute.
            - ``.trippedi``: The ``psu[X].source.protect.trippedi`` attribute.
            - ``.trippedv``: The ``psu[X].source.protect.trippedv`` attribute.
        """
        return self._protect

    @property
    def rangev(self) -> str:
        """Access the ``psu[X].source.rangev`` attribute.

        Description:
            - This attribute contains the value of the source range for voltage.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.rangev)`` query.
            - Setting this property to a value will send the ``psu[X].source.rangev = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.rangev = value
            - print(psu[X].source.rangev)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rangev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rangev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @rangev.setter
    def rangev(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].source.rangev`` attribute.

        Description:
            - This attribute contains the value of the source range for voltage.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.rangev)`` query.
            - Setting this property to a value will send the ``psu[X].source.rangev = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.rangev = value
            - print(psu[X].source.rangev)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".rangev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.rangev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def slewratev(self) -> str:
        """Access the ``psu[X].source.slewratev`` attribute.

        Description:
            - This attribute configures the voltage source slew rate.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.slewratev)`` query.
            - Setting this property to a value will send the ``psu[X].source.slewratev = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.slewratev = value
            - print(psu[X].source.slewratev)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".slewratev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.slewratev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.slewratev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @slewratev.setter
    def slewratev(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].source.slewratev`` attribute.

        Description:
            - This attribute configures the voltage source slew rate.

        Usage:
            - Accessing this property will send the ``print(psu[X].source.slewratev)`` query.
            - Setting this property to a value will send the ``psu[X].source.slewratev = value``
              command.

        TSP Syntax:
            ```
            - psu[X].source.slewratev = value
            - print(psu[X].source.slewratev)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".slewratev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.slewratev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.slewratev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class PsuItemMeasureRel(BaseTSPCmd):
    """The ``psu[X].measure.rel`` command tree.

    Properties and methods:
        - ``.enablei``: The ``psu[X].measure.rel.enablei`` attribute.
        - ``.enablep``: The ``psu[X].measure.rel.enablep`` attribute.
        - ``.enabler``: The ``psu[X].measure.rel.enabler`` attribute.
        - ``.enablev``: The ``psu[X].measure.rel.enablev`` attribute.
        - ``.leveli``: The ``psu[X].measure.rel.leveli`` attribute.
        - ``.levelp``: The ``psu[X].measure.rel.levelp`` attribute.
        - ``.levelr``: The ``psu[X].measure.rel.levelr`` attribute.
        - ``.levelv``: The ``psu[X].measure.rel.levelv`` attribute.
    """

    @property
    def enablei(self) -> str:
        """Access the ``psu[X].measure.rel.enablei`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.enablei)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.enablei = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.enablei = value
            - print(psu[X].measure.rel.enablei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablei.setter
    def enablei(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].measure.rel.enablei`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.enablei)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.enablei = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.enablei = value
            - print(psu[X].measure.rel.enablei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablei", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablei = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enablep(self) -> str:
        """Access the ``psu[X].measure.rel.enablep`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.enablep)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.enablep = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.enablep = value
            - print(psu[X].measure.rel.enablep)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablep"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablep)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablep`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablep.setter
    def enablep(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].measure.rel.enablep`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (p = power in watts)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.enablep)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.enablep = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.enablep = value
            - print(psu[X].measure.rel.enablep)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablep", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablep = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablep`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enabler(self) -> str:
        """Access the ``psu[X].measure.rel.enabler`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.enabler)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.enabler = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.enabler = value
            - print(psu[X].measure.rel.enabler)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enabler"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enabler)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enabler`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enabler.setter
    def enabler(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].measure.rel.enabler`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (r = resistance in ohms)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.enabler)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.enabler = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.enabler = value
            - print(psu[X].measure.rel.enabler)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enabler", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enabler = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enabler`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def enablev(self) -> str:
        """Access the ``psu[X].measure.rel.enablev`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.enablev)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.enablev = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.enablev = value
            - print(psu[X].measure.rel.enablev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".enablev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.enablev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @enablev.setter
    def enablev(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].measure.rel.enablev`` attribute.

        Description:
            - This attribute turns relative measurements on or off. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.enablev)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.enablev = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.enablev = value
            - print(psu[X].measure.rel.enablev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".enablev", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.enablev = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.enablev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def leveli(self) -> str:
        """Access the ``psu[X].measure.rel.leveli`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.leveli)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.leveli = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.leveli = value
            - print(psu[X].measure.rel.leveli)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".leveli"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.leveli)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @leveli.setter
    def leveli(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].measure.rel.leveli`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (i = current in
              amperes)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.leveli)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.leveli = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.leveli = value
            - print(psu[X].measure.rel.leveli)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".leveli", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.leveli = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.leveli`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelp(self) -> str:
        """Access the ``psu[X].measure.rel.levelp`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (p = power in
              watts)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.levelp)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.levelp = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.levelp = value
            - print(psu[X].measure.rel.levelp)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelp"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelp)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelp.setter
    def levelp(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].measure.rel.levelp`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (p = power in
              watts)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.levelp)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.levelp = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.levelp = value
            - print(psu[X].measure.rel.levelp)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelp", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelp = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelr(self) -> str:
        """Access the ``psu[X].measure.rel.levelr`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (r = resistance
              in ohms)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.levelr)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.levelr = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.levelr = value
            - print(psu[X].measure.rel.levelr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelr"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelr)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelr.setter
    def levelr(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].measure.rel.levelr`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (r = resistance
              in ohms)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.levelr)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.levelr = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.levelr = value
            - print(psu[X].measure.rel.levelr)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelr", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelr = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelr`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def levelv(self) -> str:
        """Access the ``psu[X].measure.rel.levelv`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.levelv)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.levelv = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.levelv = value
            - print(psu[X].measure.rel.levelv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".levelv"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.levelv)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @levelv.setter
    def levelv(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].measure.rel.levelv`` attribute.

        Description:
            - This attribute specifies the offset value for relative measurements. (v = voltage in
              volts)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rel.levelv)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rel.levelv = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rel.levelv = value
            - print(psu[X].measure.rel.levelv)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".levelv", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.levelv = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.levelv`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class PsuItemMeasure(BaseTSPCmd):
    """The ``psu[X].measure`` command tree.

    Properties and methods:
        - ``.i()``: The ``psu[X].measure.i()`` function.
        - ``.p()``: The ``psu[X].measure.p()`` function.
        - ``.r()``: The ``psu[X].measure.r()`` function.
        - ``.v()``: The ``psu[X].measure.v()`` function.
        - ``.aperture``: The ``psu[X].measure.aperture`` attribute.
        - ``.count``: The ``psu[X].measure.count`` attribute.
        - ``.nplc``: The ``psu[X].measure.nplc`` attribute.
        - ``.overlappedi()``: The ``psu[X].measure.overlappedi()`` function.
        - ``.overlappediv()``: The ``psu[X].measure.overlappediv()`` function.
        - ``.overlappedp()``: The ``psu[X].measure.overlappedp()`` function.
        - ``.overlappedr()``: The ``psu[X].measure.overlappedr()`` function.
        - ``.overlappedv()``: The ``psu[X].measure.overlappedv()`` function.
        - ``.rangei``: The ``psu[X].measure.rangei`` attribute.
        - ``.rangev``: The ``psu[X].measure.rangev`` attribute.
        - ``.rate``: The ``psu[X].measure.rate`` attribute.
        - ``.rel``: The ``psu[X].measure.rel`` command tree.
        - ``.tempcomp``: The ``psu[X].measure.tempcomp`` attribute.
    """

    def __init__(self, device: Optional["TSPControl"], cmd_syntax: str) -> None:
        super().__init__(device, cmd_syntax)
        self._rel = PsuItemMeasureRel(device, f"{self._cmd_syntax}.rel")

    @property
    def aperture(self) -> str:
        """Access the ``psu[X].measure.aperture`` attribute.

        Description:
            - This attribute configures the measurement aperture for a channel in seconds.

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.aperture)`` query.

        TSP Syntax:
            ```
            - print(psu[X].measure.aperture)
            ```

        Info:
            - ``X``, the module channel number.

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

    @property
    def count(self) -> str:
        """Access the ``psu[X].measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements performed when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.count)`` query.
            - Setting this property to a value will send the ``psu[X].measure.count = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.count = value
            - print(psu[X].measure.count)
            ```

        Info:
            - ``X``, the module channel number.

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
        """Access the ``psu[X].measure.count`` attribute.

        Description:
            - This attribute sets the number of measurements performed when a measurement is
              requested.

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.count)`` query.
            - Setting this property to a value will send the ``psu[X].measure.count = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.count = value
            - print(psu[X].measure.count)
            ```

        Info:
            - ``X``, the module channel number.

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
    def nplc(self) -> str:
        """Access the ``psu[X].measure.nplc`` attribute.

        Description:
            - This attribute configures the measurement aperture in number of power line cycles.

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.nplc)`` query.

        TSP Syntax:
            ```
            - print(psu[X].measure.nplc)
            ```

        Info:
            - ``X``, the module channel number.

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

    @property
    def rangei(self) -> str:
        """Access the ``psu[X].measure.rangei`` attribute.

        Description:
            - This attribute contains the positive, full scale value of the measurement range for
              voltage or current. (i = current in amperes)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rangei)`` query.

        TSP Syntax:
            ```
            - print(psu[X].measure.rangei)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rangei"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rangei)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangei`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rangev(self) -> str:
        """Access the ``psu[X].measure.rangev`` attribute.

        Description:
            - This attribute contains the positive, full scale value of the measurement range for
              voltage or current. (v = voltage in volts)

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rangev)`` query.

        TSP Syntax:
            ```
            - print(psu[X].measure.rangev)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rangev"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rangev)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rangev`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rate(self) -> str:
        """Access the ``psu[X].measure.rate`` attribute.

        Description:
            - This attribute configures the measure rate for a PSU channel.

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rate)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rate = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rate = value
            - print(psu[X].measure.rate)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".rate"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.rate)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @rate.setter
    def rate(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].measure.rate`` attribute.

        Description:
            - This attribute configures the measure rate for a PSU channel.

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.rate)`` query.
            - Setting this property to a value will send the ``psu[X].measure.rate = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.rate = value
            - print(psu[X].measure.rate)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".rate", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.rate = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.rate`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def rel(self) -> PsuItemMeasureRel:
        """Return the ``psu[X].measure.rel`` command tree.

        Sub-properties and sub-methods:
            - ``.enablei``: The ``psu[X].measure.rel.enablei`` attribute.
            - ``.enablep``: The ``psu[X].measure.rel.enablep`` attribute.
            - ``.enabler``: The ``psu[X].measure.rel.enabler`` attribute.
            - ``.enablev``: The ``psu[X].measure.rel.enablev`` attribute.
            - ``.leveli``: The ``psu[X].measure.rel.leveli`` attribute.
            - ``.levelp``: The ``psu[X].measure.rel.levelp`` attribute.
            - ``.levelr``: The ``psu[X].measure.rel.levelr`` attribute.
            - ``.levelv``: The ``psu[X].measure.rel.levelv`` attribute.
        """
        return self._rel

    @property
    def tempcomp(self) -> str:
        """Access the ``psu[X].measure.tempcomp`` attribute.

        Description:
            - This attribute turns temperature compensation on or off for the current measurements.

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.tempcomp)`` query.
            - Setting this property to a value will send the ``psu[X].measure.tempcomp = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.tempcomp = value
            - print(psu[X].measure.tempcomp)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".tempcomp"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.tempcomp)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tempcomp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @tempcomp.setter
    def tempcomp(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].measure.tempcomp`` attribute.

        Description:
            - This attribute turns temperature compensation on or off for the current measurements.

        Usage:
            - Accessing this property will send the ``print(psu[X].measure.tempcomp)`` query.
            - Setting this property to a value will send the ``psu[X].measure.tempcomp = value``
              command.

        TSP Syntax:
            ```
            - psu[X].measure.tempcomp = value
            - print(psu[X].measure.tempcomp)
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".tempcomp", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.tempcomp = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.tempcomp`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def i(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``psu[X].measure.i()`` function.

        Description:
            - This function makes one or more measurements. (i = current in amperes)

        TSP Syntax:
            ```
            - psu[X].measure.i()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.i({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.i()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def p(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``psu[X].measure.p()`` function.

        Description:
            - This function makes one or more measurements. (p = power in watts)

        TSP Syntax:
            ```
            - psu[X].measure.p()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.p({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.p()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def r(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``psu[X].measure.r()`` function.

        Description:
            - This function makes one or more measurements. (r = resistance in ohms)

        TSP Syntax:
            ```
            - psu[X].measure.r()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.r({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.r()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def v(self, reading_buffer: Optional[str] = None) -> str:
        """Run the ``psu[X].measure.v()`` function.

        Description:
            - This function makes one or more measurements. (v = voltage in volts)

        TSP Syntax:
            ```
            - psu[X].measure.v()
            ```

        Args:
            reading_buffer (optional): Reading buffer where the readings are stored; can be a
                dynamically allocated user-defined buffer or a dedicated reading buffer.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(str(x) for x in (reading_buffer,) if x is not None)
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.v({function_args}))"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.v()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedi(self, rbuffer: str) -> None:
        """Run the ``psu[X].measure.overlappedi()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (i = current in
              amperes)

        TSP Syntax:
            ```
            - psu[X].measure.overlappedi()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedi({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedi()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappediv(self, ibuffer: str, vbuffer: str) -> None:
        """Run the ``psu[X].measure.overlappediv()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (i = current in
              amperes, v = voltage in volts)

        TSP Syntax:
            ```
            - psu[X].measure.overlappediv()
            ```

        Args:
            ibuffer: A reading buffer object where current readings are stored.
            vbuffer: A reading buffer object where voltage readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappediv({ibuffer}, {vbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappediv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedp(self, rbuffer: str) -> None:
        """Run the ``psu[X].measure.overlappedp()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (p = power in watts)

        TSP Syntax:
            ```
            - psu[X].measure.overlappedp()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedp({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedp()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedr(self, rbuffer: str) -> None:
        """Run the ``psu[X].measure.overlappedr()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (r = resistance in
              ohms)

        TSP Syntax:
            ```
            - psu[X].measure.overlappedr()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedr({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedr()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def overlappedv(self, rbuffer: str) -> None:
        """Run the ``psu[X].measure.overlappedv()`` function.

        Description:
            - This function starts an asynchronous (background) measurement. (v = voltage in volts)

        TSP Syntax:
            ```
            - psu[X].measure.overlappedv()
            ```

        Args:
            rbuffer: A reading buffer object where readings are stored.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.overlappedv({rbuffer})"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.overlappedv()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class PsuItemConfiglist(BaseTSPCmd):
    """The ``psu[X].configlist`` command tree.

    Info:
        - ``X``, the module channel number.

    Properties and methods:
        - ``.create()``: The ``psu[X].configlist.create()`` function.
        - ``.delete()``: The ``psu[X].configlist.delete()`` function.
        - ``.query()``: The ``psu[X].configlist.query()`` function.
        - ``.recall()``: The ``psu[X].configlist.recall()`` function.
        - ``.size()``: The ``psu[X].configlist.size()`` function.
        - ``.store()``: The ``psu[X].configlist.store()`` function.
        - ``.table()``: The ``psu[X].configlist.table()`` function.
    """

    def create(self, config_list_name: str) -> None:
        """Run the ``psu[X].configlist.create()`` function.

        Description:
            - This function creates an empty configuration list.

        TSP Syntax:
            ```
            - psu[X].configlist.create()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.create("{config_list_name}")'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.create()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def delete(self, config_list_name: str, index: Optional[int] = None) -> None:
        """Run the ``psu[X].configlist.delete()`` function.

        Description:
            - This function deletes a configuration list.

        TSP Syntax:
            ```
            - psu[X].configlist.delete()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.
            index (optional): A number starting from 1 that defines a specific configuration index
                in the configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
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

    def query(
        self, config_list_name: str, index: int, field_separator: Optional[str] = None
    ) -> str:
        """Run the ``psu[X].configlist.query()`` function.

        Description:
            - This function returns a list of TSP commands and parameter settings that are stored in
              the specified configuration index.

        TSP Syntax:
            ```
            - psu[X].configlist.query()
            ```

        Args:
            config_list_name: A string that represents the name of a measure configuration list.
            index: A number starting from 1 that defines a specific configuration index in the
                configuration list.
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
                    f'"{config_list_name}"',
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

    def recall(self, config_list_name: str, index: int) -> None:
        """Run the ``psu[X].configlist.recall()`` function.

        Description:
            - This function recalls a configuration index in a configuration list.

        TSP Syntax:
            ```
            - psu[X].configlist.recall()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.
            index: A number starting from 1 that defines a specific configuration index in the
                measure configuration list.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f'{self._cmd_syntax}.recall("{config_list_name}", {index})'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.recall()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def size(self, config_list_name: str) -> str:
        """Run the ``psu[X].configlist.size()`` function.

        Description:
            - This function returns the size (number of configuration indexes) of a configuration
              list.

        TSP Syntax:
            ```
            - psu[X].configlist.size()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f'print({self._cmd_syntax}.size("{config_list_name}"))'
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.size()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def store(self, config_list_name: str, index: Optional[int] = None) -> None:
        """Run the ``psu[X].configlist.store()`` function.

        Description:
            - This function stores the active settings into the named configuration list.

        TSP Syntax:
            ```
            - psu[X].configlist.store()
            ```

        Args:
            config_list_name: A string that represents the name of a configuration list.
            index (optional): A number starting from 1 that defines a specific configuration index
                in the configuration list. This parameter is optional.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            function_args = ", ".join(
                str(x)
                for x in (
                    f'"{config_list_name}"',
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

    def table(self) -> str:
        """Run the ``psu[X].configlist.table()`` function.

        Description:
            - This function returns the name of one measure configuration lists that is stored on
              the instrument.

        TSP Syntax:
            ```
            - psu[X].configlist.table()
            ```

        Info:
            - ``X``, the module channel number.

        Returns:
            The result of the function call.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.table())"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.table()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error


class PsuItem(ValidatedDynamicNumberCmd, BaseTSPCmd):
    """The ``psu[X]`` command tree.

    Info:
        - ``X``, the module channel number.

    Properties and methods:
        - ``.abort()``: The ``psu[X].abort()`` function.
        - ``.configlist``: The ``psu[X].configlist`` command tree.
        - ``.defbuffer1``: The ``psu[X].defbuffer1`` attribute.
        - ``.defbuffer2``: The ``psu[X].defbuffer2`` attribute.
        - ``.makebuffer()``: The ``psu[X].makebuffer()`` function.
        - ``.measure``: The ``psu[X].measure`` command tree.
        - ``.overlapped``: The ``psu[X].overlapped`` attribute.
        - ``.reset()``: The ``psu[X].reset()`` function.
        - ``.source``: The ``psu[X].source`` command tree.
        - ``.trigger``: The ``psu[X].trigger`` command tree.
        - ``.waitcomplete()``: The ``psu[X].waitcomplete()`` function.
    """

    def __init__(self, device: Optional["TSPControl"] = None, cmd_syntax: str = "psu[X]") -> None:
        super().__init__(device, cmd_syntax)
        self._buffer_count = 1
        self._configlist = PsuItemConfiglist(device, f"{self._cmd_syntax}.configlist")
        self._measure = PsuItemMeasure(device, f"{self._cmd_syntax}.measure")
        self._source = PsuItemSource(device, f"{self._cmd_syntax}.source")
        self._trigger = PsuItemTrigger(device, f"{self._cmd_syntax}.trigger")

    @property
    def configlist(self) -> PsuItemConfiglist:
        """Return the ``psu[X].configlist`` command tree.

        Info:
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.create()``: The ``psu[X].configlist.create()`` function.
            - ``.delete()``: The ``psu[X].configlist.delete()`` function.
            - ``.query()``: The ``psu[X].configlist.query()`` function.
            - ``.recall()``: The ``psu[X].configlist.recall()`` function.
            - ``.size()``: The ``psu[X].configlist.size()`` function.
            - ``.store()``: The ``psu[X].configlist.store()`` function.
            - ``.table()``: The ``psu[X].configlist.table()`` function.
        """
        return self._configlist

    @cached_property
    def defbuffer1(self) -> Buffervar:
        """Access the ``psu[X].defbuffer1`` attribute.

        Description:
            - This attribute contains the default dedicated reading buffers. (1 = default buffer1)

        Usage:
            - Accessing this property will send the ``print(psu[X].defbuffer1)`` query.

        TSP Syntax:
            ```
            - print(psu[X].defbuffer1)
            ```

        Returns:
            The default buffer object.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return Buffervar(self._device, f"{self._cmd_syntax}.defbuffer1")

    @cached_property
    def defbuffer2(self) -> Buffervar:
        """Access the ``psu[X].defbuffer2`` attribute.

        Description:
            - This attribute contains the default dedicated reading buffers. (2 = default buffer2)

        Usage:
            - Accessing this property will send the ``print(psu[X].defbuffer2)`` query.

        TSP Syntax:
            ```
            - print(psu[X].defbuffer2)
            ```

        Returns:
            The default buffer object.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        return Buffervar(self._device, f"{self._cmd_syntax}.defbuffer2")

    @property
    def measure(self) -> PsuItemMeasure:
        """Return the ``psu[X].measure`` command tree.

        Sub-properties and sub-methods:
            - ``.i()``: The ``psu[X].measure.i()`` function.
            - ``.p()``: The ``psu[X].measure.p()`` function.
            - ``.r()``: The ``psu[X].measure.r()`` function.
            - ``.v()``: The ``psu[X].measure.v()`` function.
            - ``.aperture``: The ``psu[X].measure.aperture`` attribute.
            - ``.count``: The ``psu[X].measure.count`` attribute.
            - ``.nplc``: The ``psu[X].measure.nplc`` attribute.
            - ``.overlappedi()``: The ``psu[X].measure.overlappedi()`` function.
            - ``.overlappediv()``: The ``psu[X].measure.overlappediv()`` function.
            - ``.overlappedp()``: The ``psu[X].measure.overlappedp()`` function.
            - ``.overlappedr()``: The ``psu[X].measure.overlappedr()`` function.
            - ``.overlappedv()``: The ``psu[X].measure.overlappedv()`` function.
            - ``.rangei``: The ``psu[X].measure.rangei`` attribute.
            - ``.rangev``: The ``psu[X].measure.rangev`` attribute.
            - ``.rate``: The ``psu[X].measure.rate`` attribute.
            - ``.rel``: The ``psu[X].measure.rel`` command tree.
            - ``.tempcomp``: The ``psu[X].measure.tempcomp`` attribute.
        """
        return self._measure

    @property
    def overlapped(self) -> str:
        """Access the ``psu[X].overlapped`` attribute.

        Description:
            - This attribute contains the state of the overlapped mode.

        Usage:
            - Accessing this property will send the ``print(psu[X].overlapped)`` query.
            - Setting this property to a value will send the ``psu[X].overlapped = value`` command.

        TSP Syntax:
            ```
            - psu[X].overlapped = value
            - print(psu[X].overlapped)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_syntax_enabled:  # type: ignore[union-attr]
                return self._cmd_syntax + ".overlapped"
            return self._device.query(  # type: ignore[union-attr]
                f"print({self._cmd_syntax}.overlapped)"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.overlapped`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @overlapped.setter
    def overlapped(self, value: Union[str, float]) -> None:
        """Access the ``psu[X].overlapped`` attribute.

        Description:
            - This attribute contains the state of the overlapped mode.

        Usage:
            - Accessing this property will send the ``print(psu[X].overlapped)`` query.
            - Setting this property to a value will send the ``psu[X].overlapped = value`` command.

        TSP Syntax:
            ```
            - psu[X].overlapped = value
            - print(psu[X].overlapped)
            ```

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            if self._device.command_verification_enabled:  # type: ignore[union-attr]
                self._device.set_and_check(  # type: ignore[union-attr]
                    self._cmd_syntax + ".overlapped", value
                )
            else:
                self._device.write(  # type: ignore[union-attr]
                    f"{self._cmd_syntax}.overlapped = {value}"
                )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to access the ``{self._cmd_syntax}.overlapped`` attribute."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    @property
    def source(self) -> PsuItemSource:
        """Return the ``psu[X].source`` command tree.

        Info:
            - ``X``, the module channel number.

        Sub-properties and sub-methods:
            - ``.constantcurrent``: The ``psu[X].source.constantcurrent`` attribute.
            - ``.levelv``: The ``psu[X].source.levelv`` attribute.
            - ``.limiti``: The ``psu[X].source.limiti`` attribute.
            - ``.offmode``: The ``psu[X].source.offmode`` attribute.
            - ``.output``: The ``psu[X].source.output`` attribute.
            - ``.protect``: The ``psu[X].source.protect`` command tree.
            - ``.rangev``: The ``psu[X].source.rangev`` attribute.
            - ``.slewratev``: The ``psu[X].source.slewratev`` attribute.
        """
        return self._source

    @property
    def trigger(self) -> PsuItemTrigger:
        """Return the ``psu[X].trigger`` command tree.

        Sub-properties and sub-methods:
            - ``.measure``: The ``psu[X].trigger.measure`` command tree.
            - ``.source``: The ``psu[X].trigger.source`` command tree.
        """
        return self._trigger

    def abort(self) -> None:
        """Run the ``psu[X].abort()`` function.

        Description:
            - This function terminates all overlapped operations on the specified channel.

        TSP Syntax:
            ```
            - psu[X].abort()
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.abort()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.abort()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error

    def makebuffer(self, buffer_size: str, *, buffer_name: Optional[str] = None) -> Buffervar:
        """Run the ``psu[X].makebuffer()`` function.

        Description:
            - This function creates a reading buffer.

        TSP Syntax:
            ```
            - psu[X].makebuffer()
            ```

        Args:
            buffer_size: The size of the reading buffer.
            buffer_name (optional): The name of the buffer variable to create. If not provided, an
                auto-generated variable will be used.

        Returns:
            The created buffer object.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        if buffer_name is None:
            buffer_name = f"private_custom_psu_buffer_{self._buffer_count}"
            self._buffer_count += 1
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{buffer_name} = {self._cmd_syntax}.makebuffer({buffer_size})"
            )
            self._device._user_created_custom_buffers.append(buffer_name)  # pyright: ignore[reportOptionalMemberAccess,reportPrivateUsage]  # noqa: SLF001
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.makebuffer()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
        return Buffervar(self._device, buffer_name)

    def reset(self) -> None:
        """Run the ``psu[X].reset()`` function.

        Description:
            - This function turns off the output and resets the commands that begin with psu[X]. to
              their default settings.

        TSP Syntax:
            ```
            - psu[X].reset()
            ```

        Info:
            - ``X``, the module channel number.

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

    def waitcomplete(self) -> None:
        """Run the ``psu[X].waitcomplete()`` function.

        Description:
            - This function waits for all previously started overlapped commands to complete on the
              specified channel of a module.

        TSP Syntax:
            ```
            - psu[X].waitcomplete()
            ```

        Info:
            - ``X``, the module channel number.

        Raises:
            tm_devices.commands.NoDeviceProvidedError: Indicates that no device connection exists.
        """
        try:
            self._device.write(  # type: ignore[union-attr]
                f"{self._cmd_syntax}.waitcomplete()"
            )
        except AttributeError as error:
            msg = f"No TSPControl object was provided, unable to run the ``{self._cmd_syntax}.waitcomplete()`` function."  # noqa: E501
            raise NoDeviceProvidedError(msg) from error
